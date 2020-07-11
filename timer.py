from datetime import datetime, timedelta
import time
import sys
import os
import pickle

#Defining timer variables and functions
invoke_time=datetime.now()
timer={}
def setTimer(stopwatch, start, time_start, end_time):
    global timer
    timer = {
        "stopwatch":stopwatch, #Timer is counting up
        "start":start, #Timer is tiking True/False
        "time_start":time_start, #Since when we start the countdown
        "end_time":end_time, #Till which time we countdown
        "stop_time":datetime.now() #When the timer has been stopped (paused)
    }
    pickle.dump(timer, open("timer.p", "wb"))
    return timer
        
def timerReset():
    setTimer(bool(False), bool(False), invoke_time, invoke_time)    

def getTimer():
    global timer 
    timer=pickle.load(open("timer.p", "rb"))

def txt(timestring):
    txt=open("timer.txt", "w+")
    if  timestring == "reset":
        timestring=""
    elif timestring > 0:
        seconds=timestring
        hours = seconds // (60*60)
        seconds %= (60*60)
        minutes = seconds // 60
        seconds %= 60
        timestring="%02i:%02i:%02i" % (hours, minutes, seconds)
    else:
        timestring = "00:00:00"
    txt.write(timestring)
    txt.flush()
    txt.close()

#Read timer variables from file, if not present, timer will be reset
try:
    timer = pickle.load(open("timer.p", "rb"))
    print("I found timer settings: "+str(timer))
except (OSError, IOError) as e:
    timerReset()


#Main timer function invoked based on passed parameters, if no parameters are passed, stopwatch will tik.
def obspymer():  
    def tik():
        getTimer()
        if timer["start"] == False:
            exit("Timer stopped")
        if timer["stopwatch"]:
            seconds = int((datetime.now()-timer["time_start"]).total_seconds())
        else:
            seconds = int((timer["end_time"]-timer["time_start"]).total_seconds())
        txt(seconds)
        if timer["stopwatch"]:
            setTimer(bool(True), bool(True), timer["time_start"], timer["end_time"])
        else:
            setTimer(bool(False), bool(True), datetime.now(), timer["end_time"])
        if seconds < 0:
            timerReset()
            exit("Time is up")
        time.sleep(0.5)
        tik()
    if(timer["start"]):                
        tik()

#Read arguments to set/start/stop/reset timer
if len(sys.argv) > 1:
    p = sys.argv[1]
    #Check if parameter is integer
    try:
        int(p)
        print("P is an integer!")
        if not timer["start"]:
            print("Timer will be set")
            setTimer(bool(False), bool(True), invoke_time, invoke_time+timedelta(0, int(p)))
        elif not timer["stopwatch"]:
            end_time=timer["end_time"]+timedelta(0, int(p))
            setTimer(bool(False), bool(True), timer["time_start"], end_time)
            exit("Amended timer time")
    except ValueError:
        print("P is not an integer!")
        if p == "start":
            print("Timer start")
            #Resume stop watch time
            if timer["stopwatch"]:
                seconds=int((timer["stop_time"]-timer["time_start"]).total_seconds())
                start_time=datetime.now()-timedelta(0, seconds)
                setTimer(bool(True), bool(True), start_time, start_time)
            #Start new stop watch
            elif timer["time_start"] == timer["end_time"]:
                setTimer(bool(True), bool(True), invoke_time, invoke_time)
            #Resume timer time
            else:
                end_time = timer["end_time"]+timedelta(0, int((datetime.now()-timer["stop_time"]).total_seconds()))
                setTimer(bool(False), bool(True), timer["time_start"], end_time)

        elif p == "stop":
            print("Timer stop")
            setTimer(timer["stopwatch"], bool(False), timer["time_start"], timer["end_time"])

        elif p == "reset":
            print("Timer reset")
            setTimer(bool(False), bool(False), invoke_time, invoke_time)
            txt("reset")
            exit("Timer has been reset")

        else:
            exit("Invalid parameter, use an integer to set/amend timer in seconds or 'start' 'stop' 'reset', use no paramenters to start a stopwatch")

else:
    #No arguments provided, reset timer.p and start stop watch
    print("No arguments provided, starting stop watch")
    setTimer(bool(True), bool(True), invoke_time, invoke_time)

obspymer()
