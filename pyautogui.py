# 마우스 제어하는 라이브러리 설치
# pip install pyautogui

import pyautogui
# 좌표 객체 얻기
position = pyautogui.position()

# 화면 전체 크기 확인하기
print(pyautogui.size())

# x,y 좌표
print(position.x)
print(position.y)

# 마우스이동 (x,y)
pyautogui.moveTo(500,500)

# 마우스 이동(x,y, 좌표 2초간)
pyautogui.moveTo(100,100,2)

# 마우스 이동 (현재위치에서)
pyautogui.moveRel(200,300,2)
