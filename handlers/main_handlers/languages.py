TEXTS = {
    'ru': {
        'greetings': '''
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
        ''',
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
                'info': 'Информация',
                'location': 'Корпуса',
                'dormitory': 'Общежития',
                'hospital': 'Медцентр',
                'critical': 'SOS',
                'language_check': 'Тренажер',
                'back': 'Назад'
            },
            'critical_keyboard': {
                'police': 'Службы',
                'hotline': 'Горячая линия ФМС',
                'government': 'Местные органы власти',
                'consulate': 'Консульство',
                'back': 'Назад'
            },
            'dormitory_keyboard': {
                'check-in': 'Заселение в общежитие',
                'payment': 'Оплата',
                'address': 'Адреса общежитий',
                'rules': 'Правила проживания',
                'laundry': 'Прачечная',
                'no_certificate': 'Нет сертификата прививок или флюорографии',
                'back': 'Назад'
            },
            'dormitory_location_keyboard': {
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
                'back': 'Назад'
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
                'loc_12': '🩺 Мединститут',
                'loc_22': '🏊‍♂️ Бассейн',
                'loc_24': '🎓 Колледж',
                'loc_27': '⚙️ ИТИ',
                'loc_28': '💸 Экономика',
                'back': 'Назад'
            },
            'university_info_keyboard': {
                'schedule': 'Расписание',
                'scholarship': 'Стипендии',
                'office_contacts': 'Контакты учебного офиса',
                'visa_canter': 'Визово-миграционный центр',
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
*Электронное обращение доступно по ссылке*:
https://letters.gov.spb.ru/reception/form/?agency=1de5085ac50e44028bb31f2b97ac0fe2

*Личный прием граждан*
Личный прием граждан в Комитете проводится председателем Комитета или его первым заместителем, руководителями структурных подразделений и уполномоченными на то лицами. Информация о месте приема, а также об установленных для приема днях и часах доводится до сведения граждан.
При личном приеме гражданин предъявляет документ, удостоверяющий его личность.
Содержание устного обращения заносится в карточку личного приема гражданина. В случае, если изложенные в устном обращении факты и обстоятельства являются очевидными и не требуют дополнительной проверки, ответ на обращение с согласия гражданина может быть дан устно в ходе личного приема, о чем делается запись в карточке личного приема гражданина. В остальных случаях дается письменный ответ по существу поставленных в обращении вопросов.
Письменное обращение, принятое в ходе личного приема, подлежит регистрации и рассмотрению в порядке, установленном для письменных обращений.
В случае, если в обращении содержатся вопросы, решение которых не входит в компетенцию Комитета по межнациональным отношениям и реализации миграционной политики в Санкт‑Петербурге, гражданину дается разъяснение, куда и в каком порядке ему следует обратиться.
В ходе личного приема гражданину может быть отказано в дальнейшем рассмотрении обращения, если ему ранее был дан ответ по существу поставленных в обращении вопросов.

Предварительная запись на личный прием осуществляется по телефону приемной Комитета: 576-28-08, ежедневно с 9.00 до 18.00, в пятницу до 17.00, перерыв: с 13.00 до 14.00; суббота, воскресенье – выходные.
                                                    ''',

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
Для оформления места в общежитии 🏠 важно заранее подготовить необходимые документы 📋 и ознакомиться с процедурой подачи заявления 📝. Ознакомьтесь с подробной инструкцией ниже 👇:
                                            """,

                'payment_text': """
Оплатить общежитие можно двумя путями.

1. Лично. 

В кабинет № 222 административного корпуса, 2 этаж. Здесь ты получишь квитанцию для оплаты в кассе на том же этаже. Оплатить через кассу можно наличными в рублях или банковской картой.

2. Удаленно на сайте.

Первокурсники оплачивают при заселении полностью первый семестр. Далее осенний семестр оплачивается до 15 сентября, а весенний – до 15 февраля.
                                            """,

                'rules_text': """
- Содержи комнату и кухню в чистоте самостоятельно.
- Заводить домашних животных запрещено.
- Уважай соседей: соблюдай тишину с 23:00 до 08:00, будь вежлив и внимателен.
- До 22:00 можешь приглашать гостей, но ночная гостевая стоянка исключена.
- Курение и употребление алкоголя на территории университета категорически запрещено.
- Тщательно изучи технику безопасности, узнай расположение ближайших эвакуационных выходов.
- При неисправности оборудования немедленно уведомляй коменданта.
- Свяжись с администрацией общежития по любым вопросам проживания.
- Не осуществляй переезд в другую комнату без одобрения Центра социальной поддержки студентов.

_Не все общежития оснащены посудой, но еженедельно предоставляется свежее постельное бельё._

*Совет*: знакомься с комендантом сразу после вселения — он твой главный помощник в вопросах быта.
""",


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
                                                
1. *Если у вас отсутствует свежая флюорография*
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

2. *Если у вас отсутствуют сертификаты о прививках*

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

*Медицинское страхование*:
https://kantiana.ru/international/inostrannomu-studentu/oms/

*Инструкция по прикреплению к поликлинике*: 
https://kantiana.ru/students/polyclinic/

*Клиника на карте*:
https://2gis.ru/kaliningrad/search/236041%2C%20%D0%A0%D0%BE%D1%81%D1%81%D0%B8%D1%8F%2C%20%D0%9A%D0%B0%D0%BB%D0%B8%D0%BD%D0%B8%D0%BD%D0%B3%D1%80%D0%B0%D0%B4%2C%20%D1%83%D0%BB.%209%20%D0%B0%D0%BF%D1%80%D0%B5%D0%BB%D1%8F%2C%2060/firm/70000001006212174/20.524707%2C54.71579?m=20.524833%2C54.715617%2F19.07
                                            '''
            },

            'language_chack_handlers': {
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

*Локация*: https://goo.gl/maps/zRT7KcqxLXtAVaUE7
                                            """,

                'loc_2_handler': """
*Корпус №2, Институт физики, математики и информационных технологий («Физмат»), ул. А.Невского, 14*

Здесь находятся:
· Отдел по работе с иностранными обучающимися (каб. 119)
· Сектор визово-миграционной поддержки (каб. 114)
· Приемная комиссия (каб. 116 и 117)
· Библиотека, кабинет 202 («Читальный зал»)
· Служба обслуживания IT-инфраструктуры (каб. 121)

*Локация*: https://goo.gl/maps/6yt18jT8DoS5KgQv5
                                            """,
                                            
                'loc_3_handler': """
*Корпус №3, ул. Университетская, 2*
                                                    
Здесь находятся:
· Институт живых систем
· Главная университетская библиотека: научный абонемент (каб. 126), читальный зал (каб. 115)

*Локация*: https://goo.gl/maps/y2XnUi5vj5MxbRPeA
                                            """,

                'loc_4_handler': """
*Корпус №4, ул. Чернышевского, 56 («Корпус с часами»)*
                                                    
Здесь находятся:
· Институт гуманитарных наук
· Центр русского языка (каб. 01)
· Музей советского детства

*Локация*: https://goo.gl/maps/EBrY5H86euoPi6Sn9
                                            """,

                'loc_5_handler': """
*Корпус №5, ул. Чернышевского, 56а*
                                                    
Здесь находится:
· Институт образования

*Локация*: https://goo.gl/maps/xgHnL2PJ7ASXTFGG6
                                            """,

                'loc_6_handler': """
*Корпус №6, ул. А. Невского, 14б («Шайба»)*
                                                    
Здесь находятся:
· Комплекс студенческих общежитий (каб. 101)
· Управление внеучебной деятельности
*Локация *: https: // maps.app.goo.gl / pKu1EREgTPvJ6VGN7
                                            """,

                'loc_7_handler': """
*Корпус №7, ул. Фрунзе, 6*
                                                    
Здесь находятся:
· Учебная телестудия
· Юридический институт

*Локация*: https://goo.gl/maps/39LxmNSyZdSjnme16
                                            """,

                'loc_8_handler': """
*Корпус №8, ул. 9 Апреля, 5*
                                                    
Здесь находится:
· Медицинская библиотека

*Локация*: https://goo.gl/maps/Tja71g7t1QPRqtbt7
                                            """,

                'loc_9_handler': """
*Корпус №9, ул. А.Невского,14 («ФОК»)*
                                                    
Здесь находится:
· Физкультурно-оздоровительный комплекс

*Локация*: https://g.page/kantiana-sport?share
                                            """,

                'loc_10_handler': """
*Корпус №10, ул. А. Невского. 14 («Свечка»)*
                                                    
Здесь находятся:
· Центр социально-экономической поддержки студентов (каб. 14)
· Центр карьеры

*Локация*: https://goo.gl/maps/djfHWwTNer12z7caA
                                            """,

                'loc_12_handler': """
*Корпус №12, ул.Боткина, 4-6*
                                                    
Здесь находится:
· Медицинский институт

*Локация*: https://goo.gl/maps/BKJMV9WAR9G6PpaJ6
                                            """,

                'loc_22_handler': """
*Корпус №22, ул. А.Невского,14*
                                                    
Здесь находится:
· Учебно-физкультурный комплекс с бассейном

*Локация*: https://goo.gl/maps/VevnRkQyv8FmZPXcA
                                            """,

                'loc_24_handler': """
*Корпус №24, ул. Зоологическая, 2*
                                                    
Здесь находятся:
· Университетский колледж

*Локация*: https://goo.gl/maps/Fb76GxbTCQUm3zEa7
                                            """,

                'loc_27_handler': """
*Корпус №27, ул. Генерала-лейтенанта Озерова, 57*
                                                    
Здесь находятся:
· Инженерно-технический институт
· Арена «Кантиана»

*Локация*: https://goo.gl/maps/H126DeMnucPJvA1U9
                                            """,

                'loc_28_handler': """
*Корпус №28, ул. Горького, 23*
                                                    
Здесь находятся:
· Институт экономики и менеджмента

*Локация*: https://goo.gl/maps/THR3WG17cF2EBtvW6
                                            """, 
            },

            'university_info_handlers': {
                'schedule_text': '''
*Расписание занятий*:
https://schedule.kantiana.ru/
                                            ''',
                'scholarship_text': '''
*Информация о стипендиях и материальной помощи*:
https://kantiana.ru/students/scholarship/
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

Понедельник: 9:00 — 18:00    _перерыв_: 13:00—13:45

Вторник: 9:00 — 18:00        _перерыв_: 13:00—13:45

Среда: неприемный день (работа с документами)

Четверг: 9:00 — 18:00        _перерыв_: 13:00—13:45

Пятница: 9:00 — 16:45        _перерыв_: 13:00—13:45

Суббота и воскресенье: выходные дни
''',
                'visa_center_text': '''
*Визово-миграционный центр*:
https://kantiana.ru/universitys/administration/mezhdunarodnyy-ofis/

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
                'back': 'Back'
            },
            'critical_keyboard': {
                'police': 'Emergency',
                'hotline': 'FMS hotline',
                'government': 'Local authorities',
                'consulate': 'Consulate',
                'back': 'Back'
            },
            'dormitory_keyboard': {
                'check-in': 'Dormitory check-in',
                'payment': 'Payment',
                'address': 'Dormitory addresses',
                'rules': 'Dormitory rules',
                'laundry': 'Laundry',
                'no_certificate': 'No vaccination certificate or fluorography',
                'dormitory_1': 'Sommera',
                'dormitory_2': 'Chernyshevskogo',
                'dormitory_3': 'A. Nevskogo',
                'dormitory_4': 'A. Nevskogo',
                'dormitory_5': 'Tchaikovskogo',
                'dormitory_6': 'Azovskaya',
                'dormitory_7': 'Yelovaya',
                'dormitory_8': 'Yelovaya',
                'dormitory_9': 'Yubileynaya',
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
                'loc_12': '🩺 Medical Institute',
                'loc_22': '🏊‍♂️ Swimming Pool',
                'loc_24': '🎓 College',
                'loc_27': '⚙️ ITI',
                'loc_28': '💸 Economics',
                'back': 'Back'
            },
            'university_info_keyboard': {
                'schedule': 'Schedule',
                'scholarship': 'Scholarship',
                'office_contacts': 'Educational Office contacts',
                'visa_canter': 'Visa and Migration Center',
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
*The electronic appeal is available here:*
https://letters.gov.spb.ru/reception/form/?agency=1de5085ac50e44028bb31f2b97ac0fe2

*Reception of Citizens*

The reception of citizens in the Committee is conducted by the Chairman of the Committee or his first deputy, 
heads of structural units, and authorized persons. Information about the place of reception, as well as the established days and hours for receptions, 
is communicated to the citizens.During the personal reception, the citizen presents a document verifying their identity.
The content of the oral appeal is recorded in the citizen's personal reception card. If the facts and circumstances presented in the oral appeal are obvious 
and do not require additional verification, a response to the appeal may be given orally during the personal reception with the citizen's consent, 
which is then noted in the citizen's personal reception card. In other cases, a written response is provided regarding the issues raised in the appeal.

A written appeal received during the personal reception is subject to registration and consideration in accordance with the procedures established for written appeals.
If there are questions in the appeal that are outside the competence of the Committee for Interethnic Relations and Migration Policy in St. Petersburg, 
the citizen is provided with clarification on where and in what order they should turn. During the personal reception, a citizen may be denied further 
consideration of the appeal if they have previously received a substantive response to the questions raised in the appeal. 

Preliminary registration for a personal reception is carried out by calling the Committee's reception office at 576-28-08, daily from 9:00 AM to 6:00 PM, 
on Fridays until 5:00 PM, with a break from 1:00 PM to 2:00 PM; Saturday and Sunday are days off.
                                                   ''',

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
You can find out more about check-in here (https://kantiana.ru/students/kampus/obshchezhitiya/zaselenie-v-obshchezhitie/).

*How to apply for a place in the dormitory?*

1. After your enrollment in the educational program, you must submit an application for a place on the website at https://vk.com/away.php?to=https%3A%2F%2Fkantiana.ru%2Fstudents%2Fdormitory%2F&cc_key=

_Please note that the number of places in the dormitory is limited._

2. If you received a notification in your email that the dormitory has been approved, it means that your application has been accepted, 
and now you are participating in the competition. You can track the status of your application in the group of the Student Dormitory Complex: [KSO group] https://vk.com/kso_bfu

3. When you see your name in the ranking, it means that you can obtain the 2 necessary permits for accommodation. 
We will explain them in detail below.

4. With the obtained permits, go to sign the contract at KSO (Nevsky St., 14/1, office 101).

5. After signing the contract and paying for accommodation, go to the head of the specified dormitory for check-in and instructions.Upon arrival, you need to sign the rental agreement.

Upon arrival, it is necessary to sign a lease agreement for accommodation in the student dormitory at the Center for Socio-Economic Support for Students, 
obtain a referral, and pay for the dormitory for the first semester. 

_You must bring your passport._ 

*Office hours of the Center for Socio-Economic Support for Students:* 

- Mon: 10:00 to 17:00 
- Tue: 10:00 to 17:00 
- Thu: 10:00 to 17:00 
- Fri: 10:00 to 16:45 

Lunch break from 13:00 to 14:00

*Address*: A. Nevsky St., 14, building 10, 1st floor, office 14.

*Medical Certificate*

To live in the dormitory, you must provide the dormitory manager with a certificate of passing the medical examination. 
To obtain such a certificate, you need to visit office 2 at the Clinical Diagnostic Center of the I.Kant Baltic Federal University (CDC).

*Bring with you:*
- passport
- vaccination certificate (a document indicating all vaccinations you have received throughout your life, specifically including certificates for vaccinations against measles, diphtheria, tetanus, and hepatitis B)
- a fluorography not older than 1 year
- 2 negative results of PCR tests for COVID-19 / admission to classes

_Documents must be in Russian or have a certified translation into Russian._

*Address* of the CDC of I.Kant BFU: (https://goo.gl/maps/bwq24xTh5P1EctiU8)
_If you do not have these certificates at the time of check-in, you must obtain them at your own expense at any clinic._
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
- Keep the room and kitchen clean by yourself.
- Keeping pets is prohibited.
- Respect your neighbors: maintain silence from 11:00 PM to 8:00 AM, be polite and attentive.
- You can invite guests until 10:00 PM, but overnight guest parking is excluded.
- Smoking and consuming alcohol on university premises is strictly prohibited.
- Carefully study the safety regulations and learn the location of the nearest emergency exits.
- Immediately notify the supervisor of any equipment malfunctions.
- Contact the dormitory administration for any housing questions.
- Do not move to another room without the approval of the Student Social Support Center.

_Not all dormitories are equipped with dishes, but fresh bed linen is provided weekly._

*Tip*: Get to know the supervisor right after moving in – he is your main helper in domestic matters.
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

✨ Everything is organized for your convenience — please use it carefully!
                                            """,

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
*Contacts*: +7 (4012) 31-33-39 kdc@kantiana.ru

*Medical Insurance*: 
https://kantiana.ru/international/inostrannomu-studentu/oms/

*Instruction for attaching to the polyclinic*: 
https://kantiana.ru/students/polyclinic/

*Clinic on the map*:
https://2gis.ru/kaliningrad/search/236041%2C%20%D0%A0%D0%BE%D1%81%D1%81%D0%B8%D1%8F%2C%20%D0%9A%D0%B0%D0%BB%D0%B8%D0%BD%D0%B8%D0%BD%D0%B3%D1%80%D0%B0%D0%B4%2C%20%D1%83%D0%BB.%209%20%D0%B0%D0%BF%D1%80%D0%B5%D0%BB%D1%8F%2C%2060/firm/70000001006212174/20.524707%2C54.71579?m=20.524833%2C54.715617%2F19.07
                                            '''
            },

            'language_chack_handlers': {
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

*Location*: https://goo.gl/maps/zRT7KcqxLXtAVaUE7
                                            """,

                'loc_2_handler': """
*Building No. 2, Institute of Physics, Mathematics and Information Technologies, A. Nevsky St., 14*

Here are located:
· Department for Foreign Students (room 119)
· Visa and Migration Support Sector (room 114)
· Admissions Office (rooms 116 and 117)
· Library, room 202 ("Reading Room")
· IT Infrastructure Service (room 121)

*Location*: https://goo.gl/maps/6yt18jT8DoS5KgQv5
                                            """,
                                            
                'loc_3_handler': """
*Building No. 3, Universitetskaya St., 2*

Here you can find:
· Institute of Living Systems
· Main University Library: Scientific subscription (room 126), reading room (room 115)

*Location*: https://goo.gl/maps/y2XnUi5vj5MxbRPeA
                                            """,

                'loc_4_handler': """
*Building No. 4, Chernyshevsky Street, 56 (‘The Building with the Clock’)*

Here are located:
· Institute of Humanities
· Center for the Russian Language (room 01)
· Museum of Soviet Childhood

*Location*: https://goo.gl/maps/EBrY5H86euoPi6Sn9
                                            """,

                'loc_5_handler': """
*Building No. 5, 56a Chernyshevskogo Street*  

Here is located:  
· Institute of Education  

*Location*: https://goo.gl/maps/xgHnL2PJ7ASXTFGG6
                                            """,

                'loc_6_handler': """
*Building No. 6, A. Nevsky St., 14b ('Shaiba')*

Here are located:
· Complex of student dormitories (room 101)
· Office of extracurricular activities

*Location*: https://maps.app.goo.gl/pKu1EREgTPvJ6VGN7
                                            """,

                'loc_7_handler': """
*Building No. 7, Frunze St., 6* 

Here you can find: 
· Educational Television Studio 
· Law Institute 

*Location*: https://goo.gl/maps/39LxmNSyZdSjnme16
                                            """,

                'loc_8_handler': """
*Building No. 8, 9 April Street, 5*

Here is located:
· Medical Library

*Location*: https://goo.gl/maps/Tja71g7t1QPRqtbt7
                                            """,

                'loc_9_handler': """
*Building No. 9, A. Nevsky Street, 14 ('FOK')* 

Here is located: 
· Physical Culture and Health Complex 

*Location*: https://g.page/kantiana-sport?share
                                            """,

                'loc_10_handler': """
*Building No. 10, A. Nevsky St. 14 (“Candle”)*

Here are located:
· Center for Socio-Economic Support of Students (room 14)
· Career Center

*Location*: https://goo.gl/maps/djfHWwTNer12z7caA
                                            """,

                'loc_12_handler': """
*Building No. 12, Botkin Street, 4-6* 

Here is located: 
· Medical Institute 

*Location*: https://goo.gl/maps/BKJMV9WAR9G6PpaJ6
                                            """,

                'loc_22_handler': """
*Building No. 22, A. Nevsky St., 14* 

Here is located: 
· Educational and Sports Complex with a swimming pool 

*Location*: https://goo.gl/maps/VevnRkQyv8FmZPXcA
                                            """,

                'loc_24_handler': """
*Building No. 24, Zoologicheskaya St., 2*  

Here you can find:  
· University College  

*Location*: https://goo.gl/maps/Fb76GxbTCQUm3zEa7
                                            """,

                'loc_27_handler': """
*Building No. 27, Gen. Lt. Ozerov St., 57* 

Here are located:  
· Engineering and Technical Institute  
· «Kantiana» Arena  

*Location*: https://goo.gl/maps/H126DeMnucPJvA1U9
                                            """,

                'loc_28_handler': """
*Building No. 28, Gorky Street, 23*

Here are located:
· Institute of Economics and Management

*Location*: https://goo.gl/maps/THR3WG17cF2EBtvW6
                                            """, 
            },

            'university_info_handlers': {
                'schedule_text': '''
*Class schedule*:
https://schedule.kantiana.ru/
                                            ''',
                'scholarship_text': '''
*Information about scholarships and financial aid*:
https://kantiana.ru/students/scholarship/
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
https://kantiana.ru/universitys/administration/mezhdunarodnyy-ofis/

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
                'dormitory': 'Résidences universitaires',
                'hospital': 'Centre médical',
                'critical': 'SOS',
                'language_check': 'Coach',
                'back': 'Retour'
            },
            'critical_keyboard': {
                'police': 'Urgence',
                'hotline': 'Ligne directe de la FMS (USCIS)',
                'government': 'Autorités locales',
                'consulate': 'Consulat',
                'back': 'Retour'
            },
            'dormitory_keyboard': {
                'check-in': 'Installation dans le dortoir',
                'payment': 'Paiement',
                'address': 'Adresses des résidences estudiantines',
                'rules': 'Règles de vie',
                'laundry': 'Buanderie',
                'no_certificate': 'Pas de certificat de vaccination ou de radiographie des poumons.',
                'dormitory_1': 'Sommera',
                'dormitory_2': 'Tchernychevskogo',
                'dormitory_3': 'A. Nevskogo',
                'dormitory_4': 'A. Nevskogo',
                'dormitory_5': 'Tchaïkovskogo',
                'dormitory_6': 'Azovskaya',
                'dormitory_7': 'Yelovaya',
                'dormitory_8': 'Yelovaya',
                'dormitory_9': 'Yubileynaya',
                'sber_payment': 'Payer dans Sber',
                'back': 'Retour'
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
                'loc_12': '🩺 Institut médical',
                'loc_22': '🏊‍♂️ Piscine',
                'loc_24': '🎓 Collège',
                'loc_27': '⚙️ ITI',
                'loc_28': '💸 Économie',
                'back': 'Retour'
            },
            'university_info_keyboard': {
                'schedule': 'Horaires',
                'scholarship': 'Bourses',
                'office_contacts': 'Contacts du bureau académique',
                'visa_canter': 'Centre de visa et de migration',
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

📞 *Téléphone* :
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
*La demande électronique est disponible au lien*:
https://letters.gov.spb.ru/reception/form/?agency=1de5085ac50e44028bb31f2b97ac0fe2

*Réception des citoyens en personne*
La réception des citoyens au Comité est effectuée par le président du Comité ou son premier adjoint, les responsables des départements et les personnes autorisées à cet effet. 
L'information concernant le lieu de la réception, ainsi que les jours et heures fixés pour la réception, est portée à la connaissance des citoyens.
Lors de la réception en personne, le citoyen présente un document prouvant son identité.Le contenu de la demande orale est consigné dans une fiche de réception personnelle du citoyen. 
Dans le cas où les faits et circonstances exposés dans la demande orale sont évidents et ne nécessitent pas de vérification supplémentaire, la réponse à la demande, 
avec l'accord du citoyen, peut être donnée oralement lors de la réception, et cela est noté dans la fiche de réception personnelle du citoyen. 
Dans les autres cas, une réponse écrite est fournie sur le fond des questions posées dans la demande. Une demande écrite, reçue lors d'une audience personnelle, 
doit être enregistrée et examinée conformément à la procédure établie pour les demandes écrites. 
Si la demande contient des questions dont la résolution ne relève pas de la compétence du Comité des relations interethniques et de la mise en œuvre de la politique migratoire à Saint-Pétersbourg, 
le citoyen reçoit des explications sur où et selon quelle procédure il doit s'adresser. Lors de l'audience personnelle, il peut être refusé au citoyen une nouvelle considération de sa demande, 
s'il a déjà reçu une réponse sur le fond des questions soulevées dans sa demande. 

L'enregistrement préalable pour une audience personnelle se fait par téléphone au secrétariat du Comité : 576-28-08, 
tous les jours de 9h00 à 18h00, le vendredi jusqu'à 17h00, pause : de 13h00 à 14h00 ; le samedi et le dimanche – week-end.
                                                    ''',

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

                'rules_text': """
- Garde la chambre et la cuisine propres par toi-même.
- Il est interdit d'avoir des animaux domestiques.
- Respecte les voisins : fais silence de 23h00 à 08h00, sois poli et attentif.
- Avant 22h00, tu peux inviter des amis, mais les visites nocturnes sont exclues.
- Fumer et consommer de l'alcool sur le territoire de l'université est formellement interdit.
- Étudie attentivement la sécurité, renseigne-toi sur l'emplacement des sorties de secours les plus proches.
- En cas de panne d'équipement, informe immédiatement le surveillant.
- Contacte l'administration de la résidence pour toutes questions concernant le logement.
- Ne fais pas de déménagement dans une autre chambre sans l'approbation du Centre de soutien social aux étudiants.

_Toutes les résidences ne sont pas équipées de vaisselle, mais des draps propres sont fournis chaque semaine._

*Conseil* : fais connaissance avec le surveillant dès ton arrivée — c'est ton principal aide pour les questions de la vie quotidienne.
""",


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
*Contacts*: +7 (4012) 31-33-39 kdc@kantiana.ru

*Assurance maladie*: 
https://kantiana.ru/international/inostrannomu-studentu/oms/

*Instruction pour l'affiliation à la polyclinique*: 
https://kantiana.ru/students/polyclinic/

*Clinique sur la carte*: 
https://2gis.ru/kaliningrad/search/236041%2C%20Russie%2C%20Kaliningrad%2C%20rue%209%20avril%2C%2060/firm/70000001006212174/20.524707%2C54.71579?m=20.524833%2C54.715617%2F19.07                                            '''
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

*Emplacement :* https://goo.gl/maps/zRT7KcqxLXtAVaUE7
                                            """,

                'loc_2_handler': """
*Bâtiment n°2, Institut de physique, de mathématiques et de technologies de l'information (« Fizmat »), rue A. Nevski, 14*

Ici se trouvent :
· Le bureau des relations avec les étudiants étrangers (cab. 119)
· Le secteur de l'assistance à la visa et à la migration (cab. 114)
· Le bureau des admissions (cab. 116 et 117)
· La bibliothèque, salle 202 (« Salle de lecture »)
· Le service de maintenance de l'infrastructure IT (cab. 121)

*Localisation* : https://goo.gl/maps/6yt18jT8DoS5KgQv5
                                            """,
                                            
                'loc_3_handler': """
*Bâtiment n°3, rue Universitaire, 2*

Ici se trouvent :
· Institut des systèmes vivants
· Bibliothèque universitaire principale : abonnement scientifique (cab. 126), salle de lecture (cab. 115)

*Localisation* : https://goo.gl/maps/y2XnUi5vj5MxbRPeA
                                            """,

                'loc_4_handler': """
*Bâtiment n°4, rue Tchernychevski, 56 («Bâtiment avec l'horloge»)*

Ici se trouvent :
· Institut des sciences humaines
· Centre de la langue russe (cab. 01)
· Musée de l'enfance soviétique

*Localisation*: https://goo.gl/maps/EBrY5H86euoPi6Sn9
                                            """,

                'loc_5_handler': """
*Bâtiment n°5, rue Tchernychevski, 56a*

Ici se trouve :
· Institut de formation

*Localisation* : https://goo.gl/maps/xgHnL2PJ7ASXTFGG6
                                            """,

                'loc_6_handler': """
*Bâtiment n°6, rue A. Nevski, 14b («Shaïba»)*

Ici se trouvent :
· Complexe de résidences étudiantes (cab. 101)
· Gestion des activités parascolaires

*Localisation* : https://maps.app.goo.gl/pKu1EREgTPvJ6VGN7
                                            """,

                'loc_7_handler': """
*Bâtiment n° 7, rue Frunze, 6* 

Ici se trouvent :  
· Studio télévisé éducatif  
· Institut de droit  

*Localisation* : https://goo.gl/maps/39LxmNSyZdSjnme16
                                            """,

                'loc_8_handler': """
*Bâtiment n°8, rue 9 Avril, 5*

Ici se trouve :
· Bibliothèque médicale

*Localisation* : https://goo.gl/maps/Tja71g7t1QPRqtbt7
                                            """,

                'loc_9_handler': """
*Bâtiment n°9, rue A. Nevsky, 14 («FOC»)*

Ici se trouve :
· Complexe sportif et de bien-être

*Location* : https://g.page/kantiana-sport?share
                                            """,

                'loc_10_handler': """
*Bâtiment n°10, rue A. Nievsky. 14 («Bougie»)*

Ici se trouve :
· Centre de soutien socio-économique aux étudiants (cab. 14)
· Centre de carrière

*Emplacement* : https://goo.gl/maps/djfHWwTNer12z7caA
                                            """,

                'loc_12_handler': """
*Bâtiment n°12, rue Botkina, 4-6* 

Ici se trouve : 
· Institut médical 

*Localisation* : https://goo.gl/maps/BKJMV9WAR9G6PpaJ6
                                            """,

                'loc_22_handler': """
*Bâtiment n° 22, rue A. Nevski, 14* 

Ici se trouve : 
· Complexe sportif et éducatif avec piscine 

*Emplacement* : https://goo.gl/maps/VevnRkQyv8FmZPXcA
                                            """,

                'loc_24_handler': """
*Bâtiment n°24, rue Zoologique, 2* 

Voici où se trouve : 
· Collège universitaire 

*Localisation*: https://goo.gl/maps/Fb76GxbTCQUm3zEa7
                                            """,

                'loc_27_handler': """
*Bâtiment n°27, rue du général-lieutenant Ozerov, 57*

Ici se trouvent :
· Institut d'ingénierie et de technologie
· Arène "Kantiana"

*Localisation*: https://goo.gl/maps/H126DeMnucPJvA1U9
                                            """,

                'loc_28_handler': """
*Bâtiment n°28, rue Gorki, 23*

Ici se trouvent :
· Institut d'économie et de gestion

*Localisation*: https://goo.gl/maps/THR3WG17cF2EBtvW6
                                            """, 
            },

            'university_info_handlers': {
                'schedule_text': '''
*Emploi du temps des cours*:
https://schedule.kantiana.ru/
                                            ''',
                'scholarship_text': '''
*Information sur les bourses et l'aide matérielle*:
https://kantiana.ru/students/scholarship/
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
https://kantiana.ru/universitys/administration/mezhdunarodnyy-ofis/*Contacts*

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
                'dormitory': 'Residencias estudiantiles',
                'hospital': 'Centro médico',
                'critical': 'SOS',
                'language_check': 'Entrenador',
                'back': 'Atrás'
            },
            'critical_keyboard': {
                'police': 'Urgencia',
                'hotline': 'Línea directa de la FMS (Ministerio de Inclusión, Seguridad Social y Migraciones)',
                'government': 'Autoridades locales',
                'consulate': 'Consulado',
                'back': 'Atrás'
            },
            'dormitory_keyboard': {
                'check-in': 'Alojamiento en un dormitorio',
                'payment': 'Pago',
                'address': 'Direcciones de los dormitorios',
                'rules': 'Reglas de convivencia',
                'laundry': 'Lavandería',
                'no_certificate': 'No hay un certificado de vacunas o de fluorografía',
                'back': 'Atrás'
            },
            'dormitory_location_keyboard': {
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
                'loc_12': '🩺 Instituto de Medicina',
                'loc_22': '🏊‍♂️ Piscina',
                'loc_24': '🎓 Colegio',
                'loc_27': '⚙️ ITI',
                'loc_28': '💸 Economía',
                'back': 'Atrás'
            },
            'university_info_keyboard': {
                'schedule': 'Horarios',
                'scholarship': 'Becas',
                'office_contacts': 'Contactos de la oficina de estudios',
                'visa_canter': 'Centro de visas y migración',
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
*La solicitud electrónica está disponible en el enlace*: 
https://letters.gov.spb.ru/reception/form/?agency=1de5085ac50e44028bb31f2b97ac0fe2

*Atención personal al ciudadano* 

La atención personal al ciudadano en el Comité es llevada a cabo por el presidente del Comité o su primer adjunto, 
por los directores de las divisiones estructurales y por las personas autorizadas para ello. 
La información sobre el lugar de atención, así como sobre los días y horas establecidos para la atención, 
se comunica a los ciudadanos. Durante la atención personal, el ciudadano presenta un documento que acredita su identidad. 
El contenido de la solicitud oral se registra en la tarjeta de atención personal del ciudadano. 
En caso de que los hechos y circunstancias expuestos en la solicitud oral sean evidentes y no requieran verificación adicional, 
la respuesta a la solicitud, con el consentimiento del ciudadano, puede ser dada oralmente durante la atención personal, 
lo que se registra en la tarjeta de atención personal del ciudadano. En los demás casos, 
se proporciona una respuesta por escrito sobre el fondo de las cuestiones planteadas en la solicitud. 
La solicitud por escrito, recibida durante la atención personal, 
debe ser registrada y considerada de acuerdo con el procedimiento establecido para las solicitudes por escrito.
En caso de que la solicitud contenga preguntas cuya resolución no esté dentro de la competencia 
del Comité de Relaciones Interétnicas y la Implementación de la Política Migratoria en San Petersburgo, 
se le dará al ciudadano una explicación de a dónde y en qué orden debe dirigirse.Durante la recepción personal, 
se le puede negar al ciudadano el ulterior examen de la solicitud, si ya se le ha dado una respuesta sobre el fondo 
de las preguntas planteadas en la solicitud.

La inscripción previa para la recepción personal se realiza por teléfono a la oficina del Comité: 576-28-08, diariamente de 9:00 a 18:00, los viernes hasta las 17:00, con un receso de 13:00 a 14:00; sábado y domingo – días no laborables.
                                                   ''',

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
- Mantén la habitación y la cocina limpias por tu cuenta.
- No se permite tener mascotas.
- Respeta a los vecinos: guarda silencio de 23:00 a 08:00, sé educado y atento.
- Hasta las 22:00 puedes invitar a amigos, pero no se permite el alojamiento nocturno de invitados.
- Fumar y consumir alcohol en el recinto de la universidad está estrictamente prohibido.
- Estudia cuidadosamente las normas de seguridad y conoce la ubicación de las salidas de emergencia más cercanas.
- Ante cualquier fallo del equipo, informa de inmediato al conserje.
- Contacta con la administración de la residencia para cualquier pregunta sobre tu estancia.
- No te mudes a otra habitación sin la aprobación del Centro de Apoyo Social para Estudiantes.

_No todas las residencias están equipadas con utensilios de cocina, pero se proporciona ropa de cama limpia semanalmente._

*Consejo*: conéctate con el conserje inmediatamente después de mudarte; él es tu principal ayuda en cuestiones de convivencia.
""",


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
*Contactos*: +7 (4012) 31-33-39 kdc@kantiana.ru  

*Seguro médico*:  
https://kantiana.ru/international/inostrannomu-studentu/oms/  

*Instrucciones para registrarse en la clínica*:  
https://kantiana.ru/students/polyclinic/  

*Clínica en el mapa*:  
https://2gis.ru/kaliningrad/search/236041%2C%20%D0%A0%D0%BE%D1%81%D1%81%D0%B8%D1%8F%2C%20%D0%9A%D0%B0%D0%BB%D0%B8%D0%BD%D0%B8%D0%BD%D0%B3%D1%80%D0%B0%D0%B4%2C%20%D1%83%D0%BB.%209%20%D0%B0%D0%BF%D1%80%D0%B5%D0%BB%D1%8F%2C%2060/firm/70000001006212174/20.524707%2C54.71579?m=20.524833%2C54.715617%2F19.07
                                            '''
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
                                "Comparte tus impresiones de la última película que viste".
                                '¿Por qué decidiste estudiar en Kaliningrado?'
                            ],
                    'speaking_send': 'Espero tu historia sobre el tema:',
                    'handle_voice_message': 'Resultado del análisis:',
                },
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

*Ubicación*: https://goo.gl/maps/zRT7KcqxLXtAVaUE7
                                            """,

                'loc_2_handler': """
*Cuerpo Nº 2, Instituto de Física, Matemáticas y Tecnologías de la Información («Fizmat»), calle A. Nevsky, 14* 

Aquí se encuentran: 
· Departamento de trabajo con estudiantes extranjeros (oficina 119) 
· Sector de apoyo de visas y migración (oficina 114) 
· Comisión de admisión (oficinas 116 y 117) 
· Biblioteca, sala 202 («Sala de Lectura») 
· Servicio de atención a la infraestructura IT (oficina 121) 

*Ubicación*: https://goo.gl/maps/6yt18jT8DoS5KgQv5
                                            """,
                                            
                'loc_3_handler': """
*Cuerpo N° 3, calle Universitaria, 2*

Aquí se encuentran:
· Instituto de Sistemas Vivos
· Biblioteca universitaria principal: suscripción científica (of. 126), sala de lectura (of. 115)

*Ubicación*: https://goo.gl/maps/y2XnUi5vj5MxbRPeA
                                            """,

                'loc_4_handler': """
*Cuerpo N°4, calle Tchernyshevsky, 56 («Edificio con reloj»)*

Aquí se encuentran:
· Instituto de Ciencias Humanas
· Centro de la lengua rusa (oficina 01)
· Museo de la infancia soviética

*Ubicación*: https://goo.gl/maps/EBrY5H86euoPi6Sn9
                                            """,

                'loc_5_handler': """
*Cuerpo Nº5, calle Tchernyshevsky, 56a* 

Aquí se encuentra: 
· Instituto de Educación 

*Ubicación*: https://goo.gl/maps/xgHnL2PJ7ASXTFGG6
                                            """,

                'loc_6_handler': """
*Cuerpo No. 6, calle A. Nevski, 14b («Shaiba»)*

Aquí se encuentran:
· Complejo de residencias estudiantiles (cab. 101)
· Gestión de actividades extracurriculares

*Ubicación *: https://maps.app.goo.gl/pKu1EREgTPvJ6VGN7
                                            """,

                'loc_7_handler': """
*Cuerpo Nº7, calle Frunze, 6*

Aquí se encuentran:
· Estudio de teleeducación
· Instituto de Derecho

*Ubicación*: https://goo.gl/maps/39LxmNSyZdSjnme16
                                            """,

                'loc_8_handler': """
*Cuerpo Nº 8, calle 9 de abril, 5* 

Aquí se encuentra: 
· Biblioteca médica 

*Ubicación*: https://goo.gl/maps/Tja71g7t1QPRqtbt7
                                            """,

                'loc_9_handler': """
*Cuerpo N°9, calle A. Nevsky, 14 («FOK»)*

Aquí se encuentra:
· Complejo de educación física y salud

*Ubicación*: https://g.page/kantiana-sport?share
                                            """,

                'loc_10_handler': """
*Cuerpo #10, calle A. Nevski. 14 («Vela»)*

Aquí se encuentran:
· Centro de apoyo socioeconómico para estudiantes (cab. 14)
· Centro de carreras

*Ubicación*: https://goo.gl/maps/djfHWwTNer12z7caA
                                            """,

                'loc_12_handler': """
*Cuerpo Nº12, calle Botkina, 4-6*

Aquí se encuentra:
· Instituto Médico

*Ubicación*: https://goo.gl/maps/BKJMV9WAR9G6PpaJ6
                                            """,

                'loc_22_handler': """
*Cuerpo №22, calle A. Nevskogo, 14* 

Aquí se encuentra: 
· Complejo educativo y deportivo con piscina 

*Ubicación*: https://goo.gl/maps/VevnRkQyv8FmZPXcA
                                            """,

                'loc_24_handler': """
*Cuerpo nº 24, calle Zoológica, 2*

Aquí se encuentra:
· Colegio universitario

*Ubicación*: https://goo.gl/maps/Fb76GxbTCQUm3zEa7
                                            """,

                'loc_27_handler': """
*Cuerpo Nº 27, calle General-lieutenant Ozerov, 57*

Aquí se encuentran:
· Instituto de ingeniería y tecnología
· Arena «Kantiana»

*Ubicación*: https://goo.gl/maps/H126DeMnucPJvA1U9
                                            """,

                'loc_28_handler': """
*Cuerpo Nº28, calle Gorky, 23*

Aquí se encuentran:
· Instituto de Economía y Gestión

*Ubicación*: https://goo.gl/maps/THR3WG17cF2EBtvW6
                                            """, 
            },

            'university_info_handlers': {
                'schedule_text': '''
*Horario de clases*:
https://schedule.kantiana.ru/
                                            ''',
                'scholarship_text': '''
*Información sobre becas y ayuda financiera*:
https://kantiana.ru/students/scholarship/
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
https://kantiana.ru/universitys/administration/mezhdunarodnyy-ofis/

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
        },
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
                'language_check': '訓練器',
                'back': '回去'
            },
            'critical_keyboard': {
                'police': '緊急',
                'hotline': '熱線 FMS',
                'government': '地方當局',
                'consulate': '領事館',
                'back': '回去'
            },
            'dormitory_keyboard': {
                'check-in': '入住宿舍',
                'payment': '付款',
                'address': '宿舍地址',
                'rules': '居住規則',
                'laundry': '洗衣房',
                'no_certificate': '沒有疫苗接種證明或胸部X光檢查報告',
                'back': '回去'
            },
            'dormitory_location_keyboard': {
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
                'loc_12': '🩺 醫學院',
                'loc_22': '🏊‍♂️ 游泳池',
                'loc_24': '🎓 學院',
                'loc_27': '⚙️ ITI',
                'loc_28': '💸 經濟',
                'back': '回去'
            },
            'university_info_keyboard': {
                'schedule': '時刻表',
                'scholarship': '獎學金',
                'office_contacts': '聯絡學習辦公室',
                'visa_canter': '簽證移民中心',
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
*電子申請可通過以下鏈接訪問*:
https://letters.gov.spb.ru/reception/form/?agency=1de5085ac50e44028bb31f2b97ac0fe2

*公眾會見* 公共會見在委員會由委員會主席或其第一副主席、各結構部門的負責人及指定授權人員進行。
會見的地點以及指定的接待日和時間將通知市民。在面對面接見中，市民需出示證明其身份的文件。
口頭請求的內容將被記錄在市民會見的卡片上。如果口頭請求中陳述的事實和情況顯而易見且不需進一步核實，
則可在會見過程中經市民同意口頭答復請求，並在市民會見卡片上進行記錄。在其他情況下，將針對請求中提出的問題給予書面答復。
在面對面接見中接受的書面請求需按書面請求的程序進行登記和審查。
如果申請中包含的問題不在聖彼得堡民族關係與移民政策委員會的職責範圍內，則公民將被說明應該向哪裡以及以什麼方式進行申請。
在個人接待過程中，如果之前已經對申請中提出的問題給予了實質性的答覆，則可能會拒絕進一步考慮該申請。

個人接待的預約可以通過委員會的接待電話進行：576-28-08，每天從9:00到18:00，星期五至17:00，中午12:00至13:00為休息時間；星期六、星期天為休息日。
                                                    ''',

                'critical_consulate_handler': '''
*俄羅斯外交部在加里寧格勒的代表處* 🏛️

*地址*: 🏠
236022, 俄羅斯, 加里寧格勒市, 基羅夫街, 17號

*電話*: 📞
接待處: + 7 (401) 221-37-12
傳真: + 7 (401) 221-06-26
領事部: + 7 (401) 221-16-68
護照部: + 7 (401) 295-82-02
邀請函處: + 7 (4012) 21-59-28

*有關領事法律問題的公民接待時間* ⚖️
週一至週四: *9:00* 至 *17:00* （*12:00* 至 *14:00* 休息）
週五: *9:00* 至 *16:00* （*12:00* 至 *14:00* 休息）
週六至週日: 🚫 休息
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
- 請自行保持房間和廚房的清潔。
- 禁止飼養寵物。
- 尊重鄰居：請在23:00至08:00之間保持安靜，並保持禮貌和關心。
- 在22:00之前可以邀請客人，但禁止夜間的客人停留。
- 在校園內嚴禁吸煙和飲酒。
- 請仔細閱讀安全規則，了解最近的緊急出口位置。
- 如設備故障，請立即通知宿舍管理人。
- 如有任何住宿問題，請與宿舍管理部門聯繫。
- 未經學生社會支持中心的批准，不得搬遷至其他房間。

_並非所有宿舍都配備餐具，但每週會提供新鮮的床單。_

*建議*：在入住後立即與宿舍管理人熟識——他是您在生活事務上的主要幫手。
""",


                'laundry_text': """
🏢 *位置*：
每棟宿舍都有洗衣房。具體的位置和工作時間可以詢問管理員或夜班人員。

🧼 *使用規則*：
• 請攜帶自己的洗衣粉
• 使用專用的內衣袋
• *禁止* 洗鞋子（會損壞機器）
• 在使用前請參閱現場的說明書
• 在專用的設備房間內晾乾衣物

⏰ *重要！*
請在*確定的時間*內將鑰匙交還給夜班人員—其他學生也想洗自己的衣物！🙏

✨ 一切都是為了你的便利—請小心使用！                                            """,

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
*聯繫方式*: +7 (4012) 31-33-39 kdc@kantiana.ru  

*醫療保險*:  
https://kantiana.ru/international/inostrannomu-studentu/oms/  

*附加到診所的說明*:  
https://kantiana.ru/students/polyclinic/  

*診所地圖*:  
https://2gis.ru/kaliningrad/search/236041%2C%20%D0%A0%D0%BE%D1%81%D1%81%D0%B8%D1%8F%2C%20%D0%9A%D0%B0%D0%BB%D0%B8%D0%BD%D0%B8%D0%BD%D0%B3%D1%80%D0%B0%D0%B4%2C%20%D1%83%D0%BB.%209%20%D0%B0%D0%BF%D1%80%D0%B5%D0%BB%D1%8F%2C%2060/firm/70000001006212174/20.524707%2C54.71579?m=20.524833%2C54.715617%2F19.07                                            '''
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

*位置*: https://goo.gl/maps/zRT7KcqxLXtAVaUE7
                                            """,

                'loc_2_handler': """
*第二號樓，物理、數學與信息技術研究所（「菲茨」），阿·涅夫斯基街14號* 

這裡有：
· 外國學生工作部（119室）
· 簽證-移民支持部（114室）
· 招生辦公室（116和117室）
· 圖書館，202室（「閱覽室」）
· IT基礎設施服務部（121室）

*位置*: https://goo.gl/maps/6yt18jT8DoS5KgQv5
                                            """,
                                            
                'loc_3_handler': """
*第三號樓, 大學街 2 號*

這裡有：
· 生物系統研究所
· 主大學圖書館：科學訂閱（126室），閱覽室（115室）

*位置*: https://goo.gl/maps/y2XnUi5vj5MxbRPeA
                                            """,

                'loc_4_handler': """
*第四號樓, 切爾尼斯赫夫斯基街56號（“有鐘樓的建築”）*

這裡有：
· 人文科學院
· 俄語中心（01號辦公室）
· 蘇聯兒童博物館

*位置*: https://goo.gl/maps/EBrY5H86euoPi6Sn9
                                            """,

                'loc_5_handler': """
*第五大樓，切爾尼雪夫斯基街，56a*

這裡有：
· 教育研究所

*位置*：https://goo.gl/maps/xgHnL2PJ7ASXTFGG6
                                            """,

                'loc_6_handler': """
*第六號樓，阿. 涅夫斯基街，14b（“橡膠圓盤”）* 

這裡有：
· 學生宿舍綜合大樓（101室）
· 課外活動管理處

*位置*: https://maps.app.goo.gl/pKu1EREgTPvJ6VGN7
                                            """,

                'loc_7_handler': """
*第7號大樓，弗魯恩茨街6號* 

這裡有：
· 教學電視工作室
· 法律學院

*位置*: https://goo.gl/maps/39LxmNSyZdSjnme16
                                            """,

                'loc_8_handler': """
*第8號樓，4月9日街，5號* 

此處設有： 
· 醫學圖書館 

*位置*: https://goo.gl/maps/Tja71g7t1QPRqtbt7
                                            """,

                'loc_9_handler': """
*第9號大樓，A.涅夫斯基街14號（「FOK」）

*這裡有：
· 體育健身複合體

*位置*：https://g.page/kantiana-sport?share
                                            """,

                'loc_10_handler': """
*第10號樓, A. 內夫斯基街 14 號（“小蠟燭”）

*這裡有：
· 學生社會經濟支持中心（14室）
· 職業中心

*位置*: https://goo.gl/maps/djfHWwTNer12z7caA
                                            """,

                'loc_12_handler': """
*第12號樓，博特金街4-6號* 

此處有：
· 醫學院 

*位置*: https://goo.gl/maps/BKJMV9WAR9G6PpaJ6
                                            """,

                'loc_22_handler': """
*第22號大樓，A.涅夫斯基大街14號*

這裡有：
· 帶游泳池的體育訓練綜合體

*地點*：https://goo.gl/maps/VevnRkQyv8FmZPXcA
                                            """,

                'loc_24_handler': """
*第24號樓，動物學街2號* 

這裡有：
· 大學學院

*位置*: https://goo.gl/maps/Fb76GxbTCQUm3zEa7
                                            """,

                'loc_27_handler': """
*第27號建築，俄羅斯格涅拉爾-萊特南特奧捷羅夫街57號*

這裡有：
· 工程技術學院
·「康提亞那」體育館

*位置*: https://goo.gl/maps/H126DeMnucPJvA1U9
                                            """,

                'loc_28_handler': """
*第28號樓，戈爾基大街23號*

此處設有：
· 經濟與管理研究所

*位置*: https://goo.gl/maps/THR3WG17cF2EBtvW6
                                            """, 
            },

            'university_info_handlers': {
                'schedule_text': '''
*課程時間表*:
https://schedule.kantiana.ru/
                                            ''',
                'scholarship_text': '''
*獎學金和經濟援助信息*:
https://kantiana.ru/students/scholarship/
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
https://kantiana.ru/universitys/administration/mezhdunarodnyy-ofis/

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
                'language_check': 'व्यायाम मशीन',
                'back': 'पीछे'
            },
            'critical_keyboard': {
                'police': 'आपातकाल',
                'hotline': 'प्रवासन सेवा की हॉटलाइन',
                'government': 'स्थानीय सरकारी संस्थाएँ',
                'consulate': 'कांसुलीट',
                'back': 'पीछे'
            },
            'dormitory_keyboard': {
                'check-in': 'हॉस्टल में दाखिला',
                'payment': 'भुगतान',
                'address': 'होस्टल के पते',
                'rules': 'निवासी नियम',
                'laundry': 'धुलाई की जगह',
                'no_certificate': 'कोई टीकाकरण या फ्लोरोोग्राफी का प्रमाण पत्र नहीं है',
                'back': 'पीछे'
            },
            'dormitory_location_keyboard': {
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
                'loc_12': '🩺 मेडिकल इंस्टीट्यूट',
                'loc_22': '🏊‍♂️ स्विमिंग पूल',
                'loc_24': '🎓 कॉलेज',
                'loc_27': '⚙️ ITI',
                'loc_28': '💸 अर्थव्यवस्था',
                'back': 'पीछे'
            },
            'university_info_keyboard': {
                'schedule': 'अनुक्रमणिका',
                'scholarship': 'छात्रवृत्तियाँ',
                'office_contacts': 'शिक्षा कार्यालय के संपर्क',
                'visa_canter': 'विजा-आप्रवासन केंद्र',
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
            }
        },
        
        'handlers': {
            'critical_handlers': {
                'critical_police_handler': '''
🚨 *आपात संपर्क*

*आपातकालीन प्रतिक्रिया सेवाओं का एकल नंबर* (आग extinguishing, आपातकालीन सेवाएं, पुलिस, एम्बुलेंस, गैस सेवा)
📞 *112*

👨‍🚒 *अग्निशामक और बचावकर्ता*
📞 *01* (स्थानीय फोन से) | *101* (मोबाइल से)

👮 *पुलिस*
📞 *02* (स्थानीय फोन से) | *102* (मोबाइल से)

🏥 *एम्बुलेंस*
📞 *03* (स्थानीय फोन से) | *103* (मोबाइल से)

💡 इन नंबरों को जल्दी पहुँच में सुरक्षित करें!
                                                    ''',

                'critical_hotline_handler': '''
🚪 *वीज़ा-आप्रवासी सहायता विभाग*

📞 *फोन*:
+7 (4012) 595-595 (अगला 7454) — आप्रवासी पंजीकरण और वीज़ा
+7 (4012) 595-595 (अगला 7452) — वीज़ा निमंत्रण

🏢 *पता*:
रूस, शहर कलिनिनग्राद, ए. नेव्स्की स्ट्रीट, 14, कॉर्प. 2, कक्ष 114

🕒 *कार्यालय के घंटे*:

सोम 14:00–17:00
मंगल 10:00–13:00
गुरु 14:00–17:00
शुक्र 10:00–13:00

दोपहर का भोजन 13:00–14:00
                                                    ''',

                'critical_government_handler': '''
*इलेक्ट्रॉनिक अपील लिंक पर उपलब्ध है:*
https://letters.gov.spb.ru/reception/form/?agency=1de5085ac50e44028bb31f2b97ac0fe2

*नागरिकों की व्यक्तिगत सुनवाई* 

समिति में नागरिकों की व्यक्तिगत सुनवाई समिति के अध्यक्ष या उनके पहले उपाध्यक्ष, संरचनात्मक इकाइयों के नेताओं और अधिकृत व्यक्तियों द्वारा आयोजित की जाती है। 
सुनवाई के स्थान के बारे में, साथ ही सुनवाई के लिए निर्धारित दिनों और घंटों की जानकारी नागरिकों को दी जाती है। 
व्यक्तिगत सुनवाई के दौरान, नागरिक अपनी पहचान प्रमाणित करने वाला दस्तावेज प्रस्तुत करता है। 
मौखिक निवेदन की सामग्री नागरिक की व्यक्तिगत सुनवाई की पर्ची में दर्ज की जाती है। 
यदि मौखिक निवेदन में प्रस्तुत तथ्य और परिस्थितियाँ स्पष्ट हैं और अतिरिक्त जाँच की आवश्यकता नहीं है, तो नागरिक की सहमति से सुनवाई के दौरान मौखिक उत्तर दिया जा सकता है, 
जिसे नागरिक की व्यक्तिगत सुनवाई की पर्ची में दर्ज किया जाता है। अन्य मामलों में, निवेदन में उठाए गए प्रश्नों के विषय में लिखित उत्तर दिया जाता है। 
व्यक्तिगत सुनवाई के दौरान प्राप्त लिखित निवेदन की रजिस्ट्रेशन और उस पर विचार करने की प्रक्रिया को लिखित निवेदनों के लिए निर्धारित नियमों के अनुसार किया जाता है।
यदि आवेदन में ऐसे प्रश्न शामिल हैं, जिनका समाधान सेंट पीटर्सबर्ग में अंतर्राष्ट्रीय संबंधों और प्रवासन नीति के समिति की क्षमता में नहीं आता है, 
तो नागरिक को यह स्पष्ट किया जाएगा कि उसे कहाँ और किस क्रम में आवेदन करना चाहिए। व्यक्तिगत सुनवाई के दौरान, यदि पहले से आवेदन में उठाए गए प्रश्नों पर उसे जवाब दिया गया है, 
तो नागरिक को आगे की सुनवाई से इंकार किया जा सकता है। 

व्यक्तिगत सुनवाई के लिए पूर्व-निर्धारित रजिस्ट्रेशन समिति की रिसेप्शन पर फोन करके किया जा सकता है: 576-28-08, प्रतिदिन 9.00 से 18.00 तक, शुक्रवार को 17.00 बजे तक, अवकाश: 13.00 से 14.00 तक; शनिवार, रविवार - अवकाश।                                                    ''',

                'critical_consulate_handler': '''
*रूस का विदेश मंत्रालय का प्रतिनिधित्व कालिनिनग्राद में* 🏛️

*पता*: 🏠
236022, रूस, कालिनिनग्राद, किरोवा सड़क, 17

*फोन नंबर*: 📞
प्रवेश कक्ष: + 7 (401) 221-37-12
फैक्स: + 7 (401) 221-06-26
कांसुलर विभाग: + 7 (401) 221-16-68
पासपोर्ट विभाग: + 7 (401) 295-82-02
आमंत्रण प्राप्ति विभाग: + 7 (4012) 21-59-28

*कांसुलर-न्यायिक मामलों में नागरिकों की सुनवाई* ⚖️
सोम-गुरु: *9:00* बजे से *17:00* बजे तक (दोपहर का विश्राम *12:00* बजे से *14:00* बजे तक)
शुक्र: *9:00* बजे से *16:00* बजे तक (दोपहर का विश्राम *12:00* बजे से *14:00* बजे तक)
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
- अपने कमरे और रसोई को स्वच्छ रखना।
- पालतू जानवर रखना मना है।
- पड़ोसियों का सम्मान करें: रात 11:00 बजे से सुबह 8:00 बजे तक शांत रहें, विनम्र और ध्यानपूर्ण रहें।
- रात 10:00 बजे तक मेहमानों को आमंत्रित कर सकते हैं, लेकिन रात में मेहमानों की पार्किंग की अनुमति नहीं है।
- विश्वविद्यालय के परिसर में धूम्रपान और शराब पीना पूरी तरह से मना है।
- सुरक्षा नियमों का ध्यानपूर्वक अध्ययन करें, निकासी के पास के स्थानों को जानें।
- उपकरण में खराबी होने पर तुरंत वार्डन को सूचित करें।
- निवास के किसी भी प्रश्न के लिए हॉस्टल प्रशासन से संपर्क करें।
- छात्रों के सामाजिक समर्थन केंद्र की स्वीकृति के बिना किसी अन्य कमरे में न जाएं।

_सभी हॉस्टलों में बर्तन नहीं होते, लेकिन हर सप्ताह ताजा बिस्तर प्रदान किया जाता है।_

*सलाह*: निवास के तुरंत बाद वार्डन से मिलें - वह घरेलू मामलों में आपका मुख्य सहायक है।
""",


                'laundry_text': """
🏢 *स्थान*:
प्रसारक प्रत्येक छात्रावास में होते हैं। सटीक स्थान और कार्य करने का समय कमांडेंट या चौकीदार बताएगा।

🧼 *उपयोग करने के नियम*:
• अपना धोने का पाउडर लाओ
• अंडरवियर के लिए विशेष बैग का उपयोग करो
• *प्रतिबंधित* जूते धोना (यह मशीनों को नुकसान पहुंचाता है)
• उपयोग से पहले स्थान पर दिए गए निर्देशों से परिचित हो जाओ
• कपड़ों को विशेष रूप से सुसज्जित कमरे में सुखाओ

⏰ *महत्वपूर्ण!*
चौकीदार को कुंजी *ठीक समय पर* वापस करो — अन्य छात्रों को भी अपने कपड़े धोने हैं! 🙏

✨ सब कुछ आपके आराम के लिए व्यवस्थित किया गया है — सावधानी से उपयोग करो!
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

*चिकित्सा बीमा*:  
https://kantiana.ru/international/inostrannomu-studentu/oms/  

*पॉलीक्लिनिक से जुड़ने के लिए निर्देश*:  
https://kantiana.ru/students/polyclinic/  

*मानचित्र पर क्लिनिक*:  
https://2gis.ru/kaliningrad/search/236041%2C%20%D0%A0%D0%BE%D1%81%D1%81%D0%B8%D1%8F%2C%20%D0%9A%D0%B0%D0%BB%D0%B8%D0%BD%D0%B8%D0%BD%D0%B3%D1%80%D0%B0%D0%B4%2C%20%D1%83%D0%BB.%209%20%D0%B0%D0%BF%D1%80%D0%B5%D0%BB%D1%8F%2C%2060/firm/70000001006212174/20.524707%2C54.71579?m=20.524833%2C54.715617%2F19.07
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

*स्थान*: https://goo.gl/maps/zRT7KcqxLXtAVaUE7
                                            """,

                'loc_2_handler': """
*कोर्पस №2, भौतिकी, गणित और सूचना प्रौद्योगिकी संस्थान («फिजмат»), अलेक्सांद्र नेवस्की स्ट्रीट, 14* 

यहाँ स्थित हैं: 
· विदेशी छात्रों के साथ कार्य करने वाला विभाग (कमरा 119) 
· वीज़ा-आव्रजन सहायता विभाग (कमरा 114) 
· भर्ती समिति (कमरा 116 और 117) 
· पुस्तकालय, कमरा 202 («पढ़ने का क्षेत्र») 
· IT अवसंरचना सेवा (कमरा 121) 

*स्थान*: https://goo.gl/maps/6yt18jT8DoS5KgQv5
                                            """,
                                            
                'loc_3_handler': """
*कॉरपस संख्या 3, विश्वविद्यालय सड़क, 2*

यहाँ हैं:
· जीवित प्रणालियों का संस्थान
· मुख्य विश्वविद्यालय पुस्तकालय: वैज्ञानिक सदस्यता (कमरा 126), अध्ययन कक्ष (कमरा 115)

*स्थान*: https://goo.gl/maps/y2XnUi5vj5MxbRPeA
                                            """,

                'loc_4_handler': """
*कर्पस नंबर 4, चेरनिशेवस्कोवो स्ट्रीट, 56 («घड़ी वाला कर्पस»)*

यहाँ स्थित हैं:

· मानविकी संस्थान
· रूसी भाषा केंद्र (कमरा 01)
· सोवियत बचपन का संग्रहालय

*स्थान*: https://goo.gl/maps/EBrY5H86euoPi6Sn9
                                            """,

                'loc_5_handler': """
*भवन संख्या 5, चेरनिशेव्स्कोगो स्ट्रीट, 56ए* 

यहाँ स्थित है: 
· शिक्षा संस्थान 

*स्थान*: https://goo.gl/maps/xgHnL2PJ7ASXTFGG6
                                            """,

                'loc_6_handler': """
*कर्पस नंबर 6, अलेक्सांद्र नेवस्की स्ट्रीट, 14बी (शाइबा)*

यहां स्थित है:
· छात्रावासों का परिसर (कमरा 101)
· पाठ्येतर गतिविधियों का प्रबंधन

*स्थान*: https://maps.app.goo.gl/pKu1EREgTPvJ6VGN7
                                            """,

                'loc_7_handler': """
*कोर्पस नंबर 7, फ्रुन्ज़े स्ट्रीट, 6*

यहाँ हैं:
· शैक्षिक टेलीस्टूडियो
· विधि संस्थान

*स्थान*: https://goo.gl/maps/39LxmNSyZdSjnme16
                                            """,

                'loc_8_handler': """
*कोर्पस नं 8, 9 अप्रैल रोड, 5* 

यहां स्थित है: 
· चिकित्सा पुस्तकालय 

*स्थान*: https://goo.gl/maps/Tja71g7t1QPRqtbt7
                                            """,

                'loc_9_handler': """
*कॉर्पस नंबर 9, ए. नेव्स्कोय स्ट्रीट, 14 ('फोक')*

यहाँ स्थित है:
· जीवित स्वास्थ्य और खेल परिसर

*स्थान*: https://g.page/kantiana-sport?share
                                            """,

                'loc_10_handler': """
*कॉर्पस नंबर 10, ए. नेव्स्की स्ट्रीट. 14 («स्वेचका»)*

यहाँ स्थित हैं:
· छात्रों के लिए सामाजिक-आर्थिक सहायता केंद्र (कब. 14)
· करियर केंद्र

*स्थान*: https://goo.gl/maps/djfHWwTNer12z7caA
                                            """,

                'loc_12_handler': """
*कोर्पस नं १२, उल.बोटकिना, ४-६*

यहां स्थित है:
· मेडिकल इंस्टीट्यूट

*स्थान*: https://goo.gl/maps/BKJMV9WAR9G6PpaJ6
                                            """,

                'loc_22_handler': """
*कॉर्पस नंबर 22, ए. नेव्स्की स्ट्रीट, 14*

यहाँ स्थित है:
· एकेडमिक-फिजिकल कॉम्प्लेक्स जिसमें स्विमिंग पूल है

*लोकेशन*: https://goo.gl/maps/VevnRkQyv8FmZPXcA
                                            """,

                'loc_24_handler': """
*भवन संख्या 24, ज़ूलॉजिकल स्ट्रीट, 2*

यहाँ मौजूद हैं:
· यूनिवर्सिटी कॉलेज

*स्थान*: https://goo.gl/maps/Fb76GxbTCQUm3zEa7
                                            """,

                'loc_27_handler': """
*भवन संख्या 27, लेफ्टिनेंट जनरल ओज़ेरोव सड़क, 57*

यहां स्थित है:  
· इंजीनियरिंग-तकनीकी संस्थान  
· 'कांतियाना' एरेना  

*स्थान*: https://goo.gl/maps/H126DeMnucPJvA1U9
                                            """,

                'loc_28_handler': """
*भवन संख्या 28, गोर्की सड़क, 23*

यहाँ स्थित हैं:
· अर्थशास्त्र और प्रबंधन संस्थान

*स्थान*: https://goo.gl/maps/THR3WG17cF2EBtvW6
                                            """, 
            },

            'university_info_handlers': {
                'schedule_text': '''
*कक्षाओं का कार्यक्रम*:
https://schedule.kantiana.ru/
                                            ''',
                'scholarship_text': '''
*छात्रवृत्तियों और वित्तीय सहायता की जानकारी*:
https://kantiana.ru/students/scholarship/
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
https://kantiana.ru/universitys/administration/mezhdunarodnyy-ofis/*संपर्क*

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
