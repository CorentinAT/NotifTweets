from dotenv import load_dotenv
import os
import requests
import csv

def envoyer_timeline(abonnements:list)->None:
    load_dotenv()
    webhook = os.getenv("webhook")
    bearer_token = os.getenv("bearer_token")
    tab = []
    try:
        with open("derniers_tweets.csv", "r", newline="") as fichiercsv:
            reader = csv.reader(fichiercsv)
            for row in reader:
                tab.append(row)
    except:
        pass
    with open("derniers_tweets.csv", "w", newline="") as fichiercsv:
        pass
    for arobase in abonnements:
        last_id = 0
        for element in tab:
            if element[0] == arobase:
                last_id = element[1]
        url = "https://api.twitter.com/1.1/statuses/user_timeline.json"
        headers = {
            "Authorization": f"Bearer {bearer_token}"
        }
        params = {
            "screen_name": arobase,
            "exclude_replies": True,
            "tweet_mode": "extended",
            "count": 500,
            "since_id": last_id if last_id!=0 else None
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
        if len(req)>0:
            id_csv = req[0]["id"]
        else:
            for element in tab:
                if element[0]==arobase:
                    id_csv = element[1]
        with open("derniers_tweets.csv", "a", newline="", encoding="utf-8") as fichiercsv:
            writer = csv.writer(fichiercsv)
            writer.writerow([arobase, id_csv])

timeline = ["marc_le_marco", "archetic", "arkunir", "rebeudeter", "kingazo13", "aminematue", "ndoki94_"]
envoyer_timeline(timeline)
