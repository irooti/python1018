# web2.py
#웹서버에 요청
import urllib.request
#검색
from bs4 import BeautifulSoup
#파일에 저장하기
f = open('c:\\work\\webtoon.txt', 'wt', encoding='utf-8')
#수열을 만드는 함수
for i in range(1, 6):
    url = 'https://comic.naver.com/webtoon/list?titleId=20853&weekday=fri&page=' + str(i)
    print('조립한주소:', url)
    data = urllib.request.urlopen(url)
    soup = BeautifulSoup(data, 'html.parser')

    cartoons = soup.find_all('td', class_='title')
    for item in cartoons:
        title = item.find('a').text
        print(title.strip())

    for item in cartoons:
        title = item.find('a').text
        print(title.strip())
        f.write(title.strip() + '\n')

f.close()
print('웹 크롤잉 종료~~')

'''
data = urllib.request.urlopen('http://comic.naver.com/webtoon/list.nhn?titleId=20853&weekday=fri')
soup = BeautifulSoup(data, 'html.parser')

# <td class="title">
#     <a href="/webtoon/detail?titleId=20853&no=50&weekday=fri" onclick="nclk_v2(event,'lst.title','20853','50')">마음의 소리 50화 &lt;격렬한 나의 하루&gt;</a>
# </td>

cartoons = soup.find_all('td', class_='title')
#10개를 가져왔다면
print('갯수:{0}'.format(len(cartoons)))
#첫번째 방에 있는 아이템 슬라이싱
title = cartoons[0].find('a').text
link = cartoons[0].find('a')['href'] #[속성] 을 가져 온다
print(title)
print(link)

for item in cartoons:
    title = item.find('a').text
    print(title.strip())
'''