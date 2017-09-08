import os,sys
from sleekxmpp import ClientXMPP
from random import randrange
import time
import datetime
#from facebookEkoLinker import Linker as linker
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from databaseImport.databaseUpdate import DbUpdate as dbUpdate
from facebookEkoLinker import Linker as linker
lastSentId=0

class AliceBot(ClientXMPP):

    # the one and only ctor
    def __init__(self, jid, password, name):
        # init xmpp stuff
        ClientXMPP.__init__(self, jid, password)
        self.add_event_handler("session_start", self.session_start)
        self.add_event_handler("message", self.message)

        # init alice stuff

    # don't really understand what a session is
    def session_start(self, event):
        self.send_presence()
        print "session started"
        self.get_roster()

    def replyBack(self,msg,replyToBeSent,s):
    	global lastSentId;
    	dbUpdateObject=dbUpdate()
        for reply in replyToBeSent:
            if not reply[5]:
	    	getFacebookId=linker()
    	    	if(reply[5] == 0):
                	dbUpdateObject.updateResponseMessage(2,reply[0]);
                	lastSentId=reply[0]
                	print "Sending %s to %s"%(reply[2],s);
			resp=reply[2]
                	msg.reply(resp).send()



    # handle message with aiml response
    def message(self, msg):
	global lastSentId
        if msg['type'] in ('chat', 'normal'):
		message_body= str(msg['body']) 
		message_sender= str(msg['from']).split('@')[0]
	     	linkerObject=linker()
		facebook_id=str(msg['from']).split('@')[0]
		message_sender= linkerObject.returnEkoId(facebook_id);
		print message_sender
    		message_body=str(msg['body']) 
    		message_source=linkerObject.returnMessageSource();
    		message_type=linkerObject.returnMessageType(1);
    		message_status=linkerObject.returnMessageStatus();
    		message_destination=message_source;
    		dbUpdateObject=dbUpdate()
		dbUpdateObject.insertReceiveMessage(message_sender,message_body,message_source,message_type,message_status)
		print("Receiving %s from %s" % (msg['body'],msg['from']))
                s=msg['from']
        	time.sleep(2);
        
        	#to pick only unprocessed message
        	replyToBeSent= dbUpdateObject.selectResponseMessage(message_destination, lastSentId);
		print "erwrfsufchxuchxuhc", replyToBeSent
        	self.replyBack(msg,replyToBeSent,s)





   

            # get response
            # super easy sessions!
            #resp = self._k.respond(msg['body'], msg['from'])

            # try to not look like a bot?
            #time.sleep(randrange(0,3))

            # reply
      

