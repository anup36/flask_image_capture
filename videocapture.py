import time
from VideoCapture import Device
webCam = Device()
name = 1
while(True): #Take pictures forever
    webCam.saveSnapshot(name + '.jpg') #Take picture
    start = time.time()
    while not (time.time() - start > 50):
        pass
    name = name+1 #We don't want to write over the same image every time