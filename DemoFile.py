# DemoFile.py

url = "http://www.naver.com/page=?" + str(1)
print(url)

for x in range(1, 6):
    print(x, "*", "=", x * x)

print("---정렬을 변경---")
for x in range(1, 6):
    print(x, "*", x, "=", str(x * x).rjust(3))


print("---0으로 채우기---")
for x in range(1, 6):
    print(x, "*", x, "=", str(x * x).zfill(5))

print("{0:x}".format(10))
print("{0:b}".format(10))
print("{0:f}".format(4/3))
print("{0:.2f}".format(4/3))
print("{0:e}".format(4/3))
print("{0:,}".format(1500000000))

#파일쓰기
f = open("c:\\work\\demo.txt", "wt", encoding='utf-8')
f.write("첫번째라인\n두번째\n세번째\n")
f.close()

if f.closed:
    print("파일이 정상 종료")
else:
    f.close()

#파일일기
f = open("c:\\work\\demo.txt", "rt", encoding='utf-8')
print(f.read())
print(f.tell())
f.seek(0)
print('---한줄씩 읽기---')
print(f.readline())
print(f.readline())
print('---list로 받기---')
f.seek(0)
result = f.readlines()
print(result)
f.close()