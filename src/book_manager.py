import sqlite3

def connect():
    conn = sqlite3.connect('E:\\sql\\src\\database\\books.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            year INTEGER
        )
    ''')
    conn.commit()
    conn.close()

def add_book(title, author, year):
    conn = sqlite3.connect('E:\\sql\\src\\database\\books.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO books (title, author, year) VALUES (?, ?, ?)', (title, author, year))
    conn.commit()
    conn.close()

def view_books():
    conn = sqlite3.connect('E:\\sql\\src\\database\\books.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM books')
    books = cursor.fetchall()
    conn.close()
    return books

def update_book(book_id, title, author, year):
    conn = sqlite3.connect('E:\\sql\\src\\database\\books.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE books SET title = ?, author = ?, year = ? WHERE id = ?', (title, author, year, book_id))
    conn.commit()
    conn.close()

def delete_book(book_id):
    conn = sqlite3.connect('E:\\sql\\src\\database\\books.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM books WHERE id = ?', (book_id,))
    conn.commit()
    conn.close() 