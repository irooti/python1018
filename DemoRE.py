# DemoRE.py

import re
result = re.search("[0-9]*th", "39th")
print(result)
print(result.group())

# result = re.match('[0-9]*th', '39th')
# print(result)
# print(result.group())

print(bool(re.search("apple", "this is apple")))
print(bool(re.match("apple", "this is apple")))

print('---우편번호 검색---')
print(bool(re.search("\d{5}", "우리 동네는 52100")))
result = re.search("\d{5}", "우리 동네는 52100")
print(result.group())