import tweepy as tw 
import pandas as pd

api_key = ''
api_secret_key = ''
access_key =  ''
access_secret = ''

# set up authentication
auth = tw.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(access_key, access_secret)
api = tw.API(auth, wait_on_rate_limit=True)

# search to filter for
search_words = '#cdnpoli'

# set up cursor
tweets = tw.Cursor(api.search_tweets,
                   q=search_words + " -filter:retweets",
                   lang="en").items(10000)

# extract tweet data
tweet_data = [{'tweet_text': tweet.text, 
'tweet_favourite_count': tweet.favorite_count,
'tweet_created_at': tweet.created_at, 
'tweet_retweet_count': tweet.retweet_count,
'user_statuses_count': tweet.user.statuses_count, 
'user_screen_name': tweet.user.screen_name, 
'user_followers_count': tweet.user.followers_count,
} for tweet in tweets]


# save
print(tweets.num_tweets)
tweet_df = pd.DataFrame.from_records(tweet_data)
tweet_df.to_csv('tweets.csv')
