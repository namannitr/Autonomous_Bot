import sys,os
from validate import Validate
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
#from Database_Import.db_config import dbconfiguration
import dictonary,brain
#from brain import Brain as brain
#from databaseImport.databaseUpdate import DbUpdate as dbUpdate

class PickRequest(object):

	def messageSplit(self,botResponse):
		return botResponse.split('#')
		
	def pickRequest(self,dbUpdateObject,sessionObject,botResponse,item):
		print botResponse+"Response 8";
		validateObject=Validate();
		info=self.messageSplit(botResponse)
		print botResponse+"Response 9";
					
		req_fields=dictonary.required_fields[info[1]].split('&')
		bot_qry=dictonary.bot_query;
		func_map=dictonary.function_map;
		print botResponse+"Response 10";
		for i in range(0,(len(req_fields)-2)):
			info[i+2]=validateObject.validate(i,info[i+2])
			print botResponse+"Response 11";
			if str(info[i+2]) == '0' or info[i+2] == 0.0 or str(info[i+2])=='' :
				print botResponse+"Response 12";
				print bot_qry[req_fields[i+1]]
				print item[1]
				x=sessionObject.respond(bot_qry[req_fields[i+1]],item[1])
				print x;
				return x;

		temp=func_map[req_fields[len(req_fields)-1]](info,item[1],dbUpdateObject,sessionObject) ##########
		print "Naman Agarwal\n\n"+temp+"\n\n"
		dbUpdateObject.deletePendingRequest(item);
		return temp

	def responseIncompleteRequest(self,dbUpdateObject,sessionObject,botResponse,item):
		reply=dbUpdateObject.selectPendingRequest(item)
		if reply==None:
			return ("No request pending\n","Eko Help");
		else:
			l=reply[1].split('#')
			for i in range(0,len(l)):
				if l[i]=='0':
					l[i]=".....";	
			if l[1]=='reg':
				response = " Buddy, your Registration is incomplete."
				botResponse="pendingregrequest"
			elif l[1]=='send':
				response = " Buddy, your previous request for sending INR " + str(l[3]) + " to " + str(l[4])+ " is incomplete"
				botResponse="pendingsendrequest"
			elif l[1]=='rech':
				response= " Buddy, your previous request for recharching phone number " + str(l[4]) + " with INR." + str(l[3])+ " is incomplete"
				botResponse="pendingrechrequest"
			elif l[1]=='add':
				response= "Buddy, your previous request for adding INR " + str(l[3]) + " is incomplete"
				botResponse="pendingaddrequest"
			else:
				response="";
				botResponse="Register name";
			return response+ sessionObject.respond(botResponse,item[1])
