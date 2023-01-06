import sqlite3

class Telegram_bot_db:

    def __init__(self, database):
        """conecting to db and maintain connection cursor"""
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()

    def get_subscriptions(self, status = True):
        """retrieving all active bot's subscribers"""
        with self.connection:
            return self.cursor.execute("SELECT * FROM `subscriptions` WHERE `status` = ?", (status,)).fetchall()

    def subscriber_exists(self, user_id):  
        """check if the user exists in the database"""
        with self.connection:
            result = self.cursor.execute("SELECT * FROM `subscriptions` WHERE `user_id` = ?", (user_id,)).fetchall()
            return bool(len(result))

    def add_subscriber(self, user_id, status = True):
        """"adding new subscribers"""  
        with self.connection:
            return self.cursor.execute("INSERT INTO `subscriptions` (`user_id`, `status`) VALUES (?,?)", (user_id, status))
    
    def update_subscription(self, user_id, status):
        """update status of subscribers"""
        with self.connection:
            return self.cursor.execute("UPDATE `subscriptions` SET `status` = ? WHERE `user_id` = ?", (status, user_id)) 

    def close(self):
        """abort database connection with db """  
        self.connection.close()  



# class SQLighter:

#     def __init__(self, database):
#         """Подключаемся к БД и сохраняем курсор соединения"""
#         self.connection = sqlite3.connect(database)
#         self.cursor = self.connection.cursor()

#     def get_subscriptions(self, status = True):
#         """Получаем всех активных подписчиков бота"""
#         with self.connection:
#             return self.cursor.execute("SELECT * FROM `subscriptions` WHERE `status` = ?", (status,)).fetchall()

#     def subscriber_exists(self, user_id):
#         """Проверяем, есть ли уже юзер в базе"""
#         with self.connection:
#             result = self.cursor.execute('SELECT * FROM `subscriptions` WHERE `user_id` = ?', (user_id,)).fetchall()
#             return bool(len(result))

#     def add_subscriber(self, user_id, status = True):
#         """Добавляем нового подписчика"""
#         with self.connection:
#             return self.cursor.execute("INSERT INTO `subscriptions` (`user_id`, `status`) VALUES(?,?)", (user_id,status))

#     def update_subscription(self, user_id, status):
#         """Обновляем статус подписки пользователя"""
#         with self.connection:
#             return self.cursor.execute("UPDATE `subscriptions` SET `status` = ? WHERE `user_id` = ?", (status, user_id))

#     def close(self):
#         """Закрываем соединение с БД"""
#         self.connection.close()        




# class Telegram_bot_db:
    
    # def  __init__(self, db_file):
    #     self.connection = sqlite3.connect(db_file)
    #     self.cursor = self.connection.cursor()

    # def get_subs(self, status = True):
    #     with self.connection:
    #         return self.cursor.execute("SELECT FROM `subscriptions` WHERE `status`= ?",(status,)).fetchall()
    





# import sqlite3

# with sqlite3.connect("mydb.db") as db:
#     curs = db.cursor()


# -----------------------

# import turtle

# turtle.speed(1)

# def move(a):
#     turtle.forward(a)
#     turtle.left(90)

# def drawSquare(a):
#     for i in range(4):
#         move(a)


# def drawSquareColor(a, color):
#     turtle.color(color)
#     turtle.begin_fill()
#     drawSquare(a)
#     turtle.end_fill()    

# drawSquareColor(100, 'blue')
# turtle.goto(100, 100)
# drawSquareColor(40, 'green')

# -----------------------

# file = open('text.txt', mode='w');

# def write_to_file():
#     try:
#         file.write(str(10 / int(input('your number'))))
        
#     except Exception:
#         print("write integer")
#     finally:
#         file.close() 
# write_to_file()

# with open('text.txt', mode='w') as file:
#     file.write(str(10 / int(input('your number'))))

# -----------

# class Person:
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname

#     def print_info(self, n):
#         for i in range(n):
#             print(f"{self.name} {self.surname}") 

# p1 = Person('maks', 'si') 
# p2 = Person('maks2', 'si2') 
# p3 = Person('maks3', 'a')

# p2.print_info(1) 

# -----------

  
# -----------

# import sqlite3

# with sqlite3.connect("database.db") as db:
#     curs= db.cursor()

    # curs.execute("""CREATE TABLE members(
    #     id INTEGER PRIMARY KEY AUTOINCREMENT,
    #     author VARCHAR,
    #     topic VARCHAR,
    #     content TEXT
    # )
    # """)

    # values = [
    #     ("МАКС", "Cид","2001"),
    #     ("Вика","Cид", "2007")
    # ]

    # curs.executemany("INSERT INTO members(author, topic, content) VALUES(?,?,?)", values)
    # curs.execute("DELETE FROM members WHERE rowid>2")

    # curs.execute("SELECT * FROM  members")
    # print(curs.fetchall())

