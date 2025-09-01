TEXTS = {
    'ru': {
        'greetings': 'Привет! С чем помочь?',
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
        'police': 'Полиция',
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
        'dormitory_1': 'Соммера',
                'dormitory_2': 'Чернышевского',
                'dormitory_3': 'А. Невского',
                'dormitory_4': 'А. Невского',
                'dormitory_5': 'Чайковского',
                'dormitory_6': 'Азовская',
                'dormitory_7': 'Еловая',
                'dormitory_8': 'Еловая',
                'dormitory_9': 'Юбилейная',
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
                'back': '⬅️ Назад'
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
*Экстренные контакты*

Единый номер служб экстренного реагирования (пожарной охраны, МЧС, полиции, скорой помощи, газовой службы) — *112*.

Пожарные и спасатели — *01* (с городского телефона) и *101* (с мобильного)

Полиция — *02* (с городского телефона) и *102* (с мобильного).

Скорая помощь — *103* (с мобильного телефона) и *03* (с городского телефона).
                                                    ''',

        'critical_hotline_handler': '''
*Сектор визово-миграционной поддержки*

_Телефон_:

8 (4012) 595-595 (доб. 7454)— по вопросам миграционного учета и виз,

8 (4012) 595-595 (доб. 7452) доб. 7452 — по вопросам визовых приглашений

 _Адрес_: ул. А. Невского 14, корпус №2, каб. 114

_Приемные_ _часы_:

пн 14.00-17.00 
вт 10.00-13.00 
чт 14.00-17.00 
пт 10.00-13.00

обеденный перерыв 13.00-14.00
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
*Представительство МИД России в Калининграде*
Адрес: 236022, Россия, г. Калининград, ул. Кирова, 17
Приемная: + 7 (401) 221-37-12
Факс: + 7 (401) 221-06-26
Консульский отдел: + 7 (401) 221-16-68
Паспортный отдел: + 7 (401) 295-82-02
Отдел оформления приглашений: + 7 (4012) 21-59-28


*Приём граждан по консульско-правовым вопросам*

Пн, Вт, Ср, Чт: с 9-00 до 17-00 
(перерыв с 12-00 до 14-00)

Пт: с 9-00 до 16-00 
(перерыв с 12-00 до 14-00)

Сб, Вс: Выходной
                                            ''',
    },

    'dormitory_handlers': {
        'dormitory_text': """Подробнее про заселение ты можешь узнать (https://kantiana.ru/students/kampus/obshchezhitiya/zaselenie-v-obshchezhitie/).

*Как подать заявление на место в общежитии?*

1. После твоего зачисления на образовательную программу необходимо подать заявление на место на сайте по https://vk.com/away.php?to=https%3A%2F%2Fkantiana.ru%2Fstudents%2Fdormitory%2F&cc_key=

_Обращаем внимание, что количество мест в общежитии ограничено._

2. Если тебе на почту пришло уведомление о том, что общежитие одобрено, это значит, что твоя заявка принята, и теперь ты участвуешь в конкурсе. Статус своего заявления можно отслеживать по группе Комплекса студенческих общежитий: [группа КСО] https://vk.com/kso_bfu

3. Когда ты увидел свое имя в рейтинге, это значит, что тебе можно получать 2 необходимых допуска для заселения. О них подробно расскажем далее.

4. С полученными допусками подходи на подписание договора в КСО (ул.Невского, 14/1, кабинет 101).

5. После заключения договора и оплаты проживания с направлением подходи к заведующей указанного общежития для заселения и инструктажа.

По приезде необходимо подписать договор найма жилого помещения в студенческом общежитии в Центре социально-экономической поддержки студентов, получить направление и оплатить общежитие за первый семестр. 

_С собой обязательно взять паспорт._

*Приемные часы Центра социально-экономической поддержки студентов:*

- Понедельник: C 10:00 до 17:00
- Вторник: C 10:00 до 17:00
- Четверг: C 10:00 до 17:00
- Пятница: C 10:00 до 16:45 

Обеденный перерыв с 13:00 до 14:00

*Адрес: ул. А. Невского, 14, корпус 10, 1 этаж, кабинет 14.*

*Медицинская справка*

Чтобы проживать в общежитии, необходимо предоставить коменданту общежития справку о прохождении медицинской комиссии. Для получения такой справки тебе нужно посетить кабинет 2 в Клинико-диагностическом центре БФУ им. И.Канта (КДЦ). 

*С собой возьми:*

- паспорт;
- прививочный сертификат (документ, в котором указаны все прививки, которые тебе делались в течение жизни, в частности там должны быть справки о прививках от кори, дифтерии, столбняка и гепатита В);
- флюорографию не старше 1 года;
- 2 отрицательных результата ПЦР-теста на COVID-19/ допуск к занятиям.

_Документы должны быть на русском языке или иметь заверенный перевод на русский._

*Адрес* КДЦ БФУ им.И.Канта: (https://goo.gl/maps/bwq24xTh5P1EctiU8)

_В случае если на момент заселения у тебя этих справок нет, их необходимо сделать за свой счет в любой клинике._
                                            """,

        'payment_text': """
Оплатить общежитие можно двумя путями.

1. Лично. В кабинет № 222 административного корпуса, 2 этаж. Здесь ты получишь квитанцию для оплаты в кассе на том же этаже. Оплатить через кассу можно наличными в рублях или банковской картой.

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

*Совет*: знакомься с комендантом сразу после вселения — он твой главный помощник в вопросах быта.""",

        'laundry_text': """
Прачечные находятся в здании каждого общежития. Комендант или вахтер расскажут, где именно находится комната со стиральными машинами и в какое время можно брать ключ.

Стиральный порошок нужно приносить с собой. Прачечная оборудована несколькими стиральными машинами, в которых можно стирать одновременно, если много белья для стирки. Стирать нижнее белье обязательно в специальных мешках. Стирать обувь запрещается, так как это приводит к поломке стиральных машин. Внимательно перед использованием машинки ознакомься с инструкцией в комнате. Сушить белье после стирки можно в специальной комнате, которая оборудована сушилками для одежды.

*Помни*, что другие студенты в общежитии тоже хотят постирать свою одежду, поэтому возвращай ключ вахтеру или коменданту сразу после стирки, именно в то время, когда пообещал его вернуть.
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

*Медицинское страхование*:
https://kantiana.ru/international/inostrannomu-studentu/oms/

*Инструкция по прикреплению к поликлинике*: 
https://kantiana.ru/students/polyclinic/
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

        'loc_12_handler': """
*Корпус №12, ул.Боткина, 4-6*

Здесь находится:
· Медицинский институт

                                            """,

        'loc_22_handler': """
*Корпус №22, ул. А.Невского,14*

Здесь находится:
Учебно-физкультурный комплекс с бассейном

                                            """,

        'loc_24_handler': """
*Корпус №24, ул. Зоологическая, 2*

Здесь находятся:
·Университетский колледж

                                            """,

        'loc_27_handler': """
*Корпус №27, ул. Генерала-лейтенанта Озерова, 57*

Здесь находятся:
·Инженерно-технический институт
·Арена «Кантиана»
                                            """,

        'loc_28_handler': """
*Корпус №28, ул. Горького, 23*

Здесь находятся:
·Институт экономики и менеджмента
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
    'greetings': 'Hello! How can I help you?',
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
            'info': 'University Information',
            'location': 'Building location',
            'dormitory': 'Dormitories',
            'hospital': 'Medical Center',
            'critical': 'Critical situations',
            'language_check': 'Russian language check',
            'sber':'SBER',
            'back': 'Back'
        },
        'critical_keyboard': {
            'police': 'Police',
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
            'dormitory_1': 'Sommer',
            'dormitory_2': 'Chernyshevsky',
            'dormitory_3': 'Nevsky',
            'dormitory_4': 'Nevsky',
            'dormitory_5': 'Tchaikovsky',
            'dormitory_6': 'Azovskaya',
            'dormitory_7': 'Yelovaya',
            'dormitory_8': 'Yelovaya',
            'dormitory_9': 'Yubileynaya',
            'sber_payment': 'Pay in SBER',
            'more': 'More',
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
            'loc_1': 'Administrative building',
            'loc': 'Building',
            'loc_2': 'Building №2, Institute of Physics, Mathematics and IT',
            'loc_4': 'Building №4 ("The building with the clock")',
            'loc_6': 'Building №6 ("Puck")',
            'loc_9': 'Building №9 («FOС»)',
            'loc_10': 'Building №10 ("Candle")',
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
*Emergency Contacts*

The unified number for emergency response services 
(fire department, EMS, police, ambulance, gas service) — *112*.

Firefighters and rescuers — *01* (from a landline) and *101* (from a mobile)

Police — *02* (from a landline) and *102* (from a mobile).

Ambulance — *103* (from a mobile) and *03* (from a landline).
                                                    ''',

            'critical_hotline_handler': '''
*Visa and Migration Support Center*

_Phone_: 

8 (4012) 595-595 (ext. 7454) — for questions regarding migration registration and visas

8 (4012) 595-595 (ext. 7452) — for questions regarding visa invitations

_Address_: 14 A. Nevsky St., building 2, office 114

_Office_ _Hours_:

Mon 14:00-17:00
Tue 10:00-13:00
Thu 14:00-17:00
Fri 10:00-13:00

Lunch break: 13:00-14:00
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
*Representation of the Ministry of Foreign Affairs of Russia in Kaliningrad* 

Address: 236022, Russia, Kaliningrad, Kirova St., 17 
Reception: +7 (401) 221-37-12 
Fax: +7 (401) 221-06-26 
Consular Department: +7 (401) 221-16-68 
Passport Department: +7 (401) 295-82-02 
Invitation Processing Department: +7 (4012) 21-59-28

*Reception of citizens on consular-legal issues* 

Mon, Tue, Wed, Thu: 9:00 to 17:00 (break from 12:00 to 14:00) 

Fri: 9:00 to 16:00 (break from 12:00 to 14:00) 

Sat, Sun: Closed
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
The laundries are located in the building of each dormitory. 
The commandant or the security guard will tell you where exactly the room with the washing machines is and at what time you can get the key.

You need to bring your own laundry detergent. 
The laundry is equipped with several washing machines that can be used simultaneously if there is a lot of laundry to wash. 
It is mandatory to wash underwear in special bags. Washing shoes is prohibited as it leads to damage to the washing machines. 
Carefully read the instructions in the room before using the machine. You can dry the laundry after washing in a special room that is equipped with clothes dryers.

*Remember*, that other students in the dormitory also want to wash their clothes, so return the key to the security guard or the commandant immediately after washing, exactly at the time you promised to return it.
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

: https://goo.gl/maps/6yt18jT8DoS5KgQv5
                                            """,

            'loc_3_handler': """
*Building No. 3, Universitetskaya St., 2*

Here you can find:
· Institute of Living Systems
· Main University Library: Scientific subscription (room 126), reading room (room 115)

: https://goo.gl/maps/y2XnUi5vj5MxbRPeA
                                            """,

            'loc_4_handler': """
*Building No. 4, Chernyshevsky Street, 56 (‘The Building with the Clock’)*

Here are located:
· Institute of Humanities
· Center for the Russian Language (room 01)
· Museum of Soviet Childhood

: https://goo.gl/maps/EBrY5H86euoPi6Sn9
                                            """,

            'loc_5_handler': """
*Building No. 5, 56a Chernyshevskogo Street*  

Here is located:  
· Institute of Education  

: https://goo.gl/maps/xgHnL2PJ7ASXTFGG6
                                            """,

            'loc_6_handler': """
*Building No. 6, A. Nevsky St., 14b ('Shaiba')*

Here are located:
· Complex of student dormitories (room 101)
· Office of extracurricular activities

: https://maps.app.goo.gl/pKu1EREgTPvJ6VGN7
                                            """,

            'loc_7_handler': """
*Building No. 7, Frunze St., 6* 

Here you can find: 
· Educational Television Studio 
· Law Institute 

: https://goo.gl/maps/39LxmNSyZdSjnme16
                                            """,

            'loc_8_handler': """
*Building No. 8, 9 April Street, 5*

Here is located:
· Medical Library

: https://goo.gl/maps/Tja71g7t1QPRqtbt7
                                            """,

            'loc_9_handler': """
*Building No. 9, A. Nevsky Street, 14 ('FOK')* 

Here is located: 
· Physical Culture and Health Complex 

: https://g.page/kantiana-sport?share
                                            """,

            'loc_10_handler': """
*Building No. 10, A. Nevsky St. 14 (“Candle”)*

Here are located:
· Center for Socio-Economic Support of Students (room 14)
· Career Center

: https://goo.gl/maps/djfHWwTNer12z7caA
                                            """,

            'loc_12_handler': """
*Building No. 12, Botkin Street, 4-6* 

Here is located: 
· Medical Institute 

: https://goo.gl/maps/BKJMV9WAR9G6PpaJ6
                                            """,

            'loc_22_handler': """
*Building No. 22, A. Nevsky St., 14* 

Here is located: 
· Educational and Sports Complex with a swimming pool 

: https://goo.gl/maps/VevnRkQyv8FmZPXcA
                                            """,

            'loc_24_handler': """
*Building No. 24, Zoologicheskaya St., 2*  

Here you can find:  
· University College  

: https://goo.gl/maps/Fb76GxbTCQUm3zEa7
                                            """,

            'loc_27_handler': """
*Building No. 27, Gen. Lt. Ozerov St., 57* 

Here are located:  
· Engineering and Technical Institute  
· «Kantiana» Arena  

: https://goo.gl/maps/H126DeMnucPJvA1U9
                                            """,

            'loc_28_handler': """
*Building No. 28, Gorky Street, 23*

Here are located:
· Institute of Economics and Management

: https://goo.gl/maps/THR3WG17cF2EBtvW6
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
}
}
