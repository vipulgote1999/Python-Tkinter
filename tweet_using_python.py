import tweepy

#personal details
consumer_key="XXXXXXXXXXXXXXXXXX"
consumer_secret="XXXXXXXXXXXXXXX"
access_token="XXXXXXXXXXXXXXXX"
access_token_secret="XXXXXXXXXXXXXXXXXXXX"
#authentication of consumer key and secret
auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
#authentication of access token and secret
auth.set_Access_token(access_token,access_token_secret)
api=tweepy.API(auth)

#update this statud in twutter 

api.update_status(status="Hello Everyone this meassage is from python")
