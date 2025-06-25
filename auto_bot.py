from telebot import TeleBot, types
import json
import parser
import os
import botparser

for folder in ['car', 'moto', 'bus', 'truck']:
    os.makedirs(folder, exist_ok=True)

TOKEN = 
bot = TeleBot(TOKEN)


vehicles_dict={
            'car': 'Մարդատար',
            'bus': 'Ավտոբուս',
            'truck': 'Բեռնատար',
            'moto': 'Մոտոտեխնիկա'
        }

@bot.message_handler(commands=['start'])
def start_bot(message):
    inline_markup = types.InlineKeyboardMarkup()
    inline_btn1 = types.InlineKeyboardButton("🚗 Մարդատար", callback_data='car')
    inline_btn2 = types.InlineKeyboardButton("🚌 Ավտոբուս", callback_data='bus')
    inline_btn3 = types.InlineKeyboardButton("🚛 Բեռնատար", callback_data='truck')
    inline_btn4 = types.InlineKeyboardButton("🛵 Մոտոտեխնիկա", callback_data='moto')

    inline_markup.row(inline_btn1, inline_btn2)
    inline_markup.row(inline_btn3, inline_btn4)
    
    bot.send_message(message.chat.id, "Ողջույն: Բարի գալուստ ArmTopCars հայկական տելեգրամյան ալիքը: Այստեղ կարող եք տեսնել օրվա լավագույն տրանսպորտային միջոցները...")
    bot.send_message(message.chat.id, "Ընտրեք տրանսպորտային միջոցի տեսակը:", reply_markup=inline_markup)

    

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    botparser.parse_data(call.data)
    with open(f'{call.data}.json', 'r') as file:
        vehicle_dict_ = json.load(file)

    c = 0
    for i in vehicle_dict_[call.data]:
        photo_path = f'{call.data}/{c}.jpg'
        with open(photo_path, 'rb') as photo:
            bot.send_photo(
                call.message.chat.id,
                photo=photo,
                caption=i,
                parse_mode='HTML'
            )
        c += 1

    inline_markup = types.InlineKeyboardMarkup()
    inline_btn1 = types.InlineKeyboardButton("🚗 Մարդատար", callback_data='car')
    inline_btn2 = types.InlineKeyboardButton("🚌 Ավտոբուս", callback_data='bus')
    inline_btn3 = types.InlineKeyboardButton("🚛 Բեռնատար", callback_data='truck')
    inline_btn4 = types.InlineKeyboardButton("🛵 Մոտոտեխնիկա", callback_data='moto')

    inline_markup.row(inline_btn1, inline_btn2)
    inline_markup.row(inline_btn3, inline_btn4)

    bot.send_message(
        call.message.chat.id,
        "Ցանկանու՞մ եք ընտրել մեկ այլ տրանսպորտային միջոց:",
        reply_markup=inline_markup
    )


bot.polling(none_stop=True)

