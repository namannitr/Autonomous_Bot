#!/usr/bin/python
import sleekxmpp
import bot2
import signal
import sys
#import logging
#logging.basicConfig(level=logging.DEBUG)

#if len(sys.argv) != 2: sys.exit("usage: chat.py password")

password = "Nam@1695!!!!"
jid = 'minkoooooooo@chat.facebook.com'#write facebook user name in place of facebookusername
server = ('chat.facebook.com', 5222)

chatbot = bot2.AliceBot(jid,password,"Alice")
chatbot.auto_reconnect = True
chatbot.connect(server)
chatbot.process(block=False)

# exit with grace
def sigint_handler(signal, frame):
        print "exit time"

        global chatbot
        chatbot.disconnect(wait=True)        
        sys.exit(0)

signal.signal(signal.SIGINT, sigint_handler)

while True:
    pass
