import requests

api_key = "YOUR_API_KEY_HERE"  # replace 
gene = input("Enter a gene name: ")

# GNews search endpoint
url = "https://gnews.io/api/v4/search"

params = {
    "q": gene,           # search query
    "lang": "en",        # language
    "max": 5,            # num of articles
    "apikey": api_key
}

response = requests.get(url, params=params)
data = response.json()

articles = data.get("articles")

if not articles:
    print("No articles found.")
else:
    print(f"\nTop news articles about {gene}:\n")
    for article in articles:
        print("-", article["title"])
