
import pickle
import datetime


class Member:
    id = 1

    def __init__(self, name, email):
        self.name = name
        self.member_id = Member.id
        Member.id += 1
        self.email = email
        self.borrowed_books = []

    def borrow_book(self, book):
        borrow_date = datetime.datetime.now()
        return_date = borrow_date + datetime.timedelta(weeks=2)
        self.borrowed_books.append(book)
        print(f"{self.name} borrowed '{book.title}' on {borrow_date}. return date: {return_date}")

    def return_book(self, book):
        self.borrowed_books.remove(book)
        print(f"{self.name} returned '{book.title}'")

    def show_info(self):
        print(f"id: {self.member_id} - name: {self.name} - email: {self.email} - borrowed books: {len(self.borrowed_books)}")


class Book:
    total_books = 0

    def __init__(self, title, author, isbn, isborrowed=False):
        Book.total_books += 1
        self.title = title
        self.author = author
        self.isbn = isbn
        self.isborrowed = isborrowed

    def mark_as_borrowed(self):
        self.isborrowed = True

    def mark_as_returned(self):
        self.isborrowed = False

    def display_info(self):
        print(f"Title: {self.title} - Author: {self.author} - borrowed: {self.isborrowed}")


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.members = []

    def add_books(self, book):
        self.books.append(book)
        self.save_data()

    def add_member(self, member):
        self.members.append(member)
        self.save_data()

    def borrow_book(self, member_id, isbn):
        member = None
        for m in self.members:
            if m.member_id == member_id:
                member = m
                break

        book = None    
        for b in self.books:
            if b.isbn == isbn:
                book = b
                break
        
        if member and book:
            if not book.isborrowed:
                member.borrow_book(book)
                book.mark_as_borrowed()
            else:
                print(f"{book} is not available")

        self.save_data()

    def return_book(self, member_id, isbn):
        member = None
        for m in self.members:
            if m.member_id == member_id:
                member = m
                break

        book = None    
        for b in self.books:
            if b.isbn == isbn:
                book = b
                break
        
        member.return_book(book)
        book.mark_as_returned()
        self.save_data()
        

    def show_all_books(self):
        for book in self.books:
            book.display_info()

    def show_all_members(self):
        for member in self.members:
            member.show_info()

    def search_book_by_title(self, title):
        for book in self.books:
            if book.title == title:
                print("Yes, the book is available!")
                return book
        print("Book not found.")
        return None

    def search_member_by_name(self, name):
        for member in self.members:
            if member.name == name:
                print("Member found")
                return member
        print("Member not found.")
        return None

    def report_books_status(self):
        borrowed = 0
        for book in self.books:
            if book.isborrowed:
                borrowed += 1
        available = len(self.books) - borrowed
        print(f"Borrowed books: {borrowed} | Available books: {available}")


    def save_data(self):
        with open("library_data.pkl", "wb") as file:
            pickle.dump(self, file)

    @staticmethod
    def load_data():
        try:
            with open("library_data.pkl", "rb") as file:
                return pickle.load(file)
        except FileNotFoundError:
            return Library("My Library")


class StudentMember(Member):
    def borrow_book(self, book):
        if len(self.borrowed_books) < 3:
            super().borrow_book(book)
        else:
            print("You are allowed to borrow a maximum of three books.")


class TeacherMember(Member):
    def borrow_book(self, book):
        if len(self.borrowed_books) < 5:
            super().borrow_book(book)
        else:
            print("You are allowed to borrow a maximum of five books.")



library = Library.load_data()
book1 = Book("Harry Potter and the Philosopher's Stone","J.K.Rowling",1338878921)
book2= Book("Harry Potter and the Chamber of Secrets","J.K.Rowling",1338878922)
book3= Book("Harry Potter and the Prisoner of Azkaban","J.K.Rowling",1338878923)
book4= Book("Harry Potter and the Goblet of Fire","J.K.Rowling",1338878924)


member1 = StudentMember("member1", "member1@gmail.com")
member2 = StudentMember("member2", "member2@gmail.com")
member3 = StudentMember("member3", "member3@gmail.com")
member4 = TeacherMember("member4", "member3@gmail.com")

member1.borrow_book(book1)
member1.show_info()

library1 = Library("library1")
library1.add_books(book1)
library1.add_books(book2)
library1.add_books(book3)
library1.add_books(book4)

library1.add_member(member1)
library1.add_member(member2)
library1.add_member(member3)
library1.add_member(member4)

library1.borrow_book(1, 1338878921)
library1.borrow_book(1, 1338878922)
library1.borrow_book(1, 1338878923)
library1.borrow_book(1, 1338878924)
library1.borrow_book(4, 1338878924)

library1.show_all_books()