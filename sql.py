import sqlite3

def show_db():
    cursor = conn.cursor()

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = cursor.fetchall()

    for table in tables:
        table_name = table[0]
        cursor.execute(f"SELECT * FROM {table_name}")
        rows = cursor.fetchall()
        print(f"\nСодержимое таблицы {table_name}:")
        cursor.execute(f"PRAGMA table_info({table_name})")
        print([i[1] for i in cursor.fetchall()])
        for row in rows:
            print(row)
    
    
try:
    conn = sqlite3.connect('coffeeshop.db')
except Exception as e:
    file = open("coffeeshop.db", "w+")
    file.close()
    conn = sqlite3.connect('coffeeshop.db')

text = '''
Создать таблицы - 0
Заполнить таблицы - 1
Посмотреть таблицы - 2
input.txt - запрос без редактирования бд - 3
input.txt - изменение бд - 4    
Завершить работу - всё остальное'''
print(text)

while True:
    try:
        com = input('\n')
        if com in ["0", "1"]:
            file_name = "data/create_table.txt"
            if com == "1":
                file_name = "data/add_data.txt"
            file = open(file_name)
            commands = file.read().split('\n\n')
            file.close()
            cursor = conn.cursor()
            for el in commands:
                cursor.execute(el)
            conn.commit()
            
        elif com == "2":
            show_db()
        elif com in ["3", "4"] :
            cursor = conn.cursor()
            file = open('input.txt')
            el = file.read()
            file.close()
            cursor.execute(el)
            if com == "3":
                result = cursor.fetchall()
                for el in result:
                    print(el)
            else:
                conn.commit()
        else:
            break
            
    except Exception as e:
        print("Ошибка: " + str(e))
    
conn.close()
