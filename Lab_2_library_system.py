class Book:
    def __init__(self, title: str, author: str, book_id: int):
        self.title = title
        self.author = author
        self.book_id = book_id
        self.is_available = True

    def __str__(self):
        status = "Available" if self.is_available else "Borrowed"
        return f"[{self.book_id}] {self.title} by {self.author} - {status}"


class Library:
    def __init__(self, name: str):
        self.name = name
        self.books = []

    def add_book(self, title: str, author: str, book_id: int):
        """Add a new book to the library."""
        book = Book(title, author, book_id)
        self.books.append(book)
        print(f"Book '{title}' added successfully.")

    def display_books(self):
        """Display all books in the library."""
        if not self.books:
            print("No books in the library.")
            return

        print(f"\n=== Books in {self.name} ===")
        for book in self.books:
            print(book)
        print()

    def borrow_book(self, book_id: int):
        """Borrow a book by its ID."""
        for book in self.books:
            if book.book_id == book_id:
                if book.is_available:
                    book.is_available = False
                    print(f"You have successfully borrowed '{book.title}'.")
                else:
                    print(f"Sorry, '{book.title}' is already borrowed.")
                return
        print(f"Book with ID {book_id} not found.")

    def return_book(self, book_id: int):
        """Return a borrowed book by its ID."""
        for book in self.books:
            if book.book_id == book_id:
                if not book.is_available:
                    book.is_available = True
                    print(f"You have successfully returned '{book.title}'.")
                else:
                    print(f"'{book.title}' was not borrowed.")
                return
        print(f"Book with ID {book_id} not found.")


# ---------- Example Usage ----------
if __name__ == "__main__":
    # Create a library
    library = Library("City Central Library")

    # Add some books
    library.add_book("The Alchemist", "Paulo Coelho", 101)
    library.add_book("Atomic Habits", "James Clear", 102)
    library.add_book("Rich Dad Poor Dad", "Robert Kiyosaki", 103)
    library.add_book("The Psychology of Money", "Morgan Housel", 104)

    # Display all books
    library.display_books()

    # Borrow a book
    library.borrow_book(102)
    library.borrow_book(104)

    # Display books after borrowing
    library.display_books()

    # Try to borrow an already borrowed book
    library.borrow_book(102)

    # Return a book
    library.return_book(102)

    # Final status
    library.display_books()