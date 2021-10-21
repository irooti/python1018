# web1.py
from bs4 import BeautifulSoup

#웹페이지를 로딩
#메서드나 함수를 메서드체인(연속으로 호출)
page = open('c:\\work\\test01.html', encoding='utf-8').read()
#검색이 용이한 객체 (html태그 문서를 검색-상수)
soup = BeautifulSoup(page, 'html.parser') #옵션 4개 
#soup = BeautifulSoup(page, 'lxml') 해석 엔진
#print(soup.prettify()) #문서 그대로 보여줘

#<p> 몽땅 검색
#print(soup.find_all('p')) # 리스트로 담아 준다
#<a> 태그 잡아와~~~
#print(soup.find_all('a'))
#print(soup.find('a'))

#검색 조건: <p class='outer-text'>
#파이썬의 키워드로 class가 제공 그래서 이름 충동 class_
#print(soup.find_all('p', class_='outer-text'))

#태그 안쪽에 컨텐츠만 가져오기
for item in soup.find_all('p'):
    data = item.text.strip()
    data = data.replace('\n', '')
    data = data.replace('\t', '')
    print(data)