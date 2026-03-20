from pygame import mixer
import time
import datetime

mixer.init()
def water_sound():
    mixer.music.load("drink_water_patrice.mp3")
    mixer.music.play()
    mixer.music.set_volume(1.0)
    while(True):
        work_done=input("Enter Drank for the work done\n").capitalize()
        if work_done=="Drank":
            water_closing()
            break
        else:
            print("Please write the correct line if u don't wish to hear this song again now")
              


def eyes_sound():
    mixer.music.load("soft-inspiring-corporate-background-music-450667.mp3")
    mixer.music.play()
    mixer.music.set_volume(1.0)
    while(True):
        work_done=input("Enter Eydone for the work done\n").capitalize()
        if work_done=="EyDone":
               eyes_closing()
               break
        else:
            print("Please write the correct line if u don't wish to hear this song again now")


def eyes_closing():
    mixer.music.stop()
    

def eyes_file():
    with open("Eyes_log.txt",'a') as e:
        mats=datetime.datetime.now()
        e.write(f"{mats} - Exercised the eyes\n")
     

def exercise_sound():
    mixer.music.load("sport-workout-gym-music-346427.mp3")
    mixer.music.play()
    mixer.music.set_volume(1.0)
    while(True):
        work_done=input("Enter Exdone when the work is done\n").capitalize()
        if work_done=="Exdone":
            exercise_closing()
            break
        else:
            print("Please input the correct input if u don't want to hear this song again")


def exercise_closing():
    mixer.music.stop()

    

def exercise_file():
    with open("Exercise_records.txt",'a') as x:
        mat=datetime.datetime.now()
        x.write(f"{mat} - Exercise done\n")

    
  
def water_closing():
    mixer.music.stop()

def water_file():
    with open("Water_records.txt",'a') as w:
        material=datetime.datetime.now()
        w.write(f"{str(material)} Drank 220ml of water")

if __name__=="__main__":
    name=input("what's ur name\n")
    print(f"Welcome to the program of healthy programmer {name}")
    
    water_gap=30*60
    eyes_gap=30*60
    exercise_gap=45*60

    water_time=time.time()+(30*60)
    eyes_time=time.time()+(40*60)
    exercise_time=time.time()+(50*60)

    work_out_hour=17
    while(True):
        now=time.time()
        if now-water_time>=water_gap and datetime.datetime.now().hour < work_out_hour:
           water_sound()
           water_file()

           water_time=now
        if now-eyes_time>=eyes_gap and datetime.datetime.now().hour < work_out_hour:
           eyes_sound()
           eyes_file()

           eyes_time=now
        if now-exercise_time>=exercise_gap and datetime.datetime.now().hour < work_out_hour:
            exercise_sound()
            exercise_file()

            exercise_time=now

        time.sleep(2)    