import time

class BookManager:
    @staticmethod   
    def add_book(books):
        print("\n-------도서 정보 추가-------")
        isbn = input("ISBN: ")
        title = input("제목: ")
        author = input("저자: ")
        publisher = input("출판사: ")
        category = input("카테고리: ")
        price = input("가격: ")
    
        book = {
            "isbn": isbn,
            "title": title,
            "author": author,
            "publisher": publisher,
            "category": category,
            "price": price,
            "is_borrowed": False
        }
    
        books.all_books.append(book)
        print("\n도서가 추가되었습니다.")
        time.sleep(1)
        
    @staticmethod     
    def change_book(books):
        print("\n-------도서 정보 수정-------")
        isbn = input("\n수정할 도서의 ISBN을 입력해주세요 : ")
        
        for book in books.all_books:
            if book["isbn"] == isbn:
                for key, value in book.items():
                    print(f"\n현재 도서 정보 {key} : {value}")
                    
                    print("\n수정할 항목을 선택하세요 ")
                    print(f"1. 제목 (현재: {book['title'] if book['title'] else '정보 없음'})")
                    print(f"2. 저자 (현재: {book['author'] if book['author'] else '정보 없음'})")
                    print(f"3. 출판사 (현재: {book['publisher'] if book['publisher'] else '정보 없음'})")
                    print(f"4. 카테고리 (현재: {book['category'] if book['category'] else '정보 없음'})")
                    print(f"5. 가격 (현재: {book['price'] if book['price'] else '정보 없음'})")
                    

                    choice = input("메뉴 선택 (1-5) : ")
                    
                    if choice == '1':
                        book['title'] = input("\n제목 : " )
                    elif choice == '2':
                        book['author'] = input("\n저자 : ")
                    elif choice == '3':
                        book['publisher'] = input("\n출판사 : ")
                    elif choice == '4':
                        book['category'] = input("\n카테고리 : ")
                    elif choice == '5':
                        book['price'] = input("\n가격 : ")
                    else:
                        print("잘못 입력하셨습니다. 다시 입력해주세요")
                        time.sleep(1)
                        return

                    print("\n수정된 도서 정보:")
                    for key, value in book.items():
                        print(f"{key}: {value}")
            
                    print("\n도서 정보가 성공적으로 수정되었습니다.")
                    time.sleep(3)
                    return

        print(f"ISBN {isbn}에 해당하는 도서를 찾을 수 없습니다.")
        
    @staticmethod   
    def delete_book(books):
        print("\n-------도서 정보 삭제-------")
        isbn = input("삭제할 도서의 ISBN을 입력해주세요 : ")
        for book in books.all_books:
            if book['isbn'] == isbn:
                books.all_books.remove(book)
                print(f"\nISBN {isbn}의 도서가 삭제되었습니다.")
                time.sleep(1.5)
                return
           
    @staticmethod    
    def view_books(books):
        print("\n-----전체 도서 목록 보기-----")
        if not books.all_books:
            print("등록된 도서가 없습니다")
        else:
            for index, book in enumerate(books.all_books, start=1):
                print(f"\n[{index}번째 책]")
                print(f"ISBN: {book['isbn'] if book['isbn'] else '정보 없음'}")
                print(f"제목: {book['title'] if book['title'] else '정보 없음'}")
                print(f"저자: {book['author'] if book['author'] else '정보 없음'}")
                print(f"출판사: {book['publisher'] if book['publisher'] else '정보 없음'}")
                print(f"카테고리: {book['category'] if book['category'] else ' 정보 없음'}")
                print(f"가격: {book['price'] if book['price'] else '정보 없음'}")
                print(f"대출 상태: {'대출 중' if book['is_borrowed'] else '대출 가능'}")
                print("-" * 28)
    
        input("\n메인 메뉴로 돌아가려면 Enter를 누르세요")