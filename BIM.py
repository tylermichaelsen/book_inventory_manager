import sqlite3
import os
import time
import database as db

def main():
 db.create_table()

 menu()


def menu():
 os.system('clear')
 print(f'Book Inventory Manager')
 print(f'----------------------')
 print(f'1) Add a book to the database')
 print(f'2) View all stored books')
 print(f'3) Search book records')
 print(f'4) Delete a book record')
 print(f'5) Exit application')

 
 while (menu_choice := input('Select an option: ')) not in ['1','2','3','4','5']:
  print('Invalid menu selection.')

 os.system('clear')

 if menu_choice == '1':
  add_book()
 if menu_choice == '2':
  view_books()
 if menu_choice == '3':
  search_book()
 if menu_choice == '4':
  delete_book()
 if menu_choice == '5':
  quit()

def add_book():
 title = input('Enter the title of the book: ')
 author = input('Enter the author of the book: ')
 year_published = int(input('Enter the year the book was published: '))
 isbn = input('Enter the ISBN of the book: ')
 db.add_record((title, author, year_published, isbn))
 time.sleep(2)
 menu()

def view_books():
 books = db.get_all_records()
 display_heading()
 for row in books:
  print(f'{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}')
 input('Press enter to continue.')
 menu()

def search_book():
 print(f'You can search by title or author.')
 print(f'Enter \'t\' for title or \'a\' for author:')

 while (search_field := input().lower()) not in ['t','a']:
  print(f'The option you chose was invalid.')
  print(search_field)
 os.system('clear')

 if search_field == 't':
  search_string = input('Enter the title of the book to search for: ')
 elif search_field == 'a':
  search_string = input('Enter the author of the book to search for: ')
 search_query = db.search_record(search_string, search_field)
 os.system('clear')
 display_heading()
 for row in search_query:
  print(f'{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}')
 input('Press enter to continue.')
 menu()

def delete_book():
 deletion = input('Enter the ISBN of the book you wish to delete: ')
 os.system('clear')
 db.delete_record(deletion)
 input('Press enter to continue.')
 menu()

def display_heading():
 print(f'Title\tAuthor\tYear\tISBN')
 print('-----------------------------')

if __name__ == '__main__':
 main()