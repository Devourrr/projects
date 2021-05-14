'''
다음의 문자열을 year, month, day, weather 로
나누어 각각 출력해보세요.
'''

a = '20210323Sunny'

print (a[0:4])
print (a[4:6])
print (a[6:8])
print (a[8:13])


a = '20210323Cloudy'
print (a[:4])
print (a[4:6])
print (a[6:8])
print (a[8:])

a = '현재 온도는 18도 입니다'
print(a[:])
print('____________________________________________')
# 문자열 포맷팅
'''
%d: 정수형
%s: 문자열/숫자형 모두 가능
'''

print('-------')
print("I eat %d apples." % 3)
print("I eat %d apples." % 5)
#print("I eat %d apples." % 'four') # TypeError : %d 자리에는 숫자만 입력 가능

print("I eat %s apples." % 'four')
print("I eat %s apples." % 5)

number = 10
day = "three"
# print("I ate %d apples. so i was sick for %s days.")% (number, day))
print("I ate %d apples. so i was sick for %s days."% (5, 'three'))
# print("I ate %d apples. so i was sick for %s days."% (number, number))
print("I ate %d apples. so i was sick for %s days."% (5, 3))


print("")

print("Error is %d%%." % 98) # %글자 출력시 %%사용
# print("Error is %d%." % 98)   오류 발생
print("Error is %d%%." %98)

# format 함수를 이용한 포맷팅
print("I eat {0} apples". format(3))
print("I eat {0} apples.". format(4))
print("I eat {0} apples.". format('five'))


# number = 10
# day = "three"
# print(" I ate {0} apples. so i was sick for {1} days.".format(number, day))
# print(" I ate {1} apples. so i was sick for {0} days.".format(number, day))
# print(" I ate {1} apples. so i was sick for {1} days.".format(number, day))
# print(" I ate {0} apples. so i was sick for {0} days.".format(number, day))

# number = 10
# day ="three"
# print("i ate {0} apples. so I was sick for {1} days.". format(number, day))
# print("i ate {1} apples. so I was sick for {0} days.". format(number, day))
# print("i ate {1} apples. so I was sick for {1} days.". format(number, day))
# print("i ate {0} apples. so I was sick for {0} days.". format(number, day))
#2개 이상의 값을 넣을 경우 문자열의 {0}, {1}과 같은 인덱스 항목이 format 함수의 입력값으로 순서에 맞게 바뀐다. 
# 즉 위 예에서 {0}은 format 함수의 첫 번째 입력값인 number로 바뀌고 {1}은 format 함수의 두 번째 입력값인 day로 바뀐다.

number = 10
day = "three"
print(" I ate {0} apples. so i was sick for {1} days.".format(number, day))
print(" I ate {0} apples. so i was sick for {0} days.".format(number, day))
print(" I ate {1} apples. so i was sick for {1} days.".format(number, day))

# 문자열 포맷팅(f-string)
name = '홍길동'
age = 30
print(f'나의 이름은 {name}입니다. 나이는 {age}입니다')
# print(f'나의 이름은 {name*2}입니다. 나이는 {age*10}입니다')

print('---------')
# 문자열 관련 함수
# 문자열 개수 세기
# a = 'hobby'
# print(a.count('h'))
# print(a.count('o'))
# print(a.count('b'))
# print(a.count('b'))
# print(a.count('y'))
# print(a.count('xyz'))
# print('h',a.count('h'))
# print('o',a.count('o'))
# print('b',a.count('b'))
# print('b',a.count('b'))
# print('y',a.count('y'))
# print('z',a.count('z'))

# print('---------------')
# print(f"h: {a.count{'h')}")
# print(f"o: {a.count{'o')}")
# print(f"b: {a.count{'b')}")
# print(f"b: {a.count{'b')}")
# print(f"y: {a.count{'y')}")
# print(f"z: {a.count{'z')}")

print('------------------')

# 위치 알려주기 (인덱스 번호 획득)
a = "Python is the best choice"
print('t:', a.find('t'))
print('h:', a.find('h'))
print('z:', a.find('z'))  # 없는 문자는 -1 반환

start = a.find('best')
print(a[start : start+4]) # 'best' 문자열의 첫번째 인덱스 번호 획득

start = a.find('Python is the best choice')
print('the:', a.find('the'))
print(a[start+10 : start+14])
print(a[start : start+3])

