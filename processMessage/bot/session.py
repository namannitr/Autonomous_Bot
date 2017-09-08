import os,sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from bot import aiml
import marshal

class Session(object):
	firsttime=0;
	k=aiml.Kernel()
	
#response from AIML
	def respond(self,message,id):
		return self.k.respond(message,id)

#learn the AIML files
	def learn(self):
		self.k.learn("../bot/bot_aiml/*.aiml");
		path = '../bot/User_Sessions/';
		for filename in os.listdir(os.path.abspath(path)):
			sessionFile = file(path + filename, "rb");
			session = marshal.load(sessionFile);
			sessionFile.close();
			for pred,value in session.items():
				self.k.setPredicate(pred, value, filename.split('.')[0]);

#write the session data in a folder 'User Sessions'
	def write_session(self,item):
		global k,firsttime;
		path = "../bot/User_Sessions/";
		if (str(item[1])+".ses") not in os.listdir(os.path.abspath(path)):
			fo = open("../bot/User_Sessions/"+str(item[1]) + ".ses", "wb");
			fo.close();
			self.firsttime=1
		session = self.k.getSessionData(item[1]);
		sessionFile = file("../bot/User_Sessions/"+str(item[1]) + ".ses", "wb");
		marshal.dump(session, sessionFile);
		sessionFile.close();
	
	def learnSingleSession(self,fileName):
		path = '../bot/User_Sessions/';
		sessionFile = file(path + fileName, "rb");
		session = marshal.load(sessionFile);
		sessionFile.close();
		for pred,value in session.items():
			self.k.setPredicate(pred, value, fileName.split('.')[0]);
