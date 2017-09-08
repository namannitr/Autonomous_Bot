# This module is to start and run the whatsapp client continuously inspite of any error 
import receiveMessage

def initiateReceive():
	receiveMessage.receive()
	'''try:
		receiveMessage.receive()
	except:
		return 1;'''

if __name__=="__main__":
	while(1):
		tmp=initiateReceive()
