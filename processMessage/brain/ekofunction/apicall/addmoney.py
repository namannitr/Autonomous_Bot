import urllib2,datetime
from Bank import main

def addmoney(item_pr,number,dbUpdateObject,sessionObject):
	'''url='http://59.162.111.216/eko/cellrequest.do?method=handle&originationAddress=1919191919&sendSms=1&requestText=123&source=CONNECT'
	req = urllib2.Request(url)
	response = urllib2.xurlopen(req)
	the_page = response.read()'''
	print item_pr
	#return "Greetings " + str(item_pr[2]) + " !!\nI have added the money in your account.\nYour current account balance as dated on:" + str(datetime.datetime.now()) + " is INR." + str(x)+"\n This is the testing version";	
	return main.load_balance(number,500,item_pr[3])

def addmoneywithamount(number,amount):
	'''url='http://59.162.111.216/eko/cellrequest.do?method=handle&originationAddress=1919191919&sendSms=1&requestText=123&source=CONNECT'
	req = urllib2.Request(url)
	response = urllib2.xurlopen(req)
	the_page = response.read()'''
	#return "Greetings " + str(item_pr[2]) + " !!\nI have added the money in your account.\nYour current account balance as dated on:" + str(datetime.datetime.now()) + " is INR." + str(x)+"\n This is the testing version";	
	return main.load_balance(number,amount,'1111')
