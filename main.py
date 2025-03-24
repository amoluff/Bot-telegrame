from telegram.ext import Updater
   import os
   import time

   TOKEN = os.getenv('7675816176:AAFUQQVLjVtUJmzElWqhIdLTwLou1bm4t-k')

   def main():
       updater = Updater(TOKEN, use_context=True)
       
       # إضافة أوامر البوت هنا
       updater.dispatcher.add_handler(CommandHandler('start', start))
       
       updater.start_polling()
       print("✅ البوت يعمل الآن!")
       
       # للحفاظ على التشغيل
       updater.idle()

   if __name__ == '__main__':
       main()
