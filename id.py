# id는 파이선의 명령어 중 하나로 id(object) 형식으로 구현이 된다. 고유값의 일련번호를 찾는것이다.
print(f"a = {id('a')}\nb = {id('b')}\n1 = {id(1)}\n2 = {id(2)}")
print(f"null = {id(None)}")