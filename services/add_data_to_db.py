import sqlite3

conn = sqlite3.connect('../db.sqlite3')
cursor = conn.cursor()

advertisements = [
    ('Установка видеонаблюдения и домофонии', 'Primtec', 794, 1),
    ('Установка видеонаблюдения и видеокамер в домах во Владивостоке', 'ООО "ТЕСЛА"', 1751, 2),
    ('Установка/обслуживание: видеонаблюдения, домофонов, СКУД, сигнализации во Владивостоке',
     'ИП Якименко Алексей Андреевич', 1308, 3),
    ('Монтаж видеонаблюдения Hikvision HiWatch Trassir, СКУД, домофонов во Владивостоке',
     'doneit', 452, 4),
    ('Видеонаблюдение Установка Продажа Настройка Видеокамер IP во Владивостоке', 'TVi MART', 1420, 5),
    ('ВидеоКИТ - Системы видеонаблюдения, установка, обслуживание во Владивостоке',
     'VideoKIT', 136, 6),
    ('Установка, монтаж систем видеонаблюдения установка камер во Владивостоке', 'Den2078', 2556, 7),
    ('Установим Видеодомофон в квартиру или частный дом! Видеонаблюдение во Владивостоке', 'Подряд', 89, 8),
    ('Установка видеонаблюдения от Vladrec | Монтаж | Обслуживание | СКУД во Владивостоке', 'VLADREC', 161, 9),
    ('IP WiFi видеонаблюдение! Установка видеокамер! Проектирование, монтаж во Владивостоке', 'Умный Дом Z-Wave',
     3788, 10)
]

cursor.executemany('''
    INSERT INTO ads_advertisement (title, author, views_count, ad_position) VALUES (?, ?, ?, ?)
''', advertisements)

conn.commit()

conn.close()

print("Записи успешно добавлены")
