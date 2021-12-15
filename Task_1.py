# Перепишіть програму-банкомат на використання бази даних 
# для збереження всих даних.
# Використовувати БД sqlite3 та натівний Python.
# 
# Дока з прикладами: https://docs.python.org/3/library/
# sqlite3.html
# Туторіал (один із): https://www.sqlitetutorial.net/sqlite-
# python/
#
# Для уніфікації перевірки, в базі повинні бути 3 користувача:
# ім'я: user1, пароль: user1
# ім'я: user2, пароль: user2
# ім'я: admin, пароль: admin (у цього користувача - права інкасатора)

import sqlite3

con = sqlite3.connect('atm.db')
cur = con.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS users
               (id integer PRIMARY KEY, name text NOT NULL, password text NOT NULL, is_incassator bit DEFAULT false)''')
cur.execute("INSERT INTO users VALUES ('1','user1','user1', 'False')")
cur.execute("INSERT INTO users VALUES ('2','user2','user2', 'False')")
cur.execute("INSERT INTO users VALUES ('3','admin','admin', 'True')")
con.commit()
cur.execute('''CREATE TABLE IF NOT EXISTS balance
               (user_id integer NOT NULL, amount integer NOT NULL DEFAULT 0, FOREIGN KEY (user_id) REFERENCES users(id))''')
cur.execute("INSERT INTO balance VALUES ('1', '0')")
cur.execute("INSERT INTO balance VALUES ('2', '100')")
con.commit()
cur.execute('''CREATE TABLE IF NOT EXISTS banknotes
               (id integer, nom integer NOT NULL PRIMARY KEY, quantity integer NOT NULL DEFAULT 0)''')
cur.execute("INSERT INTO balance VALUES ('1', '10', '0')")
cur.execute("INSERT INTO balance VALUES ('2', '20', '0')")
cur.execute("INSERT INTO balance VALUES ('3', '50', '0')")
cur.execute("INSERT INTO balance VALUES ('4', '100', '0')")
cur.execute("INSERT INTO balance VALUES ('5', '200', '0')")
cur.execute("INSERT INTO balance VALUES ('6', '500', '0')")
cur.execute("INSERT INTO balance VALUES ('7', '1000', '0')")

con.close()
