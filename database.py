import sqlite3

def create_table():
	try:
		con = sqlite3.connect('book_records.db')
		cur = con.cursor()
		cur.execute("CREATE TABLE IF NOT EXISTS book(title TEXT, author TEXT, year_published INTEGER, isbn TEXT PRIMARY KEY)")
		con.commit()
	except Exception as err:
		print('Error creating table.', err)
	finally:
		con.close()


def add_record(book):
	try:
		con = sqlite3.connect('book_records.db')
		cur = con.cursor()
		cur.execute('''
 			INSERT  INTO book (title, author, year_published, isbn)
 			VALUES (?,?,?,?)''', book)
		con.commit()
		print(f'Successfully added \'{book[0]}\' to database.')
	except Exception as err:
		print('Error adding record.', err)
	finally:
		con.close()

def get_all_records():
	try:
		con = sqlite3.connect('book_records.db')
		cur = con.cursor()
		cur.execute('''SELECT * FROM book''')
		return cur.fetchall()
	except:
		print('Error retrieving records.')
		return []
	finally:
		con.close()


def search_record(string, field):
	try:
		con = sqlite3.connect('book_records.db')
		cur = con.cursor()
		if field == 't':
			cur.execute('''SELECT * FROM book WHERE title=?''', (string, ))
		elif field == 'a':
			cur.execute('''SELECT * FROM book WHERE author=?''', (string, ))
		return cur.fetchall()
	except:
		print('Error searching records.')
		return []
	finally:
		con.close()


def delete_record(deletion):
	try:
		con = sqlite3.connect('book_records.db')
		cur = con.cursor()
		cur.execute('''DELETE FROM book WHERE isbn=?''', (deletion, ))
		print(f'Successfully removed book with ISBN \'{deletion}\' from database.')
	except:
		print(f'Error deleting record.')
	finally:
		con.commit()
		con.close()

