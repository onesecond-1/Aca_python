class ElectionProgram:
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

    def removeCandidate(self):
        print("=====후보자 등록 취소=====")
        name = input("이름 입력: ")

        if name in self.candidate:
            del self.candidate[name]
            print(f"{name}후보자가 ")

    def election_program(self):
        while True:
            temp = '''
=====반장 선거 프로그램=====
1. 후보자 등록
2. 후보자 등록 현황
3. 후보자 취소
4. 투표하기
5. 득표수 현황
6. 투표 종료하기
'''
            print(temp)