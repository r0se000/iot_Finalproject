import I2C_LCD_driver
import sys,time
import urllib.request
import json
import MySQLdb

pin=4
mylcd = I2C_LCD_driver.lcd()

city="1841811"
key="3646bf2d9b4ce4204dfe1cad5306f4c6"
url="https://api.openweathermap.org/data/2.5/weather?id=%s&appid=%s&units=metric" %(city,key)
data=urllib.request.urlopen(url)
a=json.loads(data.read().decode())


def LCD(b):
    cur=b.cursor()
    temp=(a['main']['temp'])
    hum=(a['main']['humidity'])
    now=time.strftime('%Y-%m-%d %H:%M:%S') 
    mylcd.lcd_display_string("Time:%s"%now,1)
    mylcd.lcd_display_string("temp:%d hum:%d"%(temp,hum),2)
    time.sleep(5)
    mylcd.lcd_clear()
    cur.execute("select temp from datain order by time desc limit 1")
    mylcd.lcd_display_string("Temperature:%d"%(cur.fetchone()),1)
    cur.execute("select humid from datain order by time desc limit 1")
    mylcd.lcd_display_string("Humidity:%d"%(cur.fetchone()),2)
