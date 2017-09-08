from apicall import register,send,recharge,balance,history,addmoney

required_fields = {'reg':'&name&register.register','send':'&name&amount&number&pin&send.send','rech':'&name&amount&number&pin&recharge.recharge','bal':'&name&balance.balance','hist':'&name&history.history','add':'&name&transactionid&addmoney.addmoney'};
bot_query={'name':"Register name",'amount':"Send amount",'number':"Send number",'pin':"Send pin",'transactionid': "send transactionid"};
function_map={"register.register":register.register,"send.send":send.send,"recharge.recharge":recharge.recharge,"balance.balance":balance.balance,"history.history":history.history,"addmoney.addmoney":addmoney.addmoney};
