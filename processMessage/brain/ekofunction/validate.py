import re

class Validate(object):

	def checkphone(self,num):
		if re.match("^[789][0-9]{9}$", num):
			return "91"+str(num)
		return 0;
	def validatephone(self,num):
		num=num.replace('-','')
		if len(num)==10:
			return self.checkphone(num)
		elif len(num)==11:
			if num[0]=='0':
				return self.checkphone(num[1:])
			elif num[0]=='+':
            			return self.checkphone(num[1:])
    		elif len(num)==12:
        		if(num[0]=='9' and num[1]=='1'):
            			return self.checkphone(num[2:])
        		elif(num[0]=='+' and num[1]=='0'):
				return self.checkphone(num[2:])
		elif len(num)==13:
			if(num[0]=='+' and num[1]=='9' and num[2]=='1'):
				return self.checkphone(num[3:])
		elif num==" myphone":
			return num
		else:
			return 0

	def validateamount(self,num):
		if re.match("^\d+?\.\d+?$", num) or re.match("^\d+?$",num):
			return num
		else:
			return 0

	def validatepin(self,num):
		if len(num)==4:
			if re.match("^\d+?$",num):
				return num
		return 0;

	qstring=''
	x=[]
	def validate(self,x,num):
		if x==0:
			return num;
		if x==1:
			return self.validateamount(num)
		if x==2:
			return self.validatephone(num)
		if x==3:
			return self.validatepin(num)
		else:
			return 0;
