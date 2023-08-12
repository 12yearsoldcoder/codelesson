class Hanglenum:
    def __init__(self, data):
        if type(data) is not str:
            raise TypeError("문자열를 입력해주세요")
        self.num = data

    def __int__(self):
        int = 0
        plusorminus = 1
        if "마이너스" in self.num:
            plusorminus = -1
            self.num = self.num[4:]
        buffer = 0
        l1 = {"천": 1000, "백": 100, "십": 10, "일": 1, "만": 10000, "억" : 100000000}
        l2 = {"영": 0, '일': 1, "이": 2, '삼': 3, "사": 4, '오': 5, '육': 6, "칠": 7, '팔': 8, "구": 9}
        for i in self.num:
            if i in l1:
                if buffer == 0:
                    int += l1[i]
                    continue
                else:
                    int += buffer*l1[i]
                    buffer = 0
                    continue
            buffer += l2[i]

        return plusorminus*(int + buffer)

    def __str__(self):
        string = ""
        l1 = {1000: '천', 100: "백", 10: "십", 1: "일"}
        l2 = {0: "영", 1: '일', 2: "이", 3: '삼', 4: "사", 5: '오', 6: '육', 7: "칠", 8: '팔', 9: "구"}
        if str(self.num)[0] == "-":
            string += "마이너스"
            self.num = int(str(self.num)[1:])
        if self.num in l1.keys():
            return l1[self.num]
        if self.num in l2.keys():
            return l2[self.num]
        while len(str(self.num)) != 1:
            for i in l1.keys():
                front = l2[int(str(self.num)[0])]
                if self.num%i != self.num:
                    if front == "일":
                        string += l1[i]
                    else:
                        string += front + l1[i]
                    self.num %= i
        for j in l2.values():
            if j + "일" in string:
                string = string[:-1]
        return string


a = Hanglenum("이억만이천삼백사십오")
print(int(a))
