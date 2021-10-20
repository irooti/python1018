# DemoDB.py

import sqlite3

#파일을 먼저 생성(일단은 메모리에서 미리 연습)
con = sqlite3.connect('c:\\work\\sample.db')
#SQL 구문을 실행할 커서 객체 생성
cur = con.cursor()
#데이터 구조 만들기 (테이블 스키마)
cur = con.execute("create table PhoneBook (Name text, PhoneNum text);")
#1건 입력
cur.execute("insert into PhoneBook values('derick', '010-111');")
#입력 파라미터 처리
cur.execute('insert into PhoneBook values (?, ?);', ('길동', '010-222')) #튜플로 입력 전달
#N건 입력하기
datalist = (('우치', '010-123'), ('순신', '010-456'))
cur.executemany('insert into PhoneBook values (?, ?)', datalist)

# #결과 검색
cur.execute('select * from PhoneBook;')

print('---fetchone()---')
print(cur.fetchone())
print('---fetchmany(2)---')
print(cur.fetchmany(2))
#cur.execute('select * from PhoneBook;')
print('---fetchall()---')
print(cur.fetchall())

# for row in cur:
#     print(row)

#정상적으로 작업 완료
con.commit()