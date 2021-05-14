from openpyxl import Workbook
import requests
from bs4 import BeautifulSoup
import openpyxl

url =  'https://unse.daily.co.kr/?p=zodiac'
res = requests.get(url)
bs = BeautifulSoup(res.text,'html.parser')
print(res)
'''
li 전부 가져온다
li밑에 span태그 중에 
class가 tit이면서 
txt가 yearbirth인 것을 만나면 p태그를 출력
'''
li = #code_1 > li:nth-child(2)
wb = openpyxl.Workbook()
# yearbirth = input("출생년도입력:")
span = li.select_one('span').get_text()
txt = li.select_one('p').get_text()
print(span, txt,lis)
lis = bs.select("li")
# for li in lis:
#     if span class =='tit'
    
#     span = li.select_one('span')

    
    
    

        

# ws.append(yearbirth)            
# wb.save('dailyfortune.xlsx')