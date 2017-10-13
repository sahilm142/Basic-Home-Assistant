import feedparser           
import bluetooth
import RPi.GPIO as GPIO                #calling for header file which helps in using GPIOs of PI
from grove_rgb_lcd import *
import time
import os
from gtts import gTTS                   
import pyowm
from pprint import pprint
from google import search
import wikipedia
from random import randint

news_list=[]
def playaudio(a):
    tts=gTTS(text=a,lang='en')
    tts.save("hellow.mp3")                         #   function for playing audio
    os.system("omxplayer hellow.mp3")

def getweather(c):
    owm = pyowm.OWM("35eaa9264eefb54b29922d52532bdc32")  
    observation = owm.weather_at_place(c+",in")  
    w =observation.get_weather()
    status =w.get_status()                              #function for getting weather from openweather api using pyowm
    wind = w.get_wind()
    temp=w.get_temperature()
    pprint(wind)
    pprint(temp)
    a=status+' temp:'+str(temp['temp_max']-273)+' wind:'+str(wind['speed'])+'m/s'
    setText(a)
    if(status=='Haze'):
        status='full of smog'
    s='The weather is '+status+' with temperature '+str(temp['temp_max']-273)+' degree and windspeed '+str(wind['speed'])+' meter per second'
    playaudio(s)
    return s

def getnews(n) :
    i=0;
    d = feedparser.parse('http://timesofindia.indiatimes.com/rssfeeds/-2128936835.cms')
    for post in  d.entries :
       a=post.title
       news_list.append(a)     #  function for  getting news from times of india feeds 
       #setText(a)
       #playaudio(a)
       i=i+1
       if(i==n):
           break
    return(a)
       

def getwikipedia(data):
    i=data.find('ok')
    if(i!=-1):
        data1=data[0:i]
    for url in search(data1+'wiki',stop=2):
        s=str(url)
        print (s)
        break                         #      function for  google search and wiki search
    j=s.rfind('/')
    print (s[j:])
    playaudio("wait a sec.....")
    a='According to wikipedia '+wikipedia.summary(s[j+1:],sentences=1)
    setText(a)
    print (a)
    playaudio(a)
    return(a)
    
setRGB(0,0,255)
setText("")
server_socket=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
port = 1
server_socket.bind(("",port))                          #  bluetooth initilization
server_socket.listen(1)
client_socket,address = server_socket.accept()
print "Accepted connection from ",address
connected="Connection-"
connected+=str(address)
setText(connected)
playaudio("hellow")
data=""

getnews(3)
playaudio("what can i do for you..")



while 1:    
 data=data+client_socket.recv(1024)
 
 if(data.find('weather')!=-1) :
   playaudio("ok")
   data=""
   getweather('Patna')

 if(data.find(' hi')!=-1) :
   playaudio("i am listening....")
   data=""
   
 if(data.find('news')!=-1) :
   playaudio("ok..here are some top headlines...")
   data=""
   playaudio(news_list[randint(0,2)])
   #getnews(1)
   
 if(data.find('music')!=-1):
   data=""
   playaudio("I have something which can cheer you up....")
   os.system('omxplayer music/music'+str(randint(1,4))+'.mp3')
   
 if(data.find(' ok')!=-1):
   playaudio("ok")
   getwikipedia(data)
   data=""

 if(data.find('quit')!=-1):
   print "quit"
   data=""
   playaudio("thank you...")
   setText("Quitting")  
   break




client_socket.close()
server_socket.close()
  


 
 





    
    

