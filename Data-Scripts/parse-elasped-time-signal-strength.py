#!/bin/python
import os
import glob

#This file reads in timestamps from previously recorded data files and converts the recorded 24 hour times into an elapsed time - this model was required for the later experiments

# Used for matching signal strength readings with elapsed time

# Usage: $ python parse-elapsed-time-signal-strength.py

def nonblank_lines(f):
    for l in f:
        line = l.rstrip()
        if line:
            yield line                                

cwd = os.getcwd()
if not os.path.isdir(cwd+"/elapsed_time_mesh_devices"):
    os.mkdir(cwd+"/elapsed_time_mesh_devices")
    os.mkdir(cwd+"/elapsed_time_mesh_devices/mesh_devices")

global starttime
global currenttime
one_list = []
another_list = []
for file in glob.iglob('mesh_devices/*.txt'):
    with open(file,"r") as f:
        filename="elapsed_time_mesh_devices/"+f.name
        for line in nonblank_lines(f):
	    currenttime=line.split(' ')[0]
            print currenttime
            one_list.append(currenttime)
	    sig_str=line.split(' ')[1]
            print sig_str
            another_list.append(sig_str)
	    if one_list.index(currenttime) == 0:
	        starttime=float(currenttime)
                starttime=round(starttime, 2)
 	        f = open( filename, 'a' )
                f.write("{} {}".format(0,sig_str)+'\n')
            else:
	        elapsedtime=float(currenttime)-float(starttime)
	        elapsedsystemtime=round(elapsedtime, 2)
                f = open( filename, 'a' )
                f.write("{} {}".format(elapsedsystemtime,sig_str)+'\n')
