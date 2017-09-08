import urllib2
from Bank import main
def recharge(item_pr,number,dbUpdateObject,sessionObject):
	'''url='http://59.162.111.216/eko/cellrequest.do?method=handle&originationAddress=1919191919&sendSms=1&requestText=123&source=CONNECT'
	req = urllib2.Request(url)
	response = urllib2.urlopen(req)
	the_page = response.read()'''
	return main.recharge(number,item_pr[3],item_pr[5])
	print item_pr
	if str(item_pr[4])==" myphone":
		return "Greetings " + str(item_pr[2]) + " !!\nRecharging phone no: " + str(number) + " by INR." + str(item_pr[3])+ "\n This is the testing version";
	
	return "Greetings " + str(item_pr[2]) + " !!\nRecharging phone no: " + str(item_pr[4]) + " by INR." + str(item_pr[3])+ "\n This is the testing version";
