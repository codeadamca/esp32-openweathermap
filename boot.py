# boot.py -- run on boot-up
import network

# Connect to wifi
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect('<SSID>', '<PASSWORD>')

# Check if wifi is connected
while not wifi.isconnected():
    print('connecting...')
    sleep(0.25)
    pass

# Check which wifi protocol is active
# sta_if = network.WLAN(network.STA_IF)
# ap_if = network.WLAN(network.AP_IF)
# print(sta_if.active())
# print(ap_if.active())

# Output wifi results
# print(wifi.status())
# print(wifi.isconnected())
# print(wifi.ifconfig())