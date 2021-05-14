price_list  = [32100, 32150, 32000, 32500]
for i in range(4):
    print(price_list[i])

# # range함수
# 필요한 만큼의 숫자를 만들어내는 유용한 기능입니다.
# for문과 함께 자주 사용되는 함수입니다.
# 이 함수는 입력받은 숫자에 해당되는 범위의 값을 반복 가능한 객체로 만들어 리턴합니다.

for i in range(len(price_list)):
    print(price_list[i])
# len() 함수를 사용하면 price_list 가 변해도 코드의 수정이 필요없습니다.
#  아래가 더 좋은 코드입니다
for i, data in enumerate(price_list):
    print(i, data) #enumerate()함수
# 리스트가 있는 경우 순서와 리스트의 값을 전달하는 기능을 가집니다.
# enumerate는 “열거하다”라는 뜻입니다.
# 이 함수는 순서가 있는 자료형(list, set, tuple, dictionary, string)을 입력으로 받아 인덱스 값을 포함하는 enumerate 객체를 리턴합니다.
# 보통 enumerate 함수는 for문과 함께 자주 사용됩니다.

for i in range(len(price_list)):
    print((len(price_list)-1)-i, price_list[i])
