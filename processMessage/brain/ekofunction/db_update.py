import sys,os,pickrequest
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import brain
import validate
#db= brain.dbconfiguration.db1
#cur=db.cursor()
def delete(item):
	cur.execute("DELETE FROM process_request WHERE user_id =" + str(item[1]));
	db.commit();
	
def insert(bot_reply,item):
	info=bot_reply.split('#')
	if not (info[1]== "add" or info[1]== "reg"): 
		info=list(info)
		if info[3]!='0':
			info[3]=validate.validateamount(info[3])
		if str(info[4]) != '0' or info[4] != 0.0 or info[4]!='' :
			info[4]=validate.validatephone(info[4])
		if info[5]!='0':
			info[5]=validate.validatepin(info[5])
		info=tuple(info)
		new_bot_reply = "#"+str(info[1])+"#"+str(info[2])+"#"+str(info[3])+"#"+str(info[4])+"#"+str(info[5])
	else:
		new_bot_reply= bot_reply
	cur.execute("INSERT INTO `process_request`(`user_id`, `request`, `complete_flag`, `status_flag`) VALUES (%s,%s,%s,%s)", (item[1],new_bot_reply,0,0));
	db.commit();
	return pickrequest.pick_request(new_bot_reply,item);

def update(bot_reply,item):
	delete(item)
	return insert(bot_reply,item)
	
def continue1(bot_reply,item):
	query="SELECT * FROM process_request WHERE complete_flag = 0 AND user_id = " + str(item[1])
	cur.execute(query);
	
	bot_reply=cur.fetchone()[1]
	db.commit();
	return pickrequest.pick_request(bot_reply,item);
def selectprocessrequest(item):
	query="SELECT * FROM process_request WHERE complete_flag = 0 AND user_id = " + str(item[1])
	cur.execute(query);
	db.commit();
	return cur.fetchone()
