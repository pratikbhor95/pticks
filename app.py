from flask import Flask
import datetime
app = Flask(__name__)

@app.route('/tick/<string:val>')
def tick(val):
       
    t0 = datetime.datetime(1, 1, 1)
    now = datetime.datetime.utcnow()
    # val = "25-02-2024 21:14:27"
    val = datetime.datetime.strptime(val , '%d-%m-%Y %H:%M:%S')
    print(val)
    
    seconds = (val - t0).total_seconds()

    ticks = int(seconds * 10**7)
    return str(ticks)

@app.route('/dateoftick/<string:val>')
def dateoftick(val):
    t0 = datetime.datetime(1, 1, 1)
    t1 = datetime.datetime(1970, 1, 1)
    seconds = (t1 - t0).total_seconds()
    val = int(int(val) / 10**7)
    val = int(val)- int(seconds)
    val = datetime.datetime(1970, 1, 1) + datetime.timedelta(seconds=val)
    return str(val)

# val = "25/02/2024 21:14:27"
# val = datetime.datetime.strptime(val , '%d/%m/%Y %H:%M:%S')
# print(tick(val))

