import sys,os
import random
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
#from databaseImport.databaseConnect import dbConnect as dbConnect
from databaseImport.databaseUpdate import DbUpdate as dbUpdate
class Linker(object):

	def checkForExistingTwitterId(self,twitter_id):
		dbUpdateObject=dbUpdate()
		listOfLinks=dbUpdateObject.selectTwitterLinkId(twitter_id);
		if listOfLinks == None:
			return 0;
		#elif not twitter_id in listOfLinks:
			#return 0;
		return 1;
	####
	def returnEkoId(self,twitter_id):
		if self.checkForExistingTwitterId(twitter_id):
			dbUpdateObject=dbUpdate()
			listOfLinks=dbUpdateObject.selectTwitterLinkId(twitter_id);
			return listOfLinks[5];
		else:
			dbUpdateObject=dbUpdate()
			temp="TEMP" + str(random.randrange(1000000000,9999999999))
			if dbUpdateObject.selectEkoId(temp) is not None:
				return self.returnEkoId(twitter_id)
			else:
				dbUpdateObject.insertTwitterLinkId(twitter_id,temp)
				return temp
	
	def returnMessageSource(self):
		return 3;
	
	def returnMessageType(self,type):
		return type;
	
	def returnMessageStatus(self):
		return 0;
	####
	def returnTwitterId(self,eko_id):
		dbUpdateObject=dbUpdate()
		relate_id=dbUpdateObject.convertEkoIdtoOther(eko_id)
		return str(relate_id[2])







