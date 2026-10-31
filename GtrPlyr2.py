from time import *
from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)

bpm = 100

f1 = "inactive"
f2 = "inactive"
f3 = "inactive"
f4 = "inactive"
f5 = "inactive"

s1 = "inactive"
s2 = "inactive"
s3 = "inactive"
s4 = "inactive"
s5 = "inactive"
s6 = "inactive"


    

def s01():
    global f1

    'knuckle'
    kit.servo[9].angle = 0
    sleep(.075)
    'finger'
    kit.servo[8].angle = 0
    f1 = "inactive"

def s02():
    global f2

    'knuckle'
    kit.servo[7].angle = 180
    sleep(.075)
    'finger'
    kit.servo[6].angle = 90
    f2 = "inactive"

def s03():
    global f3

    'knuckle'
    kit.servo[5].angle = 180
    sleep(.075)
    'finger'
    kit.servo[4].angle = 90
    f3 = "inactive"

def s04():
    global f4

    'knuckle'
    kit.servo[3].angle = 180
    sleep(.075)
    'finger'
    kit.servo[2].angle = 90
    f4 = "inactive"
    
def s05():
    global f5

    'knuckle'
    kit.servo[1].angle = 180
    sleep(.075)
    'finger'
    kit.servo[0].angle = 90
    f5 = "inactive"



def s61(lngth=1): 
    global f1
    global f2
    
    global s6

    s01()
    
    if s6 == "active":
        s00()
    else:
        if f2 == "active":
            s02()

    'finger'
    kit.servo[8].angle = 18
    sleep(.075)
    'knuckle'
    kit.servo[9].angle = 60
    sleep(60/bpm*lngth)
    f1 = "active"
    s6 = "active"

def s51(lngth=1): 
    global f1
    global f2

    global s5

    s01()    
    
    if s5 == "active":
        s00()
    else:
        if f2 == "active":
            s02()
    
    'finger'
    kit.servo[8].angle = 30
    sleep(.075)
    'knuckle'
    kit.servo[9].angle = 55
    sleep(60/bpm*lngth)
    f1 = "active"
    s5 = "active"
    
def s41(lngth=1): 
    global f1
    global f2

    global s4

    s01()
    
    if s4 == "active":
        s00()
    else:
        if f2 == "active":
            s02()
    
    'finger'
    kit.servo[8].angle = 43
    sleep(.075)
    'knuckle'
    kit.servo[9].angle = 52
    sleep(60/bpm*lngth)
    f1 = "active"
    s4 = "active"
    
def s31(lngth=1): 
    global f1
    global f2
    
    global s3

    s01()
    
    if s3 == "active":
        s00()
    else:
        if f2 == "active":
            s02()
    
    'finger'
    kit.servo[8].angle = 54
    sleep(.075)
    'knuckle'
    kit.servo[9].angle = 40
    sleep(60/bpm*lngth)
    f1 = "active"
    s3 = "active"

def s21(lngth=1): 
    global f1
    global f2

    global s2

    s01()
    
    if s2 == "active":
        s00()
    else:
        if f2 == "active":
            s02()    
    
    'finger'
    kit.servo[8].angle = 64
    sleep(.095)
    'knuckle'
    kit.servo[9].angle = 45
    print(bpm)
    sleep(60/bpm*lngth)
    f1 = "active"
    s2 = "active"

def s11(lngth=1): 
    global f1
    global f2
    
    global s1

    s01()
    
    if s1 == "active":
        s00()
    else:
        if f2 == "active":
            s02()  
    
    'finger'
    kit.servo[8].angle = 76.5
    sleep(.075)
    'knuckle'
    kit.servo[9].angle = 45
    sleep(60/bpm*lngth)
    f1 = "active"
    s1 = "active"



def s62(lngth=1): 
    global f1
    global f2
    global f3

    global s6

    s02()
    
    if s6 == "active":
        s00()
    else:
        if f1 == "active":
            s01()
        if f3 == "active":
            s03()  
    
    'finger'
    kit.servo[6].angle = 112
    sleep(.075)
    'knuckle'
    kit.servo[7].angle = 44
    sleep(60/bpm*lngth)
    f2 = "active"
    s6 = "active"

