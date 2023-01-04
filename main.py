from dotenv import load_dotenv
import os
import requests

def envoyer_timeline(abonnements:list)->None:
    load_dotenv()
    webhook = os.getenv("webhook")
    bearer_token = os.getenv("bearer_token")
    for arobase in abonnements:
        url = "https://api.twitter.com/1.1/statuses/user_timeline.json"
        headers = {
            "Authorization": f"Bearer {bearer_token}"
        }
        params = {
            "screen_name": arobase,
            "exclude_replies": True,
            "tweet_mode": "extended",
            "count": 500
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
                "color": 3092479,
                "thumbnail": {
                    "url": tweet["user"]["profile_image_url"]
                },
                "image": {
                    "url": images[0] if len(images)>0 else None
                }
            }]
            message = {
                "embeds": embeds
            }
            requests.post(webhook, json=message)

timeline = ["ndoki94_"]
envoyer_timeline(timeline)