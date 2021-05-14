def print_even(num_list):
    for i in num_list: #{num_list} 집합은 반복문 돌릴수 없음
        if i % 2 == 0:
            print(i)

print_even([1,3,2,10,12,11,15])

def print_keys(dic):
    for keys in dic.keys(): # i.keys i딕셔너리에 들어있는 데이터값 나열
        print(keys)

print_keys({"이름": "김말똥", "나이":30, "성별":0})

my_dict = {"10/26": [100,130,100,100],
           "10/27": [10,12,10,11]}

def print_value_by_key(my_dict,key):
    print(my_dict[key]) #딕셔너리로부터 key값 구하기

print_value_by_key(my_dict,"10/26")

# 입력 문자열을 한 줄에 다섯글자씩 출력하는 print_5xn(string) 함수를 작성하라.
def print_5xn(line):
    chunk_num = int(len(line)/5)
    for i in range (chunk_num+1):
        print(line[i*5:i*5+5])

print_5xn("아이엠어보이유알어걸")

def print_mxn(line,num):
    chunk_num = int(len(line)/num)
    for i in range(chunk_num + 1):
        print(line[i*num:i*num+num])

print_mxn("아이엠어보이유알어걸",3)

# 연봉을 입력받아 월급을 계산하는 
# calc_monthly_salary(annual_salary) 함수를 정의하라.
#  회사는 연봉을 12개월로 나누어 분할 지급하며, 
# 이 때 1원 미만은 버림한다.
# 입력된 값을 12로 나누고 형변환을 해서 1원 미만을 절사합니다
def calc_monthly_salary(annual_pay):
    monthly_pay = int(annual_pay/12)
    return monthly_pay

calc_monthly_salary(12000000)