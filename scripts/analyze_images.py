import os
import tensorflow as tf
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.vgg16 import VGG16, preprocess_input, decode_predictions
import numpy as np

# Load pre-trained model
model = VGG16(weights='imagenet')

# Directory where Instaloader saves images
image_dir = 'data/images'

# Function to predict image class
def predict_image_class(img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)

    preds = model.predict(img_array)
    decoded_preds = decode_predictions(preds, top=3)[0]
    return decoded_preds

# Analyze images in directory
for img_file in os.listdir(image_dir):
    if img_file.endswith('.jpg'):
        img_path = os.path.join(image_dir, img_file)
        predictions = predict_image_class(img_path)
        print(f'Predictions for {img_file}: {predictions}')
