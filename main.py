import time
import subprocess
import reconfPushbutton as rp


def setAlarm(waketime_raw):
    waketime = time.strptime(waketime_raw, "%H%M")
    if waketime.tm_hour < 0 or waketime.tm_hour > 23:
        raise ValueError("Invalid waketime")
    if waketime.tm_min < 0 or waketime.tm_min > 59:
        raise ValueError("Invalid waketime")
    return waketime

def getTime():
    return time.localtime()

def realAlarm(value):
    while True:
        if value.tm_hour == getTime().tm_hour and value.tm_min == getTime().tm_min:
            subprocess.Popen([browser, file])
            break
        time.sleep(1)

if __name__ == '__main__':
    setValue = setAlarm(input("Please enter desired waketime:"))
    reconfPushbutton = rp.ReconfPushbutton()
    browser = reconfPushbutton.ret_player_link()
    file = reconfPushbutton.ret_file_link()
    realAlarm(setValue)

