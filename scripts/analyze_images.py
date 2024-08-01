import os
from google.cloud import storage
import tensorflow as tf
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.resnet50 import preprocess_input
import numpy as np
from pymongo import MongoClient
from dotenv import load_dotenv
import certifi
import requests
import json

# Load environment variables from .env file
load_dotenv()

# Google Cloud Storage setup
storage_client = storage.Client.from_service_account_json(os.getenv('GOOGLE_APPLICATION_CREDENTIALS'))
bucket_name = 'web-scraped-fashion-data'
bucket = storage_client.bucket(bucket_name)

# MongoDB setup
mongodb_uri = os.getenv('MONGODB_URI')
client = MongoClient(mongodb_uri, tlsCAFile=certifi.where())
db = client['influencer-fashion']
collection = db['images']

# Load FashionNet model
fashion_model_url = 'https://path-to-your-fashion-model/fashion_model.h5'
fashion_model_path = '/tmp/fashion_model.h5'
if not os.path.exists(fashion_model_path):
    r = requests.get(fashion_model_url, stream=True)
    with open(fashion_model_path, 'wb') as f:
        for chunk in r.iter_content(chunk_size=8192):
            f.write(chunk)
model = tf.keras.models.load_model(fashion_model_path)

# Load FashionNet class index
fashion_class_index_url = 'https://path-to-your-fashion-class-index/fashion_class_index.json'
fashion_class_index_path = '/tmp/fashion_class_index.json'
if not os.path.exists(fashion_class_index_path):
    r = requests.get(fashion_class_index_url, stream=True)
    with open(fashion_class_index_path, 'wb') as f:
        for chunk in r.iter_content(chunk_size=8192):
            f.write(chunk)
with open(fashion_class_index_path) as f:
    class_index = json.load(f)

def decode_predictions(preds, top=3):
    results = []
    for pred in preds:
        top_indices = pred.argsort()[-top:][::-1]
        result = [(class_index[str(i)], float(pred[i])) for i in top_indices]
        results.append(result)
    return results

# Function to predict image class
def predict_image_class(img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)

    preds = model.predict(img_array)
    decoded_preds = decode_predictions(preds, top=3)[0]
    return decoded_preds

# Function to download image from GCS
def download_image_from_gcs(blob_name, destination_file_name):
    blob = bucket.blob(blob_name)
    blob.download_to_filename(destination_file_name)
    print(f'Blob {blob_name} downloaded to {destination_file_name}.')

# Function to process images in GCS
def process_images_in_gcs():
    blobs = bucket.list_blobs()
    for blob in blobs:
        if blob.name.endswith('.jpg'):
            local_file_name = os.path.join('/tmp', os.path.basename(blob.name))
            download_image_from_gcs(blob.name, local_file_name)

            predictions = predict_image_class(local_file_name)
            print(f'Predictions for {blob.name}: {predictions}')

            # Store predictions in MongoDB
            collection.insert_one({
                'image': blob.name,
                'predictions': [
                    {'class': predictions[0][0], 'probability': predictions[0][1]} if len(predictions) > 0 else {},
                    {'class': predictions[1][0], 'probability': predictions[1][1]} if len(predictions) > 1 else {},
                    {'class': predictions[2][0], 'probability': predictions[2][1]} if len(predictions) > 2 else {}
                ]
            })

            # Remove the local file to save space
            os.remove(local_file_name)

# Run the script
print('Starting the image processing...')
process_images_in_gcs()
print('Finished processing all images.')