def s52(lngth=1): 
    global f1
    global f2
    global f3

    global s5

    s02()
    
    if s5 == "active":
        s00()
    else:
        if f1 == "active":
            s01()
        if f3 == "active":
            s03()  
    
    'finger'
    kit.servo[6].angle = 98
    sleep(.075)
    'knuckle'
    kit.servo[7].angle = 55
    sleep(60/bpm*lngth)
    f2 = "active"
    s5 = "active"

def s42(lngth=1): 
    global f1
    global f2
    global f3

    global s4
    
    s02()
    
    if s4 == "active":
        s00()
    else:
        if f1 == "active":
            s01()
        if f3 == "active":
            s03()  
    
    'finger'
    kit.servo[6].angle = 83
    sleep(.075)
    'knuckle'
    kit.servo[7].angle = 65
    sleep(60/bpm*lngth)
    f2 = "active"
    s4 = "active"

def s32(lngth=1): 
    global f1
    global f2
    global f3

    global s3


    s02()
    
    if s3 == "active":
        s00()
    else:
        if f1 == "active":
            s01()
        if f3 == "active":
            s03()
            
    'finger'
    kit.servo[6].angle = 72
    sleep(.075)
    'knuckle'
    kit.servo[7].angle = 75
    sleep(60/bpm*lngth)
    f2 = "active"
    s3 = "active"

def s22(lngth=1): 
    global f1
    global f2
    global f3

    global s2

    s02()
    
    if s2 == "active":
        s00()
    else:
        if f1 == "active":
            s01()
        if f3 == "active":
            s03()
    
    'finger'
    kit.servo[6].angle = 58
    sleep(.075)
    'knuckle'
    kit.servo[7].angle = 85
    sleep(60/bpm*lngth)
    f2 = "active"
    s2 = "active"
    
def s12(lngth=1): 
    global f1
    global f2
    global f3

    global s1

    s02()
    
    if s1 == "active":
        s00()
    else:
        if f1 == "active":
            s01()
        if f3 == "active":
            s03()
            
    'finger'
    kit.servo[6].angle = 48
    sleep(.075)
    'knuckle'
    kit.servo[7].angle = 95
    sleep(60/bpm*lngth)  
    f2 = "active"
    s1 = "active"

  
    
def s63(lngth=1): 
    global f2
    global f3
    global f4

    global s6

    s03()
    
    if s6 == "active":
        s00()
    else:
        if f2 == "active":
            s02()
        if f4 == "active":
            s04()
            
    'finger'
    kit.servo[4].angle = 93
    sleep(.075)
    'knuckle'
    kit.servo[5].angle = 58
    sleep(60/bpm*lngth)
    f3 = "active"
    s6 = "active"    

def s53(lngth=1): 
    global f2
    global f3
    global f4
    
    global s5


    s03()
    
    if s5 == "active":
        s00()
    else:
        if f2 == "active":
            s02()
        if f4 == "active":
            s04()
    
    'finger'
    kit.servo[4].angle = 80
    sleep(.075)
    'knuckle'
    kit.servo[5].angle = 80
    sleep(60/bpm*lngth)
    f3 = "active"
    s5 = "active" 

def s43(lngth=1): 
    global f2
    global f3
    global f4

    global s4

    s03()
    
    if s4 == "active":
        s00()
    else:
        if f2 == "active":
            s02()
        if f4 == "active":
            s04()
    
    'finger'
    kit.servo[4].angle =67
    sleep(.075)
    'knuckle'
    kit.servo[5].angle = 90
    sleep(60/bpm*lngth)
    f3 = "active"
    s4 = "active" 

def s33(lngth=1): 
    global f2
    global f3
    global f4
    
    global s3

    s03()
    
    if s3 == "active":
        s00()
    else:
        if f2 == "active":
            s02()
        if f4 == "active":
            s04()
            
    'finger'
    kit.servo[4].angle = 55
    sleep(.075)
    'knuckle'
    kit.servo[5].angle = 100
    sleep(60/bpm*lngth)
    f3 = "active"
    s3 = "active" 

