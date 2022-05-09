#경기 결과 입력 받는 곳
name = input("나의 이름은 무엇인가?")
age = input("나의 나이가 얼마인가?")
hobby = input("나의 취미가 무엇인가?")
favorite = input("내가 가장 좋아하는것은?")
food = input("내가 가장 좋아하는 음식은?")
advantage= input("나의 장점은 무엇인가? ")
weakness= input("나의 단점은 무엇인가? ")

#자기 소개 작성하는 곳
news ="자기소개를 시작 해보겠습니다."
news = news + "나는"+ name +"이다.""나의 나이는 " + age + " 입니다."
news = news + "나의 취미는 " + hobby + " 입니다."
news = news+ "내가 가장 좋아하는것은 "+ favorite +"이고 "+ food +"는 내가 가장 좋아하는 음식이다."
news = news+"나의 장점은 "+ advantage +"이다."
news = news+"나의 단점은"+weakness+"이다."
    
 #음성으로 들려주는 곳
from gtts import gTTS
import playsound
import os #파일관리 함수
 
tts=gTTS(text=news,lang='ko')
tts.save("suhan.mp3") #기존에 같은 이름의 파일이 존재하면 에러가 생김
playsound.playsound("suhan.mp3",False) #True 멈춰서 해당 하나만 재생, False 밑에 코드랑 동시재생(배경음악)
playsound.playsound("THURSDAY MORNING CHILL JAZZ Sweet March Morning - Spring Jazz &amp Bossa Nova for Good Mood.mp3",True)
os.remove("suhan.mp3")
os.remove("THURSDAY MORNING CHILL JAZZ Sweet March Morning - Spring Jazz &amp Bossa Nova for Good Mood.mp3")
print(news)