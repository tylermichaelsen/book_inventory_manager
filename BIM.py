import sqlite3
import os
import platform
import time
import database as db

def main():
    db.create_table()

    menu()


def menu():
    clear_screen()

    print(f'Book Inventory Manager')
    print(f'----------------------')
    print(f'1) Add a book to the database')
    print(f'2) View all stored books')
    print(f'3) Search book records')
    print(f'4) Delete a book record')
    print(f'5) Exit application')

    while (menu_choice := input('Select an option: ')) not in ['1','2','3','4','5']:
     print('Invalid menu selection.')
    
    clear_screen()

    match(menu_choice):
     case '1':
       add_book()
     case '2':
       view_books()
     case '3':
       search_book()
     case '4':
       delete_book()
     case '5':
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
    clear_screen()

    if search_field == 't':
     search_string = input('Enter the title of the book to search for: ')
    elif search_field == 'a':
     search_string = input('Enter the author of the book to search for: ')
    search_query = db.search_record(search_string, search_field)
    clear_screen()
    display_heading()
    for row in search_query:
     print(f'{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}')
    input('Press enter to continue.')
    menu()

def delete_book():
    deletion = input('Enter the ISBN of the book you wish to delete: ')
    clear_screen()
    db.delete_record(deletion)
    input('Press enter to continue.')
    menu()

def display_heading():
    print(f'Title\tAuthor\tYear\tISBN')
    print('-----------------------------')

def clear_screen():
    match(platform.system()):
       case 'Linux':
           os.system('clear')
       case 'Darwin':
           os.system('clear')
       case 'Windows':
           os.system('cls')

if __name__ == '__main__':
    main()