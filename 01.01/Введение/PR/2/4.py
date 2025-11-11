class Library:
    def __init__(self):
        self.books = []  # Создаём пустой список для хранения

    def add_book(self, title, author):  # Метод для добавления книг
        self.books.append({"title": title, "author": author})  # Добавляем словарь

    def remove_book(self, title):  # Метод для удаления книг по названию
        for book in self.books:
            if book["title"] == title:
                self.books.remove(book)
                return True
        return False

    def find_books_by_author(self, author):  # Метод для поиска книг по автору
        return [book for book in self.books if book["author"] == author]

    def get_all_books(self):  # Метод для получения всех книг
        return self.books

# Пример 
if __name__ == "__main__":
    lib = Library() 
    lib.add_book("1999", "The Book")
    lib.add_book("Animals", "George")
    lib.add_book("Преступление и наказание", "Достоевский")

    print("Все книги:")
    for book in lib.get_all_books():
        print(f"  {book['title']} — {book['author']}")

    print("\nКниги:")
    for book in lib.find_books_by_author("George"):
        print(f"  {book['title']}")

    print("\nУдалено:")
    lib.remove_book("1999")
    for book in lib.get_all_books():
        print(f"  {book['title']} — {book['author']}")