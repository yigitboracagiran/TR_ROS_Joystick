#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist

hiz=Twist()
hiz.linear.x=0.0
hiz.angular.z=0.0

maxHizSiniri=0.5 #Robotun ulasacagi max ve min hizlar.
minHizSiniri=-0.5
hizDegistirmeMiktari=0.01
basamakSayisi=maxHizSiniri/hizDegistirmeMiktari #Joystickte olceklendirmede kullanilacak.

def HizYayinlama():
    global hiz, hizDegistirmeMiktari
    hiz.linear.x = round(hiz.linear.x - int(hiz.linear.x), 3) #Hizin virgulden sonraki gereksiz yerler duzeltiliyor. Ornek: 3.000000004 -> 3.0000000000 oluyor
    hiz.angular.z = round(hiz.angular.z - int(hiz.angular.z), 3)
    rospy.Publisher("/cmd_vel", Twist, queue_size=1).publish(hiz) #Hiz yayinlama ve ekrana yazdirma.
    print("Lineer Hiz: ", hiz.linear.x)
    print("Acisal Hiz: ", hiz.angular.z)

def Dur():
    global hiz, hizDegistirmeMiktari
    for i in range(int(abs((hiz.linear.x)*10*(0.1/hizDegistirmeMiktari)))):
        if hiz.linear.x>0:
            hiz.linear.x-=hizDegistirmeMiktari
        else:
            hiz.linear.x+=hizDegistirmeMiktari
        HizYayinlama()
    for i in range(int(abs((hiz.angular.z)*10*(0.1/hizDegistirmeMiktari)))):
        if hiz.angular.z>0:
            hiz.angular.z-=hizDegistirmeMiktari
        else:
            hiz.angular.z+=hizDegistirmeMiktari
        HizYayinlama()
        
def MaxIleriHiz():
    global hiz, hizDegistirmeMiktari
    for i in range(int((maxHizSiniri-hiz.linear.x)*(1/hizDegistirmeMiktari))):
        hiz.linear.x+=hizDegistirmeMiktari
        HizYayinlama()
    
def MaxGeriHiz():
    global hiz, hizDegistirmeMiktari
    for i in range(int(abs((minHizSiniri-hiz.linear.x)*(1/hizDegistirmeMiktari)))):
        hiz.linear.x-=hizDegistirmeMiktari
        HizYayinlama()

def MaxSolaHiz():
    global hiz, hizDegistirmeMiktari
    for i in range(int((maxHizSiniri-hiz.angular.z)*(1/hizDegistirmeMiktari))):
        hiz.angular.z+=hizDegistirmeMiktari
        HizYayinlama()

def MaxSagaHiz():
    global hiz, hizDegistirmeMiktari
    for i in range(int(abs((minHizSiniri-hiz.angular.z)*(1/hizDegistirmeMiktari)))):
        hiz.angular.z-=hizDegistirmeMiktari
        HizYayinlama()

def LineerHizArttirma():
    global hiz, hizDegistirmeMiktari
    if hiz.linear.x<maxHizSiniri:
        hiz.linear.x+=hizDegistirmeMiktari
        HizYayinlama()

def LineerHizAzaltma():
    global hiz, hizDegistirmeMiktari
    if hiz.linear.x>minHizSiniri:
        hiz.linear.x-=hizDegistirmeMiktari
        HizYayinlama()

def AcisalHizArttirma():
    global hiz, hizDegistirmeMiktari
    if hiz.angular.z<maxHizSiniri:
        hiz.angular.z+=hizDegistirmeMiktari
        HizYayinlama()

def AcisalHizAzaltma():
    global hiz, hizDegistirmeMiktari
    if hiz.angular.z>minHizSiniri:
        hiz.angular.z-=hizDegistirmeMiktari
        HizYayinlama()

def JoystickAcisalHizAyarlama(veri):
    global hiz
    hiz.angular.z=veri
    HizYayinlama()

def JoystickLineerHizAyarlama(veri):
    global hiz
    hiz.linear.x=veri
    HizYayinlama()

def JoystickIslemleri(joystickVerisi):
    global basamakSayisi
    print("aaa")
    if joystickVerisi.buttons[2]==1: #Mavi tus
        MaxSolaHiz()
    if joystickVerisi.buttons[0]==1: #Yesil tus
        Dur()
    if joystickVerisi.buttons[1]==1: #Kirmizi tus
        MaxSagaHiz()
    if joystickVerisi.buttons[3]==1: #Sari tus
        MaxIleriHiz()
    if joystickVerisi.buttons[5]==1: #R1 tus
        MaxGeriHiz()
    if joystickVerisi.axes[7]==1: #Siyah ust tus
        LineerHizArttirma()
    elif joystickVerisi.axes[7]==-1: #Siyah alt tus
        LineerHizAzaltma()
    if joystickVerisi.axes[6]==1: #Siyah sol tus
        AcisalHizArttirma()
    elif joystickVerisi.axes[6]==-1: #Siyah sag tus
        AcisalHizAzaltma() 
    if joystickVerisi.axes[3]!=0: #Sag Joysitck Sola-Saga
        JoystickAcisalHizAyarlama(hizDegistirmeMiktari*int(joystickVerisi.axes[3]*(basamakSayisi))) #Hizi olceklendirip gonderiyoruz.
    if joystickVerisi.axes[1]!=0: #Sol Joystick Ileri-Geri
        JoystickLineerHizAyarlama(hizDegistirmeMiktari*int(joystickVerisi.axes[1]*(basamakSayisi)))


rospy.init_node('Joy_Deneme')
rospy.Subscriber("/joy", Joy, JoystickIslemleri)

rate = rospy.Rate(10)  
while not rospy.is_shutdown():
    HizYayinlama()
    rate.sleep()