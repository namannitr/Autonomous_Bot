import MySQLdb

db = MySQLdb.connect("localhost","root","Nam@1695!!","eko_Project") #write db password in place of password
cur=db.cursor();

def insertnewuser(eko_id,user_name,balance,pin):
	query="SELECT * FROM bank WHERE eko_id = '" + str(eko_id)+"'";
	cur.execute(query);
	l=cur.fetchone();
	db.commit();
	if l==None:
		insert(eko_id,user_name,balance,pin)
		return "RegistrationSuccessful"
	else:
		return "Existing User with user_name "+ str(l[1]) +". "
	
def fetchbalance(eko_id):
	query="SELECT * FROM bank WHERE eko_id = '" + str(eko_id)+"'";
	cur.execute(query);
	l= cur.fetchone()[2]
	db.commit();
	return l 
		
def fetchusername(eko_id):
	query="SELECT * FROM bank WHERE eko_id = '" + str(eko_id)+"'";
	cur.execute(query);
	l= cur.fetchone()[1]
	db.commit();
	return l
	
def updateBalance(eko_id,balance):
	cur.execute("UPDATE bank SET balance = " +str(balance)+ " WHERE  eko_id= '"+ str(eko_id)+"'");
        db.commit();
	
def insert(eko_id,user_name,balance,pin):
	cur.execute("INSERT INTO bank(`eko_id`, `user_name`, `balance`, `pin`) VALUES (%s,%s,%s,%s)", (eko_id,user_name,balance,pin));
	db.commit();

'''def delete(eko_id):
	query="SELECT * FROM bank WHERE eko_id = '" + str(eko_id)+"'"
	cur.execute(query);
	l=cur.fetchone();
	db.commit();
	query="DELETE from bank where eko_id= '"+ str(eko_id)+"'";
	cur.execute(query);
	db.commit();
	return l '''
