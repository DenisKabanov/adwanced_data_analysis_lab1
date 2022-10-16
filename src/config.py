# PATH
RAW_PATH = '../data/raw/'

# COLS
TARGET_COLS = ['Артериальная гипертензия', 'ОНМК', 'Стенокардия, ИБС, инфаркт миокарда', 'Сердечная недостаточность', 'Прочие заболевания сердца'] # множество столбцов-таргетов
ID_COL = 'ID'
EDU_COL = 'Образование'

CAT_COLS = ['Пол', 'Семья', 'Этнос', 'Национальность', 'Религия', 'Образование',
       'Профессия', 'Статус Курения', 'Частота пасс кур', 'Алкоголь',
       'Время засыпания', 'Время пробуждения'] # категориальные признаки

ONE_COLS = ['Вы работаете?', 'Выход на пенсию', 'Прекращение работы по болезни', 'Сахарный диабет', 'Гепатит', 'Онкология', 'Хроническое заболевание легких',
 'Бронжиальная астма', 'Туберкулез легких ', 'ВИЧ/СПИД', 'Регулярный прим лекарственных средств', 'Травмы за год', 'Переломы', 'Пассивное курение',
 'Сон после обеда', 'Спорт, клубы', 'Религия, клубы']  # столбцы, в которых может быть только два варианта ответа (0 или 1)

REAL_COLS = ['Возраст курения', 'Сигарет в день', 'Возраст алког'] # столбцы с типом float
NEW_COLS = ['Жаворонок', 'Образование_ord']
MANY_MISSING_DATA_COLS = ['Возраст курения', 'Сигарет в день', 'Частота пасс кур', 'Возраст алког']