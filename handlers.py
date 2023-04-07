from aiogram import types
from aiogram import asyncio
from aiogram.types import Message, CallbackQuery, MediaGroup, InputFile, LabeledPrice, PreCheckoutQuery
from aiogram.dispatcher.filters import Command
from aiogram.types.message import ContentType
from keyboard import *
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
import aioschedule as schedule
from datetime import datetime, timedelta, timezone
import random
import aiogram.utils.markdown as md
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import Message, MediaGroup
from aiogram.types import InputMediaDocument
from config import *
from main import dp,bot

import sqlite3


class Form(StatesGroup):
    feedback  = State()





@dp.message_handler(Command('start'))
async def start(message: Message):

    await message.answer(f"Привет, {message.chat.first_name}👋\nТы попал на интенсив-марафон «Простить и отпустить».\n\nМеня зовут Юлия Королева. Я дипломированный практикующий клинический психолог, член ассоциации КПТ.\nПомогаю справляться с трудными жизненными ситуациями.\n\n<b>Безвыходных ситуаций нет – нужно только найти решение</b>\n\nЕсли в процессе у вас возникнут вопросы или сложности - нажмите на кнопку «мне нужна помощь» и я отвечу\n\n<b>Нажимай на кнопочки и начинаем</b>""", reply_markup=fkb)
    connect = sqlite3.connect('marathon.db')
    cursor = connect.cursor()
    if cursor.execute("SELECT * FROM users WHERE user_id = ?", (message.chat.id,)).fetchone() == None:
        cursor.execute("INSERT INTO users (user_id, name, username) VALUES (?, ?, ?)", [message.chat.id, message.chat.first_name,message.from_user.username ])
        cursor.close()
        connect.commit()
        connect.close()
    else:
        cursor.close()
        connect.commit()
        connect.close()

@dp.message_handler(Command('add_user_db_payed'))
async def start(message: Message):
    command = message.get_full_command()
    connect = sqlite3.connect('marathon.db')
    cursor = connect.cursor()
    cursor.execute("INSERT INTO pay_user (user_name) VALUES (?)", [command[1]])
    cursor.close()
    connect.commit()
    connect.close()


@dp.callback_query_handler(text= 'marathon')
async def l1(call:types.callback_query):
    await call.message.edit_text('<b>Чтобы получить доступ к марафону нужно произвести оплату 500 ₽ </b>\n\nПерейдите по ссылке ниже и ОБЯЗАТЕЛЬНО укажите имя пользователя телеграмм <b>в сообщении к оплате</b>, после этого отправьте мне в личные сообщения скриншот после оплаты',reply_markup = paym)


@dp.callback_query_handler(text= 'l2_1')
async def l1(call:types.callback_query):
    connect = sqlite3.connect('marathon.db')
    cursor = connect.cursor()
    # print(call.from_user.username)
    if cursor.execute("SELECT * FROM pay_user WHERE user_name = ?", (call.from_user.username,)).fetchone() != None:
        await call.message.edit_text('<b>Впереди, тебя ждут практики по борьбе с обидой!</b>\n\nМы будем учиться прощать. Я не скажу вам «Просто прости» или «Не обижайся, это плохо».\nЯ дам вам такие методы, которые дадут ответы на вопросы «Как не обижаться, если обидно?», «Как простить обиду, если обиделись?», «Как быть с обидами из самого детства?»\n\nПосле успешного прохождения всех практик, тебя ждут подарки',reply_markup = marathon_kb_1)
        cursor.close()
        connect.commit()
        connect.close()
    else:
        cursor.close()
        connect.commit()
        connect.close()
        await call.message.edit_text('<b>К сожалению вас нет среди участников марафона</b>\n\nПроверьте:\nПрошел ли платеж?\nПрислали скришот об оплате мне в личные сообщения?\n\nЕсли все эти моменты закрыты, не переживайте, скоро вас добавят в участники ',reply_markup = glab)




@dp.callback_query_handler(text= 'l1')
async def l1(call:types.callback_query):
    await call.message.edit_text('<b>Небольшая диагностика</b>\n\nЭта техника позволит осознать механизм переживания обиды, услышать свое «Я» и понять свои потребности, а кроме того – развить эмоциональный интеллект и научиться формировать адекватные ожидания.\n\nНужно подготовить бумагу для рисования, простые и цветные карандаши.\nДалее нужно вспомнить обиду, которая нанесена недавно либо которая ранила глубже других обид. Вспомнить нужно все детали ситуации, в которой была нанесена обида\n',reply_markup = marathon_kb_2)