def s23(lngth=1): 
    global f2
    global f3
    global f4
    
    global s2

    s03()

    if s2 == "active":
        s00()
    else:
        if f2 == "active":
            s02()
        if f4 == "active":
            s04()
            
    'finger'
    kit.servo[4].angle = 44
    sleep(.075)
    'knuckle'
    kit.servo[5].angle = 105
    sleep(60/bpm*lngth)
    f3 = "active"
    s2 = "active" 
    
def s13(lngth=1): 
    global f2
    global f3
    global f4

    global s1

    s03()
    
    if s1 == "active":
        s00()
    else:
        if f2 == "active":
            s02()
        if f4 == "active":
            s04()
            
    'finger'
    kit.servo[4].angle = 33
    sleep(.075)
    'knuckle'
    kit.servo[5].angle = 110
    sleep(60/bpm*lngth) 
    f3 = "active"
    s1 = "active" 



def s64(lngth=1): 
    global f3
    global f4
    global f5

    global s6

    s04()
    
    if s6 == "active":
        s00()
    else:
        if f3 == "active":
            s03()
        if f5 == "active":
            s05()
            
    'finger'
    kit.servo[2].angle = 93
    sleep(.075)
    'knuckle'
    kit.servo[3].angle = 40
    sleep(60/bpm*lngth) 
    f4 = "active"
    s6 = "active" 

def s54(lngth=1): 
    global f3
    global f4
    global f5

    global s5

    s04()
    
    if s5 == "active":
        s00()
    else:
        if f3 == "active":
            s03()
        if f5 == "active":
            s05()
            
    'finger'
    kit.servo[2].angle = 79
    sleep(.075)
    'knuckle'
    kit.servo[3].angle = 45
    sleep(60/bpm*lngth) 
    f4 = "active"
    s5 = "active" 

def s44(lngth=1): 
    global f3
    global f4
    global f5

    global s4

    s04()
    
    if s4 == "active":
        s00()
    else:
        if f3 == "active":
            s03()
        if f5 == "active":
            s05()
    
    'finger'
    kit.servo[2].angle = 67
    sleep(.075)
    'knuckle'
    kit.servo[3].angle = 57
    sleep(60/bpm*lngth) 
    f4 = "active"
    s4 = "active" 

def s34(lngth=1): 
    global f3
    global f4
    global f5

    global s3

    s04()
        
    if s3 == "active":
        s00()
    else:
        if f3 == "active":
            s03()
        if f5 == "active":
            s05()
            
    'finger'
    kit.servo[2].angle = 55
    sleep(.075)
    'knuckle'
    kit.servo[3].angle = 68
    sleep(60/bpm*lngth) 
    f4 = "active"
    s3 = "active" 

def s24(lngth=1):
    global f3
    global f4
    global f5

    global s2

    s04()
            
    if s2 == "active":
        s00()
    else:
        if f3 == "active":
            s03()
        if f5 == "active":
            s05()
            
    'finger'
    kit.servo[2].angle = 44
    sleep(.075)
    'knuckle'
    kit.servo[3].angle = 78
    sleep(60/bpm*lngth) 
    f4 = "active"
    s2 = "active" 

def s14(lngth=1):
    global f3
    global f4
    global f5

    global s1

    s04()
    
    if s1 == "active":
        s00()
    else:
        if f3 == "active":
            s03()
        if f5 == "active":
            s05()
            
    'finger'
    kit.servo[2].angle = 32
    sleep(.075)
    'knuckle'
    kit.servo[3].angle = 78
    sleep(60/bpm*lngth) 
    f4 = "active"
    s1 = "active" 



def s65(lngth=1):
    global f4
    global f5

    global s6

    s05()
        
    if s6 == "active":
        s00()
    else:
        if f4 == "active":
            s04()
            
    'finger'
    kit.servo[0].angle = 91
    sleep(.075)
    'knuckle'
    kit.servo[1].angle = 50
    sleep(60/bpm*lngth)
    f5 = "active"
    s6 = "active" 

