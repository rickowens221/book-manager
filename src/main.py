from book_manager import connect, add_book, view_books, update_book, delete_book

def main():
    connect()
    while True:
        print("\nМенеджер Книг")
        print("1. Добавить книгу")
        print("2. Просмотреть все книги")
        print("3. Обновить информацию о книге")
        print("4. Удалить книгу")
        print("5. Выход")
        choice = input("Выберите действие (1-5): ")

        if choice == '1':
            title = input("Название книги: ")
            author = input("Автор: ")
            year = input("Год выпуска: ")
            add_book(title, author, year)
            print("Книга добавлена.")
        elif choice == '2':
            books = view_books()
            for book in books:
                print(f"ID: {book[0]}, Название: {book[1]}, Автор: {book[2]}, Год: {book[3]}")
        elif choice == '3':
            book_id = input("Введите ID книги для обновления: ")
            title = input("Новое название книги: ")
            author = input("Новый автор: ")
            year = input("Новый год выпуска: ")
            update_book(book_id, title, author, year)
            print("Информация о книге обновлена.")
        elif choice == '4':
            book_id = input("Введите ID книги для удаления: ")
            delete_book(book_id)
            print("Книга удалена.")
        elif choice == '5':
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Пожалуйста, попробуйте снова.")

if __name__ == '__main__':
    main() 