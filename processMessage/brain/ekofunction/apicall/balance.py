import urllib2,datetime
from Bank import main
def balance(item_pr,number,dbUpdateObject,sessionObject):
	'''url='http://59.162.111.216/eko/cellrequest.do?method=handle&originationAddress=1919191919&sendSms=1&requestText=123&source=CONNECT'
	req = urllib2.Request(url)
	response = urllib2.xurlopen(req)
	the_page = response.read()'''
	x=5000
	return main.balance_check(number)
	return "Greetings " + str(item_pr[2]) + " !!\nYour current account balance as dated on:" + str(datetime.datetime.now()) + " is INR." + str(x)+"\n This is the testing version";
