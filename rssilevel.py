import subprocess
import os,sys
from glob import glob

S1 = raw_input("SSID =")
for t in range(1,10):
    subprocess.call("sudo iw dev wlan0 scan | grep -B7 "+S1+" | grep signal",shell=True)
    subprocess.call("sudo iw dev wlan0 scan | grep -B5 -A10 "+S1+" | grep Channels ",shell=True)

for t in range(1,10):
    subprocess.call("sudo iwlist wlan0 scan | grep -B5 -A24 "+S1+" | grep Quality ",shell=True)


