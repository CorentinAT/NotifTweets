from dotenv import load_dotenv
import os
import requests
import csv   

def send_tweet(tweet, arobase, webhook):
    try:
        tweet = tweet["retweeted_status"]
        retweet = 1
    except:
        retweet = 0
        pass
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
    if retweet==1:
        message["content"] = f"Retweeted by : **@{arobase}**"
    requests.post(webhook, json=message)


def send_timeline(timeline:list)->None:
    load_dotenv()
    webhook = os.getenv("webhook")
    bearer_token = os.getenv("bearer_token")
    tab = []
    try:
        with open("last_tweets.csv", "r", newline="") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                tab.append(row)
    except:
        pass
    with open("last_tweets.csv", "w", newline="") as csvfile:
        pass
    for arobase in timeline:
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
            "count": 500 if last_id != 0 else 30,
            "since_id": last_id if last_id!=0 else None
        }

        response = requests.get(url, params=params, headers=headers)
        req = response.json()

        for tweet in req:
            send_tweet(tweet, arobase, webhook)
        if len(req)>0:
            id_csv = req[0]["id"]
        else:
            for element in tab:
                if element[0]==arobase:
                    id_csv = element[1]
        with open("last_tweets.csv", "a", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([arobase, id_csv])

timeline = ["marc_le_marco", "archethic", "kingazo13", "Un4v5s8bgsVk9Xp"]
send_timeline(timeline)
