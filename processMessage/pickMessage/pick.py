#This module is to pick message from received table and send it to brain for processing
import os,sys,time,MySQLdb
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from brain.brain import Brain
from bot.session import Session
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
from databaseImport.databaseUpdate import DbUpdate as dbUpdate
from dumpMessage.dump import Dump


#class PickMessage(object):


def pickAndProcess(dbUpdateObject,sessionObject,brainObject, dumpObject):
	l=dbUpdateObject.selectResponseMessageLastEntry()
	if(l!=None):
		l=dbUpdateObject.selectReceiveMessageById(str(l[0]));
	else:
		l=dbUpdateObject.selectReceiveMessageAll();
	for item in l:
		brainObject.brain1(dbUpdateObject,sessionObject,item, dumpObject)

if __name__ =="__main__":
	dbUpdateObject=dbUpdate()
	sessionObject=Session();
	brainObject=Brain();
	dumpObject=Dump();
	#pickObject=PickMessage();
	sessionObject.learn();
	while(1):
		pickAndProcess(dbUpdateObject,sessionObject,brainObject, dumpObject);
		time.sleep(1);
