#!/bin/python

import os

#This file reads in timestamps from previously recorded data files and converts the recorded 24 hour times into an elapsed time - this model was required for the later experiments

cwd = os.getcwd()

global starttime
global currenttime
one_list = []
another_list = []
with open("Path-to-F.txt.xls", "r") as this_file:
    for line in this_file:
	currenttime=line.split(' ')[0]
        one_list.append(currenttime)
	sig_str=line.split(' ')[1]#[:3]
        another_list.append(sig_str)
	if one_list.index(currenttime) == 0:
	    starttime=currenttime
 	    f = open( cwd+"/Metric-Elapsed.txt", 'a' )
            f.write("{} {}".format(0,sig_str)+'\n')
        else:
            elapsedsystemtime = float(float(currenttime)-float(starttime))/1000
	    # elapsedsystemtime=float(currenttime)-float(starttime)/100
            # elapsedsystemtime2=float(float(currenttime)-float(starttime))
            # print elapsedtime
	    # elapsedsystemtime=round(elapsedtime, 2)
#            print elapsedsystemtime2/100
            # elapsedsystemtime=elapsedtime/100.0
#            print elapsedsystemtime
 	    f = open( cwd+"/Metric-Elapsed.txt", 'a' )
            f.write("{} {}".format(elapsedsystemtime,sig_str)+'\n')