@dp.callback_query_handler(text= 'l2')
async def l1(call:types.callback_query):
    await call.message.edit_text('После на горизонтально расположенном листе в любой части листа нужно нарисовать небольшое <b>транспортное средство🚗</b> (какое угодно – по выбору), после – <b>небольшой флажок🚩</b>\n\nДалее нужно заполнить оставшуюся чистой поверхность листа рисунком <b>природного ландшафта</b>. Это может быть совершенно фантастический ландшафт, где кактусы растут в ледяных пустынях, облака лежат на земле, а по солнцу можно пройти или проехать. Рисуйте реки, моря, горы, пляжи, ледники, болота, степи, леса, поля, тучи, небесные тела - что угодно…\n\nПо окончании рисования <b>проложите пунктиром маршрут от транспортного средства к флажку</b>. После этого проанализируйте, как именно пролегает этот маршрут',reply_markup = marathon_kb_3)




@dp.callback_query_handler(text='info')
async def mar(call:types.callback_query):
    await call.message.edit_text( text='Нарисовали?\n\nОтлично! Теперь смотрите расшифровку рисунка в файле👇', reply_markup = marathon_kb_4 )
    media = MediaGroup()
    media.attach(InputMediaDocument(open('answers.pdf', 'rb')))
    await bot.send_media_group(call.message.chat.id, media=media)


@dp.callback_query_handler(text= 'l2_1_2')
async def l1(call:types.callback_query):
    await call.message.delete()
    media = MediaGroup()
    media.attach(InputMediaDocument(open('questionnaire.pdf', 'rb')))
    await bot.send_media_group(call.message.chat.id, media=media)
    await bot.send_message(call.message.chat.id,'<b>А теперь первая техника «Анкета для радикального прощения»</b>.\n\nВ прикрепленном документе анкета, которую вы можете распечатать или переписать в тетрадь. Используя эту анкету, вы сможете преобразовывать ситуации или отношения с окружающими людьми.\n\n<b>Используйте анкету для освобождения от негативных чувств и эмоций!</b>',reply_markup = quest_kb)


@dp.callback_query_handler(text= 'l3')
async def l1(call:types.callback_query):
    await call.message.edit_text('<b>Рекомендую вам написать ТРИ письма своему обидчику</b>\n\nВ первом письме нужно излить весь свой гнев и обиду. Если вам от этого станет легче, пригрозите обидчику страшной местью. Пишите до тех пор, пока у вас есть что сказать.\n\nВозможно, при написании этого письма вам захочется плакать – это будут слезы гнева, печали, возмущения и обиды. Пусть текут. Если вас переполняет гнев, покричите в подушку или совершите другие физические действия, которые помогут вам прочувствовать гнев.\n\n<b>❗️Ни в коем случае не отсылайте ваши письма</b>',reply_markup = letter_kb)


@dp.callback_query_handler(text= 'nl1')
async def l1(call:types.callback_query):
    await call.message.edit_text('<b>Напишите второе письмо ✉️</b>\n\nВ нем должно быть уже намного меньше гнева и злобы, однако вы все еще держите своего обидчика в «черном теле» за то, что он, по вашему мнению, сделал вам плохого.\n\nОднако теперь попытайтесь проявить сострадание, понимание и великодушие, а также допустить возможность прощения',reply_markup = letter_kb_2)

@dp.callback_query_handler(text= 'nl2')
async def l1(call:types.callback_query):
    await call.message.edit_text('<b>И наконец, напишите третье письмо ✉️</b>\n\nЗдесь попытайтесь дать новую интерпретацию ситуации, основанную на принципах Радикального прощения.\n\nПишите третье письмо в свободной форме (своими словами), но опираясь на пункты, изложенные в анкете для радикального прощения.',reply_markup = next_pract)
    

@dp.callback_query_handler(text= 'l4')
async def l1(call:types.callback_query):
    await call.message.edit_text('<b>«Рисунок обиды»</b>\n\nРисунок позволяет «переместить из внутреннего мира во внешний» мысли и чувства, которые человек привык подавлять.\n\nОн может «рассказать» гораздо больше, чем вы осознаете...\nС ним можно в процессе работы что-то делать и т.д.\n\nПо сути это «исследовательский этап», но, прежде чем что-либо уничтожить хорошо бы узнать, что оно из себя представляет, почему и для чего существует',reply_markup = day_3_kb)


