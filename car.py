class Car:
    # 속성(클래스/인스턴스 변수)
    num = 0
    color = ''
    speed = 0
    freq = 0
    total_count = 100
    type = ""

    # 생성자 메서드(Car 객체가 만들어질 때 자동 실행됨)
    def __init__(self, n, c, type = '승용차'):
        self.num = n        # 인스턴스 변수
        self.color = c      # 인스턴스 변수
        self.speed = 0      # 인스턴스 변수
        self.type=type
        Car.total_count = Car.total_count + 1 # 클래스 변수
        print(f"{n} 자동차가 생산되었습니다. ({c}) - 총 생산대수 : { Car.total_count}")
    
    # 기능(메서드)
    def horn(self):
        print(f' {self.num} 자동차가 경적을 울립니다.')

    def radio(self, f):
        self.freq = f
        print(f"{self.num} 자동차가 라디오를 켭니다. (주파수: {self.freq}")
    
    def navigation(self,start,end):
        url = f"https://www.google.com/maps/dir/{start}/{end}"
        
        self.navigation
        print(f"{self.num} 차량이 {start} 에서 {end} 까지 안내합니다.")
        import webbrowser
        webbrowser.open(url)
    def light(self, way, light):
        self.light
        print(f"{self.num} 차량이 {way}방향 {light}을 켭니다")

    def y(self,y):
        self.y
        print(f"{self.num} 차량이 {y}")
    def crush(self,crush):
        self.crush
        print(f"{self.num} 차량이 {self.type}와 충돌합니다")



        
        # pyttsx3 검색
#         import pyttsx3
# # TTS 엔진 초기화
# engine = pyttsx3.init()

# # 말하는 속도
# engine.setProperty('rate', 180)
# rate = engine.getProperty('rate')

# # 소리 크기
# engine.setProperty('volume', 0.5) # 0~1 
# volume = engine.getProperty('volume')

# # 목소리
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[1].id) # 남성
# #engine.setProperty('voice', voices[1].id) # 여성

# # 말하기
# engine.say("안녕하세요. 반갑습니다.") 
# engine.runAndWait() # 말 다할때까지 대기
# engine.stop() # 끝

        # from playsound import playsound # python play mp3 검색
        # playsound('Blossoms - Charlemagne.mp3')          
        # free mp3 통해 음악다운로드 => 파일 소스폴더로 이동
        #파일이름 복사 => playsound(파일명)
        # 터미널 창에 pip install playsound 입력
        # 검색하는 습관을 가지자
        # tts 검색

    def change_speed(self,v):
        self.speed = self.speed + v
        if self.speed > 200:
            self.speed = 200    #속력을 200으로 제한
        print(f'{self.num} 차량의 현재 속력: {self.speed}')
from gtts import gTTS

# text = ' 안녕하세요. 반갑습니다.'
# tts_ko = gTTS(text=text, lang='ko')
# tts_ko.save('ko.mp3')
# Car 객체 생성(사용)
car1 = Car(8247,'white')    
car2 = Car(2514,'black')    
# car1은 Car의 객체, Car는 car1이란 객체의 인스턴스
print(car1.num, car1.color)
print(car2.num, car2.color)

print(car1.total_count)
print(car2.total_count)

car1.horn()
car2.horn()

# car1.change_speed(100)
# car1.change_speed(500)
# car1.change_speed(-20)

car2.change_speed(50)
car2.change_speed(10)
car2.change_speed(20)

print('='* 80)

# car1.change_speed(100)
# car1.change_speed(100)
# car1.change_speed(100)

print('='* 80)

#라디오 기능을 만들어 주세요. (radio)
car1.radio(95.9)
car2.radio(107.7)

# class 상속
class Bus(Car): # Car 클래스를 상속받는 Bus 클래스
   def card(self,remains): # 부모에 없는 기능 추가
       print(f"{self.num} 자동차 카드 인식")
   def change_speed(self,v):
        self.speed = self.speed + v
        if self.speed > 100:
            self.speed = 100    #속력을 200으로 제한
        print(f'{self.num} 차량의 현재 속력: {self.speed}')
   def navigation(self,start,end):
        print(f"버스에는 내비게이션 기능이 없습니다.")
   def y(self,y):
        self.y
        print(f"{self.num} 차량이 {y}")
   def crush(self,crush):
        self.crush
        print(f"{self.num} 차량이 {crush}와 충돌합니다")

bus1 = Bus(1, 'yellow',type = '버스')
bus2 = Bus(1, 'green', type = '버스')

car1.change_speed(100)
car1.change_speed(100)
car1.change_speed(100)

bus1.change_speed(50)   #오버라이딩
bus1.change_speed(100)
bus1.change_speed(100)

car1.navigation('둔촌역', '인천공항')
bus1.navigation('천호역', '덕풍시장역')

car1.light('왼쪽','지시등')
car2.y('양보합니다')
bus1.y('양보하지 않습니다')

bus1.horn()

bus1.crush('bus1')