def s55(lngth=1):
    global f4
    global f5

    global s5

    s05()
            
    if s5 == "active":
        s00()
    else:
        if f4 == "active":
            s04()
            
    'finger'
    kit.servo[0].angle = 76
    sleep(.075)
    'knuckle'
    kit.servo[1].angle = 70
    sleep(60/bpm*lngth)     
    f5 = "active"
    s5 = "active" 

def s45(lngth=1):
    global f4
    global f5

    global s4

    s05()
                
    if s4 == "active":
        s00()
    else:
        if f4 == "active":
            s04()
   
    'finger'
    kit.servo[0].angle = 62
    sleep(.075)
    'knuckle'
    kit.servo[1].angle = 70
    sleep(60/bpm*lngth) 
    f5 = "active"
    s4 = "active" 

def s35(lngth=1):
    global f4
    global f5

    global s3

    s05()
                    
    if s3 == "active":
        s00()
    else:
        if f4 == "active":
            s04()
    
    'finger'
    kit.servo[0].angle = 49
    sleep(.075)
    'knuckle'
    kit.servo[1].angle = 80
    sleep(60/bpm*lngth) 
    f5 = "active"
    s3 = "active" 

def s25(lngth=1):
    global f4
    global f5

    global s2

    s05()
                        
    if s2 == "active":
        s00()
    else:
        if f4 == "active":
            s04()
    
    'finger'
    kit.servo[0].angle = 38
    sleep(.075)
    'knuckle'
    kit.servo[1].angle = 91
    sleep(60/bpm*lngth) 
    f5 = "active"
    s2 = "active" 

def s15(lngth=1):
    global f4
    global f5

    global s1

    s05()
                          
    if s1 == "active":
        s00()
    else:
        if f4 == "active":
            s04()
      
    'finger'
    kit.servo[0].angle = 27
    sleep(.075)
    'knuckle'
    kit.servo[1].angle = 95
    sleep(60/bpm*lngth) 
    f5 = "active"
    s1 = "active"


def s00(isNote=False, lngth=1):
    global f1
    global f2
    global f3
    global f4
    global f5
    
    global s1
    global s2
    global s3
    global s4
    global s5
    global s6
    
    f1 = "active"
    f2 = "active"
    f3 = "active"
    f4 = "active"
    f5 = "active"

    s1 = "active"
    s2 = "active"
    s3 = "active"
    s4 = "active"
    s5 = "active"
    s6 = "active"
    
    s01()
    s02()
    s03()
    s04()
    s05()
    
    f1 = "inactive"
    f2 = "inactive"
    f3 = "inactive"
    f4 = "inactive"
    f5 = "inactive"
    
    s1 = "inactive"
    s2 = "inactive"
    s3 = "inactive"
    s4 = "inactive"
    s5 = "inactive"
    s6 = "inactive"
    if isNote:
        sleep(60/bpm*lngth)

def testF0():
    s01()
    s02()
    s03()
    s04()
    s05()

def testF1():
    s01()
    s11()
    s21()
    s31()
    s41()
    s51()
    s61()
    s01()
    
def testF2():
    s02()
    s12()
    s22()
    s32()
    s42()
    s52()
    s62()
    s02()

def testF3():
    s03()
    s13()
    s23()
    s33()
    s43()
    s53()
    s63()
    s03()
    
def testF4():
    s04()
    s14()
    s24()
    s34()
    s44()
    s54()
    s64()
    s04()
        
def testF5():
    s05()
    s15()
    s25()
    s35()
    s45()
    s55()
    s65()
    s05()

def testFrets():
    testF0()
    testF1()
    testF2()
    testF3()
    testF4()
    testF5()

def testS1():
    s00()
    s11()
    s01()
    s12()
    s02()
    s13()
    s03()
    s14()
    s04()
    s15()
    s05()

def testS2():
    s00()
    s21()
    s01()
    s22()
    s02()
    s23()
    s03()
    s24()
    s04()
    s25()
    s05()

def testS3():
    s00()
    s31()
    s01()
    s32()
    s02()
    s33()
    s03()
    s34()
    s04()
    s35()
    s05()

def testS4():
    s00()
    s41()
    s01()
    s42()
    s02()
    s43()
    s03()
    s44()
    s04()
    s45()
    s05()

