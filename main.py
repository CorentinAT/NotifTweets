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
    "screen_name": "rebeudeter",
    "exclude_replies": True,
    "tweet_mode": "extended",
}

response = requests.get(url, params=params, headers=headers)

req = response.json()

for tweet in req:
    print(f"{tweet}\n\n")
    media = []
    try:
        media = tweet["extended_entities"]["media"]
    except:
        pass

    images = []
    for image in media:
        images.append(image["media_url"])

    embeds = [{
        "description": tweet["full_text"],
        "title": tweet["user"]["name"]+f" (@{tweet['user']['screen_name']})",
        "image": {
            "url": images[0] if len(images)>0 else None
        }
    }]
    message = {
        "embeds": embeds
    }

    requests.post(webhook, json=message)