# coding=UTF-8
class SmiliSub(object):
	facebookSmiliDictionary={"smiley1":":)","smiley2":"B-)","smiley3":":(","smiley4":"","smiley5":"","smiley6":"",}
	s="ðŸ˜Š";
	whatsappSmiliDictionary={"smiley1":"😊 ","smiley2":"😎","smiley3":"😞","smiley4":"💸","smiley5":"✨ ","smiley6":" 📱 ",}
	def  replaceWhatsappSmili(self, botResponse):
		for word in botResponse.split(" "):
			try :
				if not self.whatsappSmiliDictionary[word]==None:
					print botResponse
					print self.whatsappSmiliDictionary[word]
					botResponse=botResponse.replace(word,self.whatsappSmiliDictionary[word]);
					print botResponse
			except :
				pass
		return botResponse;
	def  replaceFacebookSmili(self, botResponse):
		for word in botResponse.split(" "):
			try:
				if not self.facebookSmiliDictionary[word]==None:
					botResponse=botResponse.replace(word,self.facebookSmiliDictionary[word]);
			except:
				pass;
		return botResponse;
	def  replaceSmili(self, botResponse,item):
		if item[3]==1:
			return self.replaceWhatsappSmili(botResponse)
		elif item[3]==2:
			return self.replaceFacebookSmili(botResponse)
		else :
			return botResponse;
		
		
		




 

