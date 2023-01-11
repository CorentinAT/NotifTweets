# NotifTweets

Program that sends a given twitter timeline to discord via a webhook.

It uses the twitter api version 1.1, and the discord webhook api.

## Status

Not finished (~40%)

## Done

### 03/01/2023
- Retrieve all tweets from a selected tweet, with all necessary information (arobase, tn, pp, text content of the tweet)
- Formatting of the tweet for embedding on discord
- Retrieve and send the first image of the tweet

### 04/01/2023
- Works with a list of arobases
- Save the last tweet sent by arobase in the file "derniers_tweets.csv" so that it is not sent back the next time it is executed

### 11/01/2023
- Taking into account of retweets : sending of the retweeted tweet with, in addition, the arobase of the person who retweeted it

## To do

- Separate the code into several functions to make it cleaner
- Take into account the quoted tweets
- Get all the images of the tweet
- Make the requests asynchronous to have a mixed timeline, and a faster executions
