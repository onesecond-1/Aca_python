'''
반장 선거 프로그램
Election이라는 클래스를 선언하려고 한다.
해당 클래스는 생성자가 존재하며, 생성자 실행 시 candidate라는 딕셔너리 멤버 변수를
선언 및 빈 딕셔너리로 초기화한다.
해당 클래스에는 몇가지 메서드가 존재한다.
enroll이라는 메서드가 존재하며, 해당 메서드는 후보 등록을 의미한다. 따라서, enroll 실행 시 하나의 매개변수(= 후보자 이름)를 문자열로 받으며, candidate 멤버 변수에 매개변수를 key로 value는 0으로 추가한다.
vote라는 메서드가 존재하며, 해당 메서드는 투표를 의미한다. 따라서 vote 실행 시 하나의 매개변수(= 후보자 이름)를 문자열로 받으며, 매개변수의 값이 딕셔너리 안에 존재한다면, 해당 key의 value를 1 증가시키고, 매개변수의 값이 딕셔너리 안에 존재하지 않다면 "해당 후보자는 등록되지 않았습니다."라고 출력한다.
deadline이라는 메서드가 존재하며, 해당 메서드는 투표 종료를 의미한다. 따라서 deadline 실행 시 딕셔너리 안에 저장된 가장 큰 value 값의 key를 반환하여 반장으로 당선된 후보자 이름을 반환하는 기능을 한다.
'''
'''
추가할 기능
1. 후보자 등록 상황
2. 득표수 현황

기능 수정 사항
1. deadline 메서드 실행 시, 동률의 상황 대처
'''
class Election:
    def __init__(self):
        self.candidate= {}
        # 빈 딕셔너리 멤버 변수를 만드는 것이기 때문에 매개변수 안 만들고 candidate가 딕셔너리임을 표현해주면 됨.

    def enroll(self): # 후보자 선정하고 해당 인원의 투표수 기록할 수 있도록
        enrollname=input("후보 이름: ")
        self.candidate[enrollname]=0
        # 후보자가 표를 받은 상태라면 key가 0으로 초기화되는 상태

    def vote(self): # 후보자의 투표수를 1 올림
        votename=input("투표할 후보 이름: ")
        if votename in self.candidate:
            # votename += 1 # key 가져와서 수정
            self.candidate[votename] = self.candidate.get(votename) + 1
        else:
            print("해당 후보자는 등록되지 않았습니다.")

    def deadline(self):
        # 현재 value를 활용중으로 key의 값을 수정하도록
        deadlinename = 0
        for i in range(len(self.candidate)):
            if i > deadlinename:
                deadlinename=i