@dp.callback_query_handler(text= 'glav')
async def glav(call:types.callback_query):
    await call.message.edit_text(f"Привет, {call.message.chat.first_name}👋\nТы попал на интенсив-марафон «Простить и отпустить».\n\nМеня зовут Юлия Королева. Я эксперт по эмоциям, чувствам и метафорическим картам, помогаю восстановить отношения после рождения ребенка в семье, пережить измену, потерю и развод, справиться с обидой, чувством вины и стыда, повысить уверенность в себе, поднять самооценку.\n\n<b>Нажимай на кнопочки и начинаем</b>""", reply_markup=fkb)


@dp.callback_query_handler(text= 'ris')
async def l1(call:types.callback_query):
    await call.message.edit_text('<b>Представьте свою обиду и ответьте на ряд вопросов:</b>\n\nГде она живет (в груди, в голове и т.д.)?\nОбратите внимание на тело и спросите себя: что вы чувствуете, когда обида там сидит?\n\n•Как её пребывание в вашем теле отражается на вашем самочувствии?\n\n•Какого обида размера?\n\n•Какой консистенции (жидкая, твердая, газообразная)?\n\n•Какой температуры (холодная, теплая, горячая)?\n\n•Какая она на ощупь (приятная, липкая, мягкая, меняющая форму)?\n\n•Какого она цвета?',reply_markup = sory_kb)


@dp.callback_query_handler(text= 'ris_2')
async def l1(call:types.callback_query):
    await call.message.edit_text('<b>Нарисуйте обиду (желательно в виде какого-то образа)</b>\n\nПосмотрите на этот образ, какие у него «индивидуальные особенности» и опишите историю возникновения обиды.\n\n•С какого момента она существует?\n\n•Сколько места в вашей жизни занимает?\n\n•В какие моменты она появляется?\n\n•Какие негативные и позитивные функции она выполняет?\n\n•Готовы ли вы от нее отказаться и что вы можете сделать, чтобы обида ушла?',reply_markup = sory_kb_2)


@dp.callback_query_handler(text= 'ris_3')
async def l1(call:types.callback_query):
    await call.message.edit_text('<b>Прощание с обидой - это и есть прощение</b>\n\nВ конце работы рисунок уничтожьте (например вы можете его рвать, сжигать или мысленно отправлять обиду в небо («пускать по ветру»), следя, как по мере удаления она становится все меньше и меньше)',reply_markup = next_ex)


@dp.callback_query_handler(text= 'next_ex')
async def l1(call:types.callback_query):
    await call.message.edit_text('<b>Техника - «Пустой стул»</b>\n\nПсихологи, и я в том числе, иногда используют эту технику в рамках консультаций, чтобы помочь справиться с гневом, обидой, виной.\nВсе, что вам нужно, это поставить перед собой пустой стул, представить себе на нем обидчика, высказать ему все. Можно кричать и делать с этим стулом или с любым предметом то, что вы так хотели бы сделать для восстановления справедливости с обидчиком.\n\nЗадача в том, чтобы прожив чувства полностью, избавиться от них\n\n<b>Ты уже прошел половину заданий! Надеюсь ты помнишь о подарке😄</b>',reply_markup = day_5)


@dp.callback_query_handler(text= 'day_5')
async def l1(call:types.callback_query):
    await call.message.edit_text('<b>Сегодня мы с вами немного поработаем с психосоматикой</b>\n\nПонадобится листочек бумажки и ручка. Алгоритм содержит в себе три этапа. Работаем с симптомом. Если у вас обида никак симптомом не проявляется, то работайте с образом обиды\n\n<b>Первый этап</b>\n1. С кем из родных, близких или знакомых людей у вас ассоциируется образ бронхиальной астмы (аллергии, гипертонии, мастопатии, онкологической опухоли и т. д.)?\n\n2. Что вы чувствуете к этому человеку?\n\n3. Выпишите минимум 5 пунктов или ситуаций, по поводу которых вы обижаетесь\n\n4. Оцените свою обиду от 0 до 100, где 0 - совсем не обижаюсь, а 100 - обижаюсь очень сильно.\n\nМы будем работать с обидами, процент которых выше, чем 40',reply_markup = day_5_2)


@dp.callback_query_handler(text= 'day_5_2')
async def l1(call:types.callback_query):
    await call.message.edit_text('<b>Второй этап</b>\n1. Что противоположно обиде? (К примеру, легкость)\n\n2. Когда эта легкость может ощущаться? (К примеру, когда иду по берегу моря)\n\n3. Попадите туда и соединитесь с этим образом.\n\n4. Как сейчас видятся ситуации? На сколько процентов можно отпустить обиды сейчас?',reply_markup = day_5_3)

