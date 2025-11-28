def loan(book_name, book_list):
    book_list.append(book_name)

def back(book_name, book_list):
    book_list.remove(book_name)

def now(book_list):
    for i in range(len(book_list)):
        if len(book_list)==0:
            print('현재 대출된 도서가 없습니다.')
        else:
            print(f'{i+1}. {book_list[i]}')


def library_program():
    booklist = []
    while True:
        temp='''
=====도서 대출 프로그램=====
1. 도서 대출
2. 도서 반납
3. 도서 대출 현황
4. 프로그램 종료

'''
        print(temp)
        try:
            num=int(input('번호 입력: '))
            if num==1:
                book=input('대출할 도서 제목: ')
                loan(book, booklist)
                print(f'{book}이 대출되었습니다.')
            elif num==2:
                book=input('반납할 도서 제목: ')
                back(book, booklist)
                print(f'{book}이 반납되었습니다.')
            elif num==3:
                now(booklist)
            elif num==4:
                print('프로그램 종료')
                break
        except Exception:
            print('지정되지 않은 명령어입니다.')

library_program()


