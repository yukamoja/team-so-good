import requests
import yaml
from time import sleep

f = open("hosts.yaml", "r+")
data = yaml.load(f, Loader=yaml.FullLoader)
print(data["sensors"][0].keys)


while True:
    url = 'http://'
    with open('/var/log/sensors.log', 'w') as file:
        for sensor int data["sensors"]:
            response = requests.get(url + data["sensors"].value)
            file.write(response.body)

    sleep(5)
