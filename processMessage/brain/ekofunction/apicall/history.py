import urllib2
from Bank import main
def history(item_pr,number,dbUpdateObject,sessionObject):
	'''url='http://59.162.111.216/eko/cellrequest.do?method=handle&originationAddress=1919191919&sendSms=1&requestText=123&source=CONNECT'
	req = urllib2.Request(url) 
	response = urllib2.urlopen(req)
	the_page = response.read()'''
	return "Greetings " + str(item_pr[2]) + " !!\nYour last 10 transactions are: \n 1. Test 1\n 2. Test 2\n 3. Test 3\n 4. Test 4\n 5. Test 5\n 6. Test 6\n 7. Test 7\n 8. Test 8\n 9. Test 9\n 10. Test 10\n This is the testing version";
