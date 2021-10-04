#! /usr/bin/python3
from skpy import Skype
sk = Skype("Your_Skype_Number", "Your_Skype_Password")

with open('/root/skype-bot/message.txt','r') as file:
    msgStr = file.read()
print(msgStr)

sk.user
sk.contacts
sk.chats


group = sk.chats.chat("19:Your_Channel_Address.skype")
group.sendMsg(msgStr)
