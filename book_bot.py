from telegram.ext import Updater, CommandHandler, MessageHandler, Filters 
from goodreads import client
gc = client.GoodreadsClient("J7asX1xgQHBfotcBA4myA", "xJJdA53Ep3dowcwyP9wdOc7EY0LMflbKXvc0nVBw")
gc.authenticate("J7asX1xgQHBfotcBA4myA", "xJJdA53Ep3dowcwyP9wdOc7EY0LMflbKXvc0nVBw")

def greet_user(bot, update):
    print('Вызван/ start')
    bot.sendMessage(update.message.chat_id, text='Давай общаться!')
def show_error(bot, update, error):
    print('Update "{}" caused error "{}"'.format(update, error))


def get_an_author(bot, update):
    book = update.message.text
    authors = book.authors
    name_of_the_auther = authors[0].name
    bot.sendMessage(update.message.chat_id, name_of_the_authors)
    
#переписать через get_id?




dialog = {"привет": "и тебе привет!", "как дела": "лучше всех", "пока":"увидимся"}
def talk_to_me(bot, update):
    print("Пришло сообщение: " + update.message.text)
    bot.sendMessage(update.message.chat_id, chat[key.lower])

   
def main():
    updater = Updater("329926022:AAEees6cYptoUarJW4NjKaLpAmsZ3wS9EJk")
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler([Filters.text], talk_to_me))
    dp.add_handler(MessageHandler([Filters.text], get_an_author))
    dp.add_error_handler(show_error)
    updater.start_polling()
    updater.idle()
if __name__== '__main__':
    main()

"""
book = gc.book(1)
print(book.title)

authors = book.authors
print(authors[0].name)
print(book.average_rating)
"""