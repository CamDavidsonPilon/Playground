
# rnu this in console mode.
import android
import time
droid = android.Android()

droid.startSensingTimed(2,20)
time.sleep(3)
while(1):
    z = int(droid.readSensors().result['zforce'])
    x = int(droid.readSensors().result['xforce'])
    y = int(droid.readSensors().result['yforce'])
    print (11+z)*" "+'z' #x has a default of about 9.
    print (20+x)*" "+'x'
    print (20+y)*" "+'y'
