# skype-bot-SDK-SkPy
Create a bot for sending message with skype and used SkPy library
<br>
For example I do it in zabbix, I export items details from zabbix API and I sent some of those details to a skype channel
<br>
# So your requirements are:
<br>
- zabbix JSON API opration
<br>
- python on your zabbix server and SkPy package and create "bot.py" file
<br>
- create a "fetch.sh" bash file for fetching data 
<br>
- create three text files in "/root/skype-bot" path with opposite names : draft.txt, first.txt and message.txt
<br>
<br>
message output :
<br>
====================================
<br>
Mon Oct  4 13:47:32 +0330 2021
<br>
====================================
<br>
"itemid":"58994"
<br>
"name":"OnlineUser"
<br>
"master_itemid":"0"
<br>
"lastvalue":"408"
<br>
"itemid":"41374"
<br>
"name":"InterfaceGi0/0/3.108(User):Bitsreceived"
<br>
"master_itemid":"0"
<br>
"lastvalue":"19718184"
<br>
