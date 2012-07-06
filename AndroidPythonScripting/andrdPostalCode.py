# script to record my location.

from time import sleep
import csv

import android
i=0
documentCount = 0
droid = android.Android()
while 1:
    try: 
        sleep(5)
        droid.startLocating(30,5)
        sleep(5)
        location = droid.readLocation().result
        droid.stopLocating()
        
        if hasattr( location, 'gps'):
            location = location['gps']
            provider = 'gps'
        elif hasattr( location, 'network'):
            location = location['network']
            provider = 'network'
        else:
            location = droid.getLastKnownLocation().result
            if location['gps']:
                location = location['gps']
                provider = 'gps'

            else:
                location = location['network']
                provider = 'network'

        file=open('/sdcard/pythonLocations/location'+ str(documentCount) + '.csv', 'a')
        csvwriter = csv.writer( file, delimiter=',')
        csvwriter.writerow( [location['time'], provider, location['longitude'], location['latitude'], location['accuracy'] ] )
        file.close()
        print i
        i += 1
        if i %10 == 0:
            documentCount += 1
        
    except Exception, e:
        droid.notify('Error', str(e))

