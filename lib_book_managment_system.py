#Library Book Management System
#Scenario: Create a program to manage a library's book inventory. Each book has details like
#title, author, genre, and availability status. Implement the following functionalities:
#Store the books in a List of custom objects.
#Allow users to search for books by title, author, or genre using string matching.
#Add a method to borrow a book (mark it as unavailable). Throw an exception if the book is already borrowed.
#Add a method to return a book (mark it as available).
#Handle cases where a user tries to borrow or return a book that doesn’t exist.

#class to make book object
class Book:
    def __init__(self, title, author, genre, status):
        """
        title : str
        author : str
        genre : str
        status : bool
        """
        self.title = title
        self.author = author
        self.genre = genre
        self.status = status

    def __str__(self):
        return self.title    


#creating a sample database
library = [
    Book("1984", "George Orwell", "Dystopian", True),
    Book("To Kill a Mockingbird", "Harper Lee", "Classic", False),
    Book("The Great Gatsby", "F. Scott Fitzgerald", "Classic", True),
    Book("The Catcher in the Rye", "J.D. Salinger", "Fiction", False),
    Book("Pride and Prejudice", "Jane Austen", "Romance", True),
    Book("The Hobbit", "J.R.R. Tolkien", "Fantasy", True),
    Book("Fahrenheit 451", "Ray Bradbury", "Dystopian", False),
    Book("The Alchemist", "Paulo Coelho", "Adventure", True),
    Book("Moby-Dick", "Herman Melville", "Adventure", False),
    Book("Jane Eyre", "Charlotte Brontë", "Gothic Fiction", True)
]


#input/output functions
def book_searcher(field :object,key :str) -> None:
    """
    Searching the book in the library based on the keyword and field given

    Args: field (obj)
          key (str)
    """
    found = False
    for book in library:
        attr = getattr(book, field)
        if key.lower() in attr.lower():
            status = "Available" if book.status else "Borrowed"
            print(f"{book.title} by {book.author} | Genre: {book.genre} | Status: {status}")
            found = True
    if not found:
        print("No matching books found.")


def search_book(choice :int) -> None:
    """
    This func take input from user and use book_searcher func to find the book on specified keyword

    Args: choice (int)
    """
    if type(choice) != int:
        print("Please enter a valid input")
    elif choice == 1:
        keyword = input("Enter the title: ")
        book_searcher("title", keyword)
    elif choice == 2:
        keyword = input("Enter the author's name: ")
        book_searcher("author", keyword)
    elif choice == 3:
        keyword = input("Enter the genre: ")
        book_searcher("genre", keyword)
    else:
        print("Invalid choice")

#borrowing the book
def borrow_book() -> None:
    """
    this function update the status(borrowed or not) of books in the library 
    status true -> false
    """
    title = input("Enter the title of book you want to borrow: ")
    for book in library:
        if book.title.lower() == title.lower():
            if book.status:
                book.status = False
                print(f"You have borrowed {book.title}.")
                return
            else:
                print(f"{book.title} is already borrowed.")
                return
    print("Book not found")        

#returning the book
def return_book() -> None:
    """
    this function update the status(borrowed or not) of books in the library 
    status false -> true
    """
    title = input("Enter the title of the book to return: ")
    for book in library:
        if book.title.lower() == title.lower():
            if not book.status:
                book.status = True
                print(f"You have returned '{book.title}'.")
                return
            else:
                print(f"'{book.title}' was not borrowed.")
                return
    print("Book not found")          

def input_manager(user_input :int) -> bool:
    """
    This func take input from user and does the specief task by the user

    Args: user_input (int)

    Return: bool value
    """
    try:
        user_input = int(user_input)
    except ValueError:
        print("Please enter a valid input.")
        return True

    if user_input == 1:
        while True:
            print("1.Search by title")
            print("2.Search by Author")
            print("3.Search by Genre")
            print("4.Back")
            choice = input("enter the command: ")
            try:
                choice = int(choice)
                if choice == 4:
                    break
                search_book(choice)
            except ValueError:
                print("Invalid input. Please enter a number.")
    elif user_input == 2:
        borrow_book()
    elif user_input == 3:
        return_book()    
    elif user_input == 4:
        return False
    return True    


print("Welcome to the Library Book Management System: ")

while True:
    print("What can we do for you: ")
    print("1.Search a Book")
    print("2.Borrow a Book")
    print("3.Return a Book")
    print("4.Exit")

    user_input = input("enter the command: ")
    input_manager(user_input)
