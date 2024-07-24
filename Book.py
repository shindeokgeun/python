import os
import time
from BookManager import BookManager

class Book:
    all_books = []
 
    def __init__(self, isbn, title, author, publisher, category, price):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.publisher = publisher
        self.category = category
        self.price = price
        self.is_borrowed = False
        
    @classmethod
    def SelectMenu(books):
        os.system("cls")
        print("##########################################")
        print("       도서 관리 프로그램 ver. 0.1.0      ")
        print("##########################################")
        print()
        print("1: 도서 정보 추가")
        print("2: 도서 정보 수정")
        print("3: 도서 정보 삭제")
        print("4: 전체 도서 목록 보기")
        print("0: 종료")
        return input("\n메뉴 선택 : ")
        
    @classmethod
    def main(books):
        while True:
            menu = books.SelectMenu()
            
            if menu == "0":
                break
            elif menu == "1":
                books.addBook()
            elif menu == "2":
                books.changeBook()
            elif menu == "3":
                books.deleteBook()
            elif menu == "4":
                books.viewBook()
            else:
                print("\n잘못 입력하셨습니다. 다시 입력해주세요.")
                time.sleep(1)
        
    @classmethod
    def addBook(books):
        BookManager.add_book(books)
        
    @classmethod    
    def changeBook(books):
        BookManager.change_book(books)
        
    @classmethod
    def deleteBook(books):
        BookManager.delete_book(books)
        
    @classmethod
    def viewBook(books):
        BookManager.view_books(books)
        
if __name__ == "__main__":
    Book.main()
