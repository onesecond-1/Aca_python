#클래스 선언
'''
클래스 이름: Player
멤버변수: 이름(name), 나이(age), 직업(job)
멤버 메서드:
생성자 1개(이름, 나이, 직업 초기화)
이름 수정(이름은 nameUpdate이며, 파라미터를 활용하여 name의 값을 수정)
나이 수정(이름은 ageUpdate이며, 파라미터를 활용하여 age의 값을 수정)
직업 수정(이름은 jobUpdate이며, 파라미터를 활용하여 job의 값을 수정)
출력(이름은 introduce이며, name, age, job을 출력)
'''
# 다시 생각하기
"""
class Player:
    def __init__(self, name, age, job):
        self.name=""
        self.age=0
        self.job=""
    def set_name(self, name):
        self.name=name
    def set_age(self, age):
        self.age=age
    def set_job(self, job):
        self.job=job
    def introduce(self):
        print(f"제 이름은 {name}이고, 나이는 {age}, 직업은 {job}입니다.")
"""



class Player:
    def __init__(self):
        self.name=""
        self.age=0
        self.job=""
    def nameUpdate(self, name):
        self.name=name
    def ageUpdate(self, age):
        self.age=age
    def jobUpdate(self, job):
        self.job=job
    def introduce(self):
        print(f"제 이름은 {name}이고, 나이는 {age}, 직업은 {job}입니다.")
selfIntro=Player()
selfIntro.nameUpdate("김철수")
selfIntro.ageUpdate(20)
selfIntro.jobUpdate("대학생")
selfIntro.introduce()
