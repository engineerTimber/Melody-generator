import winsound
import random
import time

# "C3":131, "D3":147, "E3":165, "F3":175, "G3":196, "A3":220, "B3":247

notes = {"C3":131, "D3":147, "E3":165, "F3":175, "G3":196, "A3":220, "B3":247, 
         "C4":262, "D4":294, "E4":330, "F4":350, "G4":392, "A4":440, "B4":494}
notes = dict(zip(notes.values(),notes.keys()))
mynotes = []

scale1 = [131,147,165,175,196,220,247]
scale2 = []
for i in range(0,2):
    for j in range(0,7):
        scale2.append(scale1[j]*(2**i))
duration1 = [200,400,800]
duration2 = []
t = 0
Ans21 = 0


Ans1 = int(input("請問音階範圍需橫跨幾個八度?(1 or 2)"))
Ans2 = input("請問節奏是否需要隨機?(Y or n)")
if Ans2 == "n":
    Ans21 = input("是否自訂節奏?(Y or n)")
    if Ans21 == "Y":
        Ans22 = input("請輸入節奏(每個音的長度)(1 = 一拍,負號視為空拍):(ex: 1,2,-2,1,2)")
        Ans23 = int(float(input("你希望一拍幾秒?(ex: 0.4)"))*1000)
        duration2 = Ans22.split(",")
        duration2 = [int(i)*Ans23 for i in duration2]
Ans3 = int(input("請問時長?(秒數)"))


while t < Ans3*1000:
    if Ans1 == 1:
        note = random.choice(scale1)
    elif Ans1 == 2:
        note = random.choice(scale2)

    if Ans2 == "Y":
        d = random.choice(duration1)
        winsound.Beep(note, d)
        a = int(d/200)
        mynotes.append(notes[note]*a)
        t = t + d

    elif Ans2 == "n" and Ans21 == "n":
        d = 500
        winsound.Beep(note, d)
        mynotes.append(notes[note])
        t = t + d

    elif Ans2 == "n" and Ans21 == "Y":
        for i in duration2:
            if i > 0:
                d = i
                if Ans1 == 1:
                    note = random.choice(scale1)
                elif Ans1 == 2:
                    note = random.choice(scale2)
                winsound.Beep(note, d)
                a = int(d/Ans23)
                mynotes.append(notes[note]*a)
                t = t + d
            if i < 0:
                d = -i
                time.sleep(d/1000)
                a = int(d/Ans23)
                mynotes.append("__"*a)
                t = t + d


print("結果如下(連在一起為連續音):", end = "  ")
for i in mynotes:
    print(i,end = " ")