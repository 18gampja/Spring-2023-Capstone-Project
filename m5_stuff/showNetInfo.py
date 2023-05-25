import network
import machine
import wifiCfg
from m5stack import * 
from m5ui import * 
from uiflow import * 


setScreenColor(0x880088) 
wifiCfg.autoConnect(lcdShow=True) 
payload = "" 
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
ip = wifi.ifconfig()[0]
lcd.print("",70,70)
lcd.print("IP:  " + ip)
mac = wifi.config('mac')
lcd.print("MAC:  " + ":".join("{:02x}".format(x) for x in mac), 45, 120)