from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import message_manager



mm = message_manager.MessageManager()
jobsDict = {}



def myJob(bot, job):
      bot.send_message(chat_id=job.context, text="you should listen to more metal... \n"+mm.GetMetal())

def start(bot, update):
      if update.message.chat_id not in jobsDict:  
            jobsDict[update.message.chat_id] = job_q.run_repeating(myJob, context=update.message.chat_id, interval=15, first=0)
            bot.send_message(chat_id=update.message.chat_id, text="Metal suggestions are on")

def stopLoop(bot, update):
      jobsDict[update.message.chat_id].schedule_removal()
      del jobsDict[update.message.chat_id]
      bot.send_message(chat_id=update.message.chat_id, text="Metal suggestions are off")
      
def msg(bot, update):
      if "metal" in update.message.text:
            mm.SaveMsg(update.message.text)
            bot.send_message(chat_id=update.message.chat_id, text=f"{update.message.text.upper()} \m/")

def getMetal(bot, update):
      link = mm.GetMetal()
      bot.send_message(chat_id=update.message.chat_id, text=link)
      
def setMetal(bot, update, args):
      mm.SetMetal(' '.join(args))
      bot.send_message(chat_id=update.message.chat_id, text="So Metal!")





updater = Updater('your_access_token')

updater.dispatcher.add_handler(CommandHandler('getmetal', getMetal))
updater.dispatcher.add_handler(CommandHandler('setmetal', setMetal, pass_args=True))

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('stoploop', stopLoop))

updater.dispatcher.add_handler(MessageHandler(Filters.text, msg))

job_q = updater.job_queue

updater.start_polling()
updater.idle()
