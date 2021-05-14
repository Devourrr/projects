# #mod2.py
# PI = 3.141592   #상수값은 일반적으로 대문자 변수로 지정

# class Math:
#     def solv(self, r):
#         return PI * (r**2)

# def add (a,b):
#     return a+b


import random
args = '/오늘의메뉴'
menu = ['김치 찌개', '백반', '삼계탕','돈까스']



for i in range(len(menu)):
    i = random.randint(0,len(menu) -1)

print("오늘의메뉴:",menu[i])