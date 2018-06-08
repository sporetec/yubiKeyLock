import re
import subprocess
import sys
import ctypes
from subprocess import check_output
from time import sleep
yubiSerial="XXXXXXX"
first=True
startupinfo = subprocess.STARTUPINFO()
startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW

while(1):
    p = subprocess.Popen("ykneomgr.exe -s", stdout=subprocess.PIPE, stderr=subprocess.PIPE, startupinfo=startupinfo)
    yubiRead, _ = p.communicate()
    if "error" in str(yubiRead):
        yubiRead="ERROR"
    else:
        yubiRead = re.sub('[^0-9]','', str(yubiRead))
    print (yubiRead)
    
    if(yubiRead!=yubiSerial):
        if(first):
            sys.exit(0)
        print ("locking")
        ctypes.windll.user32.LockWorkStation()
    else:
        print ("Yubikey found")
    first=False
    sleep(10)
