
TEXTS = {
    'ru': {
        'greetings': """
Привет, студент БФУ! 🌍✨

Рады тебя видеть в официальном чат-боте для иностранных студентов Балтийского федерального университета им. И. Канта! 🎓🇷🇺

Я твой персональный помощник по любым вопросам в Калининграде. Со мной ты сможешь:

🧠 Прокачать русский язык с помощью умного ИИ-тренажера
🏛️ Узнать полезную информацию об университете и его жизни:
📍 Найти корпуса и общежития
🏠 Решить вопросы с заселением
🤝 Получить поддержку и помощь
🏦 Узнать про полезные услуги СБЕР 😊
🚀 Адаптироваться в городе и найти единомышленников

С чего начнем? 👇 Выбери пункт меню! 
        """,

        'language_selection': 'Выберите язык/Choose a language:',
                              'errors': {
    'start_error': 'Произошла ошибка при запуске бота. Пожалуйста, попробуйте позже.',
    'info_error': 'Ошибка при загрузке информации',
    'back_error': 'Ошибка при возврате в главное меню',
    'audio_error': 'Ошибка при обработке',
    'photo_error': 'Произошла ошибка при загрузке фото',
    'gigachat_error': 'Ошибка инициализации GigaChat:',
},

'keyboards': {
    'main_keyboard': {
        'info': 'Инфо',
                'location': 'Корпуса',
                'dormitory': 'Общежития',
                'hospital': 'Медцентр',
                'sber': 'СБЕР',
                'critical': 'SOS',
                'language_check': 'Тренажер',
                'back': 'Назад'
            },
            'critical_keyboard': {
                'police': 'Службы',
                'hotline': 'Горячая линия ФМС',
                'government': 'Местные органы власти',
                'consulate': 'Консульство',
                'back': 'Назад',
                'appeal':'Электронное обращение'
            },
            'dormitory_keyboard': {
                'check-in': 'Заселение в общежитие',
                'payment': 'Оплата',
                'address': 'Адреса общежитий',
                'rules': 'Правила проживания',
                'laundry': 'Прачечная',
                'no_certificate': 'Нет сертификата прививок или флюорографии',
                'details': 'Подробнее',
                'back': 'Назад'
            },
            'dormitory_locations_keyboard': {
                'dormitory_1': 'Соммера',
                'dormitory_2': 'Чернышевского',
                'dormitory_3': 'А. Невского',
                'dormitory_4': 'А. Невского',
                'dormitory_5': 'Чайковского',
                'dormitory_6': 'Азовская',
                'dormitory_7': 'Еловая',
                'dormitory_8': 'Еловая',
                'dormitory_9': 'Юбилейная',
            },
            'payment_keyboard': {
                'sber_payment': 'Оплатить в Сбере',
        'back': 'Назад',
        'more': 'Подробнее'
    },
    'language_check_keyboard': {
        'grammar_keyboard': {
            'to_russian': 'Перевести на русский',
            'from_russian': 'Перевести с русского',
            'back': 'Назад'
        },
        'speaking_keyboard': {
            'back': 'Назад'
        },
        'language_check_keyboard': {
            'Authorization':'Напиши свое имя',
            'to_lessons':'Учить русский',
            'audio': 'Аудирование',
            'grammar': 'Грамматика',
            'speaking': 'Говорение',
            'back': 'Назад'
        }
    },
    'location_keyboard': {
                'loc_1': '🏛️ Админкорпус',
                'loc_2': '🧮 Физмат',
                'loc_3': '🧬 Живые системы',
                'loc_4': '🏫 ИГН',
                'loc_5': '👨‍🏫 Образование',
                'loc_6': '🛌 Шайба',
                'loc_7': '⚖️ Юридический',
                'loc_8': '📚 Медбиблиотека',
                'loc_9': '🏐 ФОК',
                'loc_10': '👩‍🏫 Свечка',
                'loc_11': '✨ Ресурсцентр',
                'loc_12': '🩺 Мединститут',
                'loc_13': '👩‍⚕️ Клиника',
                'loc_14': '🚗 Транспортный',
                'loc_19': '🏡 База №19',
                'loc_20': '🏡 База №20',
                'loc_21': '🌳 Ботанический',
                'loc_22': '🏊‍♂️ Бассейн',
                'loc_23': '🧪 Лабкорпус',
                'loc_24': '🎓 Колледж',
                'loc_25': '👨‍🔬 Киберфиз',
                'loc_27': '⚙️ ИТИ',
                'loc_28': '💸 Экономика',
                'loc_29': '🥽 Геофизика',
                'loc_32': '🔬 Фабрика',
                'loc_35': '🏊‍♂️ Бассейн',
                'back': '⬅️ Назад'
    },
    'university_info_keyboard': {
        'schedule': 'Расписание',
        'scholarship': 'Стипендии',
        'office_contacts': 'Контакты учебного офиса',
        'visa_center': 'Визово-миграционный центр',
        'back': 'Назад'
    },
    'language_selection_keyboard': {
        'back': 'Назад'
    },
    'sber_keyboard': {
        'educational_loan': 'Образовательный кредит',
        'sber_card': 'Карта для стипендии',
        'useful_links': 'Полезные ссылки',
        'details': 'Подробнее',
        'back': 'Назад'
    },

    'hospital_keyboard': {
        'insurance':'Медицинское страхование',
        'attachment':'Прикреплению к поликлинике'
    }
},

'handlers': {
    'critical_handlers': {
        'critical_police_handler': '''
🚨 *Экстренные контакты*

*Единый номер служб экстренного реагирования*
(пожарной охраны, МЧС, полиции, скорой помощи, газовой службы)
📞 *112*

👨‍🚒 *Пожарные и спасатели*
📞 *01* (с городского телефона) | *101* (с мобильного)

👮 *Полиция*
📞 *02* (с городского телефона) | *102* (с мобильного)

🏥 *Скорая помощь*
📞 *03* (с городского телефона) | *103* (с мобильного)

💡 Сохрани эти номера в быстром доступе!
                                                    ''',

        'critical_hotline_handler': '''
🚪 *Сектор визово-миграционной поддержки*

📞 *Телефон*:
+7 (4012) 595-595 (доб. 7454) — миграционный учет и визы 
+7 (4012) 595-595 (доб. 7452) — визовые приглашения

🏢 *Адрес*:
Россия, г. Калининград, ул. А. Невского, 14, корп. 2, каб. 114

🕒 *Приемные часы*:
Пн 14:00–17:00
Вт 10:00–13:00
Чт 14:00–17:00
Пт 10:00–13:00

Обед 13:00–14:00 
                                                    ''',

        'critical_government_handler': '''
🏛️ *Комитет по межнациональным отношениям и реализации миграционной политики в Санкт‑Петербурге*

Вы можете записаться на онлайн- или офлайн-встречу!

1. 📅 *Офлайн-формат* (личный прием граждан)
Как записаться?
Запись по телефону: *576-28-08* 1.
Часы работы приемной:
• Понедельник – четверг: *9:00 – 18:00*
• Пятница: *9:00 – 17:00*
• Обеденный перерыв: *13:00 – 14:00* (звонки не принимаются)
• Суббота и воскресенье: выходные.

*Что взять с собой?*

Паспорт или иной документ, удостоверяющий личность.

*Как проходит прием?*
Вас примет председатель Комитета, его заместитель или уполномоченные лица 4.

Обращение фиксируется в карточке личного приема.

Простые вопросы → устный ответ (с записью в карточку).

Сложные вопросы → письменный ответ позже.

Вопрос не в компетенции Комитета → вас направят в соответствующую инстанцию.
⚠️ Если по вашему вопросу уже был дан ответ, в повторном приеме могут отказать.

2. 🌐 *Онлайн-прием*
Записаться можно через официальные ресурсы Комитета.
Ссылка для записи:''',

        'critical_consulate_handler': '''
*Представительство МИД России в Калининграде* 🏛️

*Адрес*: 🏠
236022, Россия, г. Калининград, ул. Кирова, 17

*Телефоны*: 📞
Приемная: + 7 (401) 221-37-12
Факс: + 7 (401) 221-06-26
Консульский отдел: + 7 (401) 221-16-68
Паспортный отдел: + 7 (401) 295-82-02
Отдел оформления приглашений: + 7 (4012) 21-59-28

*Приём граждан по консульско-правовым вопросам* ⚖️
Пн-Чт: с *9:00* до *17:00* (перерыв с *12:00* до *14:00*)
Пт: с *9:00* до *16:00* (перерыв с *12:00* до *14:00*)
Сб-Вс: 🚫 Выходной
                                            ''',
    },

    'dormitory_handlers': {
        'dormitory_text': """
       Для оформления места в общежитии 🏠 важно заранее подготовить необходимые документы 📋 и ознакомиться с процедурой подачи заявления 📝. Ознакомьтесь с подробной инструкцией ниже 👇:""",

        'payment_text': """
Оплатить общежитие можно двумя путями.

1. Лично. В кабинет № 222 административного корпуса, 2 этаж. Здесь ты получишь квитанцию для оплаты в кассе на том же этаже. Оплатить через кассу можно наличными в рублях или банковской картой.

2. Удаленно на сайте.

Первокурсники оплачивают при заселении полностью первый семестр. Далее осенний семестр оплачивается до 15 сентября, а весенний – до 15 февраля.
                                            """,
        'rules_text': """
        Нажми сюда 🏘️ «Правила проживания», чтобы ознакомиться с важными правилами и рекомендациями, которые помогут сделать твоё пребывание комфортным и безопасным. Здесь ты найдёшь всю необходимую информацию о режиме работы, обязанностях жильцов, правилах поведения и многое другое.✨""",
        'laundry_text': """
🏢 *Расположение*:
Прачечные находятся в каждом общежитии. Точное расположение и график работы подскажут комендант или вахтёр.

🧼 *Правила использования*:
• Приноси свой стиральный порошок
• Используй специальные мешки для нижнего белья
• *Запрещено* стирать обувь (это ломает машины)
• Перед использованием ознакомься с инструкцией на месте
• Суши белье в специальной оборудованной комнате

⏰ *Важно!*
Возвращай ключ вахтёру *точно в оговоренное время* — другие студенты тоже хотят постирать свои вещи! 🙏

✨ Всё организовано для твоего удобства — пользуйся аккуратно!
                                            """,
        'no_certificate_text': """
ЕСЛИ НЕТ СЕРТИФИКАТА ПРИВИВОК ИЛИ ФЛЮОРОГРАФИИ

1 *Если у вас отсутствует свежая флюорография*
Вы можете сделать ее в нескольких местах, например:
- В КДЦ БФУ за 320 руб. по карте студента (она должна быть в
наличии). Расположение КДЦ: [https://goo.gl/maps/P4djCkwJ3ZQHThgGA]
(https://goo.gl/maps/P4djCkwJ3ZQHThgGA)
- в Медэксперте (ул. Космическая или московский пр-т), до 17:00, за
450 руб. без снимка. Расположение:
[https://goo.gl/maps/rRiC1Nh35BNPw2w3A](https://goo.gl/maps/rRiC1Nh35BNPw2w3A)
- Novomed (Гагарина 2В) до 17:00, 350 руб.
Расположение:
[https://goo.gl/maps/kgEkj4yLnWBNbFUm6](https://goo.gl/maps/kgEkj4yLnWBNbFUm6)

2 *Если у вас отсутствуют сертификаты о прививках*

Обратитесь в любое отделение Медэксперта. Там вам необходимо
сдать анализ крови, который называется “Напряженность к иммунитету
для кори и дифтерии”. Анализ можно сдать каждый день, понедельник
- пятница с 7:30 до 19, выходные с 7:30 до 17:00.

Анализ сдается натощак.

Результат выдается через 4 рабочих дня (результат можно получить в
личном кабинете).
                                                """,
    },

    'dormitory_location_handlers': 'Общежитие №',

    'hospital_handlers': {
        'hospital_text': '''
*Университетская клиника БФУ им. И. Канта*

*Адрес*: 236041, Россия, Калининград, ул. 9 апреля, 60
*Контакты*: +7 (4012) 31-33-39    kdc@kantiana.ru
  '''
    },

    'language_check_handlers': {
        'grammar_handlers': {
            'language_grammar_handler': '''
                                            *Выберите вариант перевода*:
                                            ''',
            'translate_to_russian_handler': '''
                                            Переведите данный текст на русский язык:
                                            ''',
            'translate_from_russian_handler': '''
                                            Переведите данный текст с русского языка на свой:
                                            ''',
        },

        'listening_handlers': {
            'send_voice': 'Прослушайте текст и попробуйте написать его на русском.',
        },

        'speaking_handlers': {
            'topics': [
                'Расскажите немного о своей семье.',
                'Есть ли у вас домашнее животное?',
                'Какие блюда вам нравятся?',
                'Опишите свою комнату.',
                'Какой ваш любимый вид транспорта?',
                'Где вы любите проводить свободное время?',
                'Как вы проводите свое воскресенье?',
                'Ваше самое яркое воспоминание детства?',
                'Куда вы хотели бы отправиться в путешествие?',
                'Какие привычки помогают вам оставаться продуктивным?',
                'Как прошёл твой вчерашний день?',
                'Кем ты работаешь и чем занимаешься на работе?',
                'О чём мечтает твоя семья?',
                'Что интересного произошло с тобой на прошлой неделе?',
                'Чем увлекается твой лучший друг?',
                'Поделись своими впечатлениями от последнего фильма, который смотрел.',
                'Почему ты решил учиться в Калининграде?'
            ],
            'speaking_send': 'Жду твой рассказ на тему:',
            'handle_voice_message': 'Результат анализа:',
        }
    },

    'location_handlers': {
        'addresses_handler': 'Выбери корпус',
        'loc_1_handler': """
*Административный корпус, ул. А.Невского, 14*

Здесь находятся:
· Делопроизводство (каб. 115)
· Служба бухгалтерского учета (каб. 212)
· Архив (каб. 221)
· Группа расчетов по доходам и налоговому учету (каб.222)
· Касса (второй этаж)
· Зал Аквариум
· Зал Максимум
· Столовая (первый этаж)

                                            """,

        'loc_2_handler': """
*Корпус №2, Институт физики, математики и информационных технологий («Физмат»), ул. А.Невского, 14*

Здесь находятся:
· Отдел по работе с иностранными обучающимися (каб. 119)
· Сектор визово-миграционной поддержки (каб. 114)
· Приемная комиссия (каб. 116 и 117)
· Библиотека, кабинет 202 («Читальный зал»)
· Служба обслуживания IT-инфраструктуры (каб. 121)

                                            """,

        'loc_3_handler': """
*Корпус №3, ул. Университетская, 2*

Здесь находятся:
· Институт живых систем
· Главная университетская библиотека: научный абонемент (каб. 126), читальный зал (каб. 115)

                                            """,

        'loc_4_handler': """
*Корпус №4, ул. Чернышевского, 56 («Корпус с часами»)*

Здесь находятся:
· Институт гуманитарных наук
· Центр русского языка (каб. 01)
· Музей советского детства

                                            """,

        'loc_5_handler': """
*Корпус №5, ул. Чернышевского, 56а*

Здесь находится:
· Институт образования

                                            """,

        'loc_6_handler': """
*Корпус №6, ул. А. Невского, 14б («Шайба»)*

Здесь находятся:
·Комплекс студенческих общежитий (каб. 101)
·Управление внеучебной деятельности
                                            """,

        'loc_7_handler': """
*Корпус №7, ул. Фрунзе, 6*

Здесь находятся:
·Учебная телестудия
·Юридический институт
                                            """,

        'loc_8_handler': """
*Корпус №8, ул. 9 Апреля, 5*

Здесь находится:
· Медицинская библиотека

                                            """,

        'loc_9_handler': """
*Корпус №9, ул. А.Невского,14 («ФОК»)*

Здесь находится:
Физкультурно-оздоровительный комплекс

                                            """,

        'loc_10_handler': """
*Корпус №10, ул. А. Невского. 14 («Свечка»)*

Здесь находятся:
· Центр социально-экономической поддержки студентов (каб. 14)
· Центр карьеры

                                            """,

        'loc_11_handler': """
*Корпус №11, ул.Боткина, 3*

Здесь находится:
· Региональный ресурсный центр симуляционного обучения и аккредитации в медицине

                                            """,

        'loc_12_handler': """
*Корпус №12, ул.Боткина, 4-6*

Здесь находится:
· Медицинский институт

                                            """,

        'loc_13_handler': """
*Корпус №13, ул.Боткина, 4-6*

Здесь находится:
· Университетская клиника

                                            """,

        'loc_14_handler': """
*Корпус №14, ул. Александра Невского, 14, корп. 4*

Здесь находится:
· Группа транспортного обслуживания
· Управление по эксплуатации имущественного комплекса
· Отдел по обеспечению режимов
                                            """,
        
        'loc_19_handler': """
*Корпус №19, Пионерский, пос. Рыбное, 23*

Здесь находится:
· База учебных практик

                                            """,

        'loc_20_handler': """
*Корпус №20, Светлогорск, Калининградский проспект, 102*

Здесь находится:
· База учебных практик

                                            """,

        'loc_21_handler': """
*Корпус №21, ул. Лесная, 12*

Здесь находится:
· Ботанический сад

                                            """,

        'loc_22_handler': """
*Корпус №22, ул. А.Невского,14*

Здесь находится:
· Учебно-физкультурный комплекс с бассейном

                                            """,

        'loc_23_handler': """
*Корпус №23, ул. Дмитрия Донского, 27к1*

Здесь находится:
· Учебно-лабораторный корпус Высшей школы медицины

                                            """,

        'loc_24_handler': """
*Корпус №24, ул. Зоологическая, 2*

Здесь находятся:
· Университетский колледж

                                            """,

        'loc_25_handler': """
*Корпус №25, ул. Космонавта Пацаева, 12*

Здесь находятся:
· ОНК Институт высоких технологий
· Высшая школа киберфизических систем

                                            """,

        'loc_27_handler': """
*Корпус №27, ул. Генерала-лейтенанта Озерова, 57*

Здесь находятся:
· Инженерно-технический институт
· Арена «Кантиана»
                                            """,

        'loc_28_handler': """
*Корпус №28, ул. Горького, 23*

Здесь находятся:
· Институт экономики и менеджмента
                                            """,
        
        'loc_29_handler': """
*Корпус №29, ул. Пролетарская, 131*

Здесь находятся:
· НИИ прикладной информатики и математической геофизики
                                            """,
        
        'loc_32_handler': """
*Корпус №32, ул. Гайдара, 6*

Здесь находятся:
· Научно-технологический парк «Фабрика»
                                            """,

        'loc_35_handler': """
*Корпус №35, ул. Александра Невского, 14В*

Здесь находятся:
· Плавательный бассейн
                                            """,
    },

    'university_info_handlers': {
        'schedule_text': '''
*Расписание занятий*:
                                            ''',
        'scholarship_text': '''
*Информация о стипендиях и материальной помощи*:
                                            ''',
        'office_contacts_text': '''
*Контакты*:

_Адрес_: 236041, Калининград, ул. Александра Невского, 14
_Контактный телефон_: +7 (4012) 59-55-95
_Приемная комиссия_: ул. Александра Невского, 14

8 (800) 600-52-39 звонок бесплатный
+7 (4012) 59-55-96

_Канцелярия_: +7 (4012) 59-55-97

_E-mail_: post@kantiana.ru

*Время работы административных служб*

Понедельник: 9:00 — 18:00    
_перерыв_: 13:00—13:45

Вторник: 9:00 — 18:00        
_перерыв_: 13:00—13:45

Среда: неприемный день (работа с документами)

Четверг: 9:00 — 18:00        
_перерыв_: 13:00—13:45

Пятница: 9:00 — 16:45        
_перерыв_: 13:00—13:45

Суббота и воскресенье: выходные дни
''',
        'visa_center_text': '''
*Визово-миграционный центр*:

*Контакты*

_Адрес_: 236041, Россия, Калининград, ул. А. Невского 14, корпус 2, каб. 119
_Часы_ _работы_: Понедельник — четверг с 9:00 до 18:00, пятница до с 9:00 до 16:45
_Телефон_: +7 (4012) 31-33-99
_Email_: international-study@kantiana.ru
'''
    },

    'sber_handlers': {
        'useful_links_text': """
🔗 Полезные ресурсы Сбера и партнёров:

• [Платформа Нетология](https://netology.ru/navigation) — онлайн‑курсы и профессии
• [Тренируй спокойствие](http://interview.sberstudent.ru/?utm_source=sber&utm_medium=internal&utm_campaign=salaryprojectmanagement) — тренажёр для собеседований
• [Школа 21](https://sbergraduate.ru/careerofthefuture/) — бесплатное IT‑образование
• [СберСова](https://sbersova.ru/academy/courses/kibergramotnost?utm_source=event&utm_medium=free&utm_campaign=speaker) — образовательная платформа
• [Кибрарий](https://sber.ru/kibrary) — цифровая библиотека
• [Цифровой марафон](https://it-marathon.21-school.ru/?utm_source=ter_bank&utm_medium=referral&utm_campaign) — соревнования и челленджи
• [Стартап от Сбера](https://sberstudent.sberclass.ru/) — поддержка стартапов
• [Стажировки](https://sbergraduate.ru/practice/) — вакансии и стажировки
""",

        'sber_card_text': """
💳 *Карта Сбера*

✨ *Бесплатное обслуживание навсегда*
💸 *До 5% кэшбэка* за любимые покупки
📈 *Проценты на накопительный счёт* до *16%* годовых
🎨 *Уникальные стикеры от Сбера* для каждой транзакции — коллекционируй и делись с друзьями!
🎯 *Специальные предложения для молодежи* — скидки на развлечения, образование и многое другое

Нажми *кнопку ниже* для подробностей:
""",

        'educational_loan_text': """
🎓 *Образовательный кредит от Сбера*

🎯 *Всего 3% годовых*
📚 *Платите только проценты во время обучения* 
👨‍🎓 *Оформление с 14 лет*
⏳ *Рассрочка до 15 лет после выпуска*

Нажми *кнопку ниже* для подробностей:
"""
    }
}
},

'en': {
    'greetings': """
Hello, IKBFU student! 🌍✨

We're glad to see you in the official chat bot for international students of the Immanuel Kant Baltic Federal University! 🎓🇷🇺

I'm your personal assistant for any questions in Kaliningrad. With me you can:

🧠 Practice Russian with a smart AI tutor
🏛️ Find useful information about university life:
📍 Locate campuses and dormitories
🏠 Solve accommodation issues
🤝 Get support and help
🏦 Learn about useful SBER services 😊
🚀 Adapt to the city and find like-minded people

Where shall we start? 👇 Choose a menu item!""",
    'errors': {
        'start_error': 'An error occurred while starting the bot. Please try again later.',
        'info_error': 'Error loading information',
        'back_error': 'Error when returning to the main menu',
        'audio_error': 'Error during processing',
        'photo_error': 'An error occurred while uploading the photo',
        'gigachat_error': 'Error initializing GigaChat:',
    },

        'keyboards': {
            'main_keyboard': {
                'info': 'Information',
                'location': 'Buildings',
                'dormitory': 'Dormitories',
                'hospital': 'Medical Center',
                'critical': 'SOS',
                'language_check': 'Trainer',
                'sber':'SBER',
                'back': 'Back'
            },
            'critical_keyboard': {
                'police': 'Emergency',
                'hotline': 'FMS hotline',
                'government': 'Local authorities',
                'consulate': 'Consulate',
                'back': 'Back',
                'appeal':'Online request'
            },
            'dormitory_keyboard': {
                'check-in': 'Dormitory check-in',
                'payment': 'Payment',
                'address': 'Dormitory addresses',
                'rules': 'Dormitory rules',
                'laundry': 'Laundry',
                'details': 'Learn more',
                'no_certificate': 'No vaccination certificate or fluorography',
                'back': 'Back'
            },

            'dormitory_locations_keyboard': {
                'dormitory_1': 'Sommera',
                'dormitory_2': 'Chernyshevskogo',
                'dormitory_3': 'A. Nevskogo',
                'dormitory_4': 'A. Nevskogo',
                'dormitory_5': 'Tchaikovskogo',
                'dormitory_6': 'Azovskaya',
                'dormitory_7': 'Yelovaya',
                'dormitory_8': 'Yelovaya',
                'dormitory_9': 'Yubileynaya',
            },

            'payment_keyboard':{
                'sber_payment': 'Pay at Sber',
                'back': 'Back'
            },

            'language_check_keyboard': {
                'grammar_keyboard': {
                    'to_russian': 'Translate into Russian',
                    'from_russian': 'Translate from Russian',
                    'back': 'Back'
                },
                'speaking_keyboard': {
                    'back': 'Back'
                },
                'language_check_keyboard': {
                    'audio': 'Listening',
                    'grammar': 'Grammar',
                    'speaking': 'Speaking',
                    'back': 'Back'
                }
            },
            'location_keyboard': {
                'loc_1': '🏛️ Admin building',
                'loc_2': '🧮 Physics and Mathematics',
                'loc_3': '🧬 Live systems',
                'loc_4': '🏫 IGN',
                'loc_5': '👨‍🏫 Education',
                'loc_6': '🛌 Puck',
                'loc_7': '⚖️ Juridical',
                'loc_8': '📚 Medlibrary',
                'loc_9': '🏐 FOC',
                'loc_10': '👩‍🏫 Candle',
                'loc_11': '✨ Resource',
                'loc_12': '🩺 Medical Institute',
                'loc_13': '👩‍⚕️ Clinic',
                'loc_14': '🚗 Transport',
                'loc_19': '🏡 Base №19',
                'loc_20': '🏡 Base №20',
                'loc_21': '🌳 Botanic',
                'loc_22': '🏊‍♂️ Swimming Pool',
                'loc_23': '🧪 Lab',
                'loc_24': '🎓 College',
                'loc_25': '👨‍🔬 Ciberphysics',
                'loc_27': '⚙️ ITI',
                'loc_28': '💸 Economics',
                'loc_29': '🥽 Geophysycs',
                'loc_32': '🔬 Fabrica',
                'loc_35': '🏊‍♂️ Swimming pool',
                'back': 'Back'
            },
            'university_info_keyboard': {
                'schedule': 'Schedule',
                'scholarship': 'Scholarship',
                'office_contacts': 'Educational Office contacts',
                'visa_center': 'Visa and Migration Center',
                'back': 'Back'
            },
            'language_selection_keyboard': {
                'back': 'Back'
            },
            'sber_keyboard': {
                'educational_loan': 'Educational loan',
                'sber_card': 'Scholarship card',
                'useful_links': 'Useful links',
                'details': 'Details',
                'back': 'Back'
            },
'hospital_keyboard': {
    'insurance': 'Health Insurance',
    'attachment': 'Clinic Attachment'
}
        },

    'handlers': {
        'critical_handlers': {
            'critical_police_handler': '''
🚨 *Emergency Contacts*

*Unified Emergency Response Number*
(fire department, emergency services, police, ambulance, gas service)
📞 *112*

👨‍🚒 *Firefighters and Rescuers*
📞 *01* (from landline) | *101* (from mobile)

👮 *Police*
📞 *02* (from landline) | *102* (from mobile)

🏥 *Ambulance*
📞 *03* (from landline) | *103* (from mobile)

💡 Save these numbers for quick access!
                                                    ''',

            'critical_hotline_handler': '''
🚪 *Visa and Migration Support Division*

📞 *Phone*:
+7 (4012) 595-595 (доб. 7454) — migration registration and visas
+7 (4012) 595-595 (доб. 7452) — visa invitations

🏢 *Address*:
Russia, Kaliningrad, 14 Alexander Nevsky St., Bldg. 2, Office 114 3

🕒 *Office Hours*:
Mon 14:00–17:00
Tue 10:00–13:00
Thu 14:00–17:00
Fri 10:00–13:00

Lunch break: 13:00–14:00 
                                                    ''',

            'critical_government_handler': '''
🏛️ *Committee on Interethnic Relations and Migration Policy in St. Petersburg*
You can book an online or offline meeting!

1. 📅 *Offline format* (in-person reception)
How to book?
Call: *576-28-08* 1.
Reception hours:
• Monday–Thursday: 9:00 AM – 6:00 PM
• Friday: 9:00 AM – 5:00 PM
• Lunch break: 1:00 PM – 2:00 PM (calls not accepted)
• Saturday and Sunday: closed.

*What to bring?*

Passport or ID.

*How does the reception work?*
You will be received by the Committee Chair, deputies, or authorized personnel 4.

Your query is recorded in a reception card.

Simple questions → verbal response (recorded in the card).

Complex questions → written response later.

Issue outside the Committee’s competence → you will be redirected to the relevant authority.
⚠️ If your issue has already been addressed, a repeat reception may be denied.

2. 🌐 *Online reception*
Book via the Committee’s official resources.
Booking link: ''',

            'critical_consulate_handler': '''
*Representative Office of the Ministry of Foreign Affairs of Russia in Kaliningrad* 🏛️

*Address*: 🏠
236022, Russia, Kaliningrad, 17 Kirova Street

*Phones*: 📞
Reception: + 7 (401) 221-37-12
Fax: + 7 (401) 221-06-26
Consular Section: + 7 (401) 221-16-68
Passport Office: + 7 (401) 295-82-02
Invitation Processing Department: + 7 (4012) 21-59-28

*Reception of citizens on consular and legal matters* ⚖️
Mon-Thu: from *9:00* to *17:00* (break from *12:00* to *14:00*)
Fri: from *9:00* to *16:00* (break from *12:00* to *14:00*)
Sat-Sun: 🚫 Day off
                                            ''',
        },

        'dormitory_handlers': {
            'dormitory_text': """
            To apply for a place in the dormitory 🏠, it is important to prepare the necessary documents 📋  in advance and familiarize yourself with the application procedure. Check out the detailed instructions below 👇:
""",

            'payment_text': """
You can pay for the dormitory in two ways. 

1. In person. 
Go to room 222 in the administrative building, 2nd floor. 
Here you will receive a receipt for payment at the cash desk on the same floor. 
You can pay at the cash desk in cash in rubles or by bank card. 

2. Remotely on the website. First-year students pay the full amount for the first semester upon check-in. 
Subsequently, the autumn semester is to be paid by September 15, and the spring semester by February 15.
                                            """,

            'rules_text': """
Click here 🏘️ "Rules of Residence" to learn about important rules and recommendations that will make your stay comfortable and safe. Here you will find all the necessary information about operating hours, resident responsibilities, code of conduct, and much more.✨
""",

            'laundry_text': """
🏢 *Location*:
Laundry rooms are located in every dormitory building. The exact location and operating hours can be provided by the warden or supervisor.

🧼 *Usage Rules*:
• Bring your own detergent
• Use special mesh bags for underwear
• *Do not* wash shoes (this breaks the machines)
• Read the instructions on-site before use
• Dry clothes in the specially equipped room

⏰ *Important!*
Return the key to the supervisor *exactly at the agreed time* — other students also want to wash their clothes! 🙏

✨ Everything is organized for your convenience — please use it carefully!""",

            'no_certificate_text': """
IF THERE IS NO VACCINATION OR FLUOROGRAPHY CERTIFICATE

1. *If you do not have a recent fluorography*

You can get it done in several places, for example:

- At the KDC BFU for 320 rubles with a student card (it must be available). Location KDC: [https://goo.gl/maps/P4djCkwJ3ZQHThgGA]
- At Medexpert (Kosmicheskaya St. or Moscow Ave.), until 5:00 PM, for 450 rubles without a photo. Location: [https://goo.gl/maps/rRiC1Nh35BNPw2w3A]
- Novomed (Gagarina 2V) until 5:00 PM, 350 rubles. Location: [https://goo.gl/maps/kgEkj4yLnWBNbFUm6]

2. *If you do not have vaccination certificates*

Contact any Medexpert branch. You will need to have a blood test, called “Titer to immunity for measles and diphtheria.” 
The test can be taken every day, Monday to Friday from 7:30 AM to 7 PM, weekends from 7:30 AM to 5 PM.
The test is done on an empty stomach.
The result is provided within 4 working days (it can be obtained in the personal account).
                                                """,
        },

        'dormitory_location_handlers': 'Dormitory №',

        'hospital_handlers': {
            'hospital_text': '''
*University Clinic of BFU named after I. Kant*

*Address*: 236041, Russia, Kaliningrad, ul. 9 April, 60
*Contacts*: +7 (4012) 31-33-39 kdc@kantiana.ru'''
        },

        'language_check_handlers': {
            'grammar_handlers': {
                'language_grammar_handler': '''
                                            *Choose an option for translation*:
                                            ''',
                'translate_to_russian_handler': '''
                                            Translate this text into Russian:
                                            ''',
                'translate_from_russian_handler': '''
                                            Translate this text from Russian into your native language:
                                            ''',
            },

            'listening_handlers': {
                'send_voice': 'Listen to the text and try to write it in Russian.',
            },

            'speaking_handlers': {
                'topics': [
                    'Tell us a little about your family.',
                    'Do you have a pet?',
                    'What dishes do you like?',
                    'Describe your room.',
                    'What is your favourite mode of transport?',
                    'Where do you like to spend your free time?',
                    'How do you spend your Sunday?',
                    'What is your most vivid childhood memory?',
                    'Where would you like to travel?',
                    'What habits help you stay productive?',
                    'How was your yesterday?',
                    'What do you do for a job and what do you do at work?',
                    'What is your family dreaming about?',
                    'What interesting things happened to you last week?',
                    'What is your best friend interested in?',
                    'Share your impressions of the last movie you saw.',
                    'Why did you decide to study in Kaliningrad?'
                ],
                'speaking_send': 'I\'m waiting for your story on the topic:',
                'handle_voice_message': 'Analysis result:',
            }
        },

        'location_handlers': {
            'addresses_handler': 'Choose a building',
            'loc_1_handler': """
*Administrative building, A. Nevsky St., 14*

Here you can find:
· Document management (office 115)
· Accounting department (office 212)
· Archive (office 221)
· Income and tax accounting group (office 222)
· Cash desk (second floor)
· Aquarium Hall
· Maximum Hall
· Cafeteria (first floor)
                                            """,

            'loc_2_handler': """
*Building No. 2, Institute of Physics, Mathematics and Information Technologies, A. Nevsky St., 14*

Here are located:
· Department for Foreign Students (room 119)
· Visa and Migration Support Sector (room 114)
· Admissions Office (rooms 116 and 117)
· Library, room 202 ("Reading Room")
· IT Infrastructure Service (room 121)
                                            """,

            'loc_3_handler': """
*Building No. 3, Universitetskaya St., 2*

Here you can find:
· Institute of Living Systems
· Main University Library: Scientific subscription (room 126), reading room (room 115)
                                            """,

            'loc_4_handler': """
*Building No. 4, Chernyshevsky Street, 56 (‘The Building with the Clock’)*

Here are located:
· Institute of Humanities
· Center for the Russian Language (room 01)
· Museum of Soviet Childhood
                                            """,

            'loc_5_handler': """
*Building No. 5, 56a Chernyshevskogo Street*  

Here is located:  
· Institute of Education  
                                            """,

            'loc_6_handler': """
*Building No. 6, A. Nevsky St., 14b ('Shaiba')*

Here are located:
· Complex of student dormitories (room 101)
· Office of extracurricular activities
                                            """,

            'loc_7_handler': """
*Building No. 7, Frunze St., 6* 

Here you can find: 
· Educational Television Studio 
· Law Institute 
                                            """,

            'loc_8_handler': """
*Building No. 8, 9 April Street, 5*

Here is located:
· Medical Library
                                            """,

            'loc_9_handler': """
*Building No. 9, A. Nevsky Street, 14 ('FOK')* 

Here is located: 
· Physical Culture and Health Complex 
                                            """,

            'loc_10_handler': """
*Building No. 10, A. Nevsky St. 14 (“Candle”)*

Here are located:
· Center for Socio-Economic Support of Students (room 14)
· Career Center
                                            """,

            'loc_11_handler': """
*Building No. 11, 3 Botkina Street*

Here is located:
· The Regional Resource Center for Simulation Training and Accreditation in Medicine

                                            """,

            'loc_12_handler': """
*Building No. 12, Botkina Street, 4-6* 

Here is located: 
· Medical Institute 
                                            """,

            'loc_13_handler': """
*Building No. 13, 4-6 Botkina Street*

Here is located:
· University Clinic

                                            """,

            'loc_14_handler': """
*Building No. 14, 14 Aleksandra Nevskogo Street, Building No. 4*

Here are located:
· Transport Services Group
· Property Management Department
· Security Department
                                            """,
        
            'loc_19_handler': """
*Building No. 19, Pionersky, village Rybnoye, 23*

Here are located:
· The base of educational practices

                                            """,

            'loc_20_handler': """
*Building No. 20, Svetlogorsk, Kaliningrad Avenue, 102*

Here is located:
· Training practice base

                                            """,

            'loc_21_handler': """
*Building 21, 12 Lesnaya Street*

Here is located:
· Botanical Garden

                                            """,

            'loc_22_handler': """
*Building No. 22, A. Nevsky St., 14* 

Here is located: 
· Educational and Sports Complex with a swimming pool 
                                            """,

            'loc_23_handler': """
*Building No. 23, 27k1 Dmitriya Donskogo Street*

 Here is located:
· Educational and laboratory building of the Higher School of Medicine

                                            """,

            'loc_24_handler': """
*Building No. 24, Zoologicheskaya St., 2*  

Here is located:  
· University College  
                                            """,

            'loc_25_handler': """
*Building No. 25, 12 Kosmonavta Patsaeva Street*

Here are located:
· ONK Institute of High Technologies
· Higher School of Cyberphysical Systems

                                            """,

            'loc_27_handler': """
*Building No. 27, Gen. Lt. Ozerov St., 57* 

Here are located:  
· Engineering and Technical Institute  
· «Kantiana» Arena  
                                            """,

            'loc_28_handler': """
*Building No. 28, Gorky Street, 23*

Here is located:
· Institute of Economics and Management
                                            """,

            'loc_29_handler': """
*Building No. 29, 131 Proletarskaya Street*

Here are located:
· Research Institute of Applied Informatics and Mathematical Geophysics
                                            """,
        
            'loc_32_handler': """
*Building No. 32, 6 Gaidara Street*

Here are located:
· Factory Science and Technology Park
                                            """,

            'loc_35_handler': """
*Building No. 35, 14B Aleksandra Nevskogo Street*

Here is located:
· Swimming pool
                                            """,
        },

        'university_info_handlers': {
            'schedule_text': '''
*Class schedule*:
                                            ''',
            'scholarship_text': '''
*Information about scholarships and financial aid*:
                                            ''',
            'office_contacts_text': '''
*Contacts*:

_Address_: 236041, Kaliningrad, Alexander Nevsky St., 14
_Contact phone_: +7 (4012) 59-55-95
_Admissions Committee_: Alexander Nevsky St.

148 (800) 600-52-39 call is free
+7 (4012) 59-55-96

_Office_: +7 (4012) 59-55-97
_E-mail_: post@kantiana.ru

*Working hours of administrative services*

Monday: 9:00 — 18:00    _break_: 13:00 — 13:45 
Tuesday: 9:00 — 18:00   _break_: 13:00 — 13:45 
Wednesday: no reception day (document processing)
Thursday: 9:00 — 18:00  _break_: 13:00 — 13:45 
Friday: 9:00 — 16:45    _break_: 13:00 — 13:45 
Saturday and Sunday: days off
''',
            'visa_center_text': '''
*Visa and Migration Center*:

*Contacts*  

_Address_: 236041, Russia, Kaliningrad, A. Nevsky St. 14, building 2, office 119  

_Working_ _Hours_: 

Monday — Thursday from 9:00 to 18:00
Friday from 9:00 to 16:45  

_Phone_: +7 (4012) 31-33-99  
_Email_: international-study@kantiana.ru
'''
        },

        'sber_handlers': {
            'useful_links_text': """
🔗 Useful resources from Sber and partners:

• [Netology Platform](https://netology.ru/navigation) — online courses and professions
• [Train Calmness](http://interview.sberstudent.ru/?utm_source=sber&utm_medium=internal&utm_campaign=salaryprojectmanagement) — interview simulator
• [School 21](https://sbergraduate.ru/careerofthefuture/) — free IT education
• [SberSova](https://sbersova.ru/academy/courses/kibergramotnost?utm_source=event&utm_medium=free&utm_campaign=speaker) — educational platform
• [Kibrary](https://sber.ru/kibrary) — digital library
• [Digital Marathon](https://it-marathon.21-school.ru/?utm_source=ter_bank&utm_medium=referral&utm_campaign) — competitions and challenges
• [Startup from Sber](https://sberstudent.sberclass.ru/) — startup support
• [Internships](https://sbergraduate.ru/practice/) — job vacancies and internships
""",

            'sber_card_text': """
💳 *Sber Card*

✨ *Free maintenance forever*
💸 *Up to 5% cashback* on favorite purchases
📈 *Interest on savings account* up to *16%* per annum
🎨 *Unique stickers from Sber* for each transaction - collect and share with friends!
🎯 *Special offers for youth* - discounts on entertainment, education, and much more

Click the *button below* for details:
""",

            'educational_loan_text': """
🎓 *Educational loan from Sber*    

🎯 *Only 3% annual interest*  
📚 *Pay only interest during your studies*  
👨‍🎓 *Available for ages 14 and up*  
⏳ *Repayment period up to 15 years after graduation*    

Click the *button below* for details:
"""
            }
        }
    },

    'fr': {
        'greetings': '''
Salut, étudiant de l'Université fédérale de la Baltique ! 🌍✨

Nous sommes heureux de te voir dans le chatbot officiel pour les 
étudiants étrangers de l'Université fédérale de la Baltique nommée d'I. Kant ! 🎓🇷🇺

Je suis ton assistant personnel pour toute question à Kaliningrad. 
Avec moi, tu pourras :

🧠 Améliorer ton russe grâce à un entraîneur intelligent IA
🏛️ Découvrir des informations utiles sur l'université et sa vie :
📍 Trouver des bâtiments et des résidences universitaires
🏠 Résoudre des questions de logement
🤝 Obtenir du soutien et de l'aide
🏦 Découvrir des services utiles de SBER 😊
🚀 S'adapter dans la ville et trouver des personnes partageant les mêmes idées

Par quoi allons-nous commencer ? 👇 Choisis un élément du menu !
        ''',
        'errors': {
            'start_error': 'Une erreur est survenue lors du lancement du bot. Veuillez réessayer plus tard.',
            'info_error': 'Erreur lors du chargement des informations',
            'back_error': 'Erreur lors du retour au menu principal',
            'audio_error': 'Erreur lors du traitement',
            'photo_error': 'Une erreur est survenue lors du chargement de la photo.',
            'gigachat_error': 'Erreur d\'initialisation de GigaChat :',
        },

        'keyboards': {
            'main_keyboard': {
                'info': 'Information',
                'location': 'Bâtiments',
                'dormitory': 'Résidences',
                'hospital': 'Santé',
                'critical': 'SOS',
                'language_check': 'Coach',
                'sber':'SBER',
                'back': 'Retour'
            },
            'critical_keyboard': {
                'police': 'Urgence',
                'hotline': 'Ligne directe de la FMS (USCIS)',
                'government': 'Autorités locales',
                'consulate': 'Consulat',
                'back': 'Retour',
                'appeal':'Demande en ligne'
            },
            'dormitory_keyboard': {
                'check-in': 'Installation dans le dortoir',
                'payment': 'Paiement',
                'address': 'Adresses des résidences estudiantines',
                'rules': 'Règles de vie',
                'laundry': 'Buanderie',
                'details': 'En savoir plus',
                'no_certificate': 'Pas de certificat de vaccination ou de radiographie des poumons.',
                'sber_payment': 'Payer dans Sber',
                'back': 'Retour'
            },

            'dormitory_locations_keyboard': {
                'dormitory_1': 'Sommera',
                'dormitory_2': 'Tchernyshevskogo',
                'dormitory_3': 'A. Nevskogo',
                'dormitory_4': 'A. Nevskogo',
                'dormitory_5': 'Tchaikovskogo',
                'dormitory_6': 'Azovskaya',
                'dormitory_7': 'Yelovaya',
                'dormitory_8': 'Yelovaya',
                'dormitory_9': 'Yubileynaya',
            },

            'language_check_keyboard': {
                'grammar_keyboard': {
                    'to_russian': 'Traduire en russe',
                    'from_russian': 'Traduire du russe',
                    'back': 'Retour'
                },
                'speaking_keyboard': {
                    'back': 'Retour'
                },
                'language_check_keyboard': {
                    'audio': 'Écoute',
                    'grammar': 'Grammaire',
                    'speaking': 'Parler',
                    'back': 'Retour'
                }
            },
            'location_keyboard': {
                'loc_1': '🏛️ Administration',
                'loc_2': '🧮 Physique-Mathématiques',
                'loc_3': '🧬 Systèmes vivants',
                'loc_4': '🏫 IGN',
                'loc_5': '👨‍🏫 Éducation',
                'loc_6': '🛌 Disque',
                'loc_7': '⚖️ Juridique',
                'loc_8': '📚 Bibliothèque médicale',
                'loc_9': '🏐 FOC',
                'loc_10': '👩‍🏫 Bougie',
                'loc_11': '✨ Ressources',
                'loc_12': '🩺 Institut médical',
                'loc_13': '👩‍⚕️ Clinique',
                'loc_14': '🚗 Transport',
                'loc_19': '🏡 Base №19',
                'loc_20': '🏡 Base №20',
                'loc_21': '🌳 Botanique',
                'loc_22': '🏊‍♂️ Piscine',
                'loc_23': '🧪 Lab',
                'loc_24': '🎓 Collège',
                'loc_25': '👨‍🔬 Cyberfiz',
                'loc_27': '⚙️ ITI',
                'loc_28': '💸 Économie',
                'loc_29': '🥽 Géophysique',
                'loc_32': '🔬 Fabrique',
                'loc_35': '🏊‍♂️ Piscine',
                'back': 'Retour'
            },
            'university_info_keyboard': {
                'schedule': 'Horaires',
                'scholarship': 'Bourses',
                'office_contacts': 'Contacts du bureau académique',
                'visa_center': 'Centre de visa et de migration',
                'back': 'Retour'
            },
            'language_selection_keyboard': {
                'back': 'Retour'
            },
            'sber_keyboard': {
                'educational_loan': 'Crédit éducatif',
                'sber_card': 'Carte pour la bourse',
                'useful_links': 'Liens utiles',
                'details': 'Plus de détails',
                'back': 'Retour'
            },
            'hospital_keyboard': {
                'insurance': 'Assurance médicale',
                'attachment': 'Affiliation à la polyclinique'
            }
        },

        'handlers': {
            'critical_handlers': {
                'critical_police_handler': '''
🚨 *Contacts d'urgence*

*Numéro unique des services d'urgence*(pompiers, ministère des situations d'urgence, police, ambulance, service gaz)
📞 *112*

👨‍🚒 *Pompiers et sauveteurs*
📞 *01* (depuis un téléphone fixe) | *101* (depuis un mobile)

👮 *Police*
📞 *02* (depuis un téléphone fixe) | *102* (depuis un mobile)

🏥 *Ambulance*
📞 *03* (depuis un téléphone fixe) | *103* (depuis un mobile)

💡 Enregistrez ces numéros pour un accès rapide!
                                                    ''',

                'critical_hotline_handler': '''
🚪 *Secteur de soutien aux visas et à la migration*

📞 *Téléphone*:
+7 (4012) 595-595 (poste 7454) — enregistrement migratoire et visas
+7 (4012) 595-595 (poste 7452) — invitations de visa

🏢 *Adresse* :
Russie, ville de Kaliningrad, rue A. Nevskogo, 14, bâtiment 2, bureau 114

🕒 *Heures d'ouverture* :
Lun 14:00–17:00
Mar 10:00–13:00
Jeu 14:00–17:00
Ven 10:00–13:00

Pause déjeuner 13:00–14:00
                                                    ''',

                'critical_government_handler': '''
🏛️ *Comité des relations interethniques et de la politique migratoire à Saint-Pétersbourg*
Vous pouvez prendre rendez-vous en ligne ou en présentiel !

1. 📅 *Format présentiel* (réception en personne)
Comment prendre rendez-vous ?
Appelez le *576-28-08* 1.
Heures de réception :
• Lundi-jeudi : *9h00 – 18h00*
• Vendredi : *9h00 – 17h00*
• Pause déjeuner : *13h00 – 14h00* (appels non acceptés)
• Samedi et dimanche : fermé.

*Que apporter ?*

Passeport ou pièce d’identité.

*Comment se déroule la réception ?*
Vous serez reçu par le président du Comité, ses adjoints ou des personnel autorisés 4.

Votre demande est inscrite dans une fiche de réception.

Questions simples → réponse verbale (consignée dans la fiche).

Questions complexes → réponse écrite ultérieure.

Question hors compétence du Comité → vous serez orienté vers l’autorité compétente.
⚠️ Si votre demande a déjà été traitée, une nouvelle réception peut être refusée.

2. 🌐 *Réception en ligne*
Réservation via les ressources officielles du Comité.
Lien de réservation: ''',

                'critical_consulate_handler': '''
*Représentation du ministère des Affaires étrangères de la Russie à Kaliningrad* 🏛️

*Adresse*: 🏠
236022, Russie, Kaliningrad, rue Kirova, 17

*Téléphones*: 📞
Standard: + 7 (401) 221-37-12
Fax: + 7 (401) 221-06-26
Service consulaire: + 7 (401) 221-16-68
Service des passeports: + 7 (401) 295-82-02
Service de délivrance des invitations: + 7 (4012) 21-59-28

*Accueil du public pour les questions consulaires et juridiques* ⚖️

Lun-Jeu: de *9h00* à *17h00* (pause de *12h00* à *14h00*)
Ven: de *9h00* à *16h00* (pause de *12h00* à *14h00*)
Sam-Dim: 🚫 Fermé
                                            ''',
            },

            'dormitory_handlers': {
                'dormitory_text': """
Pour réserver un logement en résidence universitaire 🏠, il est important de préparer à l'avance les documents nécessaires 📋 et de se familiariser avec la procédure de dépôt de demande 📝. Veuillez consulter le guide détaillé ci-dessous 👇 :
                                            """,

                'payment_text': """
Il existe deux façons de payer le logement étudiant.

1. En personne. 

Au bureau n° 222 du bâtiment administratif, 2ème étage. Vous y recevrez un reçu pour le paiement à la caisse au même étage. 
Vous pouvez payer à la caisse en espèces en roubles ou par carte bancaire.

2. À distance sur le site.

Les étudiants de première année paient la totalité du premier semestre lors de l'emménagement. Ensuite, le semestre d'automne est payé avant le 15 septembre, 
et le semestre de printemps avant le 15 février.                                            
""",

                'rules_text': """Clique ici 🏘️ « Règles de résidence » pour prendre connaissance des règles et recommandations importantes qui rendront ton séjour confortable et sûr. Ici tu trouveras toutes les informations nécessaires sur les heures d'ouverture, les responsabilités des résidents, les règles de conduite et bien plus encore.✨""",

                'laundry_text': """
🏢 *Emplacement* :
Les laveries se trouvent dans chaque résidence étudiante. Le responsable ou le concierge vous renseignera 
sur l'emplacement exact et les horaires d'ouverture.

🧼 *Règles d'utilisation* :
• Apporte ta propre lessive
• Utilise des sacs spéciaux pour le linge
• *Interdit* de laver des chaussures (cela casse les machines)
• Consulte les instructions sur place avant d'utiliser
• Fais sécher le linge dans une salle spécialement équipée

⏰ *Important !*
Rends la clé au concierge *exactement à l'heure convenue* — d'autres étudiants veulent aussi laver leurs affaires ! 🙏

✨ Tout est organisé pour ton confort — utilise avec soin !
""",

                'no_certificate_text': """
S'IL N'Y A PAS DE CERTIFICAT DE VACCINATION OU DE RADIOGRAPHIE

1. *Si vous n'avez pas de radiographie récente*

Vous pouvez en faire une à plusieurs endroits, par exemple: 

- Au KDC de l'Université fédérale de l'Oural pour 320 roubles avec la carte d'étudiant (elle doit être en possession). Emplacement du KDC : [https://goo.gl/maps/P4djCkwJ3ZQHThgGA]
- chez Medexpert (rue Kosmicheskaya ou avenue de Moscou), jusqu'à 17h00, pour 450 roubles sans photo. Emplacement : [https://goo.gl/maps/rRiC1Nh35BNPw2w3A]
- Novomed (Gagarin 2B) jusqu'à 17h00, 350 roubles. Emplacement : [https://goo.gl/maps/kgEkj4yLnWBNbFUm6]

2. *Si vous n'avez pas de certificats de vaccination*

Adressez-vous à n'importe quelle agence de Medexpert. Vous devez y faire un test sanguin appelé "Niveau d'immunité contre la rougeole et la diphtérie". Le test peut être effectué tous les jours, du lundi au vendredi de 7h30 à 19h, le week-end de 7h30 à 17h.

Le test doit être effectué à jeun.

Le résultat est délivré dans un délai de 4 jours ouvrables (le résultat peut être obtenu dans le cabinet personnel).
                                                """,
            },

            'dormitory_location_handlers': 'Résidence universitaire №',

            'hospital_handlers': {
                'hospital_text': '''
*Clinique universitaire de l'Université d'État de Kaliningrad, nommée d'après I. Kant*

*Adresse*: 236041, Russie, Kaliningrad, rue du 9 avril, 60
*Contacts*: +7 (4012) 31-33-39 kdc@kantiana.ru'''
            },

            'language_chack_handlers': {
                'grammar_handlers': {
                    'language_grammar_handler': '''
                                            *Choisissez l'option de traduction*:
                                            ''',
                    'translate_to_russian_handler': '''
                                            Traduisez ce texte en russe:
                                            ''',
                    'translate_from_russian_handler': '''
                                            Traduisez ce texte de la langue russe vers la vôtre:
                                            ''',
                },

                'listening_handlers': {
                    'send_voice': 'Écoutez le texte et essayez de l\'écrire en russe.',
                },

                'speaking_handlers': {
                    'topics': [
                        'Parlez-moi un peu de votre famille.',
                        'Avez-vous un animal de compagnie ?',
                        'Quels plats aimez-vous ?',
                        'Décrivez votre chambre.',
                        'Quel est votre moyen de transport préféré ?',
                        'Où aimez-vous passer votre temps libre ?',
                        'Comment passez-vous votre dimanche ?',
                        'Quel est votre souvenir d\'enfance le plus marquant ?',
                        'Où aimeriez-vous partir en voyage ?',
                        'Quelles habitudes vous aident à rester productif ?',
                        'Comment s\'est passé votre journée d\'hier ?',
                        'Quel est votre emploi et que faites-vous au travail ?',
                        'De quoi rêve votre famille ?',
                        'Quoi d\'intéressant vous est arrivé la semaine dernière ?',
                        'Quels sont les loisirs de votre meilleur ami ?',
                        'Partagez vos impressions du dernier film que vous avez regardé.',
                        'Pourquoi avez-vous décidé d\'étudier à Kaliningrad ?'
                    ],
                    'speaking_send': 'J\'attends ton récit sur le thème :',
                    'handle_voice_message': 'Résultat de l\'analyse :',
                }
            },

            'location_handlers': {
                'addresses_handler': 'Choisissez le boîtier',
                'loc_1_handler': """
*Bâtiment administratif, rue A. Nevski, 14*

Ici se trouvent :
· Département de la gestion des documents (cab. 115)
· Service de comptabilité (cab. 212)
· Archives (cab. 221)
· Groupe des calculs des revenus et de la comptabilité fiscale (cab. 222)
· Caisse (deuxième étage)
· Salle Aquarium
· Salle Maximum
· Cafétéria (premier étage)
                                            """,

                'loc_2_handler': """
*Bâtiment n°2, Institut de physique, de mathématiques et de technologies de l'information (« Fizmat »), rue A. Nevski, 14*

Ici se trouvent :
· Le bureau des relations avec les étudiants étrangers (cab. 119)
· Le secteur de l'assistance à la visa et à la migration (cab. 114)
· Le bureau des admissions (cab. 116 et 117)
· La bibliothèque, salle 202 (« Salle de lecture »)
· Le service de maintenance de l'infrastructure IT (cab. 121)
                                            """,

                'loc_3_handler': """
*Bâtiment n°3, rue Universitaire, 2*

Ici se trouvent :
· Institut des systèmes vivants
· Bibliothèque universitaire principale : abonnement scientifique (cab. 126), salle de lecture (cab. 115)
                                            """,

                'loc_4_handler': """
*Bâtiment n°4, rue Tchernychevski, 56 («Bâtiment avec l'horloge»)*

Ici se trouvent :
· Institut des sciences humaines
· Centre de la langue russe (cab. 01)
· Musée de l'enfance soviétique
                                            """,

                'loc_5_handler': """
*Bâtiment n°5, rue Tchernychevski, 56a*

Ici se trouve :
· Institut de formation
                                            """,

                'loc_6_handler': """
*Bâtiment n°6, rue A. Nevski, 14b («Shaïba»)*

Ici se trouvent :
· Complexe de résidences étudiantes (cab. 101)
· Gestion des activités parascolaires
                                            """,

                'loc_7_handler': """
*Bâtiment n° 7, rue Frunze, 6* 

Ici se trouvent :  
· Studio télévisé éducatif  
· Institut de droit  
                                            """,

                'loc_8_handler': """
*Bâtiment n°8, rue 9 Avril, 5*

Ici se trouve :
· Bibliothèque médicale
                                            """,

                'loc_9_handler': """
*Bâtiment n°9, rue A. Nevsky, 14 («FOC»)*

Ici se trouve :
· Complexe sportif et de bien-être
                                            """,

                'loc_10_handler': """
*Bâtiment n°10, rue A. Nievsky. 14 («Bougie»)*

Ici se trouve :
· Centre de soutien socio-économique aux étudiants (cab. 14)
· Centre de carrière
                                            """,

                'loc_11_handler': """
*Bâtiment №11, rue Botkin, 3*

Ici se trouve:
· Centre régional de ressources pour la formation et l'accréditation en Médecine

                                            """,

                'loc_12_handler': """
*Bâtiment n°12, rue Botkina, 4-6* 

Ici se trouve : 
· Institut médical 
                                            """,

                'loc_13_handler': """
*Bâtiment n ° 13, rue Botkin, 4-6*

Ici se trouve:
· Clinique universitaire

                                            """,

                'loc_14_handler': """
*Bâtiment №14, rue Alexander Nevsky, 14, bâtiment. 4*

Ici se trouve:
· Groupe des transports
· Gestion du complexe immobilier
· Division des régimes
                                            """,
        
                'loc_19_handler': """
*Bâtiment №19, Pionersky, village.*

Ici se trouve:
· Base de pratiques pédagogiques

                                            """,

                'loc_20_handler': """
*Bâtiment №20, Svetlogorsk, Kaliningrad Prospekt, 102*

Ici se trouve:
· Base de pratiques pédagogiques

                                            """,

                'loc_21_handler': """
*Bâtiment №21, rue Lesnaya, 12*

Ici se trouve:
· Jardin des plantes

                                            """,

                'loc_22_handler': """
*Bâtiment n° 22, rue A. Nevski, 14* 

Ici se trouve : 
· Complexe sportif et éducatif avec piscine 
                                            """,

                'loc_23_handler': """
*Bâtiment №23, rue Dmitry Donskoy, 27k1*

Ici se trouve:
· Corps de formation et de laboratoire de l'école Supérieure de Médecine

                                            """,

                'loc_24_handler': """
*Bâtiment n°24, rue Zoologique, 2* 

Voici où se trouve : 
· Collège universitaire 
                                            """,

                'loc_25_handler': """
*Bâtiment n ° 25, rue Du cosmonaute patsaev, 12*

Ici sont:
· Institut ONC de haute technologie
· École supérieure des systèmes cyberphysiques

                                            """,

                'loc_27_handler': """
*Bâtiment n°27, rue du général-lieutenant Ozerov, 57*

Ici se trouvent :
· Institut d'ingénierie et de technologie
· Arène "Kantiana"
                                            """,

                'loc_28_handler': """
*Bâtiment n°28, rue Gorki, 23*

Ici se trouvent :
· Institut d'économie et de gestion
                                            """,

                'loc_29_handler': """
*Bâtiment №29, rue Proletarskaya, 131*

Ici sont:
· Institut de recherche en informatique appliquée et géophysique mathématique
                                            """,
        
                'loc_32_handler': """
*Bâtiment n ° 32, rue Gaydar, 6*

Ici sont:
· Parc scientifique et technologique «Factory»
                                            """,

                'loc_35_handler': """
*Bâtiment №35, rue Alexander Nevsky, 14B*

Ici sont:
· Piscine
                                            """,
            },

            'university_info_handlers': {
                'schedule_text': '''
*Emploi du temps des cours*:
                                            ''',
                'scholarship_text': '''
*Information sur les bourses et l'aide matérielle*:
                                            ''',
                'office_contacts_text': '''
*Contacts*:

_Adresse_: 236041, Kaliningrad, rue Alexandre Nevski, 14
_Téléphone de contact_: +7 (4012) 59-55-95
_Commission des admissions_: rue Alexandre Nevski, 14

8 (800) 600-52-39 appel gratuit
+7 (4012) 59-55-96

_Secrétariat_: +7 (4012) 59-55-97

_E-mail_: post@kantiana.ru

*Heures d'ouverture des services administratifs*

Lundi: 9:00 — 18:00 _pause_: 13:00—13:45
Mardi: 9:00 — 18:00 _pause_: 13:00—13:45
Mercredi: jour sans réception (traitement des documents)
Jeudi: 9:00 — 18:00 _pause_: 13:00—13:45
Vendredi: 9:00 — 16:45 _pause_: 13:00—13:45
Samedi et dimanche: jours de repos
''',
                'visa_center_text': '''
*Centre de visa et de migration* :

*Contacts*

_Adresse_ : 236041, Russie, Kaliningrad, rue A. Nievski 14, bâtiment 2, bureau 119

_Horaires_ _d'ouverture_ : 
Du lundi au jeudi de 9:00 à 18:00, le vendredi de 9:00 à 16:45

_Téléphone_ : +7 (4012) 31-33-99
_Email_ : international-study@kantiana.ru
'''
            },

            'sber_handlers': {
                'useful_links_text': """
🔗 Ressources utiles de Sber et de ses partenaires :
• [Plateforme Netologie](https://netology.ru/navigation) — cours en ligne et professions
• [Entraîne ta tranquillité](http://interview.sberstudent.ru/?utm_source=sber&utm_medium=internal&utm_campaign=salaryprojectmanagement) — simulateur d'entretiens
• [École 21](https://sbergraduate.ru/careerofthefuture/) — éducation IT gratuite
• [SberSova](https://sbersova.ru/academy/courses/kibergramotnost?utm_source=event&utm_medium=free&utm_campaign=speaker) — plateforme éducative
• [Cyberbibliothèque](https://sber.ru/kibrary) — bibliothèque numérique
• [Marathon numérique](https://it-marathon.21-school.ru/?utm_source=ter_bank&utm_medium=referral&utm_campaign) — compétitions et défis
• [Startup de Sber](https://sberstudent.sberclass.ru/) — soutien aux startups
• [Stages](https://sbergraduate.ru/practice/) — offres d'emploi et stages
""",

                'sber_card_text': """
💳 *Carte de Sber*

✨ *Entretien gratuit pour toujours*
💸 *Jusqu'à 5 % de cashback* sur vos achats préférés
📈 *Intérêts sur le compte d'épargne* allant jusqu'à *16 %* par an
🎨 *Autocollants uniques de Sber* pour chaque transaction — collectionnez et partagez avec vos amis !
🎯 *Offres spéciales pour les jeunes* — réductions sur les loisirs, l'éducation et bien plus

Cliquez sur *le bouton ci-dessous* pour plus de détails :
""",

                'educational_loan_text': """
🎓 *Crédit éducatif de Sber* 
🎯 *Seulement 3% par an* 
📚 *Payer uniquement les intérêts pendant les études* 
👨‍🎓 *Ouverture dès 14 ans* 
⏳ *Échelonnement jusqu'à 15 ans après l'obtention du diplôme* 

Clique sur *le bouton ci-dessous* pour plus de détails:
"""
            }
        }
    },

    'es': {
        'greetings': '''
¡Hola, estudiante de la BFU! 🌍✨

¡Nos alegra verte en el chatbot oficial para estudiantes internacionales de la Universidad Federal del Báltico Im. I. Kant! 🎓🇷🇺

Soy tu asistente personal para cualquier pregunta en Kaliningrado. 
Conmigo podrás:

🧠 Mejorar tu ruso con la ayuda de un inteligente entrenador de IA
🏛️ Obtener información útil sobre la universidad y su vida:
📍 Encontrar edificios y residencias
🏠 Resolver cuestiones de alojamiento
🤝 Recibir apoyo y ayuda
🏦 Conocer servicios útiles de SBER 😊
🚀 Adaptarte en la ciudad y encontrar personas afines

¿Con qué empezamos? 👇 ¡Elige un punto del menú!
        ''',
        'errors': {
            'start_error': 'Se produjo un error al iniciar el bot. Por favor, inténtelo más tarde.',
            'info_error': 'Error al cargar la información',
            'back_error': 'Error al regresar al menú principal',
            'audio_error': 'Error al procesar',
            'photo_error': 'Se produjo un error al cargar la foto.',
            'gigachat_error': 'Error de inicialización de GigaChat:',
        },

        'keyboards': {
            'main_keyboard': {
                'info': 'Información',
                'location': 'Cuerpos',
                'dormitory': 'Residencias',
                'hospital': 'Centro médico',
                'critical': 'SOS',
                'language_check': 'Entrenador',
                'sber':'SBER',
                'back': 'Atrás'
            },
            'critical_keyboard': {
                'police': 'Urgencia',
                'hotline': 'Línea Migración (FMS)',
                'government': 'Autoridades locales',
                'consulate': 'Consulado',
                'back': 'Atrás',
                'appeal':'Solicitud en línea'
            },
            'dormitory_keyboard': {
                'check-in': 'Alojamiento en un dormitorio',
                'payment': 'Pago',
                'address': 'Direcciones de los dormitorios',
                'rules': 'Reglas de convivencia',
                'laundry': 'Lavandería',
                'details': 'Leer más',
                'no_certificate': 'No hay un certificado de vacunas o de fluorografía',
                'back': 'Atrás'
            },
            'dormitory_locations_keyboard': {
                'dormitory_1': 'Sommera',
                'dormitory_2': 'Tchernyshevskogo',
                'dormitory_3': 'A. Nevskogo',
                'dormitory_4': 'A. Nevskogo',
                'dormitory_5': 'Tchaikovskogo',
                'dormitory_6': 'Azovskaya',
                'dormitory_7': 'Yelovaya',
                'dormitory_8': 'Yelovaya',
                'dormitory_9': 'Yubileynaya',
            },
            'payment_keyboard': {
                'sber_payment': 'Pagar en Sber',
                'back': 'Atrás'
            },
            'language_check_keyboard': {
                'grammar_keyboard': {
                    'to_russian': 'Traducir al ruso',
                    'from_russian': 'Traducir del ruso',
                    'back': 'Atrás'
                },
                'speaking_keyboard': {
                    'back': 'Atrás'
                },
                'language_check_keyboard': {
                    'audio': 'Audición',
                    'grammar': 'Gramática',
                    'speaking': 'Hablando',
                    'back': 'Atrás'
                }
            },
            'location_keyboard': {
                'loc_1': '🏛️ Cuerpo administrativo',
                'loc_2': '🧮 Físico-matemático',
                'loc_3': '🧬 Sistemas vivos',
                'loc_4': '🏫 IGN',
                'loc_5': '👨‍🏫 Educación',
                'loc_6': '🛌 Disco',
                'loc_7': '⚖️ Jurídico',
                'loc_8': '📚 Medicina Biblioteca',
                'loc_9': '🏐 FOC',
                'loc_10': '👩‍🏫 Vela',
                'loc_11': '✨ Recursos',
                'loc_12': '🩺 Instituto de Medicina',
                'loc_13': '👩‍⚕️ Clínica',
                'loc_14': '🚗 Transporte',
                'loc_19': '🏡 Base №19',
                'loc_20': '🏡 Base №20',
                'loc_21': '🌳 Botánico',
                'loc_22': '🏊‍♂️ Piscina',
                'loc_23': '🧪 Lab',
                'loc_24': '🎓 Colegio',
                'loc_25': '👨‍🔬 Cyberfiz',
                'loc_27': '⚙️ ITI',
                'loc_28': '💸 Economía',
                'loc_29': '🥽 Geofísica',
                'loc_32': '🔬 Fábrica',
                'loc_35': '🏊‍♂️ Piscina',
                'back': 'Atrás'
            },
            'university_info_keyboard': {
                'schedule': 'Horarios',
                'scholarship': 'Becas',
                'office_contacts': 'Contactos de la oficina de estudios',
                'visa_center': 'Centro de visas y migración',
                'back': 'Atrás'
            },
            'language_selection_keyboard': {
                'back': 'Atrás'
            },
            'sber_keyboard': {
                'educational_loan': 'Crédito educativo',
                'sber_card': 'Mapa para la beca',
                'useful_links': 'Enlaces útiles',
                'details': 'Más detalles',
                'back': 'Atrás'
            },
            'hospital_keyboard': {
                'insurance': 'Seguro médico',
                'attachment': 'Afiliación a la policlínica'
            }
        },

        'handlers': {
            'critical_handlers': {
                'critical_police_handler': '''
🚨 *Contacts d'urgence*

*Numéro unique des services d'urgence*(pompiers, ministère des situations d'urgence, police, ambulance, service gaz)
📞 *112*

👨‍🚒 *Pompiers et sauveteurs*
📞 *01* (depuis un téléphone fixe) | *101* (depuis un mobile)

👮 *Police*
📞 *02* (depuis un téléphone fixe) | *102* (depuis un mobile)

🏥 *Ambulance*
📞 *03* (depuis un téléphone fixe) | *103* (depuis un mobile)

💡 Enregistrez ces numéros pour un accès rapide!
                                                   ''',

                'critical_hotline_handler': '''
🚪 *Sector de apoyo visa-migratorio*

📞 *Teléfono*:
+7 (4012) 595-595 (ext. 7454) — registro migratorio y visas
+7 (4012) 595-595 (ext. 7452) — invitaciones de visa

🏢 *Dirección*:
Rusia, ciudad de Kaliningrado, ul. A. Nevski, 14, corp. 2, oficina 114

🕒 *Horarios de atención*:

Lun 14:00–17:00
Mar 10:00–13:00
Jue 14:00–17:00
Vie 10:00–13:00

Almuerzo 13:00–14:00
                                                    ''',

                'critical_government_handler': '''
🏛️ *Comité de Relaciones Interétnicas y Implementación de Políticas Migratorias en San Petersburgo*
¡Puedes agendar una cita en línea o presencial!

1. 📅 *Formato presencial* (recepción personal)
¿Cómo agendar?
Llama al *576-28-08* 1.
Horario de recepción:
• Lunes–jueves: *9:00 – 18:00*
• Viernes: *9:00 – 17:00*
• Pausa para comer: *13:00 – 14:00* (no se atienden llamadas)
• Sábado y domingo: cerrado.

*¿Qué llevar?*

Pasaporte o documento de identidad.

*¿Cómo se desarrolla la recepción?*
Serás atendido por el presidente del Comité, su adjunto o personal autorizado 4.

Tu solicitud se registra en una ficha de recepción.

Preguntas simples → respuesta verbal (registrada en la ficha).

Preguntas complejas → respuesta escrita posterior.

Si el tema no es competencia del Comité → se te derivará a la instancia correspondiente.
⚠️ Si tu consulta ya fue respondida, podrían denegar una nueva recepción.

2. 🌐 *Recepción en línea*
Agenda a través de los recursos oficiales del Comité.
*Enlace para agendar*:''',

                'critical_consulate_handler': '''
*Representación del Ministerio de Relaciones Exteriores de Rusia en Kaliningrado* 🏛️

*Dirección*: 🏠
236022, Rusia, ciudad de Kaliningrado, calle Kirova, 17

*Teléfonos*: 📞
Recepción: + 7 (401) 221-37-12
Fax: + 7 (401) 221-06-26
Departamento consular: + 7 (401) 221-16-68
Departamento de pasaportes: + 7 (401) 295-82-02
Departamento de tramitación de invitaciones: + 7 (4012) 21-59-28

*Atención al público en cuestiones consulares y legales* 
⚖️Lun-Jue: de *9:00* a *17:00* (pausa de *12:00* a *14:00*)
Vie: de *9:00* a *16:00* (pausa de *12:00* a *14:00*)
Sáb-Dom: 🚫 Cerrado
                                            ''',
            },

            'dormitory_handlers': {
                'dormitory_text': """
Para la tramitación del lugar en el alojamiento 🏠 es importante preparar con anticipación los documentos necesarios 📋 y familiarizarse con el procedimiento de presentación de solicitudes 📝. Consulte las instrucciones detalladas a continuación 👇:
                                         """,

                'payment_text': """
Se puede pagar el alojamiento de dos maneras.

1. Personalmente. 

En la oficina número 222 del edificio administrativo, segundo piso. Aquí recibirás un recibo para el pago en la caja del mismo piso. 
Se puede pagar en la caja en efectivo en rublos o con tarjeta bancaria.

2. De forma remota en el sitio web.

Los estudiantes de primer año pagan el primer semestre en su totalidad al momento de la llegada. 
Posteriormente, el semestre de otoño se paga hasta el 15 de septiembre, y el semestre de primavera hasta el 15 de febrero.
                                            """,

                'rules_text': """
Haz clic aquí 🏘️ "Normas de Convivencia" para conocer las reglas y recomendaciones importantes que harán tu estancia cómoda y segura. Aquí encontrarás toda la información necesaria sobre horarios, responsabilidades de los residentes, normas de comportamiento y mucho más.✨""",

                'laundry_text': """
🏢 *Ubicación*: 
Las lavanderías se encuentran en cada residencia. La ubicación exacta y el horario de funcionamiento te lo indicará el conserje o el portero.

🧼 *Reglas de uso*: 
• Trae tu propio detergente
• Usa bolsas especiales para ropa interior
• *Está prohibido* lavar calzado (esto daña las máquinas)
• Antes de usar, familiarízate con las instrucciones en el lugar
• Seca la ropa en la sala equipada especialmente para ello

⏰ *¡Importante!* 
Devuelve la llave al portero *exactamente a la hora acordada* — ¡otros estudiantes también quieren lavar sus cosas! 🙏

✨ Todo está organizado para tu comodidad — ¡úsalo con cuidado!
""",

                'no_certificate_text': """
SI NO TIENES CERTIFICADO DE VACUNAS O DE FLUOROGRAFÍA

1. *Si no tienes una fleografía reciente*

Puedes hacerla en varios lugares, por ejemplo:
- En el KDC BFU por 320 rublos con la tarjeta de estudiante (debe estar disponible). Ubicación del KDC: [https://goo.gl/maps/P4djCkwJ3ZQHThgGA] (https://goo.gl/maps/P4djCkwJ3ZQHThgGA)
- En Medexpert (calle Kosmicheskaya o avenida Moscú), hasta las 17:00, por 450 rublos sin radiografía. Ubicación: [https://goo.gl/maps/rRiC1Nh35BNPw2w3A](https://goo.gl/maps/rRiC1Nh35BNPw2w3A)
- Novomed (Gagarina 2B) hasta las 17:00, 350 rublos. Ubicación: [https://goo.gl/maps/kgEkj4yLnWBNbFUm6](https://goo.gl/maps/kgEkj4yLnWBNbFUm6)

2. *Si no tienes certificados de vacunación*

Dirígete a cualquier sucursal de Medexpert. Allí necesitas hacerte un análisis de sangre, que se llama “Tensión de inmunidad para sarampión y difteria”. 
El análisis se puede realizar todos los días, de lunes a viernes de 7:30 a 19:00, y los fines de semana de 7:30 a 17:00.

El análisis se realiza en ayunas.

El resultado se emite en 4 días hábiles (el resultado se puede obtener en el área personal).
                                                """,
            },

            'dormitory_location_handlers': 'Residencia estudiantil №',

            'hospital_handlers': {
                'hospital_text': '''
*Clínica Universitaria BFU im. I. Kanta*  

*Dirección*: 236041, Rusia, Kaliningrado, calle 9 de abril, 60  
*Contactos*: +7 (4012) 31-33-39 kdc@kantiana.ru'''
            },

            'language_chack_handlers': {
                'grammar_handlers': {
                    'language_grammar_handler': '''
                                            *Elija la opción de traducción*:
                                            ''',
                    'translate_to_russian_handler': '''
                                            Traduce este texto al ruso:
                                            ''',
                    'translate_from_russian_handler': '''
                                            Traduce este texto del ruso a tu idioma:
                                            ''',
                },

                'listening_handlers': {
                    'send_voice': 'Escucha el texto e intenta escribirlo en ruso.',
                },

                'speaking_handlers': {
                    'topics': [
                        'Cuéntanos un poco sobre tu familia',
                        '¿Tienes una mascota?',
                        '¿Qué platos te gustan?',
                        'Describe tu habitación',
                        '¿Cuál es su medio de transporte favorito?',
                        '¿Dónde te gusta pasar tu tiempo libre?',
                        '¿Cómo pasas tu domingo?',
                        '¿Cuál es tu recuerdo más vívido de la infancia?',
                        '¿A dónde te gustaría viajar?',
                        '¿Qué hábitos te ayudan a mantenerte productivo?',
                        '¿Cómo estuvo tu día ayer?',
                        '¿A qué te dedicas y qué haces en el trabajo?',
                        '¿Con qué sueña tu familia?',
                        '¿Qué cosas interesantes te pasaron la semana pasada?',
                        '¿Qué le interesa a tu mejor amigo?',
                        "Comparte tus impresiones de la última película que viste",
                        '¿Por qué decidiste estudiar en Kaliningrado?'
                    ],
                    'speaking_send': 'Espero tu historia sobre el tema:',
                    'handle_voice_message': 'Resultado del análisis:',
                }
            },

            'location_handlers': {
                'addresses_handler': 'Elige el cuerpo',
                'loc_1_handler': """
*Cuerpo administrativo, calle A. Nevski, 14* 

Aquí se encuentran: 
· Oficina de administración (of. 115) 
· Servicio de contabilidad (of. 212) 
· Archivo (of. 221) 
· Grupo de cálculos de ingresos y contabilidad fiscal (of. 222) 
· Caja (segundo piso) 
· Sala Acuario 
· Sala Máximo 
· Comedor (primer piso) 
                                            """,

                'loc_2_handler': """
*Cuerpo Nº 2, Instituto de Física, Matemáticas y Tecnologías de la Información («Fizmat»), calle A. Nevsky, 14* 

Aquí se encuentran: 
· Departamento de trabajo con estudiantes extranjeros (oficina 119) 
· Sector de apoyo de visas y migración (oficina 114) 
· Comisión de admisión (oficinas 116 y 117) 
· Biblioteca, sala 202 («Sala de Lectura») 
· Servicio de atención a la infraestructura IT (oficina 121) 
                                            """,

                'loc_3_handler': """
*Cuerpo N° 3, calle Universitaria, 2*

Aquí se encuentran:
· Instituto de Sistemas Vivos
· Biblioteca universitaria principal: suscripción científica (of. 126), sala de lectura (of. 115)
                                            """,

                'loc_4_handler': """
*Cuerpo N°4, calle Tchernyshevsky, 56 («Edificio con reloj»)*

Aquí se encuentran:
· Instituto de Ciencias Humanas
· Centro de la lengua rusa (oficina 01)
· Museo de la infancia soviética
                                            """,

                'loc_5_handler': """
*Cuerpo Nº5, calle Tchernyshevsky, 56a* 

Aquí se encuentra: 
· Instituto de Educación 
                                            """,

                'loc_6_handler': """
*Cuerpo No. 6, calle A. Nevski, 14b («Shaiba»)*

Aquí se encuentran:
· Complejo de residencias estudiantiles (cab. 101)
· Gestión de actividades extracurriculares
                                            """,

                'loc_7_handler': """
*Cuerpo Nº7, calle Frunze, 6*

Aquí se encuentran:
· Estudio de teleeducación
· Instituto de Derecho
                                            """,

                'loc_8_handler': """
*Cuerpo Nº 8, calle 9 de abril, 5* 

Aquí se encuentra: 
· Biblioteca médica 
                                            """,

                'loc_9_handler': """
*Cuerpo N°9, calle A. Nevsky, 14 («FOK»)*

Aquí se encuentra:
· Complejo de educación física y salud
                                            """,

                'loc_10_handler': """
*Cuerpo #10, calle A. Nevski. 14 («Vela»)*

Aquí se encuentran:
· Centro de apoyo socioeconómico para estudiantes (cab. 14)
· Centro de carreras
                                            """,

                'loc_11_handler': """
*Edificio Nº 11, calle botkina, 3*

Aquí está:
· Centro regional de recursos de capacitación en simulación y acreditación en medicina

                                            """,

                'loc_12_handler': """
*Cuerpo Nº12, calle Botkina, 4-6*

Aquí se encuentra:
· Instituto Médico
                                            """,

                'loc_13_handler': """
*Edificio no. 13, ST. botkina, 4-6*

Aquí está:
· Clínica universitaria

                                            """,

                'loc_14_handler': """
*Edificio no. 14, ST. Alexander Nevsky, 14, Corp. 4*

Aquí está:
· Dependencia de transporte
· Oficina de administración del complejo de bienes
· División de regímenes
                                            """,
        
                'loc_19_handler': """
*Edificio №19, Pionersky, pueblo de pescado, 23*

Aquí está:
· Base de prácticas educativas

                                            """,

                'loc_20_handler': """
*Edificio no. 20, Svetlogorsk, kaliningradsky Prospekt, 102*

Aquí está:
· Base de prácticas educativas

                                            """,

                'loc_21_handler': """
*Edificio no. 21, calle Lesnaya, 12*

Aquí está:
· Jardín botánico

                                            """,

                'loc_22_handler': """
*Cuerpo №22, calle A. Nevskogo, 14* 

Aquí se encuentra: 
· Complejo educativo y deportivo con piscina 
                                            """,

                'loc_23_handler': """
*Edificio no. 23, ST. Dmitry Donskoy, 27k1*

Aquí está:
· Cuerpo de enseñanza y laboratorio de la escuela Superior de medicina

                                            """,

                'loc_24_handler': """
*Cuerpo nº 24, calle Zoológica, 2*

Aquí se encuentra:
· Colegio universitario
                                            """,

                'loc_25_handler': """
*Edificio no. 25, calle Cosmonauta patsayev, 12*

Aquí están:
· Instituto ONC de alta tecnología
· Escuela superior de sistemas ciberfísicos

                                            """,

                'loc_27_handler': """
*Cuerpo Nº 27, calle General-lieutenant Ozerov, 57*

Aquí se encuentran:
· Instituto de ingeniería y tecnología
· Arena «Kantiana»
                                            """,

                'loc_28_handler': """
*Cuerpo Nº28, calle Gorky, 23*

Aquí se encuentran:
· Instituto de Economía y Gestión
                                            """,

                'loc_29_handler': """
*Edificio Nº 29, calle proletarskaya, 131*

Aquí están:
· Instituto de Ciencias de la computación aplicada y geofísica matemática
                                            """,
        
                'loc_32_handler': """
*Edificio no. 32, calle Gaidar, 6*

Aquí están:
· Parque científico y tecnológico "fábrica"
                                            """,

                'loc_35_handler': """
*Edificio no. 35, ST. Alexander Nevsky, 14V*

Aquí están:
· Nadadero
                                            """,
            },

            'university_info_handlers': {
                'schedule_text': '''
*Horario de clases*:
                                            ''',
                'scholarship_text': '''
*Información sobre becas y ayuda financiera*:
                                            ''',
                'office_contacts_text': '''
*Contactos*:  

_Dirección_: 236041, Kaliningrado, calle Aleksandra Nevski, 14  
_Teléfono de contacto_: +7 (4012) 59-55-95  
_Comisión de admisión_: calle Aleksandra Nevski, 14  

8 (800) 600-52-39 llamada gratuita  
+7 (4012) 59-55-96  

_Oficina_: +7 (4012) 59-55-97  
_Correo electrónico_: post@kantiana.ru  

*Horario de trabajo de los servicios administrativos*  

Lunes: 9:00 — 18:00 _pausa_: 13:00—13:45  
Martes: 9:00 — 18:00 _pausa_: 13:00—13:45  
Miércoles: día no laboral (trabajo con documentos)  
Jueves: 9:00 — 18:00 _pausa_: 13:00—13:45  
Viernes: 9:00 — 16:45 _pausa_: 13:00—13:45  
Sábado y domingo: días no laborables
''',
                'visa_center_text': '''
*Centro de visa y migración*:

*Contactos*

_Dirección_: 236041, Rusia, Kaliningrado, calle A. Névsky 14, edificio 2, oficina 119

_Horario de atención_: 

Lunes a jueves de 9:00 a 18:00, viernes de 9:00 a 16:45

_Teléfono_: +7 (4012) 31-33-99
_Email_: international-study@kantiana.ru
'''
            },

            'sber_handlers': {
                'useful_links_text': """
🔗 Recursos útiles de Sber y sus socios:
• [Plataforma Netología](https://netology.ru/navigation) — cursos y profesiones en línea
• [Entrena la calma](http://interview.sberstudent.ru/?utm_source=sber&utm_medium=internal&utm_campaign=salaryprojectmanagement) — simulador para entrevistas
• [Escuela 21](https://sbergraduate.ru/careerofthefuture/) — educación IT gratuita
• [SberSova](https://sbersova.ru/academy/courses/kibergramotnost?utm_source=event&utm_medium=free&utm_campaign=speaker) — plataforma educativa
• [Cibiblioteca](https://sber.ru/kibrary) — biblioteca digital
• [Maratón digital](https://it-marathon.21-school.ru/?utm_source=ter_bank&utm_medium=referral&utm_campaign) — competiciones y desafíos
• [Startup de Sber](https://sberstudent.sberclass.ru/) — apoyo a startups
• [Prácticas](https://sbergraduate.ru/practice/) — ofertas de empleo y prácticas
""",

                'sber_card_text': """
💳 *Tarjeta de Sber*  
✨ *Mantenimiento gratuito para siempre*  
💸 *Hasta un 5% de devolución en efectivo* en tus compras favoritas  
📈 *Intereses en cuenta de ahorros* de hasta *16%* anuales  
🎨 *Pegatinas únicas de Sber* para cada transacción — ¡colecciona y comparte con amigos!  
🎯 *Ofertas especiales para jóvenes* — descuentos en entretenimiento, educación y mucho más  

Haz clic en *el botón de abajo* para más detalles:
""",

                'educational_loan_text': """
🎓 *Crédito educativo de Sber* 
🎯 *Solo 3% anual* 
📚 *Solo paga los intereses durante los estudios* 
👨‍🎓 *Contratación desde los 14 años* 
⏳ *Plazo de hasta 15 años después de la graduación* 

Haz clic en *el botón de abajo* para más detalles:
"""
            }
        }
    },

    'cn': {
        'greetings': '''
你好，BFU的學生！🌍✨

我們很高興在官方的加爾滕巴爾捷國立大學外國學生聊天機器人中見到你！🎓🇷🇺

我是你在卡廖林格勒的個人助理，任何問題都可以找我。
你可以和我一起：

🧠 通過智能AI訓練器提升你的俄語水平
🏛️ 獲得有關大學及其生活的有用信息：
📍 找到各個校區和宿舍
🏠 解決住宿問題
🤝 獲得支持和幫助
🏦 知道有用的SBER服務😊
🚀 在城市裡適應並找到志同道合的人

我們從哪裡開始？👇 選擇菜單項！
        ''',
        'errors': {
            'start_error': '啟動機器人時發生錯誤。請稍後再試。',
            'info_error': '載入資訊時出錯',
            'back_error': '返回主菜單時出錯',
            'audio_error': '處理時出錯',
            'photo_error': '載入照片時發生錯誤',
            'gigachat_error': 'GigaChat初始化錯誤:',
        },

        'keyboards': {
            'main_keyboard': {
                'info': '資訊',
                'location': '機構',
                'dormitory': '宿舍',
                'hospital': '醫療中心',
                'critical': 'SOS',
                'sber':'SBER',
                'language_check': '訓練器',
                'back': '回去'
            },
            'critical_keyboard': {
                'police': '緊急',
                'hotline': '熱線 FMS',
                'government': '地方當局',
                'consulate': '領事館',
                'back': '回去',
                'appeal':'線上申請 '
            },
            'dormitory_keyboard': {
                'check-in': '入住宿舍',
                'payment': '付款',
                'address': '宿舍地址',
                'rules': '居住規則',
                'laundry': '洗衣房',
                'details': '了解更多',
                'no_certificate': '沒有疫苗接種證明或胸部X光檢查報告',
                'back': '回去'
            },
            'dormitory_locations_keyboard': {
                'dormitory_1': 'Sommera',
                'dormitory_2': 'Tchernyshevskogo',
                'dormitory_3': 'A. Nevskogo',
                'dormitory_4': 'A. Nevskogo',
                'dormitory_5': 'Tchaikovskogo',
                'dormitory_6': 'Azovskaya',
                'dormitory_7': 'Yelovaya',
                'dormitory_8': 'Yelovaya',
                'dormitory_9': 'Yubileynaya',
            },
            'payment_keyboard': {
                'sber_payment': '在 Sber 銀行支付',
                'back': '回去'
            },
            'language_check_keyboard': {
                'grammar_keyboard': {
                    'to_russian': '翻譯成俄語',
                    'from_russian': '從俄語翻譯',
                    'back': '回去'
                },
                'speaking_keyboard': {
                    'back': '回去'
                },
                'language_check_keyboard': {
                    'audio': '聆聽',
                    'grammar': '語法',
                    'speaking': '說話',
                    'back': '回去'
                }
            },
            'location_keyboard': {
                'loc_1': '🏛️ 管理機構',
                'loc_2': '🧮 物理數學',
                'loc_3': '🧬 活的系統',
                'loc_4': '🏫 IGN',
                'loc_5': '👨‍🏫 教育',
                'loc_6': '🛌 圓盤',
                'loc_7': '⚖️ 法律的',
                'loc_8': '📚 醫學圖書館',
                'loc_9': '🏐 FOC',
                'loc_10': '👩‍🏫 蠟燭',
                'loc_11': '✨ 资源中心',
                'loc_12': '🩺 醫學院',
                'loc_13': '👩‍⚕️ 诊所',
                'loc_14': '🚗 运输业',
                'loc_19': '🏡 基地 №19',
                'loc_20': '🏡 基地 №20',
                'loc_21': '🌳 植物学',
                'loc_22': '🏊‍♂️ 游泳池',
                'loc_23': '🧪 实验室大楼',
                'loc_24': '🎓 學院',
                'loc_25': '👨‍🔬 网络物理学',
                'loc_27': '⚙️ ITI',
                'loc_28': '💸 經濟',
                'loc_29': '🥽 地球物理学',
                'loc_32': '🔬 工厂',
                'loc_35': '🏊‍♂️ 游泳池',
                'back': '回去'
            },
            'university_info_keyboard': {
                'schedule': '時刻表',
                'scholarship': '獎學金',
                'office_contacts': '聯絡學習辦公室',
                'visa_center': '簽證移民中心',
                'back': '回去'
            },
            'language_selection_keyboard': {
                'back': '回去'
            },
            'sber_keyboard': {
                'educational_loan': '教育貸款',
                'sber_card': '獎學金地圖',
                'useful_links': '有用的鏈接',
                'details': '更詳細的資訊',
                'back': '回去'
            },
            'hospital_keyboard': {
                'insurance': '醫療保險',
                'attachment': '診所附屬'
            }
        },

        'handlers': {
            'critical_handlers': {
                'critical_police_handler': '''
🚨 *緊急聯絡方式*

*緊急救援服務統一號碼*（消防、緊急情況部、警察、急救、燃氣服務）
📞 *112*

👨‍🚒 *消防員和救援人員*
📞 *01*（從固定電話撥打）| *101*（從手機撥打）

👮 *警察*
📞 *02*（從固定電話撥打）| *102*（從手機撥打）

🏥 *急救*
📞 *03*（從固定電話撥打）| *103*（從手機撥打）

💡 保存這些號碼以便快速使用！
                                                    ''',

                'critical_hotline_handler': '''
🚪 *簽證與移民支持部門*

📞 *電話*:
+7 (4012) 595-595 (分機 7454) — 移民登記與簽證
+7 (4012) 595-595 (分機 7452) — 簽證邀請

🏢 *地址*:
俄羅斯，加林寧格勒，A. 涅夫斯基街，14號，2號樓，114室

🕒 *辦公時間*:
週一 14:00–17:00
週二 10:00–13:00
週四 14:00–17:00
週五 10:00–13:00

午餐 13:00–14:00
                                                    ''',

                'critical_government_handler': '''
🏛️ *圣彼得堡民族关系与移民政策委员会
您可预约线上或线下会议*

1. 📅 *线下形式*（线下接待）
如何预约？
拨打电话：*576-28-08*1。
接待时间：
• 周一至周四：*9:00 – 18:00*
• 周五：*9:00 – 17:00*
• 午休时间：*13:00 – 14:00*（不接听电话）
• 周六和周日：休息。

需携带文件：

护照或其他身份证明文件。

接待流程：
由委员会主席、副主席或授权人员接待4。

您的诉求将记录在接待卡中。

简单问题 → 口头答复（记录在卡中）。

复杂问题 → 后续书面答复。

不属委员会职权范围 → 告知您应联系的相关部门及方式。
⚠️ 若您的问题已答复过，可能拒绝再次接待。

2. 🌐 线上接待
通过委员会官方资源预约。
*预约链接*：''',

                'critical_consulate_handler': '''
*俄羅斯外交部駐加里寧格勒代表處* 🏛️

*地址*: 🏠
236022, 俄羅斯, 加里寧格勒市, 基羅夫街 17號
(236022, Russia, Kaliningrad, ul. Kirova, 17)

*電話*: 📞
接待處: + 7 (401) 221-37-12
傳真: + 7 (401) 221-06-26
領事部門: + 7 (401) 221-16-68
護照部門: + 7 (401) 295-82-02
邀請函辦理部門: + 7 (4012) 21-59-28

*受理公民領事和法律事務* ⚖️
週一至週四: *9:00* 至 *17:00* (休息時間 *12:00* 至 *14:00*)
週五: *9:00* 至 *16:00* (休息時間 *12:00* 至 *14:00*)
週六-週日: 🚫 休息日
                                            ''',
            },

            'dormitory_handlers': {
                'dormitory_text': """
為了在宿舍辦理入住 🏠，提前準備必要的文件 📋 並了解申請程序 📝 是非常重要的。請參閱下面的詳細指導 👇:
                                            """,

                'payment_text': """
支付宿舍費用可以通過兩種方式。 

1. 親自到訪。

前往行政大樓的222號辦公室，二樓。在這裡，你將獲得一張收據，用於在同一樓層的收銀台付款。你可以選擇用盧布現金或銀行卡通過收銀台付款。

2. 在線上支付。 

一年級新生在入住時需全額支付第一學期的費用。此後秋季學期的費用需在9月15日之前支付，而春季學期的費用需在2月15日之前支付。                                            
""",

                'rules_text': """
點擊這裡 🏘️ «住宿規則» 以了解重要規則和建議，這些將使您的住宿舒適安全。在這裡您會找到關於工作時間、住宿者責任、行為規範等所有必要信息。✨
""",

                'laundry_text': """
🏢 *位置*：
每棟宿舍樓均設有洗衣房。管理員或舍監將告知具體位置和使用時間。

🧼 *使用規則*：
• 請自帶洗衣粉
• 內衣必須使用專用洗衣網
• 禁止清洗鞋子（會導致機器損壞）
• 使用前請閱讀現場說明
• 可在配備烘乾設備的專用房間晾乾衣物

⏰ *重要提示!*
請準時歸還鑰匙給管理員——其他學生也需要使用洗衣機！🙏

✨ 一切均為您的方便而設——請仔細使用！
""",
                'no_certificate_text': """
如果沒有疫苗接種證明或胸部X光片

1. *如果您缺少最新的胸部X光檢查* 

您可以在幾個地方進行檢查，例如：
- 在BФУ的KДЦ，使用學生證檢查需320盧布（必須持有學生證）。KДЦ的位置：[https://goo.gl/maps/P4djCkwJ3ZQHThgGA](https://goo.gl/maps/P4djCkwJ3ZQHThgGA) 
- 在醫學專家（宇宙街或莫斯科大街），17:00之前，無拍攝需450盧布。位置：[https://goo.gl/maps/rRiC1Nh35BNPw2w3A](https://goo.gl/maps/rRiC1Nh35BNPw2w3A) 
- Novomed（加加林街2В），17:00之前，需350盧布。位置：[https://goo.gl/maps/kgEkj4yLnWBNbFUm6](https://goo.gl/maps/kgEkj4yLnWBNbFUm6) 

2. *如果您缺少疫苗接種證書* 

請聯繫任何醫學專家的分支機構。您需要進行一項稱為“麻疹和白喉免疫狀況”的血液檢查。檢查可以在每個工作日進行，週一至週五，7:30至19:00，週末7:30至17:00。

檢查需空腹進行。

結果在4個工作日後發放（結果可以在個人帳戶中獲得）。
                                                """,
            },

            'dormitory_location_handlers': '宿舍 №',

            'hospital_handlers': {
                'hospital_text': '''
*BFU康特大學醫療診所*  

*地址*: 236041，俄羅斯，卡里寧格勒，4月9日街60號  
*聯繫方式*: +7 (4012) 31-33-39 kdc@kantiana.ru '''
},

            'language_chack_handlers': {
                'grammar_handlers': {
                    'language_grammar_handler': '''
                                            *選擇翻譯選項*:
                                            ''',
                    'translate_to_russian_handler': '''
                                            請將這段文字翻譯成俄語：
                                            ''',
                    'translate_from_russian_handler': '''
                                            將這段文字從俄語翻譯成你的語言:
                                            ''',
                },

                'listening_handlers': {
                    'send_voice': '聽文本並嘗試將其寫成俄語。',
                },

                'speaking_handlers': {
                    'topics': [
                        '談談你的家庭。',
                        '你有寵物嗎？',
                        '你喜歡什麼菜？',
                        '描述一下你的房間。',
                        '你最喜歡的交通工具是什麼？',
                        '你喜歡在空閒時間做什麼？',
                        '你周日是怎麼度過的？',
                        '你最難忘的童年回憶是什麼？',
                        '你想去哪裡旅行？',
                        '有哪些習慣幫助你保持生產力？',
                        '你昨天過得怎麼樣？',
                        '你從事什麼工作，工作內容是什麼？',
                        '你的家庭夢想著什麼？',
                        '上週有什麼有趣的事情發生在你身上？',
                        '你最好的朋友喜歡什麼？',
                        '分享一下你對最近看過的電影的感受。',
                        '為什麼你決定在加里寧格勒學習？'
                    ],
                    'speaking_send': '我在等你講述的主題：',
                    'handle_voice_message': '分析結果：',
                }
            },

            'location_handlers': {
                'addresses_handler': '選擇機殼',
                'loc_1_handler': """
*行政大樓，亞歷山大·涅夫斯基街14號*

這裡有：
· 文書處理 (115室)
· 會計服務 (212室)
· 檔案館 (221室)
· 收入和稅務會計結算組 (222室)
· 現金櫃 (二樓)
· 水族館大廳
· 最大值大廳
· 餐廳 (一樓)
                                            """,

                'loc_2_handler': """
*第二號樓，物理、數學與信息技術研究所（「菲茨」），阿·涅夫斯基街14號* 

這裡有：
· 外國學生工作部（119室）
· 簽證-移民支持部（114室）
· 招生辦公室（116和117室）
· 圖書館，202室（「閱覽室」）
· IT基礎設施服務部（121室）
                                            """,

                'loc_3_handler': """
*第三號樓, 大學街 2 號*

這裡有：
· 生物系統研究所
· 主大學圖書館：科學訂閱（126室），閱覽室（115室）
                                            """,

                'loc_4_handler': """
*第四號樓, 切爾尼斯赫夫斯基街56號（“有鐘樓的建築”）*

這裡有：
· 人文科學院
· 俄語中心（01號辦公室）
· 蘇聯兒童博物館
                                            """,

                'loc_5_handler': """
*第五大樓，切爾尼雪夫斯基街，56a*

這裡有：
· 教育研究所
                                            """,

                'loc_6_handler': """
*第六號樓，阿. 涅夫斯基街，14b（“橡膠圓盤”）* 

這裡有：
· 學生宿舍綜合大樓（101室）
· 課外活動管理處
                                            """,

                'loc_7_handler': """
*第7號大樓，弗魯恩茨街6號* 

這裡有：
· 教學電視工作室
· 法律學院
                                            """,

                'loc_8_handler': """
*第8號樓，4月9日街，5號* 

此處設有： 
· 醫學圖書館 
                                            """,

                'loc_9_handler': """
*第9號大樓，A.涅夫斯基街14號（「FOK」）

*這裡有：
· 體育健身複合體
                                            """,

                'loc_10_handler': """
*第10號樓, A. 內夫斯基街 14 號（“小蠟燭”）

*這裡有：
· 學生社會經濟支持中心（14室）
· 職業中心
                                            """,

                'loc_11_handler': """
*博金街11号楼3号*

它位于这里:
· 医学模拟培训及认证区域资源中心

                                            """,

                'loc_12_handler': """
*第12號樓，博特金街4-6號* 

此處有：
· 醫學院 
                                            """,

                'loc_13_handler': """
*博金街4-6号13楼*

它位于这里:
· 大学诊所

                                            """,

                'loc_14_handler': """
*亚历山大*涅夫斯基街14号楼4号楼*

它位于这里:
· 运输服务组
· 管理物业综合大楼的运作
· 政权保证部
                                            """,
        
                'loc_19_handler': """
*Rybnoye村Pionersky19号楼23号*

它位于这里:
· 教育实践的基础

                                            """,

                'loc_20_handler': """
*20号楼，Svetlogorsk，Kaliningradsky Prospekt，102*

它位于这里:
· 教育实践的基础

                                            """,

                'loc_21_handler': """
*莱斯纳亚街21号楼, 12*

它位于这里:
· 植物园

                                            """,

                'loc_22_handler': """
*第22號大樓，A.涅夫斯基大街14號*

這裡有：
· 帶游泳池的體育訓練綜合體
                                            """,

                'loc_23_handler': """
*德米特里*顿斯科伊斯特23号楼。,27k1*

它位于这里:
· 高等医学院教育及实验室大楼

                                            """,

                'loc_24_handler': """
*第24號樓，動物學街2號* 

這裡有：
· 大學學院
                                            """,

                'loc_25_handler': """
*Kosmonavta Patsaeva街12号25号楼*

这里是:
· 昂克高科技研究所
· 网络物理系统高等学院

                                            """,

                'loc_27_handler': """
*第27號建築，俄羅斯格涅拉爾-萊特南特奧捷羅夫街57號*

這裡有：
· 工程技術學院
·「康提亞那」體育館
                                            """,

                'loc_28_handler': """
*第28號樓，戈爾基大街23號*

此處設有：
· 經濟與管理研究所
                                            """,

                'loc_29_handler': """
*Proletarskaya St.131号29号楼*

有:
· 应用信息学和数学地球物理研究所
                                            """,
        
                'loc_32_handler': """
*盖达拉街6号32号楼*

这里是:
· 法布里卡科技园
                                            """,

                'loc_35_handler': """
*亚历山大*涅夫斯基街35号楼14B*

这里是:
· 游泳池
                                            """,
            },

            'university_info_handlers': {
                'schedule_text': '''
*課程時間表*:
                                            ''',
                'scholarship_text': '''
*獎學金和經濟援助信息*:
                                            ''',
                'office_contacts_text': '''
*聯繫方式*:

_地址_: 236041, 加里寧格勒, 亞歷山大·涅夫斯基街, 14
_聯絡電話_: +7 (4012) 59-55-95
_招生辦公室_: 亞歷山大·涅夫斯基街, 14

8 (800) 600-52-39 免費電話
+7 (4012) 59-55-96

_辦公室_: +7 (4012) 59-55-97
_電子郵件_: post@kantiana.ru

*行政部門工作時間*

星期一: 9:00 — 18:00 _休息_: 13:00—13:45
星期二: 9:00 — 18:00 _休息_: 13:00—13:45
星期三: 不接待日（處理文件）
星期四: 9:00 — 18:00 _休息_: 13:00—13:45
星期五: 9:00 — 16:45 _休息_: 13:00—13:45
星期六和星期日: 休息日
''',
                'visa_center_text': '''
*簽證移民中心*:

*聯繫資訊*

_地址_: 236041, 俄羅斯, 卡林寧格勒, A. 內夫斯基街 14號, 2號樓, 119室

_工作時間_: 

星期一至星期四 9:00 至 18:00，星期五 9:00 至 16:45

_電話_: +7 (4012) 31-33-99
_電子郵件_: international-study@kantiana.ru
'''
            },

            'sber_handlers': {
                'useful_links_text': """
🔗 Sber及其合作夥伴的有用資源：
• [Netology平台](https://netology.ru/navigation) — 在線課程與職業
• [訓練冷靜](http://interview.sberstudent.ru/?utm_source=sber&utm_medium=internal&utm_campaign=salaryprojectmanagement) — 面試模擬器
• [21學校](https://sbergraduate.ru/careerofthefuture/) — 免費IT教育
• [SberSova](https://sbersova.ru/academy/courses/kibergramotnost?utm_source=event&utm_medium=free&utm_campaign=speaker) — 教育平台
• [Kibrary](https://sber.ru/kibrary) — 數位圖書館• [數位馬拉松](https://it-marathon.21-school.ru/?utm_source=ter_bank&utm_medium=referral&utm_campaign) — 競賽與挑戰
• [Sber的創業計劃](https://sberstudent.sberclass.ru/) — 對創業的支持
• [實習機會](https://sbergraduate.ru/practice/) — 職位與實習
""",

                'sber_card_text': """
💳 *俄羅斯聯邦儲備銀行卡*    
✨ *永遠免費的服務*  
💸 *對於喜愛的購物最高可達5%現金回饋*  
📈 *儲蓄賬戶利息* 可達 *16%* 年利率  
🎨 *來自俄聯儲的獨特貼紙* 每次交易都可收集並與朋友分享！  
🎯 *針對年輕人的特別優惠* — 休閒娛樂、教育等折扣    

點擊 *下方按鈕* 獲取更多詳情:
""",

                'educational_loan_text': """
🎓 *來自斯伯銀行的教育貸款*   
🎯 *年利率僅為3%*   
📚 *在學期間僅支付利息*   
👨‍🎓 *14歲即可申請*   
⏳ *畢業後可分期付款長達15年*  

請點擊 *下方按鈕* 獲取詳情：
"""
            }
        }
    },

    'in': {
        'greetings': '''
नमस्ते, BFU के छात्र! 🌍✨

आपको इमानुअस कैन्ट के नाम से बाल्टिक फेडरल यूनिवर्सिटी के विदेशी छात्रों के लिए आधिकारिक चैट-बॉट में देखकर खुशी हुई! 🎓🇷🇺

मैं कालिनिंग्राद में आपके किसी भी सवाल के लिए आपका व्यक्तिगत सहायक हूँ। 
मेरे साथ आप:

🧠 स्मार्ट AI-प्रशिक्षक के माध्यम से रूसी भाषा में सुधार कर सकते हैं
🏛️ विश्वविद्यालय और इसके जीवन के बारे में उपयोगी जानकारी प्राप्त कर सकते हैं:
📍 भवनों और छात्रावासों को ढूंढ सकते हैं
🏠 आवास के मुद्दों को हल कर सकते हैं
🤝 समर्थन और सहायता प्राप्त कर सकते हैं
🏦 एसबीईआर की उपयोगी सेवाओं के बारे में जान सकते हैं 😊
🚀 शहर में अनुकूलित कर सकते हैं और समान विचारधारा वाले लोगों को ढूंढ सकते 

हैंकहाँ से शुरू करें? 👇 मेन्यू में से एक विकल्प चुनें!
        ''',
        'errors': {
            'start_error': 'बोट चालू करने में एक त्रुटि हुई। कृपया बाद में प्रयास करें।',
            'info_error': 'जानकारी लोड करने में त्रुटि',
            'back_error': 'मुख्य मेनू में लौटने में त्रुटि',
            'audio_error': 'प्रसंस्करण में त्रुटि',
            'photo_error': 'फोटो लोड करते समय एक त्रुटि हुई',
            'gigachat_error': 'GigaChat में प्रारंभिककरण की त्रुटि:',
        },

        'keyboards': {
            'main_keyboard': {
                'info': 'जानकारी',
                'location': 'इमारतें',
                'dormitory': 'छात्रावास',
                'hospital': 'मेडिकल सेंटर',
                'critical': 'SOS',
                'sber':'SBER',
                'language_check': 'व्यायाम मशीन',
                'back': 'पीछे'
            },
            'critical_keyboard': {
                'police': 'आपातकाल',
                'hotline': 'प्रवासन सेवा की हॉटलाइन',
                'government': 'स्थानीय सरकारी संस्थाएँ',
                'consulate': 'कांसुलीट',
                'back': 'पीछे',
                'appeal':'ऑनलाइन अनुरोध'
            },
            'dormitory_keyboard': {
                'check-in': 'हॉस्टल में दाखिला',
                'payment': 'भुगतान',
                'address': 'होस्टल के पते',
                'rules': 'निवासी नियम',
                'laundry': 'धुलाई की जगह',
                'details': 'और जानें',
                'no_certificate': 'कोई टीकाकरण या फ्लोरोोग्राफी का प्रमाण पत्र नहीं है',
                'back': 'पीछे'
            },
            'dormitory_locations_keyboard': {
                'dormitory_1': 'Sommera',
                'dormitory_2': 'Tchernyshevskogo',
                'dormitory_3': 'A. Nevskogo',
                'dormitory_4': 'A. Nevskogo',
                'dormitory_5': 'Tchaikovskogo',
                'dormitory_6': 'Azovskaya',
                'dormitory_7': 'Yelovaya',
                'dormitory_8': 'Yelovaya',
                'dormitory_9': 'Yubileynaya',
            },
            'payment_keyboard': {
                'sber_payment': 'Sber में भुगतान करें',
                'back': 'पीछे'
            },
            'language_check_keyboard': {
                'grammar_keyboard': {
                    'to_russian': 'रूसी में अनुवाद करें',
                    'from_russian': 'रूसी से अनुवाद करना',
                    'back': 'पीछे'
                },
                'speaking_keyboard': {
                    'back': 'पीछे'
                },
                'language_check_keyboard': {
                    'audio': 'सुनाई',
                    'grammar': 'व्याकरण',
                    'speaking': 'बोलना',
                    'back': 'पीछे'
                }
            },
            'location_keyboard': {
                'loc_1': '🏛️ प्रशासनिक निकाय',
                'loc_2': '🧮 फिज़मैट',
                'loc_3': '🧬 जीवित प्रणाली',
                'loc_4': '🏫 IGN',
                'loc_5': '👨‍🏫 शिक्षा',
                'loc_6': '🛌 पक',
                'loc_7': '⚖️ कानूनी',
                'loc_8': '📚 मेड लाइब्रेरी',
                'loc_9': '🏐 FOC',
                'loc_10': '👩‍🏫 मोमबत्ती',
                'loc_11': '✨ संसाधन केंद्र',
                'loc_12': '🩺 मेडिकल इंस्टीट्यूट',
                'loc_13': '👩‍⚕️ क्लिनिक',
                'loc_14': '🚗 परिवहन',
                'loc_19': '🏡 आधार №19',
                'loc_20': '🏡 आधार №20',
                'loc_21': '🌳 वानस्पतिक',
                'loc_22': '🏊‍♂️ स्विमिंग पूल',
                'loc_23': '🧪 प्रयोगशाला भवन',
                'loc_24': '🎓 कॉलेज',
                'loc_25': '👨‍🔬 साइबरफिजिक्स',
                'loc_27': '⚙️ ITI',
                'loc_28': '💸 अर्थव्यवस्था',
                'loc_29': '🥽 भूभौतिकी',
                'loc_32': '🔬 फैक्टरी',
                'loc_35': '🏊‍♂️ स्विमिंग पूल',
                'back': 'पीछे'
            },
            'university_info_keyboard': {
                'schedule': 'अनुक्रमणिका',
                'scholarship': 'छात्रवृत्तियाँ',
                'office_contacts': 'शिक्षा कार्यालय के संपर्क',
                'visa_center': 'विजा-आप्रवासन केंद्र',
                'back': 'पीछे'
            },
            'language_selection_keyboard': {
                'back': 'पीछे'
            },
            'sber_keyboard': {
                'educational_loan': 'शैक्षणिक ऋण',
                'sber_card': 'छात्रवृत्ति के लिए नक्शा',
                'useful_links': 'उपयोगी लिंक',
                'details': 'अधिक जानकारी',
                'back': 'पीछे'
            },
            'hospital_keyboard': {
                'insurance': 'स्वास्थ्य बीма',
                'attachment': 'क्लिनिक से संलग्नक'
            }
        },

        'handlers': {
            'critical_handlers': {
                'critical_police_handler': '''
🚨 *आपातकालीन संपर्क*

*एकीकृत आपातकालीन प्रतिक्रिया सेवा*
(फायर ब्रिगेड, आपातकालीन सेवाएं, पुलिस, एम्बुलेंस, गैस सेवा)
📞 *112*

👨‍🚒 *फायरफाइटर्स और रेस्क्यूर्स*
📞 *01* (लैंडलाइन से) | *101* (मोबाइल से)

👮 *पुलिस*
📞 *02* (लैंडलाइन से) | *102* (मोबाइल से)

🏥 *एम्बुलेंस*
📞 *03* (लैंडलाइन से) | *103* (मोबाइल से)

💡 इन नंबरों को जल्दी एक्सेस के लिए सेव करें!
                                                    ''',

                'critical_hotline_handler': '''
                
🚪 *वीज़ा और प्रवासन सहायता विभाग*

📞 *फ़ोन*:
+7 (4012) 595-595 (एक्सट. 7454) — प्रवासन पंजीकरण और वीज़ा
+7 (4012) 595-595 (एक्सट. 7452) — वीज़ा निमंत्रण

🏢 *पता*:
रूस, कालिनिनग्राद, A. नेव्स्कोगो स्ट्रीट 14, भवन 2, कक्ष 114

🕒 *कार्यालय समय*:
सोम 14:00–17:00
मंगल 10:00–13:00
गुरु 14:00–17:00
शुक्र 10:00–13:00

दोपहर का भोजन: 13:00–14:00
                                                    ''',

                'critical_government_handler': '''
🏛️ *सेंट पीटर्सबर्ग में अंतर-जातीय संबंध और प्रवासन नीति समिति*
आप ऑनलाइन या ऑफलाइन मुलाकात के लिए अपॉइंटमेंट ले सकते हैं!

1. 📅 *ऑफलाइन प्रारूप* (नागरिकों की व्यक्तिगत स्वीकार्यता)
अपॉइंटमेंट कैसे लें?
फोन: *576-28-08* 1।
स्वीकार्यता घंटे:
• सोमवार–गुरुवार: *9:00 – 18:00*
• शुक्रवार: *9:00 – 17:00*
• लंच ब्रेक: *13:00 – 14:00* (इस दौरान कॉल स्वीकार नहीं)
• शनिवार और रविवार: बंद।

*क्या लेकर आएं?*

पासपोर्ट या कोई अन्य पहचान पत्र।

स्वीकार्यता प्रक्रिया:
आपको समिति के अध्यक्ष, उनके प्रथम उपाध्यक्ष, संरचनात्मक इकाइयों के प्रमुख या अधिकृत व्यक्ति स्वीकार करेंगे4।

आपका अनुरोध नागरिक व्यक्तिगत स्वीकार्यता कार्ड में दर्ज किया जाएगा।

सरल प्रश्न → मौखिक उत्तर (कार्ड में दर्ज)।

जटिल प्रश्न → बाद में लिखित उत्तर।

समिति की अधिकारिता से बाहर → आपको सही प्राधिकारी के पास भेजा जाएगा।
⚠️ यदि आपके प्रश्न का पहले ही उत्तर दिया जा चुका है, तो दोबारा स्वीकार्यता से इनकार किया जा सकता है।

2. 🌐 *ऑनलाइन स्वीकार्यता*
आधिकारिक संसाधनों के माध्यम से अपॉइंटमेंट लें।
*अपॉइंटमेंट लिंक*:
''',
                'critical_consulate_handler': '''
*कालिनिनग्राद में रूस के विदेश मंत्रालय का प्रतिनिधि कार्यालय* 🏛️

*पता*: 🏠
236022, रूस, कालिनिनग्राद शहर, किरोवा स्ट्रीट, 17

*फोन*: 📞
रिसेप्शन: + 7 (401) 221-37-12
फैक्स: + 7 (401) 221-06-26
कांसुलर विभाग: + 7 (401) 221-16-68
पासपोर्ट विभाग: + 7 (401) 295-82-02
निमंत्रण प्रसंस्करण विभाग: + 7 (4012) 21-59-28

*कांसुलर-कानूनी मामलों पर नागरिकों की स्वीकार्यता* ⚖️
सोम-गुरु: *9:00* से *17:00* तक (*12:00* से *14:00* तक ब्रेक)
शुक्र: *9:00* से *16:00* तक (*12:00* से *14:00* तक ब्रेक)
शनि-रवि: 🚫 बंद
                                            ''',
            },

            'dormitory_handlers': {
                'dormitory_text': """
कॉलेज के हॉस्टल में स्थान पाने के लिए 🏠 आवश्यक दस्तावेज़ों को पहले से तैयार करना 📋 और आवेदन करने की प्रक्रिया से परिचित होना महत्वपूर्ण है 📝। नीचे दिए गए विस्तृत निर्देशों से ознаком किया जाए 👇:
                                            """,

                'payment_text': """
छात्रावास का भुगतान दो तरीकों से किया जा सकता है।

1. व्यक्तिगत रूप से। 

प्रशासनिक भवन के कक्ष संख्या 222, दूसरी मंजिल में। यहाँ आपको उसी मंजिल पर भुगतान के लिए एक रसीद मिलेगी। कैश काउंटर के माध्यम से आप नकद में रूबल या बैंक कार्ड से भुगतान कर सकते हैं।

2. वेबसाइट के माध्यम से दूरस्थ रूप से।

प्रथम वर्ष के छात्र आवास लेते समय पहले सेमेस्टर का पूरा भुगतान करते हैं। इसके बाद, शरद सेमेस्टर का भुगतान 15 सितंबर तक और वसंत सेमेस्टर का भुगतान 15 फरवरी तक किया जाता है।                                            """,

                'rules_text': """
यहाँ क्लिक करें 🏘️ "रहने के नियम" महत्वपूर्ण नियमों और सिफारिशों से अवगत होने के लिए जो आके प्रवास को आरामदायक और सुरक्षित बनाएंगे। यहाँ आपको काम के घंटों, निवासियों की जिम्मेदारियों, आचरण के नियमों और भी बहुत कुछ के बारे में सभी आवश्यक जानकारी मिलेगी。✨
""",

                'laundry_text': """
🏢 *स्थान*:
हर छात्रावास भवन में लॉन्डरी रूम हैं। वार्डन या पर्यवेक्षक आपको सटीक स्थान और समय बता सकते हैं।

🧼 *उपयोग के नियम*:
• अपना डिटर्जेंट स्वयं लाएं
• अंडरवियर के लिए विशेष मेश बैग का उपयोग करें
• जूते धोने की मनाही है (इससे मशीन खराब होती है)
• उपयोग से पहले निर्देशों को पढ़ें
• कपड़े विशेष रूप से सुसज्जित कमरे में सुखाएं

⏰ *महत्वपूर्ण!*
चाबी पर्यवेक्षक को ठीक निर्धारित समय पर लौटाएं — अन्य छात्र भी अपने कपड़े धोना चाहते हैं! 🙏

✨ सब कुछ आपकी सुविधा के लिए व्यवस्थित है — कृपया सावधानी से उपयोग करें!                
""",

                'no_certificate_text': """
अगर टीकाकरण या फ्लोरोग्राफी का सर्टिफिकेट नहीं है

1. *यदि आपके पास ताजा फ्लुओरोप्टोग्राफी नहीं है*  

आप इसे कई स्थानों पर करा सकते हैं, उदाहरण के लिए:  
- बीएफयू के केडीसी में 320 रू. छात्र कार्ड पर (यह पास में होना चाहिए)। केडीसी का स्थान: [https://goo.gl/maps/P4djCkwJ3ZQHThgGA]  
- मेडएक्सपर्ट में (कосмическая स्ट्रीट या मॉस्को प्रॉस्पेक्ट), 17:00 बजे तक, बिना चित्र के 450 रू. स्थान:  [https://goo.gl/maps/rRiC1Nh35BNPw2w3A]  
- नोवोमेड (गागरिन 2वी) 17:00 बजे तक, 350 रू.  स्थान:  [https://goo.gl/maps/kgEkj4yLnWBNbFUm6]    

2. *यदि आपके पास टीकाकरण का प्रमाण पत्र नहीं है*  

किसी भी मेडएक्सपर्ट शाखा में जाएं। वहां आपको एक रक्त परीक्षण करना होगा, जिसे कहा जाता है "मिजाज प्रतिरक्षा के लिए खसरा और डिफ्थीरिया"। 
यह परीक्षण प्रत्येक दिन, सोमवार से शुक्रवार, 7:30 बजे से 19:00 बजे, शनिवार और रविवार, 7:30 बजे से 17:00 बजे के बीच किया जा सकता है।  

परीक्षण उपवास में किया जाता है।  

परिणाम 4 कार्य दिवसों के बाद जारी किया जाता है (परिणाम व्यक्तिगत खाते में प्राप्त किया जा सकता है)।
                                                """,
            },

            'dormitory_location_handlers': 'छात्रावास №',

            'hospital_handlers': {
                'hospital_text': '''
*विश्वविद्यालय क्लिनिक BFU। नाम: I. Kant*  

*पता*: 236041, रूस, कालिनिनग्राद, 9 अप्रैल सड़क, 60  
*संपर्क*: +7 (4012) 31-33-39 kdc@kantiana.ru  
'''
            },

            'language_chack_handlers': {
                'grammar_handlers': {
                    'language_grammar_handler': '''
                                            *अनुवाद विकल्प चुनें*:
                                            ''',
                    'translate_to_russian_handler': '''
                                            इस पाठ का रूसी भाषा में अनुवाद करें:
                                            ''',
                    'translate_from_russian_handler': '''
                                            इस पाठ का रूसी भाषा से अपने में अनुवाद करें:
                                            ''',
                },

                'listening_handlers': {
                    'send_voice': 'पाठ सुनें और इसे रूसी में लिखने की कोशिश करें।',
                },

                'speaking_handlers': {
                    'topics': [
                        'आप अपने परिवार के बारे में थोड़ा बताएं।',
                        'क्या आपके पास कोई पालतू जानवर है?',
                        'आपको कौन से व्यंजन पसंद हैं?',
                        'आपका कमरा कैसा है, इसका वर्णन करें।',
                        'आपका पसंदीदा परिवहन का साधन कौन सा है?',
                        'आप अपना खाली समय कहां बिताना पसंद करते हैं?',
                        'आप अपने रविवार को कैसे बिताते हैं?',
                        'आपकी बचपन की सबसे जीवंत याद क्या है?',
                        'आप किस यात्रा पर जाना चाहेंगे?',
                        'कौन सी आदतें आपको उत्पादक बने रहने में मदद करती हैं?',
                        'आपका कल का दिन कैसे गुजरा?',
                        'आप क्या काम करते हैं और काम में आप क्या करते हैं?',
                        'आपका परिवार किस चीज़ का सपना देखता है?',
                        'पिछले हफ्ते आपके साथ क्या दिलचस्प हुआ?',
                        'आपका सबसे अच्छा दोस्त किस चीज़ में रुचि रखता है?',
                        'आपने जो आखिरी फिल्म देखी, उसके बारे में अपने अनुभव साझा करें।',
                        'आपने कालिनिनग्राद में पढ़ाई करने का फैसला क्यों किया?'
                    ],
                    'speaking_send': 'मैं तेरी कहानी का इंतजार कर रहा हूँ:',
                    'handle_voice_message': 'विश्लेषण का परिणाम:',
                }
            },

            'location_handlers': {
                'addresses_handler': 'केंद्र का चयन करें',
                'loc_1_handler': """
*प्रशासनिक भवन, ए.नेव्स्कोय सड़क, 14*

यहां स्थित हैं:
· दस्तावेज प्रबंधन (कक्ष 115)
· लेखा सेवा (कक्ष 212)
· अभिलेखागार (कक्ष 221)
· आय और कर लेखांकन के लिए गणना समूह (कक्ष 222)
· नकद काउंटर (दूसरी मंजिल)
· एक्वेरियम हॉल
· मैक्सिमम हॉल
· कैफेटेरिया (पहली मंजिल)
                                            """,

                'loc_2_handler': """
*कोर्पस №2, भौतिकी, गणित और सूचना प्रौद्योगिकी संस्थान («फिजмат»), अलेक्सांद्र नेवस्की स्ट्रीट, 14* 

यहाँ स्थित हैं: 
· विदेशी छात्रों के साथ कार्य करने वाला विभाग (कमरा 119) 
· वीज़ा-आव्रजन सहायता विभाग (कमरा 114) 
· भर्ती समिति (कमरा 116 और 117) 
· पुस्तकालय, कमरा 202 («पढ़ने का क्षेत्र») 
· IT अवसंरचना सेवा (कमरा 121) 
                                            """,

                'loc_3_handler': """
*कॉरपस संख्या 3, विश्वविद्यालय सड़क, 2*

यहाँ हैं:
· जीवित प्रणालियों का संस्थान
· मुख्य विश्वविद्यालय पुस्तकालय: वैज्ञानिक सदस्यता (कमरा 126), अध्ययन कक्ष (कमरा 115)
                                            """,

                'loc_4_handler': """
*कर्पस नंबर 4, चेरनिशेवस्कोवो स्ट्रीट, 56 («घड़ी वाला कर्पस»)*

यहाँ स्थित हैं:

· मानविकी संस्थान
· रूसी भाषा केंद्र (कमरा 01)
· सोवियत बचपन का संग्रहालय
                                            """,

                'loc_5_handler': """
*भवन संख्या 5, चेरनिशेव्स्कोगो स्ट्रीट, 56ए* 

यहाँ स्थित है: 
· शिक्षा संस्थान 
                                            """,

                'loc_6_handler': """
*कर्पस नंबर 6, अलेक्सांद्र नेवस्की स्ट्रीट, 14बी (शाइबा)*

यहां स्थित है:
· छात्रावासों का परिसर (कमरा 101)
· पाठ्येतर गतिविधियों का प्रबंधन
                                            """,

                'loc_7_handler': """
*कोर्पस नंबर 7, फ्रुन्ज़े स्ट्रीट, 6*

यहाँ हैं:
· शैक्षिक टेलीस्टूडियो
· विधि संस्थान
                                            """,

                'loc_8_handler': """
*कोर्पस नं 8, 9 अप्रैल रोड, 5* 

यहां स्थित है: 
· चिकित्सा पुस्तकालय 
                                            """,

                'loc_9_handler': """
*कॉर्पस नंबर 9, ए. नेव्स्कोय स्ट्रीट, 14 ('फोक')*

यहाँ स्थित है:
· जीवित स्वास्थ्य और खेल परिसर
                                            """,

                'loc_10_handler': """
*कॉर्पस नंबर 10, ए. नेव्स्की स्ट्रीट. 14 («स्वेचका»)*

यहाँ स्थित हैं:
· छात्रों के लिए सामाजिक-आर्थिक सहायता केंद्र (कब. 14)
· करियर केंद्र
                                            """,

                'loc_11_handler': """
*बिल्डिंग नंबर 11, बोटकिन सेंट, 3*

यह यहाँ स्थित है:
· चिकित्सा में सिमुलेशन प्रशिक्षण और प्रत्यायन के लिए क्षेत्रीय संसाधन केंद्र

                                            """,

                'loc_12_handler': """
*कोर्पस नं १२, उल.बोटकिना, ४-६*

यहां स्थित है:
· मेडिकल इंस्टीट्यूट
                                            """,

                'loc_13_handler': """
*बिल्डिंग नंबर 13, बोटकिन सेंट, 4-6*

यह यहाँ स्थित है:
· विश्वविद्यालय क्लिनिक

                                            """,

                'loc_14_handler': """
*बिल्डिंग नंबर 14, अलेक्जेंडर नेवस्की सेंट, 14, बिल्डिंग 4*

यह यहाँ स्थित है:
· परिवहन सेवा समूह
· संपत्ति परिसर के संचालन के लिए प्रबंधन
· शासन आश्वासन के लिए विभाग
                                            """,

                'loc_19_handler': """
*बिल्डिंग नंबर 19, पियोनर्सकी, गांव रयबनोय, 23*

यह यहाँ स्थित है:
· शैक्षिक प्रथाओं का आधार
                                            """,

                'loc_20_handler': """
*बिल्डिंग नंबर 20, स्वेतलोगोर्स्क, कैलिनिंग्रैडस्की प्रॉस्पेक्ट, 102*

यह यहाँ स्थित है:
· शैक्षिक प्रथाओं का आधार

                                            """,

                'loc_21_handler': """
*बिल्डिंग नंबर 21, लेस्नाया स्ट्र । , 12*

यह यहाँ स्थित है:
· टनिकल गार्डन

                                            """,

                'loc_22_handler': """
*कॉर्पस नंबर 22, ए. नेव्स्की स्ट्रीट, 14*

यहाँ स्थित है:
· एकेडमिक-फिजिकल कॉम्प्लेक्स जिसमें स्विमिंग पूल है
                                            """,


                'loc_23_handler': """
*बिल्डिंग नंबर 23, दिमित्री डोंस्कॉय स्ट्र । , 27 के 1*

यह यहाँ स्थित है:
· चिकित्सा के उच्च विद्यालय के शैक्षिक और प्रयोगशाला भवन

                                            """,

                'loc_24_handler': """
*भवन संख्या 24, ज़ूलॉजिकल स्ट्रीट, 2*

यहाँ मौजूद हैं:
· यूनिवर्सिटी कॉलेज
                                            """,

                'loc_25_handler': """
*बिल्डिंग नंबर 25, 12 कोसोनावता पटसेवा सेंट । *

यहाँ हैं:
· ओएनके इंस्टीट्यूट ऑफ हाई टेक्नोलॉजीज
· साइबरफिजिकल सिस्टम के उच्च विद्यालय

                                            """,

                'loc_27_handler': """
*भवन संख्या 27, लेफ्टिनेंट जनरल ओज़ेरोव सड़क, 57*

यहां स्थित है:  
· इंजीनियरिंग-तकनीकी संस्थान  
· 'कांतियाना' एरेना  
                                            """,

                'loc_28_handler': """
*भवन संख्या 28, गोर्की सड़क, 23*

यहाँ स्थित हैं:
· अर्थशास्त्र और प्रबंधन संस्थान
                                            """,

                'loc_29_handler': """
*बिल्डिंग नंबर 29, 131 प्रोलेर्स्काया सेंट । *

वहाँ हैं:
· अनुप्रयुक्त सूचना विज्ञान और गणितीय भूभौतिकी के अनुसंधान संस्थान
                                            """,
        
                'loc_32_handler': """
*बिल्डिंग नंबर 32, 6 गेदरा सेंट । *

यहाँ हैं:
· फैबिका विज्ञान और प्रौद्योगिकी पार्क
                                            """,

                'loc_35_handler': """
*बिल्डिंग नंबर 35, अलेक्जेंडर नेवस्की सेंट, 14 बी*

यहाँ हैं:
· स्विमिंग पूल
                                            """,
            },

            'university_info_handlers': {
                'schedule_text': '''
*कक्षाओं का कार्यक्रम*:
                                            ''',
                'scholarship_text': '''
*छात्रवृत्तियों और वित्तीय सहायता की जानकारी*:
                                            ''',
                'office_contacts_text': '''
*संपर्क:* 

_पता_: 236041, कालनिनग्राद, अलेक्ज़ेंडर नेवस्की स्ट्रीट, 14 
_संपर्क फोन_: +7 (4012) 59-55-95 
_प्रवेश पत्रक कार्यालय_: अलेक्ज़ेंडर नेवस्की स्ट्रीट, 14 

8 (800) 600-52-39 कॉल मुफ्त है 
+7 (4012) 59-55-96 

_केनसिलरी_: +7 (4012) 59-55-97 
_ई-मेल_: post@kantiana.ru 

*प्रशासनिक सेवाओं का समय* 

सोमवार: 9:00 — 18:00 _ब्रेक_: 13:00—13:45 
मंगलवार: 9:00 — 18:00 _ब्रेक_: 13:00—13:45 
बुधवार: कोई प्रवेश नहीं (दस्तावेजों के साथ काम) 
गुरुवार: 9:00 — 18:00 _ब्रेक_: 13:00—13:45 
शुक्रवार: 9:00 — 16:45 _ब्रेक_: 13:00—13:45 
शनिवार और रविवार: छुट्टी के दिन
''',
                'visa_center_text': '''
*विज़ा-प्रवासन केंद्र*:

_पता_: 236041, रूस, कालिनिनग्राद, सड़कों ए. नेव्स्की 14, भवन 2, कक्ष 119

_काम करने के घंटे_: 
सोमवार — गुरुवार 9:00 से 18:00 तक, शुक्रवार 9:00 से 16:45 तक

_फोन_: +7 (4012) 31-33-99
_ईमेल_: international-study@kantiana.ru
'''
            },

            'sber_handlers': {
                'useful_links_text': """
🔗 स्बेर और भागीदारों के उपयोगी संसाधन:
• [नेटोलॉजी प्लेटफॉर्म](https://netology.ru/navigation) — ऑनलाइन पाठ्यक्रम और प्रोफेशन
• [शांत रहने की प्रैक्टिस](http://interview.sberstudent.ru/?utm_source=sber&utm_medium=internal&utm_campaign=salaryprojectmanagement) — साक्षात्कार के लिए ट्रेनर
• [स्कूल 21](https://sbergraduate.ru/careerofthefuture/) — मुफ्त आईटी शिक्षा
• [स्बेरसोवा](https://sbersova.ru/academy/courses/kibergramotnost?utm_source=event&utm_medium=free&utm_campaign=speaker) — शैक्षिक प्लेटफॉर्म
• [किब्रारी](https://sber.ru/kibrary) — डिजिटल पुस्तकालय
• [डिजिटल मैराथन](https://it-marathon.21-school.ru/?utm_source=ter_bank&utm_medium=referral&utm_campaign) — प्रतियोगिताएँ और चुनौतियाँ
• [स्बेर द्वारा स्टार्टअप](https://sberstudent.sberclass.ru/) — स्टार्टअप्स का समर्थन
• [इंटर्नशिप](https://sbergraduate.ru/practice/) — नौकरी के अवसर और इंटर्नशिप
""",

                'sber_card_text': """
💳 *Sber का कार्ड*
✨ *हमेशा के लिए मुफ्त सेवा*
💸 *पसंदीदा खरीदारी पर 5% कैशबैक*
📈 *संचय खाते पर ब्याज* *16%* वार्षिक तक
🎨 *Sber के अनोखे स्टिकर्स* हर लेनदेन के लिए — संग्रह करें और दोस्तों के साथ साझा करें!
🎯 *युवाओं के लिए विशेष प्रस्ताव* — मनोरंजन, शिक्षा और बहुत कुछ पर छूटविवरण के लिए *नीचे बटन* पर क्लिक करें:
""",

                'educational_loan_text': """
🎓 *शिक्षा ऋण स्बेर से* 
🎯 *सिर्फ 3% वार्षिक* 
📚 *शिक्षा के दौरान केवल ब्याज का भुगतान करें* 
👨‍🎓 *14 वर्ष की उम्र से आवेदन करें* 
⏳ *स्नातक होने के बाद 15 वर्ष की किस्तें* विवरण के लिए *नीचे बटन* पर क्लिक करें:
"""
            }
        }
    }
}
