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
metric-graph-generator.py file

Counts how many files are inside the metrics folder

Creates subplot for the graph containing the changes of the air time link metric value of the best quality path used by the device throughout the period of capture

For each file inside the metrics folder
  Open the file
  Read the contents of the file
  Store values of first column inside variable x (the timestamp values), then repeat for second column in y (the air time link metric)
  Then plot values onto a graph with the name of the file set to the graph
  Creates graph detailing the metric value for the connection of device A to device D throughout the duration of the execution of the Iperf System

Run on terminal:
user1:~/$ python metric-graph-generator.py

"""
#files=len(os.listdir('metrics/'))
compr = plt.figure(figsize=(200,200))
compr.set_size_inches(17, 6)
axcomp = compr.add_subplot(111)
axcomp.set_xlabel("Timestamp in Seconds")
axcomp.set_ylabel("Path Metric Intensity")

colours = ['b', 'r', 'g', 'y','m','k','c']

def nonblank_lines(f):
    for l in f:
        line = l.rstrip()
        if line:
            yield line

select_colour=0
global starttime
global currenttime
one_list = []
another_list = []
with open("Metric-Elapsed.txt", "r") as this_file:
    for line in nonblank_lines(this_file):
        currenttime=line.split(' ')[0]
	one_list.append(currenttime)
        sig_str=line.split(' ')[1]
        another_list.append(sig_str)
    plt.subplots_adjust(bottom=0.2)
    plt.xticks( rotation=25 )
    
    another_list=[float(i) for i in another_list]
    fig = plt.figure(figsize=(200,200))
    fig.set_size_inches(17, 6)
    
    ax1 = fig.add_subplot(111) 
    ax1.set_xlabel("Timestamp in Seconds")
    ax1.set_ylabel("Path Metric Intensity")
    
    ax1.plot(one_list,another_list, c='b',label='Next Hop Device',linewidth=2)
    
    leg = ax1.legend()
    
    axcomp.plot(one_list,another_list, c=colours[select_colour],label="Next Hop Device",linewidth=2)
    select_colour=select_colour+1
    
    axcomp.legend()        
compr.savefig("metric-changes.pdf",bbox_inches='tight')


#no line error - list index out of range on split call due to blank lines inside the data file
