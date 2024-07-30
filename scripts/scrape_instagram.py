import instaloader
import logging
import os
from dotenv import load_dotenv
import time

# Load environment variables from .env file
load_dotenv()

# Get Instagram credentials from environment variables
username = os.getenv('INSTAGRAM_USERNAME')
password = os.getenv('INSTAGRAM_PASSWORD')

# List of top 20 fashion profiles
fashion_profiles = [
    'weworewhat', 'camilacoelho', 'chiaraferragni', 'aimeesong', 'oliviapalermo',
    'carodaur', 'leoniehanne', 'ireneisgood', 'sincerelyjules', 'rubylyn',
    'devapollon', 'matildadjerf', 'alexachung', 'emmahill', 'oliviajade',
    'lauraharrier', 'galagonzalez', 'evameloche', 'jessicawang', 'lilychee'
]

# Configure logging
logging.basicConfig(level=logging.INFO)

# Create an instance of Instaloader
L = instaloader.Instaloader()

# Login to Instagram
try:
    L.login(username, password)
except Exception as e:
    logging.error(f'Error logging in: {e}')
    exit()

# Scrape posts from each profile
for profile_name in fashion_profiles:
    logging.info(f'Starting to scrape profile: {profile_name}')
    try:
        profile = instaloader.Profile.from_username(L.context, profile_name)
    except instaloader.exceptions.ProfileNotExistsException as e:
        logging.error(f'Profile not found: {e}')
        continue
    except Exception as e:
        logging.error(f'Error retrieving profile: {e}')
        continue

    # Create target directory if it doesn't exist
    target_dir = f'data/images/{profile_name}'
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    # Download the 50 most recent posts
    post_count = 50
    logging.info(f'Profile {profile_name} - downloading {post_count} most recent posts.')
    start_time = time.time()

    for i, post in enumerate(profile.get_posts(), 1):
        if i > post_count:
            break
        try:
            L.download_post(post, target=target_dir)
            logging.info(f'Downloaded post {i}/{post_count} from {profile_name}')
        except Exception as e:
            logging.error(f'Error downloading post: {e}')

        # Sleep to prevent rate limiting
        time.sleep(1)

    elapsed_time = time.time() - start_time
    logging.info(f'Finished scraping profile: {profile_name} in {elapsed_time:.2f} seconds')

logging.info('Finished scraping all profiles.')