def testS5():
    s00()
    s51()
    s01()
    s52()
    s02()
    s53()
    s03()
    s54()
    s04()
    s55()
    s05()

def testS6():
    s00()
    s61()
    s01()
    s62()
    s02()
    s63()
    s03()
    s64()
    s04()
    s65()
    s05()

def testStrings():
    testS1()
    testS2()
    testS3()
    testS4()
    testS5()
    testS6()

def testAll():
    startUp()
    testStrings()
    testFrets()

def startUp():
    s00()
    kit.servo[0].angle += 25     
    kit.servo[2].angle += 25    
    kit.servo[4].angle += 25     
    kit.servo[6].angle += 25 
    kit.servo[8].angle += 25
    sleep(60/bpm) 
    
    kit.servo[1].angle -= 25 
    kit.servo[3].angle -= 25 
    kit.servo[5].angle -= 25 
    kit.servo[7].angle -= 25 
    kit.servo[9].angle += 25
    sleep(60/bpm) 
    
    kit.servo[0].angle -= 25 
    kit.servo[2].angle -= 25 
    kit.servo[4].angle -= 25 
    kit.servo[6].angle -= 25 
    kit.servo[8].angle -= 24
    sleep(60/bpm) 
    
    kit.servo[1].angle += 25  
    kit.servo[3].angle += 25 
    kit.servo[5].angle += 25  
    kit.servo[7].angle += 25  
    kit.servo[9].angle -= 24
    sleep(60/bpm)



def setFireToTheRain():
    startUp()

    s00()
    s32()
    s21()
    s32()
    s00(True)
    s32()
    s21(2)

    s00(True, 0)
    s53(2)
    s00(True)
    s21(2)
    
    s00(True)
    s11(1.2)
    s00(True)
    s23()
    s63(4)
    
    
    s23(2)
    
    s00()
    s11(2)
    s32()
    s23()
    s32()
    s11()
    s32()
    s23()
    s32(2)

    #ending chord
    s21(10)

    #done
    s00()

def inTheHallOfTheMountainKing():
    startUp()

    for i in range(2):
        s00(True)
        s62()
        s63(2)
        #s50
        s52()
        s63()
        s52(2)

        s51()
        s62()
        s51(2)

        s00(True)
        s61(3)
        #s50()
        #s61()
        
        s00(True)
        s62()
        s63(2)
        #s50
        s52()
        s63()
        s52()
        s42()
        s00(True) #s40
        s52()
        s63()
        s52(2)
        #s40()
    for i in range(2):
        s52()
        s54()
        s41()
        s42()
        s44()
        s41()
        s44(2)

        s45()
        s41()
        s45(2)

        s44()
        s41()
        s44()

        s52()   
        s54()
        s41()
        s42()
        s44()
        s41()
        s44(2)

        s45()
        s41()
        s45(2)

        s44(2)

    s00(True)
    s62()
    s63(2)
    #s50
    s52()
    s63()
    s52(2)

    s51()
    s62()
    s51(2)

    s00(True)
    s61(3)
    #s50()
    #s61()
    
    s00(True)
    s62()
    s63(2)
    #s50
    s52()
    s63()
    s52()
    s42()
    s52()
    s63()
    s42(3)
    #wait a line
    #s60()


def sonsOfMIT():
    startUp()

    s43()
    s43(1.5)
    s04(.5)
    s41()
    s42()
    s43()
    s33()
    s23(1.5)
    s21(.5)
    s33()
    s32()
    s33()
    s03()
    s43(3)

    s42()
    s41(1.5)
    s52(.5)
    s53()
    s54()
    s55()
    s41()
    s43(1.5)
    s03(.5)
    s32()
    s45()
    s32()
    s33()
    s21(3)

    s43()
    s43(1.5)
    s04(.5)
    s41()
    s42()
    s43()
    s33()
    s23()
    s21()
    s33(1.5)
    s33(.5)
    s21()
    s22()
    s23(3)

    s23()
    s23(1.5)
    s23(.5)
    s24()
    s23()
    s21()
    s03()
    s43()
    s23()
    s24()
    s32()
    s33(3)
    s00(True)











bpm = 100
sonsOfMIT()