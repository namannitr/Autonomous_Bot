from yowsup.layers.interface                           import YowInterfaceLayer, ProtocolEntityCallback
from yowsup.layers.protocol_messages.protocolentities  import TextMessageProtocolEntity
from yowsup.layers.protocol_media.protocolentities  import ImageDownloadableMediaMessageProtocolEntity
from yowsup.layers.protocol_receipts.protocolentities  import OutgoingReceiptProtocolEntity
from yowsup.layers.protocol_media.protocolentities  import LocationMediaMessageProtocolEntity
from yowsup.layers.protocol_acks.protocolentities      import OutgoingAckProtocolEntity
from yowsup.layers.protocol_media.protocolentities  import VCardMediaMessageProtocolEntity
from yowsup.layers.protocol_media.protocolentities  import AudioDownloadableMediaMessageProtocolEntity
from speech_recognition_master import speech_recognition as sr
import os,sys,commands,signal,MySQLdb,datetime,time
from whatsappEkoLinker import Linker as linker
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
#from databaseImport.databaseConnect import dbConnect as dbConnect
from databaseImport.databaseUpdate import DbUpdate as dbUpdate
lastSentId=0
class EchoLayer(YowInterfaceLayer):

    def replyBack(self,messageProtocolEntity,replyToBeSent):
    	global lastSentId;
    	dbUpdateObject=dbUpdate()
        for reply in replyToBeSent:
            if not reply[5]:
	    	getWhatsappId=linker()
	   	print reply
	    	print "!@#$%^&*(*&^%$#@";
	    	whatsapp_id=getWhatsappId.returnWhatsappId(reply[1])
    	    	if(reply[5] == 0):
                	if not messageProtocolEntity.isGroupMessage():
        	        	outgoingMessageProtocolEntity = TextMessageProtocolEntity(reply[2], to = str(whatsapp_id) + "@s.whatsapp.net")
			else:
				outgoingMessageProtocolEntity = TextMessageProtocolEntity(reply[2], to = str(whatsapp_id) + "@g.us")
                	dbUpdateObject.updateResponseMessage(1,reply[0]);
                	lastSentId=reply[0]
                	print "Sending %s to %s"%(reply[2],whatsapp_id);
                	self.toLower(outgoingMessageProtocolEntity);
    
    @ProtocolEntityCallback("message")
    def onMessage(self, messageProtocolEntity):
    	if messageProtocolEntity.getType() == 'text':
        	self.onTextMessage(messageProtocolEntity)
    	elif messageProtocolEntity.getType() == 'media':
                self.onMediaMessage(messageProtocolEntity)
    
    @ProtocolEntityCallback("receipt")
    def onReceipt(self, entity):
        ack = OutgoingAckProtocolEntity(entity.getId(), "receipt", entity.getType(), entity.getFrom())
        self.toLower(ack)

    #receiving a text message, inserting it in database and sending processed message back
    def onTextMessage(self,messageProtocolEntity):
    	global lastSendId
        receipt = OutgoingReceiptProtocolEntity(messageProtocolEntity.getId(), messageProtocolEntity.getFrom());
        self.toLower(receipt);
        if not messageProtocolEntity.isGroupMessage() or (messageProtocolEntity.isGroupMessage()==1 and (messageProtocolEntity.getBody()[:3]=="eko" or messageProtocolEntity.getBody()[:3]=="Eko" or messageProtocolEntity.getBody()[:3]=="EKO")):
		#inserting in DB
		linkerObject=linker();
		print "####################################################"
		whatsapp_id=messageProtocolEntity.getFrom(False);
		print whatsapp_id
		if not messageProtocolEntity.isGroupMessage():
			groupMessage=0;
			message_body=messageProtocolEntity.getBody();
		else:
			groupMessage=1;
			participantEkoId = linkerObject.returnEkoId(str(messageProtocolEntity.getParticipant(False)),0);
			print "@@@@@@@@@@@@!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!", participantEkoId
			message_body=messageProtocolEntity.getBody()[4:] + "@" + participantEkoId
		
		print groupMessage 
		message_sender= linkerObject.returnEkoId(whatsapp_id,groupMessage);
    		message_source=linkerObject.returnMessageSource();
    		message_type=linkerObject.returnMessageType(1);
    		message_status=linkerObject.returnMessageStatus();
    		message_destination=message_source;
    		dbUpdateObject=dbUpdate();
		dbUpdateObject.insertReceiveMessage(message_sender,message_body,message_source,message_type,message_status);
        	print("Receiving %s from %s" % (message_body, messageProtocolEntity.getFrom(False)));
                
        	time.sleep(2);
        
        	#to pick only unprocessed message
        	replyToBeSent= dbUpdateObject.selectResponseMessage(message_destination, lastSentId);
        	self.replyBack(messageProtocolEntity,replyToBeSent)
        

    #receiving a media message, inserting it in database and sending processed message back
    def onMediaMessage(self, messageProtocolEntity):
    	global lastSentId
        if messageProtocolEntity.getMediaType() == "image":
            
            receipt = OutgoingReceiptProtocolEntity(messageProtocolEntity.getId(), messageProtocolEntity.getFrom())

            outImage = ImageDownloadableMediaMessageProtocolEntity(
                messageProtocolEntity.getMimeType(), messageProtocolEntity.fileHash, messageProtocolEntity.url, messageProtocolEntity.ip,
                messageProtocolEntity.size, messageProtocolEntity.fileName, messageProtocolEntity.encoding, messageProtocolEntity.width, messageProtocolEntity.height,
                messageProtocolEntity.getCaption(),
                to = messageProtocolEntity.getFrom(), preview = messageProtocolEntity.getPreview())

            print("Echoing image %s to %s" % (messageProtocolEntity.url, messageProtocolEntity.getFrom(False)))

            #send receipt otherwise we keep receiving the same message over and over
            self.toLower(receipt)
            self.toLower(outImage)

        elif messageProtocolEntity.getMediaType() == "location":

            receipt = OutgoingReceiptProtocolEntity(messageProtocolEntity.getId(), messageProtocolEntity.getFrom())

            outLocation = LocationMediaMessageProtocolEntity(messageProtocolEntity.getLatitude(),
                messageProtocolEntity.getLongitude(), messageProtocolEntity.getLocationName(),
                messageProtocolEntity.getLocationURL(), messageProtocolEntity.encoding,
                to = messageProtocolEntity.getFrom(), preview=messageProtocolEntity.getPreview())

            print("Echoing location (%s, %s) to %s" % (messageProtocolEntity.getLatitude(), messageProtocolEntity.getLongitude(), messageProtocolEntity.getFrom(False)))

            #send receipt otherwise we keep receiving the same message over and over
            self.toLower(outLocation)
            self.toLower(receipt)
            
        elif messageProtocolEntity.getMediaType() == "vcard":
        	receipt = OutgoingReceiptProtocolEntity(messageProtocolEntity.getId(), messageProtocolEntity.getFrom());
        	self.toLower(receipt);
        	x=messageProtocolEntity.getCardData()
        	received_vcard_number= x.split('TEL:')[1].split("\n")[0]

		#inserting in DB
		linkerObject=linker()
		whatsapp_id=messageProtocolEntity.getFrom(False);
		message_sender= linkerObject.returnEkoId(whatsapp_id,0);
    		message_body=received_vcard_number;
    		message_source=linkerObject.returnMessageSource();
    		message_type=linkerObject.returnMessageType(2);
    		message_status=linkerObject.returnMessageStatus();
    		message_destination=message_source;
    		dbUpdateObject=dbUpdate()
		dbUpdateObject.insertReceiveMessage(message_sender,message_body,message_source,message_type,message_status)
    	 
        	print("Receiving %s from %s" % (message_body, messageProtocolEntity.getFrom(False)));
        
        	self.toLower(receipt);
        
        	time.sleep(2);
        	#to pick only unprocessed message
        
        	replyToBeSent= dbUpdateObject.selectResponseMessage(message_destination, lastSentId);
        	self.replyBack(messageProtocolEntity,replyToBeSent)
        	
        	
        
        elif messageProtocolEntity.getMediaType() == "audio":
            
            receipt = OutgoingReceiptProtocolEntity(messageProtocolEntity.getId(), messageProtocolEntity.getFrom())
            self.toLower(receipt);
            outAudio = AudioDownloadableMediaMessageProtocolEntity(
                messageProtocolEntity.getMimeType(), messageProtocolEntity.fileHash, messageProtocolEntity.url, messageProtocolEntity.ip,
                messageProtocolEntity.size, messageProtocolEntity.fileName, messageProtocolEntity.abitrate, messageProtocolEntity.acodec, messageProtocolEntity.asampfreq,
                messageProtocolEntity.duration, messageProtocolEntity.encoding, messageProtocolEntity.origin, messageProtocolEntity.seconds,
                to = messageProtocolEntity.getFrom())

            path = str(messageProtocolEntity.url);
            commands.getoutput('wget ' + path );
            fname = path.split('/')[-1];
            commands.getoutput('ffmpeg -i ' + fname + ' ' + fname.split('.')[0] + '.wav');
            r = sr.Recognizer()
            with sr.WavFile(fname.split('.')[0] + '.wav') as source:     # use "test.wav" as the audio source
                audio = r.record(source)                        # extract audio data from the file
            try:
                print("Receiving sound. Transcription: " + r.recognize(audio))   # recognize speech using Google Speech Recognition
            except LookupError:                                 # speech is unintelligible
                print("Could not understand audio")
                return;
	    #inserting in DB
	    	whatsapp_id=messageProtocolEntity.getFrom(False);
		message_sender= linker.returnEkoId(whatsapp_id,0);
    		message_body=r.recognize(audio);
    		message_source=linker.returnmessageSource();
    		message_type=linker.returnmessageType(2);
    		message_status=linker.returnmessagestatus();
    		message_destination=message_source;
    	 	dbUpdateObject=dbUpdate()
		dbUpdateObject.insertReceiveMessage(message_sender,message_body,message_source,message_type,message_status)
        	print("Receiving %s from %s" % (r.recognize(audio), messageProtocolEntity.getFrom(False)));
        
        	self.toLower(receipt);
        
        	time.sleep(2);
        #to pick only unprocessed message
        
        	replyToBeSent= dbUpdateObject.selectResponseMessage(message_destination, self.lastSentId);
        	self.replyBack(messageProtocolEntity,replyToBeSent)
