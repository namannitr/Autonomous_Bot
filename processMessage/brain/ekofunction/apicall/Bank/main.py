import test_db_update
import datetime
def create_wallet(number, name):
	balance=100;
	pin=1234;
	return test_db_update.insertnewuser(number,name,balance,pin)
def balance_check(number):
	return "Your balance is INR " + str(test_db_update.fetchbalance(number)) + ". " + "smiley4";
	
	
def p2p(number1,number2,amount,pin):
	if number1==number2:
		return "Hey!!!!! You cant send money to yourself.";
	elif test_validate_pin(number1,pin):
		bal1=test_db_update.fetchbalance(number1);
		bal2=test_db_update.fetchbalance(number2);
		if bal1 < float(amount):
			return "Sorry buddy!! You dont have enough balance to send money";
		test_db_update.updateBalance(number1,bal1-float(amount));
		test_db_update.updateBalance(number2,bal2+float(amount));
		return "Here you go- I just sent "+ str(amount)+" bucks to "+ test_db_update.fetchusername(number2)+ " smiley2 "+ balance_check(number1);
	else:
		return "Invalid pin"
		
def load_balance(number,amount, pin):
	if pin=='1111':
		bal=test_db_update.fetchbalance(number);
		test_db_update.updateBalance(number,bal+float(amount));
		return "Successfully added your money. "+ balance_check(number)
	else:
		return "Invalid TID"
def recharge(number,amount,pin):
	if pin=='1234':
		bal=test_db_update.fetchbalance(number);
		if bal < float(amount):
			return "Sorry buddy!! You dont have enough balance to send money";
		test_db_update.updateBalance(number,bal-float(amount));
		return "Here you go. Your recharge was successful. smiley1 "+ balance_check(number)
	else:
		return "invalid pin"
	
def test_validate_pin(number1,pin):
	if pin=="1234":
		return 1;
	else:
		return 0;
def giveReward(number):
	return load_balance(number,20, "1111")
