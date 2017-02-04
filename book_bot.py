from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler  
from goodreads import client
gc = client.GoodreadsClient("J7asX1xgQHBfotcBA4myA", "xJJdA53Ep3dowcwyP9wdOc7EY0LMflbKXvc0nVBw")
gc.authenticate("J7asX1xgQHBfotcBA4myA", "xJJdA53Ep3dowcwyP9wdOc7EY0LMflbKXvc0nVBw")

GET_A_BOOK = range(1)

def greet_user(bot, update):
    print('Вызван/ start')
    bot.sendMessage(update.message.chat_id, text='Привет! Какую книгу хочешь прочитать?')

    return GET_A_BOOK


def get_a_book(bot, update):#
    book = gc.search_books(update.message.text)
    book_for_user = str(book[0])
    print(book_for_user)
    bot.sendMessage(update.message.chat_id, book_for_user)


def show_error(bot, update, error):
    print('Update "{}" caused error "{}"'.format(update, error))
    
"""def talk_to_me(bot, update):
    print("Пришло сообщение: " + update.message.text)
    bot.sendMessage(update.message.chat_id, chat[key.lower])"""


def cancel(bot, update):
    bot.sendMessage(update.message.chat_id,'Пока! Надеюсь, я помог тебе!',
                              reply_markup=ReplyKeyboardRemove())

    return ConversationHandler.END


def main():
    updater = Updater("329926022:AAEees6cYptoUarJW4NjKaLpAmsZ3wS9EJk")
    dp = updater.dispatcher
    
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', greet_user)],

        states={ 
                 
                GET_A_BOOK: [MessageHandler([Filters.text], get_a_book)]
                       
        },

        fallbacks=[CommandHandler('cancel', cancel)]
    )

    dp.add_handler(conv_handler)
    dp.add_error_handler(show_error)
    updater.start_polling()
    updater.idle()
if __name__== '__main__':
    main()



   
