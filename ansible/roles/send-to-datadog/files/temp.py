from datadog import initialize, statsd
from datetime import datetime
from os import environ
from time import sleep
from uuid import uuid1
import numpy as np

options = {
    'statsd_host':'127.0.0.1',
    'statsd_port':8125
}

initialize(**options)
tags = ['version:1', 'sensor_uuid:'+str(uuid1()), 'sensor_type:temp', 'room:CXC']

delay = np.random.randint(30, 40)
lag = np.random.randint(1, 5)

now = datetime.now()
comp = datetime(now.year, now.month, now.day, 15, lag, delay)

while True:
    now = datetime.now()
    now = datetime(now.year, now.month, now.day, now.hour, now.minute, now.second)
    diff = comp - now

    temp = 40

    if int(diff.seconds) <= delay:
        temp = 60

    send_value = temp + np.random.normal(0, 2)
    statsd.histogram('temp_metric.histogram', send_value, tags=tags)

    sleep(1)

    print("\rsend data: "+str(send_value),end="")