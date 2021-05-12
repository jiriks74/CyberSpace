import time
import datetime

class timeStr():
    # get actual time
    def getTime(self):
        ts = time.time()
        t = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        return t