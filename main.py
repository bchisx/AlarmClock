import time
import subprocess

file = input("Enter URL:")
browser = "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

def setAlarm():
    waketime_raw = input("Please enter desired waketime:")
    waketime = time.strptime(waketime_raw, "%H%M")
    return waketime
def getTime():
    return time.localtime()

def realAlarm(value):
    check = 0
    while (check == 0):
        if (value.tm_hour == getTime().tm_hour and
                value.tm_min == getTime().tm_min):
            subprocess.Popen([browser, file])
            check = 1

if __name__ == '__main__':
    #ss.SimplifiedService()
    setValue = setAlarm()
    print(setValue)
    print(getTime())

    realAlarm(setValue)
