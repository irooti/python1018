# DemoLoop.py

value = 5
while value > 0:
    print(value)
    value -= 1

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for item in lst:
    if item > 5:
        break
    print("item:{0}".format(item))

print("---continue---")
for item in lst:
    if item % 2 == 0:
        continue
    print("item:{0}".format(item)) # {0} 대치


#수열을 생성
print(range(10))
for i in range(5):
    print(i)

print(list(range(10)))
print(list(range(1, 11)))
print(list(range(2000, 2022)))

#리스트 컴ㅍ프리핸션 (리스트 내장, 함축)
lst = list(range(1, 11))
print([i**2 for i in lst if i > 5])
d = {100:"apple", 200:"orange"}
print( [v.upper() for v in d.values()])

#필터링하는 구문
lst = [10, 25, 30]

#조건절로 사용할 함수를 정의
def getBiggerThan20(i):
    return i > 20

iterL = filter(getBiggerThan20, lst)
for item in iterL:
    print(item)