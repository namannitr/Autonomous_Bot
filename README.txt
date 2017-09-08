Conversational Banking

packages needed MySQLdb, phpmyadmin, Pyaiml, yowsup, sleekxmpp, speech recognition master
import eko_project.sql 
edit database passwords in databaseImport/databaseConnect.py
 and in brain/apicall/bank/testdbupdate


Basic Model -

                   received message                                                      response message 
message from user -----------------> input adapter -----> processor ----> output adapter ----------------> message to user


Modules ---->

for Input/output adapter - "whatsappClient/facebookClient/twitterClient"

for Processing part - "processMessage" 

To store received and response message, database is used - "databaseImport"


a message is received by the input adapter and dumped into received_message table.
run "python pick.py" (in "processMessage")
this function picks the message from received_message table and sends the message to brain to generate the appropriate response through 'aiml' (in bot/bot_aiml). this message is then dumped into response_message table.
which is picked by the respective output message adapter and sent to the user.

Running the whatsappClient - 
--> Download yowsup. 
--> type "pip install yowsup2" in terminal
--> for details refer https://github.com/tgalal/yowsup 
--> register a number (steps given in the link above) and in the credentials folder in whatsappClient, update your phone number and password that you get after registering with whatsapp
--> to run the whatsapp client type "sudo python startWhatsappClient.py"
--> speech recognition folder is to convert the audio message into text file. if you send an audio message, it will be converted into text and then processed. install ffmpeg and speech_recognition master. refer google for installation.



Running the facebookClient - 
--> Download sleekxmpp
--> pip install sleekxmpp
-->  to use edit chat.py and and your jid (user name of facebook). 
--> run "python chat.py <your facebook password>"


names of the aiml needed for Eko start with "eko_ " in processMessage/bot/bot_aiml 
(like eko_send, eko_recharge etc). response for send/recharge/register etc are generated as #send#name#amount#number#pin . this message is split with "#" and processed in brain and respective APIs are called.

Linker generates appropriate EkoID (TEMP/EKO). TEMP for unregistered and EKO for registered. this EkoId is used to carry out all functions and sync the accounts
for example-
Register via whatsapp for the wallet by typing register.
Log in to facebook
Send 'hi' to the one who's working as the bot.
and type sync
Do as intstructed afterwards.

PS - twitter client doesn't function as of now

Feel free to contact the following for any doubt - 
Naman Agarwal -- namannitr@gmail.com
Rohan Bhoi -- bhoirohan172@gmail.com
Vyom Rastogi -- vyom.rastogi.ece12@itbhu.ac.in
Neeraj Dhelariya -- neeraj.dhelariya.ece12@itbhu.ac.in
