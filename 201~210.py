def print_coin():
    print("비트코인")

for i in range(100):
    print_coin()

def print_coins():
    for i in range(100):
        print_coin()

print_coins()

def message():
    print("A")
    print("B")

message()
print("C")
message()

print("A")
def message():
    print("B")

print("C")
message()

print("A")
def message1():
    print("B")

print("C")
def message2():
    print("D")

message1()
print("E")
message2()

def message1():
    print("A")

def message2():
    print("B")
    message1()

message2()
print("="*80)
def message1():
    print("A")

def message2():
    print("B")

def message3():
    for i in range(3):
        message2()
        print("C")
    message1()

message3()

def 함수(문자열):
    print(문자열)

함수("안녕")
함수("Hi")
# 함수() #  missing 1 required positional argument: '문자열'
# 함수에 정의와 다르게 함수를 호출하고 있다. 함수를 호출할 때 하나의 파라미터를 입력해야 한다

def 함수(a,b):
    print(a+b)

함수(3,4)
함수(7,8)

def print_with_smile(string):
    print(string + ":D")

print_with_smile("안녕하세요")

def print_upper_price(int):
    print(int *1.3)

print_upper_price(10)

def p_sum(a,b):
    
    
    print(a+b)

p_sum(3,5)

def print_arithmetic_opperation(a,b):
    print(a, "+", b, "=",a+b)
    print(a,"-", b, "=", a-b)
    print(a,"*",b,"=", a*b )
    print(a,"/",b,"=", a/b)

print_arithmetic_opperation(3,4)

def print_max(a,b,c):
    m=0
    if a>m:
        m=a
    if b>m:
        m=b
    if c>m:
        m>c
    print(m)

print_max(1,23,12)

def print_reverse(string):
    print(string[::-1])

print_reverse("python")

def print_score(score_list):
    print(sum(score_list)/len(score_list))

print_score([1,2,3])




