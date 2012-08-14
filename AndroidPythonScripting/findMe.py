#turn on sound and start ringing. Useful if I loose it.


import android
from time import sleep
DOC = "cranks the volume and plays a sounds repeatedly."

droid = android.Android()


droid.setMediaVolume(int(droid.getMaxMediaVolume().result))
while (1):
    droid.mediaPlay('/sdcard/Notifications/hangout_ringtone.m4a','', 1)
    sleep(2) 