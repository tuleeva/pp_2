import psycopg2
from tabulate import tabulate

conn = psycopg2.connect(
    dbname="lab11",
    user="postgres",
    password="uralsk07sila",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

def search_user():
    pattern = input("Введите шаблон для поиска (имя, фамилия или телефон): ")
    cur.execute("SELECT * FROM search_by_pattern(%s);", (pattern,))
    rows = cur.fetchall()
    print(tabulate(rows, headers=["ID", "Имя", "Фамилия", "Телефон"], tablefmt="psql"))

def insert_or_update():
    name = input("Введите имя: ")
    surname = input("Введите фамилию: ")
    phone = input("Введите телефон: ")
    cur.execute("CALL insert_or_update_user(%s, %s, %s);", (name, surname, phone))
    conn.commit()
    print("Пользователь добавлен или обновлен.")

def insert_multiple():
    n = int(input("Сколько пользователей хотите добавить? "))
    users = []
    for _ in range(n):
        name = input("Имя: ")
        surname = input("Фамилия: ")
        phone = input("Телефон: ")
        users.append([name, surname, phone])

    # Преобразуем в формат двумерного массива текста
    cur.execute("CALL insert_many_users(%s::TEXT[][], %s);", (users, None))
    conn.commit()
    print("Массовая вставка завершена.")

def paginate():
    limit = int(input("Сколько записей на странице: "))
    offset = int(input("С какого смещения начать: "))
    cur.execute("SELECT * FROM get_paginated_users(%s, %s);", (limit, offset))
    rows = cur.fetchall()
    print(tabulate(rows, headers=["ID", "Имя", "Фамилия", "Телефон"], tablefmt="psql"))

def delete_user():
    choice = input("Удалить по (1) имени или (2) телефону? ")
    if choice == "1":
        name = input("Введите имя для удаления: ")
        # правильный вызов процедуры с параметром name
        cur.execute("CALL delete_user(%s, %s);", (name, None))
    elif choice == "2":
        phone = input("Введите телефон для удаления: ")
        # правильный вызов процедуры с параметром phone
        cur.execute("CALL delete_user(%s, %s);", (None, phone))

    else:
        print("Неверный выбор.")
        return

    conn.commit()  # подтвердить изменения в базе данных
    print("Удаление завершено.")


while True:
    cmd = input("\nВведите команду (search, insert, insert_multiple, paginated, delete, exit): ").lower()
    if cmd == "search":
        search_user()
    elif cmd == "insert":
        insert_or_update()
    elif cmd == "insert_multiple":
        insert_multiple()
    elif cmd == "paginated":
        paginate()
    elif cmd == "delete":
        delete_user()
    elif cmd == "exit":
        break
    else:
        print("Неизвестная команда.")

cur.close()
conn.close()
