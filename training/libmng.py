class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def display(self):
        print(f"Name: {self._name}, Age: {self._age}")

class Librarian(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self._employee_id = employee_id

    def display(self):
        super().display()
        print(f"Employee ID: {self._employee_id}")

    def manage_books(self):
        print(f"Librarian {self._name} is managing the books.")

class Member(Person):
    def __init__(self, name, age, member_id):
        super().__init__(name, age)
        self._member_id = member_id
        self._borrowed_books = []

    def display(self):
        super().display()
        print(f"Member ID: {self._member_id}")

    def borrow_book(self, book):
        if book.available:
            self._borrowed_books.append(book)
            book.available = False
            print(f"{self._name} borrowed the book: {book._title}")
        else:
            print(f"Sorry, {book._title} is not available.")

    def return_book(self, book):
        if book in self._borrowed_books:
            self._borrowed_books.remove(book)
            book.available = True
            print(f"{self._name} returned the book: {book._title}")
        else:
            print(f"{self._name} doesn't have the book: {book._title}")
                  
class Book:
    def __init__(self, title, author, isbn):
        self._title = title
        self._author = author
        self._isbn = isbn
        self.available = True

    def display(self):
        status = "Available" if self.available else "Not Available"
        print(f"Book [Title: {self._title}, Author: {self._author}, ISBN: {self._isbn}, Availability: {status}]")

class Library:
    def __init__(self, name):
        self._name = name
        self._books = []

    def add_book(self, book):
        self._books.append(book)
        print(f"Book {book._title} added to the library.")

    def remove_book(self, isbn):
        for book in self._books:
            if book._isbn == isbn:
                self._books.remove(book)
                print(f"Book {book._title} removed from the library.")
                return
        print(f"Book with ISBN {isbn} not found in the library.")

    def display_books(self):
        print(f"Books in {self._name}:")
        for book in self._books:
            book.display()

class BookWithMagicMethods:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def __str__(self):
        return f"Book [Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}]"

    def __eq__(self, other):
        return self.isbn == other.isbn

class LibrarySystem:
    def __init__(self):
        self.library = Library("City Library")
        self.members = []
        self.librarian = None

    def add_book(self, title, author, isbn):
        new_book = Book(title, author, isbn)
        self.library.add_book(new_book)

    def remove_book(self, isbn):
        self.library.remove_book(isbn)

    def display_books(self):
        self.library.display_books()

    def add_member(self, name, age, member_id):
        new_member = Member(name, age, member_id)
        self.members.append(new_member)
        print(f"Member {name} added to the library.")

    def remove_member(self, member_id):
        member = next((m for m in self.members if m._member_id == member_id), None)
        if member:
            self.members.remove(member)
            print(f"Member with ID {member_id} removed.")
        else:
            print("Member not found.")

    def set_librarian(self, name, age, employee_id):
        self.librarian = Librarian(name, age, employee_id)
        print(f"Librarian {name} added to the library.")

    def remove_librarian(self, employee_id):
        if self.librarian and self.librarian._employee_id == employee_id:
            self.librarian = None
            print(f"Librarian with ID {employee_id} removed.")
        else:
            print("Librarian not found.")

    def borrow_book(self, member_id, isbn):
        member = next((m for m in self.members if m._member_id == member_id), None)
        book = next((b for b in self.library._books if b._isbn == isbn), None)
        if member and book:
            member.borrow_book(book)
        else:
            print("Member or Book not found.")

    def return_book(self, member_id, isbn):
        member = next((m for m in self.members if m._member_id == member_id), None)
        book = next((b for b in self.library._books if b._isbn == isbn), None)
        if member and book:
            member.return_book(book)
        else:
            print("Member or Book not found.")
def main():
    libsystem = LibrarySystem()

    libsystem.add_book("Harry Potter","JK ROWLING","B00001")
    libsystem.add_book("Percy Jackson","Rick Riodian","B0002")
    libsystem.set_librarian("teja",29,"L1001")
    libsystem.add_member("pranav",21,"M0001")
    libsystem.add_member("chaitanya",22,"M0002")

    while True:
        print("/n 1. List Books")
        print("2. Add Book to library")
        print("3. Remove Book from library")
        print("4. Borrow Book from library")
        print("5. Add Member to library")
        print("6. Remove Member from library")
        print("7. Add Librarian")
        print("8. Remove Librarian")
        print("9. Exit")
    
        choice = input("Enter Choice:")

        if choice == 1:
            libsystem.display_books()
        
        elif choice == 2:
            title = input("Enter Book Title:")
            author = input("Enter Book Author:")
            isbn = input("Enter ISBN:")
            libsystem.add_book(title,author,isbn)
        
        elif choice == 3:
            isbn = input("Enter ISBN:")
            libsystem.remove_book(isbn)

        elif choice == 4:
            member_id = input("Enter Member ID:")
            isbn = input("Enter ISBN:")
            libsystem.borrow_book(member_id,isbn)
        
        elif choice == 5:
            name = input("Enter Your Name:")
            age = input("Enter your age:")
            member_id = ("Enter your member_id:")
            libsystem.add_member(name,age,member_id)
        
        elif choice == 6:
            member_id = input("Enter your member_id:")
            libsystem.remove_member(member_id)
        
        elif choice == 7:
            name = input("Enter your name:")
            age = input("Enter your age:")
            employee_id = input("enter your employee_id:")
            libsystem.set_librarian(name,age,employee_id)
        
        elif choice == 8:
            employee_id = input("Enter your employee_id:")
            libsystem.remove_librarian(employee_id)
        
        elif choice == 9:
            print("Exiting System")
            break
        
        else:
            print("Invalid Choice")

if __name__ == "__main__":
    main()