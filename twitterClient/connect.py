import tweepy,sys,os
from random import randrange
import time
import datetime
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import simplejson as json
import requests
from twitterEkoLinker import Linker as linker
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from databaseImport.databaseUpdate import DbUpdate as dbUpdate
lastSentId=0

consumer_key="08UM5RHMMTxHaPV4hjoOcrdqe"
consumer_secret="NVlOK5fYGlkowFfDMFoV8a6ISsPmZ9DNXYhoU3xSr43tgjWGIY"
access_token="1065033811-fNCcUof7Aa0s7n7QejgY5viWz52pA0kmQlO2c0h"
access_token_secret="CeLT86p8GM42SVHXvFhvz7s4eHgVV2WzBrVAGPnm18Oj5"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

class StdOutListener(StreamListener):
    """ A listener handles tweets are the received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """
    def replyBack(self,replyToBeSent):
    	global lastSentId;
    	dbUpdateObject=dbUpdate()
        for reply in replyToBeSent:
            print "RFwpldsgknsdknvsldkngsd"
            if not reply[5]:
	    	linkerObject=linker()
	    	twitterId=linkerObject.returnTwitterId(reply[1])
	    	print twitterId;
    	    	if(reply[5] == 0):
    	    		print "1234567543"
                	dbUpdateObject.updateResponseMessage(3,reply[0]);
                	lastSentId=reply[0]
                	screenName=screen_name(api.lookup_users(twitterId))
                	print screenName;
                	print "Sending %s to %s"%(reply[2],screenName);
                	mess=reply[2]+ " @" + screenName
			api.update_status(status=mess);
                	

    def on_data(self, data):
    	global lastSentId
        print "x"
        receiveTweet= json.loads(data)
        print receiveTweet['id']
	print receiveTweet['timestamp_ms']
	print receiveTweet['text']
	print receiveTweet['user']['id']
	print receiveTweet['user']['screen_name']
        #mess="Hello! @"+receiveTweet['user']['screen_name']
        #api.update_status(status=mess,in_reply_to_status_id=receiveTweet['id'])
        
	message_body= str(receiveTweet['text']).replace("@rohanuzumaki","");
	twitter_id= str(receiveTweet['user']['id'])
     	linkerObject=linker()
	message_sender= linkerObject.returnEkoId(twitter_id);
	print message_sender 
	message_source=linkerObject.returnMessageSource();
	message_type=linkerObject.returnMessageType(1);
	message_status=linkerObject.returnMessageStatus();
	message_destination=message_source;
	dbUpdateObject=dbUpdate()
	dbUpdateObject.insertReceiveMessage(message_sender,message_body,message_source,message_type,message_status)
	print("Receiving %s from %s" % (message_body,message_sender))
	time.sleep(2);

	#to pick only unprocessed message
	replyToBeSent= dbUpdateObject.selectResponseMessage(message_destination, lastSentId);
	self.replyBack(replyToBeSent)
        return True

    def on_error(self, status):
        print(status)
''' 
api.update_status(status="This is a tweet sent automatically by a Python script! (Don't worry, friends. I'm just testing my code.)")'''
'''twt = api.search(q="Hello World!")

user = api.me()
 
print('Name: ' + user.name)
print('Location: ' + user.location)
print('Friends: ' + str(user.friends_count))'''

l = StdOutListener()
apis = Stream(auth,l)
apis.filter(track=['@rohanuzumaki'])
'''
for mention in mentions:
    print mention.text
    print mention.user.id
    print mention.user.screen_name
    print mention.timestamp_ms
    print mention.created_at
    message="Hello! @"+mention.user.screen_name
    api.update_status(status=message,in_reply_to_status_id=mention.id_str)'''

