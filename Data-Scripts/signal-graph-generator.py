#!/usr/bin/python3
import os, os.path, sys, subprocess 
import numpy as np
import glob
import matplotlib.pyplot as plt
from matplotlib import gridspec
from matplotlib import dates
import matplotlib.pyplot as plt
import matplotlib.dates as md
import numpy as np
import datetime as dt
import time
import matplotlib

font = {'weight' : 'bold',
                        'size'   : 16}

matplotlib.rc('font', **font)


"""
signal-graph-generator.py file

Counts how many files are inside the pmacs folder

Creates subplot for the graph containging an overall comparison between the signal strength of all recorded devices throughout the period of capture from the prototype system

For each file inside the pmacs folder
  Open the file
  Read the contents of the file
  Store values of first column inside variable x (the timestamp values), then repeat for second column in y (the signal strength)
  Then plot values onto a graph with the name of the file set to the graph
  Creates comparison graph showing the signal strength changes of each device together throughout the duration of the execution of the Prototype System (could also consider calculating averages for future), asigns a different colour to each found device on the graph

Run on terminal:
user1:~/$ python signal-graph-generator.py

"""
files=len(os.listdir('mesh_devices/'))
compr = plt.figure(figsize=(200,200))
compr.set_size_inches(17, 6)
axcomp = compr.add_subplot(111)
axcomp.set_xlabel("Time in Seconds")
axcomp.set_ylabel("Received Signal Strength in dBm")

colours = ['b', 'r', 'g', 'y','m','k','c']

select_colour=0

global starttime
global currenttime
timestamp_list = []
signalstrength_list = []
for file in sorted(glob.iglob('elapsed_time_mesh_devices/mesh_devices/*.txt')):
    with open(file,"r") as f:
	for line in f:        
	    currenttime=line.split(' ')[0]
	    timestamp_list.append(currenttime)
	    sig_str=line.split(' ')[1]
            signalstrength_list.append(sig_str)
        axcomp.plot(timestamp_list,signalstrength_list, c=colours[select_colour],label="Device {}".format(chr(ord('B')+select_colour)),linewidth=2)
        select_colour=select_colour+1

        filename=f.name
        filename += '.pdf'
        plt.savefig(filename, bbox_inches='tight')
        axcomp.legend()
        timestamp_list=[]
        signalstrength_list=[]
            
compr.savefig("strength-comparison.pdf",bbox_inches='tight')
