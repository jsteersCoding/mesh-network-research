from scapy.all import *
import os
import sys
import urllib
import subprocess
from operator import itemgetter
import shlex
import datetime
import time

"""
signal-recordings-using-TP-LINK.py file

Records MAC address of host device
Records current state of Mesh Path

Stores MAC address of each found mesh device in the mesh path inside a list
Saves each MAC address name as a key inside the Dict object dct

Searches for /mesh_devices inside current working directory
- if mesh_devices directory doesn't exist, then no directory is created

Defines function compare_signal_strength()
- Checks if frames received are not found as None (based on how Scapy interprets captured frames), checks if the frames received were not sent by the host device, checks if the captured frames contain the 18:d6:c7 MAC address characters (the mac address of the TP-LINK devices used for the Experiments)
-- if these properties are found inside the sniffed frame, then the frame is checked to see if a Beacon (Dot11Beacon) frame property is found inside the frame object
--- if the Beacon frame property is found, then the following information is extracted from the recorded frame object:

- transmitting mac address
- signal strength
- beacon interval
- the signal strength is stored into the dct inside the key with the matching mac address

The recorded signal strength and beacon interval is written to a file with the name of the transmitting mac address

A frame_counter variable is used to check if Beacon frames have been received in proportion to the number of devices found to be on the mesh network:
- if this is the case then the values are compared inside a for loop and the values inside the dict are compared from strongest to weakest and printed to stdout (to the terminal)

Uses Scapy module to sniff for frames on created monitor interface, and calls the compare_signal_strength function with the "prn" option, the sniff stops after the sniff timeout is exceeded

Run on terminal:
user1:~/$ python signal-recordings-using-TP-LINK.py

"""
getHostDev = subprocess.Popen(shlex.split('ip a'),stdout=subprocess.PIPE)

findMesh0Iface = subprocess.Popen(shlex.split('grep mesh0 -C1'),stdin=getHostDev.stdout,stdout=subprocess.PIPE,stderr=subprocess.PIPE)

findHostMac = subprocess.Popen(shlex.split('grep 18:d6:c7'),stdin=findMesh0Iface.stdout,stdout=subprocess.PIPE,stderr=subprocess.PIPE)

getHostDev.stdout.close() # Allow first process to receive a SIGPIPE if second process exits.

out,err=findHostMac.communicate()#Get output of subprocess commands

mac_filter = re.compile(r'(?<!-)(?:[0-9a-f]{2}[:-]){5}[0-9a-f]{2}(?!-)', re.IGNORECASE)

hostMAC = re.findall(mac_filter,out)

meshpath=os.popen("iw dev mesh0 mpath dump").read()

devicecount=meshpath.split("\n",1)[1].count("\n")

i=1
x = []

while(i<=devicecount):
    x.append(meshpath.split("\n",i)[i].split()[0])
    i=i+1

dct = {}
for i in x:
    dct['%s' % i] = 0

cwd = os.getcwd()
if not os.path.isdir(cwd+"/mesh_devices"):
    os.mkdir(cwd+"/mesh_devices")

if not os.path.isdir(cwd+"/pcaps"):
    os.mkdir(cwd+"/pcaps")
    
j=0
strength=[]
addresslist=[]
frame_counter = 0

def compare_signal_strength(frame):
    if frame[0][Dot11].addr2 is not None and '18:d6:c7' in frame[0][Dot11].addr2 and frame[0][Dot11].addr2 != hostMAC[0]:
        if Dot11Beacon in frame[0]:
            address=frame[0][Dot11].addr2
            systemtime=time.time()
            frametimestamp=frame[0][Dot11Beacon].timestamp
            sig_str=-(256-ord(frame[0].notdecoded[-2:-1]))
            strength.append(str(+(sig_str)))
            addresslist.append(address)
            f = open( cwd+"/mesh_devices/"+address+'.txt', 'a' )
            f.write("{} {} {}".format(systemtime,sig_str,frametimestamp)+'\n')
            
            wrpcap("pcaps/verify-beacons.pcap",frame,append=True)
            f.close()
 
            global frame_counter
            global j
            frame_counter+=1

            ##Store device signal in position based on current device name
            
            if frame_counter % devicecount == 0 and frame_counter != 0:
                for i in x:
                    dct[addresslist[j]] = strength[j].zfill(3)
                    j=j+1
                print "Strongest to weakest signal: ", sorted(dct.iteritems(), key=itemgetter(1))
                mac_add = [idx for idx, val in sorted(dct.iteritems(), key=itemgetter(1))]

            wrpcap("pcaps/verify-beacons.pcap",frame,append=True)

sniff(iface="mon0",prn=compare_signal_strength,timeout=60)
