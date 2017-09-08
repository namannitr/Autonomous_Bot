import sys,os
import random
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
#from databaseImport.databaseConnect import dbConnect as dbConnect
from databaseImport.databaseUpdate import DbUpdate as dbUpdate
class Linker(object):

	def checkForExistingWhatsappId(self,whatsapp_id):
		dbUpdateObject=dbUpdate()
		listOfLinks=dbUpdateObject.selectWhatsappLinkId(whatsapp_id);
		if listOfLinks == None:
			return 0;
		#elif not whatsapp_id in listOfLinks:
			#return 0;
		return 1;
	####
	def returnEkoId(self,whatsapp_id,groupMessage):
		if self.checkForExistingWhatsappId(whatsapp_id):
			dbUpdateObject=dbUpdate();
			listOfLinks=dbUpdateObject.selectWhatsappLinkId(whatsapp_id);
			return listOfLinks[5];
		else:
			print "&&&&&&&&&&&&&&&&&&&&&&&&&&"
			dbUpdateObject=dbUpdate()
			print "@@@@@@@@@@@@@@@@@@@@", groupMessage
			if groupMessage==0:
				eko_Id="TEMP" + str(random.randrange(1000000000,9999999999))
			else:
				eko_Id="GRP" + str(random.randrange(1000000000,9999999999))

			if dbUpdateObject.selectEkoId(eko_Id) is not None:
				return self.returnEkoId(whatsapp_id)
			else:
				dbUpdateObject.insertWhatsappLinkId(whatsapp_id,eko_Id)
				return eko_Id
	
	def returnMessageSource(self):
		return 1;
	
	def returnMessageType(self,type):
		return type;
	
	def returnMessageStatus(self):
		return 0;
	####
	def returnWhatsappId(self,eko_id):
		print eko_id;
		dbUpdateObject=dbUpdate()
		relateId=dbUpdateObject.convertEkoIdtoOther(eko_id)
		return str(relateId[0])

