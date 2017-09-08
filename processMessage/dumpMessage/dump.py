import MySQLdb,sys,os


class Dump(object):

	def dump(self,dbUpdateObject,botResponse,item):
		print botResponse;
		print item;
		dbUpdateObject.insertResponseMessage(item[0],item[1],botResponse,item[3],item[4]);

