
import re
import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

#start process_tweet
def processTweet(tweet):
    # process the tweets

    #Convert to lower case
    tweet = tweet.lower()
    #Convert www.* or https?://* to URL
    tweet = re.sub('((www\.[^\s]+)|(https?://[^\s]+))','URL',tweet)
    #Convert @username to AT_USER
    tweet = re.sub('@[^\s]+','AT_USER',tweet)
    #Remove additional white spaces
    tweet = re.sub('[\s]+', ' ', tweet)
    #Replace #word with word
    tweet = re.sub(r'#([^\s]+)', r'\1', tweet)
    #trim
    tweet = tweet.strip('\'"')
    return tweet
#end

ckey = 'JYoBFQLUpUN4LWxbR5Z1qOyMN'
csecret = 'alA8yeZmTqWQFWCZ14a6xk0X7JUDRtAjcPVF7Ust7spoIExFPF'
atoken ='844855012966580227-Z7SdN2bNyHnPlu7WyWe2gcc5aQGSGsF'
asecret = '8rH2myLduz9zM8MWwzzDRTXtl3mEi5REDDN7tuIaO023w'

class listener(StreamListener):
    def on_data(self, data):
        print(data)
        return True
    def on_error(self, status):
        print(status)


auth = OAuthHandler(ckey, csecret)
api = tweepy.API(auth)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())
#twitterStream.filter(track=["King"])
timeline = api.user_timeline(user_id=['844855012966580227'])
test = api.lookup_users(user_ids=['844855012966580227'])

for status in tweepy.Cursor(api.home_timeline).items(10):
    # Process a single status
    print('Raw Tweet')
    print(status.text)
    processedTweet = processTweet(status.text)
    print ('Proceeded Tweet')
    print(processedTweet)

#f = open('tweets.txt', 'w')
#f.write(timeline)
print(timeline)
for user in test:

    print(user.screen_name)
    print (user.name)
    print (user.description)
    print (user.followers_count)
    print (user.statuses_count)
    print (user.url)

    f = open('username.txt', 'w')
    f.write(user.name)
    f = open('screenname.txt', 'w')
    f.write(user.screen_name)
    f = open('statuses_count.txt', 'w')
    f.write(str(user.statuses_count))
    f = open('description.txt', 'w')
    f.write(user.description)

    f.close()
