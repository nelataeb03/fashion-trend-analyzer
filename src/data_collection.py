from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import csv
import time

# returns list containing all post URLs under a specified hashtag
def fetch_instagram_data(hashtag, max_posts=1000):
    url = f"https://www.instagram.com/explore/tags/{hashtag}/"
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get(url)
    posts = []
    while len(posts) < max_posts:
        try:
            # Scroll down to load more posts
            driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
            time.sleep(2)  # Wait for posts to load
            
            # Adjusted selector to be more general
            new_posts = driver.find_elements(By.CSS_SELECTOR, 'article a')
            print(f"Found {len(new_posts)} new posts")  # Debugging line
            
            for post in new_posts:
                link = post.get_attribute('href')
                if link not in posts:
                    posts.append(link)
                if len(posts) >= max_posts:
                    break
            print(f"Collected {len(posts)} posts so far...")
        except Exception as e:
            print(f"Error fetching data: {e}. Retrying...")
            time.sleep(5)  # Wait longer before retrying
    driver.quit()
    return posts

def save_to_csv(data, filename):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Post URL'])
        for row in data:
            writer.writerow([row])

if __name__ == "__main__":
    hashtags = ['fashiontrends']
    all_posts = []
    for hashtag in hashtags:
        posts = fetch_instagram_data(hashtag, max_posts=1000)
        all_posts.extend(posts)
    save_to_csv(all_posts, 'instagram_posts.csv')
    print(f"Saved {len(all_posts)} posts to instagram_posts.csv")





