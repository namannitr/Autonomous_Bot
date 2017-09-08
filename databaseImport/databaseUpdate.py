import os,sys
from .databaseConnect import DbConnect
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from processMessage.brain.ekofunction.pickrequest import PickRequest as pickRequest
db=DbConnect.db
cursor=db.cursor()

class DbUpdate():

	def displayCancelRequest(self,dbUpdateObject,sessionObject,botResponse,item):
		pickRequestObject=pickRequest();
		return pickRequestObject.responseIncompleteRequest(dbUpdateObject,sessionObject,botResponse,item)
	
	def completePendingRequest(self,dbUpdateObject,sessionObject,item):
		pickRequestObject=pickRequest();
		return pickRequestObject.responseIncompleteRequest(dbUpdateObject,sessionObject,' ',item)

	def databaseCommit(self):
		db.commit();

	def insertReceiveMessage(self,eko_id,message_body,message_source,message_type,message_status):
		cursor.execute("insert into received_message (`eko_id`, `message_body`, `message_source`, `message_type`, `message_status`) values ( %s, %s, %s, %s, %s)", (eko_id,message_body,message_source,message_type,message_status));
		db.commit();
		
	def insertResponseMessage(self,message_id,eko_id,message_body,message_destination,message_type):
		print "naman"
		cursor.execute("insert into response_message (message_id, eko_id, message_body, message_destination, message_type) values(%s, %s, %s, %s, %s)", (message_id,eko_id,message_body,message_destination,message_type));
		db.commit();
		
	def selectResponseMessage(self,message_destination,lastSentId):
		db.commit();
		cursor.execute("SELECT * FROM response_message where message_destination= "+ str(message_destination) + " and message_id > " + str(lastSentId));
        	l=cursor.fetchall();
        	db.commit();
        	return l;
        	
        
        def updateResponseMessage(self,message_destination,message_id):
        	cursor.execute("UPDATE response_message SET message_state = 1 WHERE  message_destination= "+ str(message_destination) + " and message_id= " + str(message_id));
        	db.commit();
        
        def selectWhatsappLinkId(self,whatsapp_id):
        	cursor.execute("SELECT * FROM id_link where whatsapp_id = '"+ whatsapp_id+"'");
        	l=cursor.fetchone();
        	db.commit();
		return l;
        def selectFacebookLinkId(self,facebook_id):
        	cursor.execute("SELECT * FROM id_link where facebook_id = '"+ facebook_id+"'");
        	l=cursor.fetchone();
        	db.commit();
		return l;	
        def selectResponseMessageLastEntry(self):
        	cursor.execute("""SELECT * FROM response_message order by message_id desc""");
		l=cursor.fetchone();
		db.commit();
		return l;
		
	def selectReceiveMessageById(self,message_id):
        	cursor.execute("SELECT * FROM received_message where message_id > " + str(message_id));
        	l=cursor.fetchall();
        	db.commit();
		return l;
        	
        def selectReceiveMessageAll(self):
        	cursor.execute("""SELECT * FROM received_message """);
		l=cursor.fetchall();
		db.commit();
		return l;
	
	def deletePendingRequest(self,item):
		cursor.execute("DELETE FROM pending_request WHERE eko_id = '" + str(item[1])+"'");
		db.commit();
	
	def insertPendingRequest(self,dbUpdateObject,sessionObject,botResponse,item):
		pickRequestObject=pickRequest()
		print botResponse+"Response 6";
		split_Request=botResponse.split('#')
		print botResponse+"Response 7";
		cursor.execute("INSERT INTO `pending_request`(`eko_id`, `request`, `complete_flag`, `status_flag`) VALUES (%s,%s,%s,%s)", (item[1],botResponse,0,0));
		db.commit();
		print botResponse+"Response 8";
		x= pickRequestObject.pickRequest(dbUpdateObject,sessionObject,botResponse,item);
		return x;
		
	def updatePendingRequest(self,dbUpdateObject,sessionObject,botResponse,item):
		self.deletePendingRequest(item);
		return self.insertPendingRequest(dbUpdateObject,sessionObject,botResponse,item);
	
	def selectPendingRequest(self,item):
		query="SELECT * FROM pending_request WHERE complete_flag = 0 AND eko_id = '" + str(item[1]+"'")
		print query
		cursor.execute(query);
		l=cursor.fetchone()
		db.commit();
		return l;
	#####
	def selectEkoId(self,eko_id):
        	cursor.execute("SELECT * FROM id_link where eko_id = '"+ eko_id+"'");
        	l=cursor.fetchone()
        	db.commit();
		return l;
	######
	def insertWhatsappLinkId(self,whatsapp_id, eko_id):
		cursor.execute("INSERT INTO id_link (`whatsapp_id`,`eko_id`) VALUES (%s, %s)", (whatsapp_id,eko_id));
		db.commit()

	def insertFacebookLinkId(self,facebook_id, eko_id):
		cursor.execute("INSERT INTO id_link (`facebook_id`,`eko_id`) VALUES (%s, %s)", (facebook_id,eko_id));
		db.commit()

	###### Function to convert eko_id to whatsapp_id
	def convertEkoIdtoOther(self,eko_id):
        	cursor.execute("SELECT * FROM id_link where eko_id = '"+ eko_id+"'");
        	l=cursor.fetchone();
        	db.commit();
		return l;

	

	################################
	def updateTempIdtoEkoId(self,eko_id,new_id):
        	cursor.execute("UPDATE id_link  SET eko_id = '" + str(new_id) + "' WHERE eko_id = '" + eko_id + "'")
               	db.commit();
	#############################
	def insertWhatsappId(self,eko_id,whatsapp_id):
		cursor.execute("UPDATE id_link SET whatsapp_id = '" + str(whatsapp_id) + "' WHERE eko_id = '" + eko_id + "'") ;
		db.commit()

	def insertFacebookId(self,eko_id,facebook_id):
		cursor.execute("UPDATE id_link SET facebook_id = '" + str(facebook_id) + "' WHERE eko_id = '" + eko_id + "'") ;
		db.commit()
	################################
	def deleteTempId(self,eko_id):
		cursor.execute("DELETE FROM id_link WHERE eko_id = '" + eko_id +"'");
		db.commit();

