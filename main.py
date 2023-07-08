# class T:
#     def __init__(self, x):
#         self.x = x
#     def print_x(self):
#         print(self.x)
#
# t = T(5)
# t.print_x()
#
# class AAA:
#     share = 10
#     def __init__(self,value):
#         self.unique = value
#
# a = AAA(1)
# b = AAA(2)
# print(a == b)
# print(a.unique == b.unique)
# print(a.share == b.share)
# AAA.share = 0
# print(a.share == b.share)
# a.share = 5
# print(a.share == b.share)
#
# class Parent_class:
#     def method(self):
#         pass
#
# class Child_class(Parent_class):
#     def __init__(self, str):
#         self.string = str
#     Parent_class.method()
#
# class Human:
#     def __init__(self,name, age, gender):
#         # print("응애응애")
#         self.name = name
#         self.age = age
#         self.gender = gender
#     def __del__(self):
#         print("나의 죽음을 알리자 마라")
#     def who(self):
#         print(f"이름: {self.name}\n나이: {self.age}\n성별: {self.gender}")
#     def setInfo(self,name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
#     def __repr__(self):
#         return f"제 이름은 {self.name}이고 나이는 {self.age}인 {self.gender}입니다."
# areum = Human("모름", 0, '모름')
# areum.who()
# # areum = Human("조아름",25, "여자")
# areum.name = "조아름"
# areum.age = 25
# areum.gender = "여자"
# areum.who()
# del areum

# class OMG :
#     def print(self ) :
#         print("Oh my god")
#
# myStock = OMG()
# myStock.print()
#
# class Stock:
#     def __init__(self, Stock_name, Stock_num, PER: float, PBR: float, dividend: float):
#         self.Stock_name = Stock_name
#         self.Stock_num = Stock_num
#         self.PER = PER
#         self.PBR = PBR
#         self.dividend = dividend
#
#     def set_name(self, Stock_name):
#         self.Stock_name = Stock_name
#
#     def set_code(self, Stock_num):
#         self.Stock_num = Stock_num
#
#     def set_PER(self, PER):
#         self.PER = PER
#
#     def set_PBR(self, PBR):
#         self.PBR = PBR
#
#     def set_dividend(self, dividend):
#         self.dividend = dividend
#
#     def get_name(self):
#         return self.Stock_name
#
#     def get_num(self):
#         return self.Stock_num
#
#     def get_PER(self):
#         return self.PER
#
#     def get_PBR(self):
#         return self.PBR
#
#     def get_배당수익률(self):
#         return self.dividend
#
# Samsung = Stock("삼성전자", "005930", 15.79, 1.33, 2.83)
# Hyundai = Stock("현대차", "005380", 8.70, 0.35, 4.27)
# LG = Stock("LG전자", "066570", 317.34, 0.69,	1.37)
#
# 주식종목리스트 = [Samsung, Hyundai, LG]
#
# for Stocks in 주식종목리스트:
#     print(Stocks.Stock_num, Stocks.PER)
#
import random
class Bank:
    cnt = 0
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.Bank_name = "SC은행"
        self.account_number = f"{str(random.randint(0,999)).zfill(3)}-{str(random.randint(0,99)).zfill(2)}-{str(random.randint(0,999999)).zfill(6)}"
        Bank.cnt += 1
    def Balance(self):
        Balance = ""
        for j, i in enumerate(str(self.balance)[::-1]):
            if j % 3 == 0:
                Balance += ","
            Balance += i
        return Balance[::-1].strip(",")


    @classmethod
    def get_account_num(cls):
        print(Bank.cnt)

    def deposit(self, amount):
        if amount == 0:
            print("1원 이상의 금액만 입금할 수 있습니다.")
            self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"잔액이 부족합니다. 현재 잔액: {self.balance}원")
        else:
            self.balance -= amount
            print(f"출금 되었습니다. 현재 잔액: {self.balance}원")

    def display_info(self):
        print(f"은행이름: {self.Bank_name}\n예금주: {self.name}\n계좌번호: {self.account_number}\n잔고: {self.Balance()}")




Kim = Bank("김김김", 100000)
Bank.get_account_num()
Park = Bank("박박빡", 10000000)
Kim.display_info()