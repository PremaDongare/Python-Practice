class Books:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def __str__(self):
        return f"{self.title} by {self.author}"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        new_book = Books(title, author)
        self.books.append(new_book)
        print("Book added!")

    def showbook(self):
        available_books = [book for book in self.books if book.available]
        if not available_books:
            print("No books available")
        else:
            print("Available books:")
            for book in available_books:
                print("-", book)

    def borrow_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower() and book.available:
                book.available = False
                print("Book borrowed successfully")
                return
        print("Book not available or already borrowed")

    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower() and not book.available:
                book.available = True
                print("Book returned successfully")
                return
        print("Book not found")

# ✅ Main code
library = Library()

while True:
    print("\n1. Add Book")
    print("2. Show Available Books")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        title = input("Enter book title: ")
        author = input("Enter author name: ")
        library.add_book(title, author)
    elif choice == '2':
        library.showbook()
    elif choice == '3':
        title = input("Enter the name of the book to borrow: ")
        library.borrow_book(title)
    elif choice == '4':
        title = input("Enter the name of the book to return: ")
        library.return_book(title)
    elif choice == '5':
        print("Exiting...")
        break
    else:
        print("Invalid choice")
