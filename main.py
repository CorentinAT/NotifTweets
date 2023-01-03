from dotenv import load_dotenv
import os
import requests

load_dotenv()
webhook = os.getenv("webhook")

headers = {
    "Authorization": "Bearer "+os.getenv("bearer_token")
}

url = "https://api.twitter.com/1.1/statuses/user_timeline.json"
params = {
    "screen_name": "cocosupersympa",
    "exclude_replies": True,
    "tweet_mode": "extended",
    "count": 1,
}

response = requests.get(url, params=params, headers=headers)

req = response.json()

for tweet in req:
    media = []
    texte = tweet["full_text"]
    try:
        media = tweet["extended_entities"]["media"]
    except:
        pass

    images = []
    for image in media:
        images.append(image["media_url"])

    embeds = [{
        "description": texte,
        "title": "tweet",
        "image": {
            "url": images[0]
        }
    },
    {
        "image": {
            "url": images[1]
        }
    }]
    message = {
        "embeds": embeds
    }

    requests.post(webhook, json=message)tt