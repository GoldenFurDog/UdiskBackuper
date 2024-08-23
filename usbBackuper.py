# zero
import os
import shutil
from pathlib import Path
from time import time, sleep

# default value : Windows
osType = True

# Define the Working Directory for Win and Linux.
# can be edited if you need
HOMEdir = str(Path.home())
workingDirForLinux = HOMEdir + r"/usbBak"
workingDirForWin = HOMEdir + r"\Documents\usbBak"
#print(HOMEdir)

# cool down time befor the udisk be backuped again
# by MINUTE
PAUSETIME = 90
#PAUSETIME = 

# drive letter of new udisks on Windows
# if you have a C:\ and a D:\ , then E:\ should be the next
# only change the "E" letter if you need
DRIVELETTER = "F:/"


class WorkingDirectoryError(RuntimeError):  # Can't mkdir
    def __init__(self):
        print("Unable to mkdir.")

class RECFileError(Warning):   # Can't open RECFile
    def __init__(self):
        print("Unable to open the RECFile.")

class CopytreeError(RuntimeError):  # Can't copytree()
    def __init__(self):
        print("copytree() ERR")


def getPlatformType():      # Get the OS type
    
    osName = os.name
    
    # Windows = True, Linux = False
    if osName == "nt":
        return(True)
    
    elif osName == "posix":
        return(False)
    
    else: raise(OSError)

osType = getPlatformType()

# mkdir($HOME/workingDirectory)
class MakeWorkingDir():
    
    # define by user 
    global workingDirForLinux
    global workingDirForWin
    
    global osType 

    # Linux
    def mkdirForLinux():
        if not os.path.exists(workingDirForLinux):
            try:
                os.mkdir(workingDirForLinux)

            except: raise(WorkingDirectoryError)

    # Windows
    def mkdirForWindows():
        if not os.path.exists(workingDirForWin):
            try:
                os.mkdir(workingDirForWin)
        
            except: raise(WorkingDirectoryError)
    
    # MakeWorkingDir.mkdir()
    def mkdir(self):
        if not osType:
            self.mkdirForLinux()
        elif osType:
            self.mkdirForWindows()


### methods to identify new Udisk on Linux shoud be added
class UdiskRecoderWindows():
    global DRIVELETTER, PAUSETIME
    global osType
    RECdir = DRIVELETTER + "\REC"
    
    def WriteRECLines(self):
        # record the baktime
        
        NOWTIME = str(time())
        
        f = open(self.RECdir, "a")
        f.write(NOWTIME)
        f.close()

    
    def ReadRECLines(self):
        # read the last bak time

        NOWTIME = time()

        if not os.path.exists(self.RECdir):
            f = open(self.RECdir, "x")
            f.close()

            f = open(self.RECdir, "a")
            f.write('0')  # initialize the RECFile
            f.close()

        try:
            f = open(self.RECdir, "r")
            RECTIME = int(f.readlines()[-1])
            f.close()
        except: raise(RECFileError)

        if NOWTIME - RECTIME >=  PAUSETIME / 60:    # rest for $PAUSETIME mins
            return(True)
        else: return(False)



# make working dir
mkdirWork = MakeWorkingDir
mkdirWork.mkdir(mkdirWork)

URecWin = UdiskRecoderWindows

# main loop only for Win
while True:
    
    if os.path.exists(DRIVELETTER) and URecWin.ReadRECLines(URecWin):     # find the udisk
        nowtime = time()

        try:
            # copy the files
            shutil.copytree(DRIVELETTER, workingDirForWin + "\%s"%(nowtime))
        except: raise(CopytreeError)

        URecWin.WriteRECLines(URecWin)

    else:
        sleep(60)
        continue
    
    sleep(PAUSETIME / 60)

