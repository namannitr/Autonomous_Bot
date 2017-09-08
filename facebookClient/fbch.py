import fbchat as fbchat
import time
import os,sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from databaseImport.databaseUpdate import DbUpdate as dbUpdate
from facebookEkoLinker import Linker as linker
lastSentId=0
#subclass fbchat.Client and override required methods
class EchoBot(fbchat.Client):
    lastSentId=0
    def __init__(self,email, password, debug=True, user_agent=None):
        fbchat.Client.__init__(self,email, password, debug, user_agent)

    def replyBack(self,replyToBeSent):
	print "NAMAN KUMAR AGARWAL \n\n\n\n"
    	global lastSentId;
	global FacebookID;
    	dbUpdateObject=dbUpdate()
	linkerObject=linker()
        for reply in replyToBeSent:
            if not reply[5]:
		print reply
		print "\n\n\n\n 	NAMAN KUMAR AGARWAL 5555555555555555\n\n\n\n\n"
	    	self.FacebookId=linkerObject.returnFacebookId(reply[1])
		print linkerObject.returnFacebookId(reply[1])
    	    	if(reply[5] == 0):
                	dbUpdateObject.updateResponseMessage(2,reply[0]);
                	lastSentId=reply[0]
                	#print "Sending %s to %s"%(reply[2]);
			#resp=reply[2]
                	self.send(unicode(self.FacebookID),reply[2])

    def on_message(self, mid, author_id, author_name, message, metadata):
	
	global lastSentId
        self.markAsDelivered(author_id, mid) #mark delivered
        self.markAsRead(author_id) #mark read

        #if you are not the author, echo
        if str(author_id) != str(self.uid):
		message_body = message
		message_sender= author_id
		linkerObject=linker()
		facebook_id=author_id
		message_sender= linkerObject.returnEkoId(facebook_id);
		#print message_sender
    		message_source=linkerObject.returnMessageSource();
    		message_type=linkerObject.returnMessageType(1);
    		message_status=linkerObject.returnMessageStatus();
    		message_destination=message_source;
    		dbUpdateObject=dbUpdate()
		dbUpdateObject.insertReceiveMessage(message_sender,message_body,message_source,message_type,message_status)
		time.sleep(1);
                #to pick only unprocessed message
		replyToBeSent= dbUpdateObject.selectResponseMessage(message_destination, lastSentId);
		#print "erwrfsufchxuchxuhc", replyToBeSent
		
		print "NAMAN KUMAR AGARWAL 1 \n\n\n\n"
		print type(author_id);
		print replyToBeSent
	        #self.replyBack(replyToBeSent)
        	for reply in replyToBeSent:
            		if not reply[5]:
    	    			if(reply[5] == 0):
                			dbUpdateObject.updateResponseMessage(2,reply[0]);
                			lastSentId=reply[0]
                			self.send(unicode(linkerObject.returnFacebookId(reply[1])),reply[2])

	        #print("%s said: %s"%(author_id, message))
		#print replyToBeSent;
		#self.send(author_id,message)

bot = EchoBot(EmailId, Password)
bot.listen()

