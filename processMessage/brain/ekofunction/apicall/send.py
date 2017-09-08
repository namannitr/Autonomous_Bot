import urllib2
from Bank import main
def send(item_pr,number,dbUpdateObject,sessionObject):
	'''url='http://59.162.111.216/eko/cellrequest.do?method=handle&originationAddress=1919191919&sendSms=1&requestText=123&source=CONNECT'
	req = urllib2.Request(url)
	response = urllib2.urlopen(req)
	the_page = response.read()'''
	try:
		EkoIdOfReceipent=dbUpdateObject.selectWhatsappLinkId(item_pr[4])[5];
	except:
		return "I'm Sorry. Your are sending money to a non-registered user. Please ask him to register first."
	print EkoIdOfReceipent
	return main.p2p(number,EkoIdOfReceipent,item_pr[3],item_pr[5]);
	return "Greetings " + str(item_pr[2]) + " !!\nSending an amount of INR." + str(item_pr[3]) + " to " + str(item_pr[4])+ "\n This is the testing version";