print('-------')

# 위치 알려주기2(인덱스 번호 획득)
a = "Life is too short"
print(a.index('i'))
print(a.index('t'))
# print(a.index('z')) # 없는 글자 조회시 오류 발생

# 문자열 삽입(join)
# print(','.join('abcd'))
# print('/'.join('abcd'))
# print(''.join('a'))
# print(''.join('b'))
# print(''.join('c'))
# print(''.join('d'))

print('\n'.join('abcd'))
print('\n'.join('python'))
# 소문자 --> 대문자
a ="hi"
print(a.upper())
# 대문자 --> 소문자
a = 'HELLO'
print(a.lower())

a = 'Hello Python'
print(a.upper())
print(a.lower())


# 공백 지우기
a = '         hi         '
print(a)            # 왼쪽 공백 제거
print(a.lstrip())   # 오른쪽 공백 제거
print(a.rstrip())   # 양쪽 공백 제거
print(a.strip())

a = '         Hello Python       '
print(a.strip())   # 양끝의 공백만 제거됨
print(a.lstrip())
print(a.rstrip())
print(a)

# 문자열 바꾸기(replace)
a = "Life is too short"
print(a.replace("Life", "Your leg").replace("short","long"))

a = 'a,b,c,d'
print(a.replace(',','^'))
print(a.replace(',','^', 1))
print(a.replace(',','^', 2))

# 문자열 나누기(split)
a = "Life is too short"
print(a.split()) # split 결과는 리스트형으로 반환
a = "a:b:c:d"
print(a.split(':')) #split 안에 입력값이 없으면 줄바꿈 또는 공백을 기준으로 나눔
a= 'a-b,c-d'
print(a.split('-'))

# 연월일을 각각 출력해보세요. 
# a = '2021-03-23'
# print(a.split(':'))

#리스트는 어떻게 만들고 사용할까?
odd = [1,3,5,7,9]
print(odd)

a = []
b = [1, 2, 3]
c = ['Life', 'is', 'too', 'short']
d = [1, 2, 'Life', 'is']
e = [1, 2, ['Life', 'is']]

print(a)
print(b)
print(c)
print(d)
print(e)

a = [1, 2, 3]
print(a[0])
print(a[1])
print(a[2])
print(a[-1])
print(a[-2])
# print(a[100]) # 오류 : 인덱스 범위를 벗어남
print ('-------------')
print(a[0] + a[2])

a = ['1', '2', '3']
print(a[0] + a[2])

# a = [1,2,'3'] # 오류 : 숫자와 문자는 덧셈 불가
# print(a[0] + a[2])
# print('--------')

a = [1,2,3,['a','b','c']]
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[-1])
print(a[-2])

# a 리스트에서 'b'만 꺼내오기
a = [1,2,3, ['a','b','c']]
b = a[-1]
print(b[1])
print(a[-1][1])

# a 리스트에서 'Life' 글자만 출력해보세요
a = [1,2, ['a','b',['Life','is']]]
print(a[2])          # ['a', 'b', ['Life', 'is']]
print(a[2][2])       # ['Life', 'is']
print(a[2][2][0])    # Life

'''
프로그램 실행 순서
1. 위에서 아래로
2. 안쪽 괄호에서 바깥쪽 괄호로
3. 왼쪽에서 오른쪽으로
'''

print('------------')
# 리스트의 슬라이싱
a = [1,2,3,4,5]
print(a[0:2])
print(a[0:1]) # 하나의 요소만 있어도 리스트로 반환
print(a[0])   # 각 요소의 자료형으로 반환

print('---------------')

a = [1,2,3,4,5]
print(a[:3])
print(a[3:])
print(a[:])
print(a[::-1])
print('--------------')
# split() 함수를 이용하여 연월일을 각각 출력해보세요
# a = "Life is too short"
# print(a.split()) # split 결과는 리스트형으로 반환
# a = "a:b:c:d"
# print(a.split(':')) #split 안에 입력값이 없으면 줄바꿈 또는 공백을 기준으로 나눔
# a= 'a-b,c-d'
# print(a.split('-'))
a = '2021-03-23'
print(a.split('-')[0])
print(a.split('-')[1])
print(a.split('-')[2])

# 내일은 리스트 자료형 복습 if문 while문 하다가 자료형 다시
