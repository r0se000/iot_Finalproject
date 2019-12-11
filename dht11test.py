import Adafruit_DHT
import sys,time
import MySQLdb
from blink import LED
from LCD import LCD
import warnings

warnings.filterwarnings("ignore")
db=MySQLdb.connect("localhost", "mine", "secret", "finalproject")
cur=db.cursor()
sensor=Adafruit_DHT.DHT11
pin=4
id=1
mid='r1'

while True:
    humid, temp = Adafruit_DHT.read_retry(sensor, pin)
    if humid is not None and temp is not None:
        print('Temp={0:0.1f}*C Humidity={1:0.1f}%'.format(temp, humid))
        LED(humid)
        time.sleep(5)
        now=time.strftime('%Y-%m-%d %H:%M:%S')
        cur.execute('insert into datain values(%s, %s, %s, %s, %s)' , (mid, temp, humid, now, id))
        db.commit()
        LCD(db)
        
    else:
        print('Failed to get reading. Try again!')

        
    
