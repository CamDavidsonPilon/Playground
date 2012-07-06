
#you wanna run this in console mode.


import android
import time
from math import log
droid = android.Android()

droid.startSensingTimed(4,20)
time.sleep(2)
while(1):
    value = droid.readSensors().result['light']
    print int(2*log(value + 2.5))*'*'
