#split
a = "hello world"
print(a.split())

ticker = "btc_krw"
print(ticker.split("_"))

date = "2020-05-01"
print(date.split("-"))

#rstrip
data = "039490          "
print(data.rstrip())

# 변수에 다음과 같이 문자열과 정수가 바인딩되어 있을 때 f-string을 사용해서 다음과 같이 출력해보세요.
name1 = "김민수"
age1= 10
name2 = "이철희"
age2 = 13

print(f'이름:{name1} 나이:{age1}' )
print(f'이름:{name2} 나이:{age2}' )

# replace
# 삼성전자의 상장주식수가 다음과 같습니다. 컴마를 제거한 후 이를 정수 타입으로 변환해보세요.
상장주식수 = "5,969,782,550"
comma = 상장주식수.replace(',','')
typeint = int(comma) # int(i)함수는 정수타입으로 형변환
print(typeint)

# strip
data = "            삼성전자            "
print(data.strip())

# list
movie_rank = ["닥터 스트레인지", "스플릿", "럭키"]
print(movie_rank)

movie_rank.append("배트맨") # .append(i)리스트 원소추가
print(movie_rank)

movie_rank.insert(1,"슈퍼맨") #.insert(인덱스위치,i) 리스트수정
print(movie_rank)

del movie_rank[3] # del list[인덱스위치] 리스트원소 삭제
print(movie_rank)

del movie_rank[1]
del movie_rank[2] # 다중삭제
print(movie_rank)

lang1 = ["c","c++","java"]
lang2 = ["python","go","c#"]
langs = lang1 + lang2  # 리스트 덧셈
print(langs)

#리스트 최댓값 최솟값 구하기
nums = [1,2,3,4,5,6,7]
print(min(nums))    #min(i) i의 최솟값 함수
print(max(nums))    #max(i) i의 최댓값 함수

print(sum(nums)) #sum(i) i의 합

cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "쏘세지", "라면", "팥빙수", "김치전"]
print(len(cook)) # len(i) i의 데이터개수 구하는 함수

avg = sum(nums)/len(nums) # 응용
print(avg)

#  날짜 정보를 제외하고 가격 정보만을 출력하라. 
price = ['20180728',100,130,140,150,160,170]
print(price[1:]) #슬라이싱

numoddeven = [1,2,3,4,5,6,7,8,9,10]
print(numoddeven[::2]) # [::int] int는 오프셋
print(numoddeven[1::2]) #[index::offset]시작인덱스위치1 오프셋2
print(numoddeven[::-1]) #인덱스값이 -1부터 -2,-3,-4...
# 리스트 역순정렬은 [::-1]

interest = ['삼성전자','LG전자','Naver']
print(interest[0],interest[2])

interesting = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print(''.join(interesting)) # join 메서드
print('/'.join(interesting)) # join 메서드
print('\n'.join(interesting)) # join 메서드

string = "삼성전자/LG전자/Naver"
print(string.split('/'))

data = [2,4,3,1,5,10,9]
up = data.sort()    # i.sort()리스트 오름차순
up2 = sorted(data)  # sorted(i) 리스트 오름차순
print(up)
print(up2)









