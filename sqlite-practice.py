import sqlite3

db = sqlite3.connect('./practicedb')
cursor = db.cursor()
cursor.execute('''
	CREATE TABLE users(id INTEGER PRIMARY KEY, name TEXT, phone TEXT, email TEXT unique, password TEXT)
''')
db.commit()

name1 = 'Andres'
phone1 = '1112222'
email1 = 'blah@blah.com'
password1 = '1234'

name2 = 'John'
phone2 = '5557241'
email2 = 'dude@dude.com'
password2 = 'asdf'

cursor.execute('''INSERT INTO users(name, phone, email, password)
				VALUES(?,?,?,?)''', (name1, phone1, email1, password1))
print('First user inserted')

cursor.execute('''INSERT INTO users(name, phone, email, password)
				VALUES(?,?,?,?)''', (name2, phone2, email2, password2))
print('Second user inserted')

db.commit()



db.close()
