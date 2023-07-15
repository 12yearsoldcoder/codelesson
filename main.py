# class 차:
#     def __init__(self, 바퀴, 가격):
#         self.바퀴 = 바퀴
#         self.가격 = 가격
#
# class 자전차(차):
#     def __init__(self, 바퀴, 가격, 구동계):
#         self.바퀴 = 바퀴
#         self.가격 = 가격
#         self.구동계 = 구동계
#
#
# a = 차(2,1000)
# print(a.바퀴)
import datetime

class Human:
    def __init__(self, name, resident_registration_number):
        self.name = name
        self.rrn = resident_registration_number
    def ret_age(self):
        if int(self.rrn[:2]) > 23:
            birth_year = '19' + self.rrn[0:1]
        else:
            birth_year = '20' + self.rrn
        today = datetime.date.today()
        a = ''
        for i in str(today).split('-'):
            a += i
        age = int(a[0:4]) - int(birth_year[0:4])
        if int(a[5:8]) < int(birth_year[5:8]):
            age -= 1
        return age
    def ret_gender(self):
        if self.rrn[7] == '1' or self.rrn[7] == '3':
            return '남자  '
        elif self.rrn[7] == '2' or self.rrn[7] == '4':
            return '여자'
        return '입력이 잘못되었습니다.'
h = Human('이용진', '100807-31234567')
print(h.ret_age())