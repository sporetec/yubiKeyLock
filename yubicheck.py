import re
import subprocess
import sys
import ctypes
from subprocess import check_output
from time import sleep
#yubiSerial="XXXXXXX"
first=True
startupinfo = subprocess.STARTUPINFO()
startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW

while(1):
    p = subprocess.Popen("yubico-piv-tool.exe -a list-readers", stdout=subprocess.PIPE, stderr=subprocess.PIPE, startupinfo=startupinfo)
    yubiRead, _ = p.communicate()
    if "Failed" in str(yubiRead):
        yubiRead="ERROR"
    else:
        yubiRead = str(yubiRead)
    print (yubiRead)
    
    if "Yubico Yubikey NEO" in yubiRead:
	    print ("Yubikey found")
    else:
        if(first):
            sys.exit(0)
        print ("locking")
        ctypes.windll.user32.LockWorkStation()
    first=False
    sleep(10)
