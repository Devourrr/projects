'''파이썬 300제'''
# 문자열
 
lang = 'python' #  문자열 인덱싱
print(lang[0], lang[2])

license_plate = '24가 2210' # 문자열 슬라이싱
print(license_plate[-4:])

string = "홀짝홀짝홀짝" #  문자열 인덱싱
print(string[::2])

string = "python" # 문자열 슬라이싱
print(string[::-1])

phone_number = '010-1111-2222' #  문자열 치환
phone_number1 = phone_number.replace('-',' ')
print(phone_number1)

#문자열 다루기
phone_number2 = phone_number.replace('-','')
print(phone_number2)

# 문자열 다루기
url =  "http://sharebook.kr"
url_split = url.split('.')
print(url_split[-1])

# 문자열은 immutable
# lang = 'python'
# lang[0] = 'p'
# print(lang) 문자열은 수정할 수 없습니다. 
# 실행 결과를 확인해보면 문자열이 할당(assignment) 메서드를 지원하지 않음을 알 수 있습니다.

# replace 메서드
string = 'abcdfe2a354a32a'
string = string.replace('a',"A")
print(string)

string = 'abcd'
string.replace('b','B')
print(string)
# abcd가 그대로 출력됩니다. 왜냐하면 문자열은 변경할 수 없는 자료형이기 때문입니다. 
# replace 메서드를 사용하면 원본은 그대로 둔채로 변경된 새로운 문자열 객체를 리턴해줍니다.

#문자열 합치기
a = '3'
b = '4'
print(a+b) # 두 문자열에 대해 덧셈 기호는 문자열의 연결을 의미합니다.
#문자열 곱하기
print("Hi"*3)
print("-"*80)

t1 = 'python'
t2 = 'java'
t3 = t1+ ' ' + t2+' '
print(t3*4)

# 문자열 출력 # % formatting
name1 = "김민수" 
age1 = 10
name2 = "이철희"
age2 = 13
print("이름:%s 나이:%d" % (name1,age1))
print("이름:%s 나이:%d" % (name2,age2))

#format 메서드 사용
print("이름: {} 나이: {}".format(name1,age1))
print("이름: {} 나이: {}".format(name2,age2))

#f-string사용
print(f"이름:{name1} 나이:{age1}")
print(f"이름:{name2} 나이:{age2}")
# 컴마제거, 문자열 정수타입으로 변환
상장주식수 = "5,969,782,550"
# 정수형으로 타입을 변환하려면 int( ) 함수를 사용하면 됩니다.
# 이때 숫자 형태의 문자열에 컴마가 있는 경우 바로 변환된지 않습니다. 
# 먼저 문자열의 replace 메서드로 컴마를 제거한 후 변환해야합니다.
컴마제거 = 상장주식수.replace(',','')
타입변환 = int(컴마제거)
print(타입변환,type(타입변환))

# 문자열 슬라이싱
분기 = "2020/03(E) (IFRS연결)"
print(분기[:7])

#  strip 메서드
data = "        삼성전자        "
data1= data.strip() #strip메서드로 좌우 공백 제가
print(data1)    # 공백 제거된 새로운 문자열로 반환

#  upper 메서드
ticker = "btc_krw"
ticker1 = ticker.upper() #  원본 문자열은 유지되고 대문자로 변경된 새로운 문자열 객체가 반환
print(ticker1) # 반환된 새로운 객체를 새로운 변수로 바인딩한 후 이를 print 함수로 출력
ticker2 = "BTC_KRW"
#lower 메서드
ticker3 = ticker2.lower()
print(ticker3)

#  capitalize 메서드
a = "hello"
a = a.capitalize()
print(a)

# endswith 메서드
file_name = "보고서.xlsx"
file_name.endswith("xlsx.xls")
print(file_name)

# startswith 메서드
file_name = "2020_보고서.xlsx"
file_name.startswith("2020")
print(file_name)

#split 메서드
a = 'hello world'
a.split() # 문자열의 split() 메서드를 사용하면 문자열에서 공백을 기준으로 분리해줍니다.
print(a)
ticker = "btc_krw"
ticker.split('_')
print(ticker)

date = "2020-05-01"
date.split("-")
print(date)

#rstrip 메서드
data = '039490      '
data = data.rstrip() # rstrip() 메서드를 사용하면 오른쪽 공백이 제거된 새로운 문자열 객체가 반환됩니다.
print(data) # 그 값을 data라는 변수가 새로 바인딩합니다.
# 기존의 공백이 포함된 문자열은 메모리에서 자동으로 삭제됩니다.

#리스트생성
movie_rank = ["닥터스트레인지", "스플릿","럭키"]
print(movie_rank)

#리스트에 원소 추가
movie_rank.append('배트맨')
print(movie_rank)

movie_rank.insert(1,'슈퍼맨') # 리스트의 insert(인덱스, 원소) 메서드를 사용하면 특정 위치에 값을 끼어넣기 할 수 있습니다.
print(movie_rank)

del movie_rank[3] # 리스트에서 어떤 값을 삭제하면 남은 값들은 새로 인덱싱됩니다. 
del movie_rank[3] # 여러 값을 삭제할 때는 어떤 값이 먼저 삭제된 후 남은 원소들에 대해서 순서를 새로 고려한 후 삭제해야 합니다.
print(movie_rank)

lang1 = ["C", "C++","JAVA"]
lang2 = ["Python", "Go", "C#"]
lang3 = lang1 + lang2 # 두 리스트를 더하면 새로운 리스트가 생성됩니다.
print(lang3)

nums = [1, 2, 3, 4, 5, 6, 7,80.4]
print(min(nums)) # 리스트 최소값 출력
print(max(nums)) # 리스트 최대값 출력

print(sum(nums)) # 리스트 합 출력

cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "쏘세지", "라면", "팥빙수", "김치전"]
print(len(cook)) # 리스트 인덱스 개수 출력

# 응용 리스트의 평균을 출력하라.
avg = sum(nums) / len(nums)
avg1 = sum(nums) % len(nums)
print(avg)
print(avg1)

# 리스트 슬라이싱
price = ['20180728', 100, 130, 140, 150, 160, 170]
print(price[1:])


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[::2]) # 리스트 홀수 출력
print(nums[1::2]) # 리스트 짝수 출력
print(nums[::-1]) # 리스트 역순 출력

# 리스트 인덱스 획득
interest = ['삼성전자', 'LG전자', 'Naver']
print(interest[:2])
print(interest[0], interest[2]) # 괄호없이

#join 메서드
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print(''.join(interest)) # 인덱스를 ''없이 획득
print('/'.join(interest)) #join 메서드를 사용하면 리스트를 문자열로 붙일 수 있습니다.

print('\n'.join(interest)) # join 줄바꿈
print('\t'.join(interest)) # join 띄어쓰기

string = "삼성전자/LG전자/Naver"
interest = string.split("/")
print(interest)

data = [2, 4, 3, 1, 5, 10, 9]
data.sort()
print(data) # 리스트 오름차순
data2 = sorted(data) # 리스트 오름차순2
print(data2)