@dp.callback_query_handler(text= 'day_5_3')
async def l1(call:types.callback_query):
    await call.message.edit_text('<b>Третий этап</b> (Если обида не проходит)\n\n1. Представить обиду как ранку.\nЧто хотелось бы с ней сделать? (К примеру, смазать мазью)\n\n2. Что это за мазь? Как она выглядит? Представьте, что делаете это.\n\n3. Как сейчас видится ситуация? На сколько процентов можно отпустить обиды сейчас?\n\n<b>Данную технику стоит делать, повторяя, до снижения уровня обиды до 40 процентов</b>',reply_markup = day_6)

@dp.callback_query_handler(text= 'day_6')
async def l1(call:types.callback_query):
    await call.message.edit_text('<b>Алфавит</b>\n\nЭта техника для перепрограммирования бессознательного. Она позволяет поменять паттерны, устойчивые бессознательные программы, привычные способы автоматического реагирования, которые по каким-то причинам перестали быть полезными. Это может быть нежелательное поведение в каком-то контексте, страхи, неправильные привычки или отсутствие правильных привычек, неприятные воспоминания, ограничивающие убеждения… Эту технику также можно использовать как технику креативного мышления, интуитивного решения сложных задач или получения ответов на сложные вопросы. А мы с вами ее используем для проживания обиды\n\nВам потребуется развитый навык наблюдения за собственным состоянием и хорошее знание того состояния, которое требуется получить в результате игры. Описание состояния приведу ниже.\n\nЧтение инструкций займет некоторое время – рекомендую перечитать их несколько раз и время от времени возвращаться к ним. Все, о чем здесь написано – важно',reply_markup = day_6_2)
    media = MediaGroup()
    media.attach(InputMediaDocument(open('instruction.pdf', 'rb')))
    await bot.send_media_group(call.message.chat.id, media=media)


@dp.callback_query_handler(text= 'day_6_2')
async def l1(call:types.callback_query):
    await call.message.delete()
    await bot.send_message(call.message.chat.id, '<b>Запустить игру!</b>' ,reply_markup = day_6_3)


@dp.callback_query_handler(text= 'day_6_3')
async def l1(call:types.callback_query):
    await call.message.edit_text('<b>Комментарии к результатам игры</b>\n\nЕсли вы заметите, что ваше отношение к ситуации стало безразличным и это вам не нравится - это может означать, что вы прошли только первую фазу, устранение сильных негативных эмоций. Поработайте с этой ситуацией еще и еще: каждый раз она будет становиться все лучше и лучше\n\nЕсли вы не заметили никаких существенных изменений – значит, вы не получили качественного состояния в результате игры. Я рекомендую вам продолжать практику, обратив особое внимание на характеристики требуемого состояния, обратиться к обратиться к опытному психологу или пройти группу  PROЧувства ❤️\n\nЕсли вы замечаете, что через несколько дней эффект игры пропадает и негативные ситуации возвращаются снова - скорее всего, вам следует поработать с более широким контекстом\n\nРегулярное выполнение данной техники поможет вам серьезно улучшить качество вашей жизни. Среднее количество упражнений, требуемое для поддержания хорошей формы - 2-3 раза в неделю',reply_markup = day_6_3_1)


@dp.callback_query_handler(text= 'day_6_3_1')
async def l1(call:types.callback_query):
    await call.message.edit_text('<b>Книга Хижина, даю почитать)</b>',reply_markup = day_6_4)
    media = MediaGroup()
    media.attach(InputMediaDocument(open('Yang_Hizhina.fb2', 'rb')))
    await bot.send_media_group(call.message.chat.id, media=media)




@dp.callback_query_handler(text= 'day_6_4')
async def l1(call:types.callback_query):
    await call.message.delete()
    await bot.send_message(call.message.chat.id, 'Подождите немного, видео загружается')
    await bot.send_video(call.message.chat.id, open('video.mp4','rb'))
    await bot.send_message(call.message.chat.id, 'И последняя техника, которую я дам вам для работы с обидой называется <b>«Прощальная открытка»</b>\nМы завершаем с вами этот путь и начинаем новый, полный открытий, любви, принятия и свободы\n\nПеред тем, как вы начнете создавать прощальную открытку, закройте ненадолго глаза и обдумайте, с кем или чем бы вы хотели попрощаться. Это может быть какое-то чувство, ваша привычная манера поведения (например, «вечная жертва») или какое-то другое ваше качество… Это может быть человек, который обидел вас, которого вы покинули, или который покинул вас… Это может быть место работы, место проживания, желание, иллюзия или что-то еще, что сейчас вам представляется важным\n\nЗакройте глаза, позвольте вашему дыханию беспрепятственно течь и попробуйте понять, почувствовать, прощание с чем или с кем для вас сейчас важнее всего…\n\n<b>Пусть ваши мысли приходят и уходят, пусть образы возникают и исчезают, пусть рождаются краски и формы…</b>',reply_markup = day_7)


