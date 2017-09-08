import sys,os
import random
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
#from databaseImport.databaseConnect import dbConnect as dbConnect
from databaseImport.databaseUpdate import DbUpdate as dbUpdate
class Linker(object):

	def checkForExistingFacebookId(self,facebook_id):
		dbUpdateObject=dbUpdate()
		listOfLinks=dbUpdateObject.selectFacebookLinkId(facebook_id);
		if listOfLinks == None:
			return 0;
		#elif not facebook_id in listOfLinks:
			#return 0;
		return 1;
	####
	def returnEkoId(self,facebook_id):
		if self.checkForExistingFacebookId(facebook_id):
			dbUpdateObject=dbUpdate()
			listOfLinks=dbUpdateObject.selectFacebookLinkId(facebook_id);
			return listOfLinks[5];
		else:
			dbUpdateObject=dbUpdate()
			temp="TEMP" + str(random.randrange(1000000000,9999999999))
			if dbUpdateObject.selectEkoId(temp) is not None:
				return self.returnEkoId(facebook_id)
			else:
				dbUpdateObject.insertFacebookLinkId(facebook_id,temp)
				return temp
	
	def returnMessageSource(self):
		return 2;
	
	def returnMessageType(self,type):
		return type;
	
	def returnMessageStatus(self):
		return 0;
	####
	def returnFacebookId(self,eko_id):
		print "NAMAN KUMAR AGARWAL 3 \n\n\n\n"
		dbUpdateObject=dbUpdate()
		relate_id=dbUpdateObject.convertEkoIdtoOther(eko_id)
		print relate_id
		return str(relate_id[1])







