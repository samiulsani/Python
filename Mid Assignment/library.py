# 1. Create the Library class
class Library:
    book_list = []

    @classmethod
    def entry_book(cls, book):
        cls.book_list.append(book)

# 2. Create the Book class and 3. Initialize Book Object
class Book:
    def __init__(self, book_id, title, author):
        self.__book_id = book_id
        self.__title = title
        self.__author = author
        self.__availability = True
        Library.entry_book(self)

# 4. Implement borrow_book() method
    def borrow_book(self):
        if self.__availability:
            self.__availability = False
            print(f"Successfully borrowed '{self.__title}'.")
        else:
            print(f"Sorry, '{self.__title}' is not available now.")

# 5. Implement return_book() method
    def return_book(self):
        if not self.__availability:
            self.__availability = True
            print(f" '{self.__title}' Book return.")
        else:
            print(f"Book '{self.__title}' not borrowed.")

# 6. Implement view_book_info() method
    def view_book_info(self):
        availability_status = "Available" if self.__availability else "Not Available"
        print(f"Book ID: {self.__book_id}, Book Name: {self.__title}, Author Name: {self.__author}, Availability: {availability_status}")

    def get_book_id(self):
        return self.__book_id

    def is_available(self):
        return self.__availability

def view_all_books():
    for book in Library.book_list:
            book.view_book_info()

def find_book_by_id(book_id):
    for book in Library.book_list:
        if book.get_book_id() == book_id:
            return book
    return None

# 7. Menu System and 8. Error Handling
def menu():
    while True:
        print("\nSelect Your Option:")
        print("1. View All Books")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            view_all_books()
        elif choice == "2":
            book_id = input("Enter Book ID to borrow: ")
            book = find_book_by_id(book_id)
            if book:
                book.borrow_book()
            else:
                print("Invalid Book ID. Please try again.")
        elif choice == "3":
            book_id = input("Enter Book ID to return: ")
            book = find_book_by_id(book_id)
            if book:
                book.return_book()
            else:
                print("Invalid Book ID. Please try again.")
        elif choice == "4":
            print("Exit. Thank you.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":

    Book("101", "Bonus", "Tipu sultan")
    Book("102", "propaganda", "Sajid Hasan")
    Book("103", "Economics", "Farhan Tushar")
    Book("104", "Megnadobodh Kabbo", "Michael Madhusudan Dutt")
    Book("105", "Jibon Amar bon ", "Mahmudul Haq")
    Book("106", "Sesher Kobita ", "Robi Tagore")

    menu()
