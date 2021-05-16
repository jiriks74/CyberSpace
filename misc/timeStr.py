import time
import datetime

class timeStr():
    """
    Returns time in format %Y-%m-%d %H:%M:%S
    """
    def getTime(self):
        ts = time.time()
        t = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        return t