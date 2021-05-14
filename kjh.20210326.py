'''파이썬 300제 51~70'''
movie_rank = ["닥터 스트레인지","스플릿","럭키"] 
# 영화 제목은 문자열로 표현 가능합니다. 여러 개의 값을 저장하기 위해 파이썬 리스트 자료형을 사용합니다.
print(movie_rank)
movie_rank.append("배트맨")
print(movie_rank)
movie_rank = ["닥터 스트레인지","스플릿","럭키"] 
movie_rank.append("배트맨")
movie_rank.insert(1,"슈퍼맨") # 리스트의 insert(인덱스, 원소) 메서드를 사용하면 특정 위치에 값을 끼어넣기 할 수 있습니다.
print(movie_rank)
movie_rank = ["닥터 스트레인지","슈퍼맨","스플릿","배트맨"] 
del movie_rank[2]
del movie_rank[2]
print(movie_rank)
# del을 이용하여 리스트에서 원소를 삭제할 수 있습니다. 리스트에서 어떤 값을 삭제하면 남은 값들은 새로 인덱싱됩니다. 
# 따라서 여러 값을 삭제할 때는 어떤 값이 먼저 삭제된 후 남은 원소들에 대해서 순서를 새로 고려한 후 삭제해야 합니다.
lang1 = ["C", "C++", "JAVA"]
lang2 = ["Python", "Go", "C#"]
langs = lang1 + lang2
print(langs)
nums = [1,2,3,4,5,6,7]
print("max", max(nums))
print("min", min(nums))
nums = [1,2,3,4,5]
print("sum",sum(nums))
cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "쏘세지", "라면", "팥빙수", "김치전"]
print(len(cook)) # len 데이터의 개수
nums = [1, 2, 3, 4, 5]
average = sum(nums) / len(nums) # sum = 합 len = 개수 average = 평균 
print(average)

# price = ['20180728', 100, 130, 140, 150, 160, 170]
# print(price[1:]) #슬라이싱 기억
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[::2]) #슬라이싱 홀수
print(nums[1::2]) #슬라이싱 짝수
nums = [1, 2, 3, 4, 5]
print(nums[::-1]) # 슬라이싱 역순
interest = ['삼성전자', 'LG전자', 'Naver'] #슬라이싱 고르기
print(interest[0],[2])
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print(" ".join(interest)) #join ""
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print("/".join(interest)) # join"/"
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print("\n".join(interest)) #join "\n"
string = "삼성전자/LG전자/Naver" 
interest = string.split("/") #split("/")
print(interest)
data = [2, 4, 3, 1, 5, 10, 9] # .sort()
data.sort()
print(data)
#수업시작
#2단계 up&down 게임
# correct = 5 # 정답
# answer = int(input('숫자입력: '))  #input결과는  

# if correct > answer:
#      print("Up")
# elif correct < answer:
#      print("Down")
# elif correct == answer:
#      print("Coorect")
# treehit = 0
# while treehit < 11:
#     treehit = treehit +1
#     # print("나무를 %d번 찍었습니다." % treehit)
#     print(f"나무를 {treehit}번 찍었습니다." )
#     if treehit == 10:
#         print("나무 넘어갑니다.")
#     elif treehit  == 5:
#         print("으쌰!")
#     if treehit > 10:
#         print("조심해!")
# prompt = """
# 1. Add
# 2. Del
# 3. List
# 4. Quit

# Enter number : """
# number = 0
# while number !=4:
#     print(prompt)
#     number = int(input())



# 3단계
# 2단계 up&down 게임
'''반복문 작성 요령
1. 반복할 내용 정의
2. While True 기억
'''

# correct = 5 # 정답
# while True:
#     answer = int(input('숫자입력: '))  #input결과는  

#     if correct > answer:
#         print("Up")
#     elif correct < answer:
#         print("Down")
#     elif correct == answer:
#         print("Coorect")
#         break # 반복문 종료 명령어는 break


# # 4단계
# import random #random.py 파일 불러오기
# #파이썬 기본폴더에 저장되어있어서 불러올 수 있음

