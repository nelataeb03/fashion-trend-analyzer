import requests
import csv
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

APP_ID = os.getenv('PINTEREST_APP_ID')
APP_SECRET = os.getenv('PINTEREST_APP_SECRET')
ACCESS_TOKEN = os.getenv('PINTEREST_ACCESS_TOKEN')

def get_access_token(app_id, app_secret, code):
    url = 'https://api.pinterest.com/v1/oauth/token'
    data = {
        'grant_type': 'authorization_code',
        'client_id': app_id,
        'client_secret': app_secret,
        'code': code
    }
    response = requests.post(url, data=data)
    return response.json()

def fetch_pins(query, access_token, max_pins=100):
    url = 'https://api.pinterest.com/v1/me/search/pins/'
    params = {
        'query': query,
        'access_token': access_token,
        'limit': max_pins
    }
    response = requests.get(url, params=params)
    if response.status_code != 200:
        raise Exception(f"Error fetching data: {response.status_code} {response.text}")
    data = response.json()
    pins = data.get('data', [])
    return pins

def save_to_csv(data, filename):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['ID', 'Link', 'Note', 'Image URL', 'Created At'])
        for row in data:
            writer.writerow([row['id'], row['link'], row['note'], row['image']['original']['url'], row['created_at']])

if __name__ == "__main__":
    QUERY = 'fashion trends'

    # Uncomment the following lines once you have the code and access token
    # CODE = 'CODE_FROM_REDIRECT_URL'
    # access_token_info = get_access_token(APP_ID, APP_SECRET, CODE)
    # ACCESS_TOKEN = access_token_info['access_token']

    # Fetch pins related to the query
    pins = fetch_pins(QUERY, ACCESS_TOKEN, max_pins=100)
    save_to_csv(pins, 'pinterest_pins.csv')
    print(f"Saved {len(pins)} pins to pinterest_pins.csv")