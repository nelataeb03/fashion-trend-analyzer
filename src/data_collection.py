import requests
from bs4 import BeautifulSoup

def fetch_instagram_data(hashtag):
    url = f"https://www.instagram.com/explore/tags/{hashtag}/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    posts = soup.find_all('div', {'class': 'v1Nh3 kIKUG  _bz0w'})
    data = []
    for post in posts:
        link = post.find('a')['href']
        data.append(f"https://www.instagram.com{link}")
    return data

if __name__ == "__main__":
    hashtags = ['fashion', 'style']
    for hashtag in hashtags:
        posts = fetch_instagram_data(hashtag)
        print(f"Posts for #{hashtag}: {posts}")
