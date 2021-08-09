import datetime
def tick():
       
    t0 = datetime.datetime(1, 1, 1)
    now = datetime.datetime.utcnow()
    print(now)
    seconds = (now - t0).total_seconds()
    ticks = int(seconds * 10**7)
    return ticks
