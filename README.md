# UdiskBackuper
A python Program backup udisk ragularly

# It haven't been finished because I met some problems below..
copytree() ERR
Traceback (most recent call last):
  File "C:\Users\lenovo\Desktop\usbBackuper\usbBackuper.py", line 144, in <module>
    shutil.copytree(DRIVELETTER, workingDirForWin + "\%s"%(nowtime))
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python311\Lib\shutil.py", line 561, in copytree
    return _copytree(entries=entries, src=src, dst=dst, symlinks=symlinks,
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python311\Lib\shutil.py", line 515, in _copytree
    raise Error(errors)
shutil.Error: [('F:/System Volume Information', 'C:\\Users\\lenovo\\Documents\\usbBak\\1724419680.23674\\System Volume Information', "[WinError 5] 拒绝访问。: 'F:/System Volume Information'")]
