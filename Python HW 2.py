#importam librariile necesare
import telebot
import random

#implementam botul
bot = telebot.TeleBot('5270168831:AAEESF_RE08EzWKpaqsRqi54m56yvyc3Scg')
types = telebot.types



# #Task 1:  Rezolvator de matematică ------------------------


@bot.message_handler(commands=['Calculator'])
#cream o functie de afisare
def me1(message):
    bot.reply_to(message, 'Scrie expresia in chat')

@bot.message_handler(regexp='\w+')
#cream o functie care o sa afiseze rezultatul expresiei cu ajutorul eval()
def Calculator(message):
    x = eval(message.text)
    bot.reply_to(message, x)
    # except Exception print('Nu este posibila rezolvarea exercitiului')




# #Task 2:  Loterie ------------------------

#punem o conditie ca call sa fie mereu true
@bot.callback_query_handler(func=lambda call: True)
#facem o fucntie care ia valoarea lui call si o compara cu nr random 
def callback_handler(call):
    x = random.randint(0, 5)
    if call.data == x:
        bot.send_message(call.from_user.id, 'Ai cistigat')
        bot.send_message(call.from_user.id, x)
    else:
        bot.send_message(call.from_user.id, 'Ai pierdut')
        bot.send_message(call.from_user.id, x)

# daca input din chat == lottery atunci executam dunctia de mai jos
@bot.message_handler(func=lambda m: m.text.lower() == 'lottery')
# ne va afisa tabelul cu numere 
def Lottery(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(
        types.InlineKeyboardButton('1', callback_data=1)
    )
    markup.add(
        types.InlineKeyboardButton('2', callback_data=2)
    )
    markup.add(
        types.InlineKeyboardButton('3', callback_data=3)
    )
    markup.add(
        types.InlineKeyboardButton('4', callback_data=4)
    )
    markup.add(
        types.InlineKeyboardButton('5', callback_data=5)
    )

    bot.send_message(message.chat.id, 'Ce numar alegi ?', reply_markup=markup)

bot.infinity_polling()
