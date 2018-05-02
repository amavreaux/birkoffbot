import telegram
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
import logging
import json

updater = Updater(token="574173947:AAE-pDcfWkTfNldoXn1FODKwUp9Y0d0wWkk")
dispatcher = updater.dispatcher
birkoff = telegram.Bot(token="574173947:AAE-pDcfWkTfNldoXn1FODKwUp9Y0d0wWkk")


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
level=logging.INFO)




def profiler(update):
  if update.message.chat.type == "private":
    username = update.message.chat_id
    info = {
    'username': username,
    'userlink': '@{}'.format(username),
    'groups': []
    }
    groupname = update.message.text
    store = open('%s.txt' % username, 'w+')
    red = store.read()
    if groupname in info['groups']:
      birkoff.sendMessage(chat_id=username, text=groupname + " is already registered")
    else:
      info['groups'].append(groupname)
      store.write(json.dumps(info))
      store.close()
      



#COMMANDS

def start(birkoff, update):
  if update.message.chat.type == "private":
    username = update.message.chat.username
    birkoff.send_message(chat_id=update.message.chat_id, text="Hello, I'm birkoffbot. I'm an adminstrator to your groups." + "\n" +
  "You can send your group link to make me your administrator")
  

def callMe(birkoff, update):
  if update.message.chat.type == "group":
    username = update.message.chat_id
    birkoff.send_message(username, text="Hello... Is there anything you would want me to do?")






startHandler = CommandHandler('start', start)
dispatcher.add_handler(startHandler)

callMeHandler = CommandHandler('birkoff', callMe)
dispatcher.add_handler(callMeHandler)


#INPUTS

def groupLink(birkoff, update):
  if update.message.chat.type == "private":
     birkoff.send_message(chat_id=update.message.chat_id, text="Okay, I've got that..." + "\n" + "1. Now make me an administrator in {}".format(update.message.text) + "\n" + "3. Send /birkoff in {}".format(update.message.text))
     profiler(update)





#INPUT HANDLER

groupLinkHandler = MessageHandler(Filters.entity('mention'), groupLink)
dispatcher.add_handler(groupLinkHandler)



#MESSAGES

def echo(birkoff, update):
     birkoff.send_message(chat_id=update.message.chat_id, text=update.message.text)



# MESSAGE HANDLERS
echo_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(echo_handler)






updater.start_polling()