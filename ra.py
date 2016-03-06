import time
import requests


starttime = time.time()
interval = 20.0
sellerid = "00000001"
while True:

    # print "tick"
    currtime = time.time()
    try:
        url = "http://ra.filamnt.io"

        files = {'payload.json': open('payload.json', 'rb')}
        response = requests.post(url, files=files)
        # print response.text

    except:
        print "error"

    time.sleep(interval - ((currtime - starttime) % interval))
