import urllib2
from Bank import main
import os,sys
import random
#sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
#from databaseImport.databaseUpdate import dbUpdate as dbUpdate
def register(name,eko_id,dbUpdateObject,sessionObject):
	'''url='http://59.162.111.216/eko/cellrequest.do?method=handle&originationAddress=1919191919&sendSms=1&requestText=123&source=CONNECT'
	req = urllib2.Request(url)
	response = urllib2.urlopen(req)
	the_page = response.read()'''
	new_id = tempIdtoEkoId(eko_id,dbUpdateObject)
	renameSessionFile(sessionObject,eko_id, new_id)
	sessionObject.respond("storeekoid " + new_id, new_id)
	print "sdsDSDdddddddddddddddddddddddddddddddd", name
	sessionObject.respond("my name is " + str(name),new_id)
	#sessionObject.learnSingleSession(new_id+".ses");
	return main.create_wallet(new_id,name), new_id;
	return "Registering Mobile number " + str(number) + " with name " + str(item_pr[2])+ " for Eko wallet \n This is the testing version";

###########
def tempIdtoEkoId(eko_id,dbUpdateObject):
	new_id = "EKO" + str(random.randrange(1000000000,9999999999))
	if dbUpdateObject.selectEkoId(new_id) is not None:
		return tempIdtoEkoId(eko_id,dpUpdateObject)
	else:
		dbUpdateObject.updateTempIdtoEkoId(eko_id,new_id)
		return new_id

def renameSessionFile(sessionObject,eko_id,new_id):
	path = '../bot/User_Sessions/'
	directory = os.path.abspath(path)
	print eko_id
	print directory
	os.rename(os.path.join(directory, eko_id +'.ses'), os.path.join(directory, new_id +'.ses'))
	sessionObject.learnSingleSession(new_id+'.ses');


