import telebot
from telebot import types


TOKEN = '6633226061:AAGvDln9DHctNj-zV16tOZObKDZt4iTNlgc'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    chat_id = message.chat.id
    photo = open('MoskvaZoo.jpg', 'rb')
    bot.send_photo(chat_id, photo)
    markup = types.InlineKeyboardMarkup()
    info_button = types.InlineKeyboardButton("INFO", callback_data='info')
    project_button = types.InlineKeyboardButton("PROJECT", callback_data='project')
    feedback_button = types.InlineKeyboardButton("Обратная связь", callback_data='feedback')
    markup.add(info_button)
    markup.add(project_button)
    markup.add(feedback_button)
    bot.send_message(chat_id, "Приветствуем вас в Московском зоопарке! Хотите узнать о нашем зоопарке, нажмите кнопочки ниже, если хотите узнать, какое вы тотемное животное, пропишите команду: /quiz", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "info":
        bot.send_message(call.message.chat.id, "Московский зоопарк — один из старейших зоопарков Европы с \
уникальной коллекцией животных и профессиональным \
сообществом. Он выполняет много функций, например, там \
проводятся разные лекции для посетителей и курсы \
профессиональной переподготовки для специалистов сферы. \
\
Важная задача зоопарка — вносить вклад в сохранение биоразнообразия планеты. \
Сотрудники зоопарка пытаются уберечь виды от вымирания и вернуть их в естественную среду обитания. \
Например, лошади Пржевальского исчезли в дикой природе и сохранились только в зоопарках. \
\
При нынешних темпах развития цивилизации к 2050 году могут \
погибнуть около 10 000 биологических видов. Московский \
зоопарк пытается сохранить их. Чтобы выполнять \
природоохранную функцию, у зоопарка есть специальные \
программы и даже целый Центр воспроизведения редких видов животных.")

    elif call.data == "project":
        bot.send_message(call.message.chat.id, "«Возьми животное под опеку» («Клуб друзей») — это одна из программ, помогающих \
зоопарку заботиться о его обитателях. Программа позволяет с помощью \
пожертвования на любую сумму внести свой вклад в развитие зоопарка и \
сохранение биоразнообразия планеты. \
\
Сейчас в Московском зоопарке живёт около 6 000 животных, представляющих \
примерно 1 100 биологических видов мировой фауны. Каждое животное уникально, и \
все требуют внимание и уход. Из ежедневного рациона питания животного как раз \
и рассчитывается стоимость его опеки.\
\
Взять под опеку можно разных обитателей зоопарка, например, слона, льва, \
суриката или фламинго. Это возможность помочь любимому животному или даже \
реализовать детскую мечту подружиться с настоящим диким зверем. Почётный \
статус опекуна позволяет круглый год навещать подопечного, быть в курсе событий \
его жизни и самочувствия.\
\
Участником программы может стать любой неравнодушный: и ребёнок, и большая корпорация. \
Поддержка опекунов помогает зоопарку улучшать условия для животных и повышать уровень их благополучия.")

    elif call.data == "feedback":
        bot.send_message(call.message.chat.id, "Номер телефона: +7(962) 971 38 75 \
                                                                                        Почта: zoofriends@moscowzoo.ru")


@bot.message_handler(content_types=['text'])
def quiz(message):
    if message.text == '/quiz':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Да')
        btn2 = types.KeyboardButton('Нет')
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, 'Давайте поиграем в викторину Вопрос&Ответ. Вы любите животных?', reply_markup=markup)


    elif message.text == 'Да':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Конечно')
        markup.add(btn1)
        bot.send_message(message.from_user.id, 'Отлично, а Вы знаете кто такие млекопитающие?', reply_markup=markup, parse_mode='Markdown')


    elif message.text == 'Конечно':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Каменная куница')
        btn2 = types.KeyboardButton('Капская землянная белка')
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, 'Это прекрасно! Тогда вам известны эти виды:', reply_markup=markup, parse_mode='Markdown')


    elif message.text == 'Каменная куница':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Стать опекуном')
        btn2 = types.KeyboardButton('/quiz')
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, """Ареал каменной куницы охватывает горные области Передней, 
    Средней  и Центральной  Азии, горные и отчасти равнинные области
    Европы (от Пиренейского полуострова до Монголии и Гималаев).  В США 
    каменная куница специально завезена для «пушной охоты».
    Внешний вид и морфология.
    Каменная куница – зверек средних размеров: длина тела 40-54 см, 
    длина хвоста 22-30 см, масса до 2,3 кг. 
    Шерсть коричневатая, довольно  жесткая. Горловое пятно белого 
    цвета (отсюда и название «белодушка»), имеет подковообразную
    форму и заходит на внутреннюю сторону передних лап. (https://moscowzoo.ru/upload/iblock/ece/ecea20c62f0796f43d3114ed2eb00311.jpg ).
    Это Ваше Тотемное животное.
    Вы можете помочь Каменной кунице, став ее опекуном, находящейся в Московском зоопарке.
    ПРОСТО НАЖМИ НА КНОПОЧКУ: СТАТЬ ОПЕКУНОМ! """, parse_mode='Markdown', reply_markup=markup)


    elif message.text == 'Стать опекуном':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.from_user.id, 'Благодарим Вас за то что Вы остались не равнодушны! Для более подробной информации пройдите по' + '[ссылке](https://moscowzoo.ru/my-zoo/become-a-guardian/)', parse_mode='Markdown')


    elif message.text == 'Капская землянная белка':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Стать опекуном')
        btn2 = types.KeyboardButton('/quiz')
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, """ Капские земляные белки обитают в южной и юго-западной части Африки, за исключением 
    прибрежных территорий. Их распространение шире, чем Капская провинция, возможно, их 
    назвали так для того, чтобы отличать от древесной белки, завезённой из Европы во второй 
    половине 19 века и найденной в окрестностях Кейптауна. 
    Внешне земляная белка напоминает обыкновенную - небольшой симпатичный зверёк с
    пушистым хвостом. Длина тела этого грызуна 22-26 см, хвоста - около 25 см, вес от 420 до 600 г.
    Половой диморфизм очень незначительный - самцы чуть крупнее и весят на 8-10 % больше самок. (https://moscowzoo.ru/upload/iblock/a42/a424a10a167636591536504a7fdfb21a.jpg ).
    Это Ваше Тотемное животное.
    Вы можите помочь Капской землянной белке, став ее опекуном, находящейся в Московском зоопарке.
    ПРОСТО НАЖМИ НА КНОПОЧКУ: СТАТЬ ОПЕКУНОМ! """, parse_mode='Markdown', reply_markup=markup)

    elif message.text == 'Стать опекуном':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.from_user.id, 'Благодарим Вас за то, что Вы не остались равнодушны! Для более подробной информации пройдите по ' + '[ссылке](https://moscowzoo.ru/my-zoo/become-a-guardian/)', parse_mode='Markdown')


    elif message.text == 'Нет':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Более менее')
        markup.add(btn1)
        bot.send_message(message.from_user.id, """Тогда другой вопрос, Вам знакомы Птицы""", reply_markup=markup, parse_mode='Markdown')


    elif message.text == 'Более менее':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Свиязь')
        btn2 = types.KeyboardButton('Турако ливингстона')
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, 'Тогда вам известны эти виды:', reply_markup=markup, parse_mode='Markdown')


    elif message.text == 'Свиязь':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Стать опекуном')
        btn2 = types.KeyboardButton('/quiz')
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, """Свиязь – объект промысловой и любительской охоты. Описание охоты на уток, в том числе и
    свиязей, можно найти у многих писателей - Тургенева, Аксакова, Пришвина.
    Свиязь гнездится в Северной Палеарктике от Исландии на западе до Чукотки и побережья
    Охотского моря на востоке. Основной ареал находится на территории России, Скандинавских стран.
    Свиязь – утка средних размеров с относительно короткой шеей, сравнительно коротким клювом и
    длинным заострённым хвостом. Общая длина 45-51 см, размах крыльев 75-86 см, масса самцов
    600-1100 г, самок – 500-1000 г. (https://animalreader.ru/wp-content/uploads/2015/07/svijaz-zhelannyj-obekt-ohoty-animal-reader.ru-001.jpg)
    Это ваше тотемное животное.
    Вы можите помочь Свиязю, став его опекуном, находящегося в Московском зоопарке. 
    ПРОСТО НАЖМИ НА КНОПОЧКУ: СТАТЬ ОПЕКУНОМ! """, parse_mode='Markdown', reply_markup=markup)


    elif message.text == 'Стать опекуном':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.from_user.id, 'Благодарим Вас за то, что Вы не остались равнодушны !Для более подробной информации пройдите по ' + '[ссылке](https://moscowzoo.ru/my-zoo/become-a-guardian/)', parse_mode='Markdown')


    elif message.text == 'Турако ливингстона':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Стать опекуном')
        btn2 = types.KeyboardButton('/quiz')
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, """Природоохранный статус - относится к видам, вызывающим  наименьшие опасения – IUCN (LC), 
однако, использовать перья этого турако для украшения разрешается только знати местных
африканских племён.
Обитает в Юго-Восточной Африке, населяет дождевые, горные и светлые листопадные леса,
пальмовые и акациевые саванны. В горы поднимается до высоты 2000 м.их панцири высокие и куполообразные. Разница в размерах самок и самцов выражена не так резко.
Длина тела вместе с хвостом около 45 см, масса от 260 до 380 г. В оперении преобладает зелёная
окраска, местами с голубым оттенком. Красные перья на крыльях видны только во время полёта.
На голове имеется хохолок, перья которого достигают длины 6,5-7,5 см. (https://sun9-26.userapi.com/impg/c856036/v856036390/1e3858/pqPPAM7WwOo.jpg?size=790x526&quality=96&sign=ca29ca45767e6cb213af938beea3d012&c_uniq_tag=kmiE9RM6yewX2CfLlPOLZFcOe2yjFefY-vlexXlJMyQ&type=album).
Это Ваше Тотемное животное.
Вы можите помочь Турако ливингстоне, став ее опекуном, находящейся в Московском зоопарке.
ПРОСТО НАЖМИ НА КНОПОЧКУ: СТАТЬ ОПЕКУНОМ! """, parse_mode='Markdown', reply_markup=markup)


    elif message.text == 'Стать опекуном':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.from_user.id, 'Благодарим Вас за то, что Вы не остались равнодушны! Для более подробной информациипройдите по ' + '[ссылке](https://moscowzoo.ru/my-zoo/become-a-guardian/)', parse_mode='Markdown')


bot.polling(none_stop=True, interval=0)