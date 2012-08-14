import android
import time
from upload import upload

DOC= "take a picture, saves to /sdcard/rootPictures and uploads to webserver."         


droid = android.Android()
cur_time = str(time.clock())
path = '/sdcard/rootPictures/%s.jpg'%cur_time

droid.cameraCapturePicture(path)

upload( path, '/AndroidUploads')