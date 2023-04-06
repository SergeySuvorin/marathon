from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

fkb = InlineKeyboardMarkup(row_width=1)
fkb_butt_1 = InlineKeyboardButton(text='Научиться прощать!', callback_data='marathon') 
fkb_butt_2 = InlineKeyboardButton(text='Запись на группу', url = 'https://psyhologspbg.ru/link?fbclid=PAAaamyd89ZneBtxWydtXa-TIYBEeIGaCzjpp6dG4hPg2jpc7yVOQoJjTrTzk')
fkb_butt_3 = InlineKeyboardButton(text='Личная консультация', url = 'https://t.me/psyhologspbg')
fkb.add(fkb_butt_1,fkb_butt_2,fkb_butt_3,)

marathon_kb_1 = InlineKeyboardMarkup(row_width=1)
marathon_kb_1.add(InlineKeyboardButton(text='Начинаем!',callback_data='l1'))


marathon_kb_2 = InlineKeyboardMarkup(row_width=1)
marathon_kb_2.add(InlineKeyboardButton(text='Я готов!',callback_data='l2'),InlineKeyboardButton(text='Главное меню', callback_data='glav'))


marathon_kb_3 = InlineKeyboardMarkup(row_width=1)
marathon_kb_3.add(InlineKeyboardButton(text='Разбор моего маршрута',callback_data='info'), InlineKeyboardButton(text='Личная консультацию по рисунку',url = 'https://t.me/psyhologspbg'),InlineKeyboardButton(text='Главное меню', callback_data='glav'))


marathon_kb_4= InlineKeyboardMarkup(row_width=1)
marathon_kb_4.add(InlineKeyboardButton(text='Следующая практика!',callback_data='l2_1'), InlineKeyboardButton(text='Личная консультацию по рисунку',url = 'https://t.me/psyhologspbg'),InlineKeyboardButton(text='Главное меню', callback_data='glav'))


quest_kb = InlineKeyboardMarkup(row_width=1)
quest_kb.add(InlineKeyboardButton(text='Следующая практика', callback_data='l3'),InlineKeyboardButton(text='Мне нужна помощь', url = 'https://t.me/psyhologspbg'),InlineKeyboardButton(text='Главное меню', callback_data='glav'))


letter_kb = InlineKeyboardMarkup(row_width=1)
letter_kb.add(InlineKeyboardButton(text='Следующее письмо',callback_data='nl1'),InlineKeyboardButton(text='Главное меню', callback_data='glav'))


letter_kb_2 = InlineKeyboardMarkup(row_width=1)
letter_kb_2.add(InlineKeyboardButton(text='Последнее письмо',callback_data='nl2'),InlineKeyboardButton(text='Главное меню', callback_data='glav'))


next_pract = InlineKeyboardMarkup(row_width=1)
next_pract.add(InlineKeyboardButton(text='Следующая практика',callback_data='l4'),InlineKeyboardButton(text='Мне нужна помощь', url = 'https://t.me/psyhologspbg'),InlineKeyboardButton(text='Главное меню', callback_data='glav'))


day_3_kb = InlineKeyboardMarkup(row_width=1)
day_3_kb.add(InlineKeyboardButton(text='Рисуем!', callback_data='ris'),InlineKeyboardButton(text='Главное меню', callback_data='glav'))

sory_kb = InlineKeyboardMarkup(row_width=1)
sory_kb.add(InlineKeyboardButton(text='Ответил, идем дальше!', callback_data='ris_2'),InlineKeyboardButton(text='Мне нужна помощь', url = 'https://t.me/psyhologspbg'),InlineKeyboardButton(text='Главное меню', callback_data='glav'))

sory_kb_2 = InlineKeyboardMarkup(row_width=1)
sory_kb_2.add(InlineKeyboardButton(text='Сделал, дальше!', callback_data='ris_3'),InlineKeyboardButton(text='Главное меню', callback_data='glav'))

next_ex = InlineKeyboardMarkup(row_width=1)
next_ex.add(InlineKeyboardButton(text='Следующая практика', callback_data='next_ex'),InlineKeyboardButton(text='Мне нужна помощь', url = 'https://t.me/psyhologspbg'),InlineKeyboardButton(text='Главное меню', callback_data='glav'))


day_5 = InlineKeyboardMarkup(row_width=1)
day_5.add(InlineKeyboardButton(text='Идем дальше!',callback_data='day_5'),InlineKeyboardButton(text='Главное меню', callback_data='glav'))

day_5_2 = InlineKeyboardMarkup(row_width=1)
day_5_2.add(InlineKeyboardButton(text='Следующий этап',callback_data='day_5_2'),InlineKeyboardButton(text='Главное меню', callback_data='glav'))

day_5_3 = InlineKeyboardMarkup(row_width=1)
day_5_3.add(InlineKeyboardButton(text='Следующий этап',callback_data='day_5_3'),InlineKeyboardButton(text='Главное меню', callback_data='glav'))


day_6 = InlineKeyboardMarkup(row_width=1)
day_6.add(InlineKeyboardButton(text='Новая практика!',callback_data='day_6'),InlineKeyboardButton(text='Мне нужна помощь', url = 'https://t.me/psyhologspbg'),InlineKeyboardButton(text='Главное меню', callback_data='glav'))

day_6_2 = InlineKeyboardMarkup(row_width=1)
day_6_2.add(InlineKeyboardButton(text='Идем дальше!',callback_data='day_6_2'),InlineKeyboardButton(text='Главное меню', callback_data='glav'))

day_6_3 = InlineKeyboardMarkup(row_width=1)
day_6_3.add(InlineKeyboardButton(text='Играть',url = 'http://www.newcode.ru/soft/alphabet.html'),InlineKeyboardButton(text='Прошел игру!',callback_data='day_6_3') ,InlineKeyboardButton(text='Главное меню', callback_data='glav'))

day_6_4 = InlineKeyboardMarkup(row_width=1)
day_6_4.add(InlineKeyboardButton(text='Последняя практика!',callback_data='day_6_4'),InlineKeyboardButton(text='Мне нужна помощь', url = 'https://t.me/psyhologspbg'),InlineKeyboardButton(text='Главное меню', callback_data='glav'))

day_7 = InlineKeyboardMarkup(row_width=1)
day_7.add(InlineKeyboardButton(text='Создать!',callback_data='day_7'),InlineKeyboardButton(text='Главное меню', callback_data='glav'))

day_7_1 = InlineKeyboardMarkup(row_width=1)
day_7_1.add(InlineKeyboardButton(text='Выполнил',callback_data='day_7_1'),InlineKeyboardButton(text='Мне нужна помощь', url = 'https://t.me/psyhologspbg'),InlineKeyboardButton(text='Главное меню', callback_data='glav'))


day_7_2 = InlineKeyboardMarkup(row_width=1)
day_7_2.add(InlineKeyboardButton(text='Идем дальше!',callback_data='day_7_2'),InlineKeyboardButton(text='Главное меню', callback_data='glav'))

day_7_3 = InlineKeyboardMarkup(row_width=1)
day_7_3.add(InlineKeyboardButton(text='Оставить отзыв😀', url = 'https://t.me/psyhologspbg'),InlineKeyboardButton(text='Хочу проработать с психологом', url = 'https://t.me/psyhologspbg'),InlineKeyboardButton(text='Запись на группу', url = 'https://psyhologspbg.ru/link?fbclid=PAAaamyd89ZneBtxWydtXa-TIYBEeIGaCzjpp6dG4hPg2jpc7yVOQoJjTrTzk'),InlineKeyboardButton(text='Главное меню', callback_data='glav'))
