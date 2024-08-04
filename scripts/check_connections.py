''' Checking if connenect to Google Cloud Storage and MongoDB are available '''

from pymongo import MongoClient
from google.cloud import storage
import os
from dotenv import load_dotenv
import certifi

load_dotenv()

# Verify Google Cloud Storage connection
storage_client = storage.Client()
print(storage_client)

# Verify MongoDB connection
mongodb_uri = os.getenv('MONGODB_URI')
client = MongoClient(mongodb_uri, tlsCAFile=certifi.where())
print(client.list_database_names())