@dp.callback_query_handler(text= 'day_7')
async def l1(call:types.callback_query):
    await call.message.edit_text('Вспомните, как вы посылаете открытки друзьям из мест, где путешествуете. Обычно на одной стороне такой открытки находится картинка, а на другой – текст.\n\nТак и на прощальных открытках. Когда ваша картинка высохнет, переверните ее и напишите на обратной стороне текст, несколько строк, обращенных к тому, с кем вы хотели бы попрощаться…\n\nЧтобы открытка дошла до адресата, на ней пишут адрес и наклеивают почтовую марку. Но, в данном случае, ваша почтовая открытка может достичь адресата только в вашем воображении. Вы не можете бросить ее в почтовый ящик, но вы можете сделать для своей открытки конверт или упаковать так, как вам хочется... Выберите подходящий упаковочный материал (бумагу, ткань и т.п.) из того, что есть, и придумайте подходящую упаковку для вашей открытки. На ней напишите имя адресата и имя отправителя. Дальше вы можете поступить с ней так, как считаете нужным, желательно уничтожить, например провести огненный ритуал\n\nРитуальное сожжение придает вашей работе завершенность. Когда вы видите, как ваши слова обращаются в пепел и улетают с дымом происходит что-то важное…',reply_markup = day_7_1)

@dp.callback_query_handler(text= 'day_7_1')
async def l1(call:types.callback_query):
    await call.message.edit_text('<b>"Ты никогда не узнаешь, куда ведёт эта дорога, если будешь стоять на месте..."\n\n"Дорогу осилит идущий"</b>',reply_markup = day_7_2)



@dp.callback_query_handler(text= 'day_7_2')
async def l1(call:types.callback_query):
    await call.message.edit_text('<b>Ну что, вам понравились практики?</b>\n\nЗачастую в жизни возникают сложные ситуации, и не всегда получается справиться со своими эмоциями. Нерешенные проблемы могут стать причиной тревоги, страхов, недостатка самоуважения и ряда других неприятностей.\n\nПриглашаю вас на индивидуальные консультации, в индивидуальную терапию и группу PROЧувства. Там вы сможете разобраться в своих чувствах, справиться с проблемами личного характера и наладить отношения с собой и окружающими.\n\nЯ помогу вам справиться с тревожными состояниями, паническими атаками, профвыгоранием. Вы сможете доверять себе, наладите отношения с собой и окружающими, уверенно посмотрите в будущее, перестанете бояться ошибок. Вы научитесь распознавать и проживать любые ваши чувства и эмоции без вреда для вашего здоровья и окружающих.\n\nВы прошли большой путь, вы уже молодец! Внизу вас ждёт подарок - гайд - основные этапы, которые проходит человек на пути к прощению. Именно на этих шагах был построен марафон.\n\nА для тех, кто поделится отзывом, я приготовила подарок🎁\nЕщё две уникальные рабочие техники, одна из них для прощения родителей, а вторая... узнаете сами:)\n\nЖду вас! До встречи.',reply_markup = day_7_3)
    media = MediaGroup()
    media.attach(InputMediaDocument(open('gift1.pdf', 'rb')))
    await bot.send_media_group(call.message.chat.id, media=media)


@dp.callback_query_handler(text= 'feed')
async def feed(call:types.callback_query):
    await call.message.delete()
    await Form.feedback.set()
    await bot.send_message(call.message.chat.id,'<b>Напишите свой отзыв, и я передам его</b>\n\nЗа решением какого вопроса Вы пришли на марафон? Решился ли ваш вопрос?\n\nЧто больше всего понравилось?\n\nКакая для вас главная ценность марафона?\n\nКому бы Вы порекомендовали мои услуги?\n\nМогу ли я использовать Ваш отзыв в социальных сетях?',reply_markup='')


@dp.message_handler(state=Form.feedback)
async def process_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['feedback'] = message.text
    await bot.forward_message(503738344, message.from_user.id, message.message_id)
    await bot.send_message(message.chat.id,'Ваш отзыв доставлен!\n\nВот ваши обещанные подарки!\n\n/start - в главное меню')
    await state.finish()
    media = MediaGroup()
    media.attach(InputMediaDocument(open('gift2.pdf', 'rb')))
    media.attach(InputMediaDocument(open('gift3.pdf', 'rb')))
    await bot.send_media_group(message.chat.id, media=media)
