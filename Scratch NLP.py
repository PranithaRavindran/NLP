#let make things easier with preload dataset
import nltk
from nltk.corpus import twitter_samples

# Download the Twitter Samples corpus if not already downloaded
nltk.download('twitter_samples')

# Load positive and negative tweets from the Twitter Samples corpus
#lead o/p
positive_tweets = twitter_samples.strings('positive_tweets.json')
negative_tweets = twitter_samples.strings('negative_tweets.json')

# Print some examples of positive and negative tweets
print("Positive tweets:")
for tweet in positive_tweets[:2]:
    print("-", tweet)

print("\nNegative tweets:")
for tweet in negative_tweets[:2]:
    print("-", tweet)
