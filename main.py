# Print all available modules
# help('modules')

import socket
import json
from time import sleep

# Define a function that uses socket to make an API call
def http_get(url):
    
    _, _, host, path = url.split('/', 3)
    addr = socket.getaddrinfo(host, 80)[0][-1]
    s = socket.socket()
    s.connect(addr)
    s.send(bytes('GET /%s HTTP/1.0\r\nHost: %s\r\n\r\n' % (path, host), 'utf8'))

    while True:

        data = s.recv(1024)

        if len(data) < 1:
            break
        
        data = data.decode()
        posit = data.find("\r\n\r\n")
        return data[posit+4:]

    s.close()

# Fetch weaher data
data = http_get('https://api.openweathermap.org/data/2.5/weather?q=Toronto,CA&appid=<OPENWEATHERMAP_API_KEY>')

# Output API response
print(data)

# Read a value from the JSON response
data = json.loads(data)

# Print out a single value
temp = data['main']['temp']
print('Temp: %d\u00B0' %temp )