# print(random.randint(1,1000)) # random.randint(최솟값, 최대값)
# correct = random.randint(1,10)
# # print(f"correct: {correct}") # 정답확인 함수
# while True:
#     answer = int(input('숫자입력: '))  #input결과는  

#     if correct > answer:
#         print("Up")
#     elif correct < answer:
#         print("Down")
#     elif correct == answer:
#         print("Coorect")
#         break # 반복문 종료 명령어는 break

    
# '''3000을 모으면 차를 사지말고 저축해라'''
# 3000 = int(input(': ')) 

#      if 3000 > money:
#          print("save")
#      elif correct < answer:
#          print("Down")
#      elif correct == answer:
#          print("Coorect")

# 5단계
# import random #random.py 파일 불러오기
# #파이썬 기본폴더에 저장되어있어서 불러올 수 있음
# count = 0
# print(random.randint(1,1000)) # random.randint(최솟값, 최대값)
# correct = random.randint(1,10)
# print(f"correct: {correct}") # 정답확인 함수
# while True:
#     answer = int(input('숫자입력: '))  #input결과는  
#     count = count + 1

#     if correct > answer:
#         print("Up", '시도횟수:', count)
#     elif correct < answer:
#         print("Down", '시도횟수:', count)
#     elif correct == answer:
#         print("Coorect", '시도횟수:', count)
#         break # 반복문 종료 명령어는 break



# coffee = 10
# while True:
#     money = int(input("돈을 넣어 주세요: "))
#     if money == 300:
#         print("커피를 줍니다.")
        
#         coffee = coffee -1
#     elif money > 300:
#         # print("거스름돈 %d를 주고 커피를 줍니다." % (money -300))
#         print(f"거스름돈 {money-300}를 주고 커피를 줍니다.") 
#         coffee = coffee -1
#     else:
#         print("돈을 다시 돌려주고 커피를 주지 않습니다.")
#         # print("남은 커피의 양"개 입니다." % coffee)
        
#     if coffee == 0:
#         print("커피가 다 떨어졌습니다. 판매를 중지 합니다.")
#         break
#     print(f"남은 커피의 양은 {coffee}개 입니다.")

# a = 0
# while a < 10:
#     a = a + 1
#     if a % 2 == 0:   #짝수
#         continue     #반복문의 다음 회차로 넘어감(아랫줄 실행)
#     print(a)

# for문
test_list = ['one', 'two', 'three'] 
for i in test_list: 
    print(i)

a = 'abcdefg'
for i in a:
    print(i)

a = [(1,2), (3,4), (5,6)]
for (first, last) in a:
    print(first + last)
print('-'*50)

#60점 이상 : 합격
#60점 미만 : 불합격
# no = 0
# marks = [90,25,67,45,80,99,21,12,77,59]
# for i in marks:
#     no = no + 1

#     if i >= 60:
#         print(f'{no}번 학생 합격')
#     else:
#         print(f'{no}번 학생 불합격')
print('+'*80)

marks = [90,25,67,45,80,99,21,12,77,59]
for no, i in enumerate(marks,1):
    if i >= 60:
        print(f'{no}번 학생 합격')
    else:
        print(f'{no}번 학생 불합격')

print('='*80)

# 1부터 10까지의 합계
add = 0
for i in range(1,11): # range(시작값, 끝값)
    add = add + i

print(add)

print('='*80)
for i in range(0,11):
    print(i)

for i in range(11):
    print(i)

for i in range(0,11,2):   # range(시작,끝,증감)
    print(i)

print('='*80)
# 구구단
'''
2 x 1 = 2
2 x 2 = 4
.........
2 x 9 = 18
'''
# dan = 2
# for i in range(1,10):
#     print(f"{dan} x {i} = {dan * i}")
# print('='*80)
dan = int(input('몇 단?'))
for i in range(1,10):
    print(f"{dan} x {i} = {dan * i}")
# 1
# print(1 * 3)
# print("1" * 3)

