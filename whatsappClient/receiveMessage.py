#to receive and send message on whats app
import sys,os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from whatsappClient.receive_stack import YowsupEchoStack


def receive():
	obj = YowsupEchoStack()
	obj.start()
