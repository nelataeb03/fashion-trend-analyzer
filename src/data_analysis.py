import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter

nltk.download('punkt')
nltk.download('stopwords')

def preprocess_text(text):
    tokens = word_tokenize(text.lower())
    tokens = [token for token in tokens if token.isalpha()]
    stop_words = set(stopwords.words('english'))
    tokens = [token for token in tokens if token not in stop_words]
    return tokens

def analyze_trends(posts):
    all_words = []
    for post in posts:
        tokens = preprocess_text(post['text'])
        all_words.extend(tokens)
    word_freq = Counter(all_words)
    return word_freq.most_common(10)

# Example usage
posts = [{'text': 'Loving the new summer fashion trends! #style #summerfashion'}, {'text': 'Check out these amazing outfits! #fashion'}]
trends = analyze_trends(posts)
print(f"Top trends: {trends}")
