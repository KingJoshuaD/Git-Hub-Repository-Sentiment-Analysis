from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

ckey = '09c6gUUBS9BLrqOlOx1jxaEkT'
csecret = 'oxQWoVMem2E1tQ8dEwz1Slm8wxk354ajgkWbyijhuzfRAWZPyb'
atoken = '844855012966580227-Z7SdN2bNyHnPlu7WyWe2gcc5aQGSGsF'
asecret = '8rH2myLduz9zM8MWwzzDRTXtl3mEi5REDDN7tuIaO023w'

class listener(StreamListener) :
    def on_data(self,data) :
        print (data)
        return True

    def on_error(self, status) :
        print (status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())
twitterStream.filter(track=["car"])
