#Processing the received message, calling AIML to respond and dumping the message in response table
import MySQLdb,sys,os,datetime,marshal
from smiliSub import SmiliSub
from ekofunction.apicall.Bank import main
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from bot import aiml
from dumpMessage.dump import Dump
from ekofunction import pickrequest
from ekofunction.apicall import register as register
from ekofunction.apicall import addmoney

class Brain(object):

	#checking if there is a pending request of the user from the process_request table
	def pendingRequest(self,dbUpdateObject,item):
		l=dbUpdateObject.selectPendingRequest(item)
		if l == None :
			return 0;
		else:
			return 1;

	def displayCancelRequest(self,dbUpdateObject,sessionObject,botResponse,item):
		return dbUpdateObject.displayCancelRequest(dbUpdateObject,sessionObject,botResponse,item)

	def cancelRequest(self,dbUpdateObject,sessionObject,botResponse,item):
		dbUpdateObject.deletePendingRequest(item);
		return "Your pending request is cancelled.";

	def continueRequest(self,dbUpdateObject,sessionObject,botResponse,item):
		return dbUpdateObject.continuePendingRequest(dbUpdateObject,sessionObject,botResponse,item);

	def newRequest(self,dbUpdateObject,sessionObject,botResponse,item):
		print botResponse+"Response 3";
		if self.pendingRequest(dbUpdateObject,item):
			print botResponse+"Response 4";
			return dbUpdateObject.updatePendingRequest(dbUpdateObject,sessionObject,botResponse,item);
			print botResponse+"Response 5";
		x=dbUpdateObject.insertPendingRequest(dbUpdateObject,sessionObject,botResponse,item);
		return x;

	def completePendingRequest(self,dbUpdateObject,sessionObject,item):
		return dbUpdateObject.completePendingRequest(dbUpdateObject,sessionObject,item)

	def addMoney(self,dbUpdateObject,sessionObject,item):
		return addmoney.addmoneywithamount(item[1],5)



	# def groupCustomerForWhatsapp(self,dbUpdateObject,sessionObject,item):
	# 	smiliSubObject=SmiliSub();
	# 	print "message body dhsidhidisjdkdsjsjidsiadji" , item[2]
	# 	groupID = item[1]
	# 	item=list(item)
	# 	item[1] = item[2].split("@")[1]
	# 	item[2] = item[2].split("@")[0]
	# 	item=tuple(item)
	# 	customerType=item[1][:3]
	# 	print customerType
	# 	if customerType=="TEM":
	# 		return self.temporaryCustomer(dbUpdateObject,sessionObject,item);
	# 	elif customerType=="EKO":
	# 		return self.existingCustomer(dbUpdateObject,sessionObject,item);










	def temporaryCustomer(self,dbUpdateObject,sessionObject,item):
		smiliSubObject=SmiliSub();
		sessionObject.write_session(item)
		if sessionObject.firsttime==1:
			setbotname=sessionObject.respond("defaultname",item[1])
			#balance check api to check if new user then only the next line follows
			botResponse=sessionObject.respond("new user",item[1])
			#uncomment the next line after balance check api is ready
			#botResponse=session.respond(item[2],item[1])
			sessionObject.firsttime=0
		else:
			botResponse=sessionObject.respond(item[2],item[1]);

		if botResponse[0]=='#':
			if botResponse[0:6]=="#reg##":
				botResponse=sessionObject.respond("Register name",item[1])

			elif botResponse[0:4]=="#reg":
				name=botResponse.split("#")[2]
				r, eko_id=register.register(name,item[1],dbUpdateObject,sessionObject)
				botResponse=sessionObject.respond("Registrationsuccessful",item[1])
				item=list(item)
				item[1]=eko_id
				item=tuple(item)
				print item
				print "printing Item"

			elif '#sync' in botResponse:
				eko_id = botResponse.split(' ')[1]
				relateId = dbUpdateObject.convertEkoIdtoOther(item[1])
				print relateId
				if item[3]==1:
					dbUpdateObject.insertWhatsappId(eko_id,relateId[0])
				elif item[3]==2:
					print "vyom", item[3]
					dbUpdateObject.insertFacebookId(eko_id,relateId[1])
				dbUpdateObject.deleteTempId(item[1])
				botResponse = sessionObject.respond("syncedaccount",item[1])
				item=list(item)
				item[1]=eko_id
				item=tuple(item)
			else :
				botResponse="You are not Registered yet.\n" + sessionObject.respond("Register name",item[1])

		botResponse = botResponse.replace("###","\n");
		botResponse= smiliSubObject.replaceSmili(botResponse,item);
		if botResponse==None:
			botResponse="Sorry"
		return (botResponse, item)





	def existingCustomer(self,dbUpdateObject,sessionObject,item):
		print "Naman 1";
		smiliSubObject=SmiliSub();
		print "Naman 2";
		sessionObject.write_session(item)
		print "Naman 3";
		botResponse=sessionObject.respond(item[2],item[1])
		print "Naman 4";


		if botResponse =='' or botResponse==None:
			botResponse="I don't know what you are talking about"

		elif "I have got your 5 bucks." in botResponse:
			self.addMoney(dbUpdateObject,sessionObject,item);

		elif botResponse[0]=='#':
			if "#reg" in botResponse:
				botResponse="Buddy you are already registered"

			elif "#candisplay" in botResponse:
				botResponse=self.displayCancelRequest(dbUpdateObject,sessionObject,botResponse,item);

			elif "#cancel" in botResponse:
				botResponse=self.cancelRequest(dbUpdateObject,sessionObject,botResponse,item);

			elif "#continue" in botResponse:
				botResponse=self.continueRequest(dbUpdateObject,sessionObject,botResponse,item);


			else:
				print botResponse+"Response 1";
				botResponse=self.newRequest(dbUpdateObject,sessionObject,botResponse,item);
				print botResponse+"Response 2";

		else:
			if self.pendingRequest(dbUpdateObject,item):
				botResponse=self.completePendingRequest(dbUpdateObject,sessionObject,item);

			elif "50/50" in botResponse:
				self.creditGameWin(dbUpdateObject,sessionObject,item);
		botResponse = botResponse.replace("###","\n");
		botResponse= smiliSubObject.replaceSmili(botResponse,item);
		if botResponse==None:
			botResponse="Sorry"
		return (botResponse,item)




	#main  function
	def brain1(self,dbUpdateObject,sessionObject,item, dumpObject):
		#dumpObject=Dump();
		customerType=item[1][:3]
		print customerType
		if customerType=="TEM":
			l = self.temporaryCustomer(dbUpdateObject,sessionObject,item);
			print l
			item=l[1]
			botResponse=l[0]
		elif customerType=="EKO":
			l = self.existingCustomer(dbUpdateObject,sessionObject,item);
			botResponse = l[0]
		#else:
		#	l = self.groupCustomerForWhatsapp(dbUpdateObject,sessionObject,item);
		#	botResponse = l[0]

		dumpObject.dump(dbUpdateObject,botResponse,item);
