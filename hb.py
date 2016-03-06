import time
import requests


starttime = time.time()
interval = 5.0
sellerid = "00000001"
while True:

    # print "tick"
    currtime = time.time()
    try:
        url = "http://hb.filamnt.io/00000002/" + currtime

        # files = {'payload.json': open('payload.json', 'rb')}
        response = requests.get(url)
        print response.text

    except:
        print "error"

    time.sleep(interval - ((currtime - starttime) % interval))
