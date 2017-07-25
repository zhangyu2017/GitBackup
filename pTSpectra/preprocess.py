#! /usr/bin/env python
# -*- coding:utf-8 -*-
import ROOT
from ROOT import * 
from array import *

def preprocess(Energy,Particle,Centrality):
    x=[]
    xl=[]
    xh=[]
    y=[]
    ey=[]
    ey1=[]
    ey2=[]
    tmp=[]
    data=open("data.txt","r")
    while(True):
        #print("loop 1 start")
        line = data.readline()
        if(line!=""):
            if(line.find(Energy)!=-1):
                while(True):
                    #print("loop 2 start")
                    line=data.readline()
                    if(line.find(Particle)!=-1 and line.find(Centrality)!=-1):
                        line=data.readline()
                        while(line.find("---")==-1):
                            tmp=line.split()
                            xl.append(tmp[0])
                            xh.append(tmp[1])
                            y.append(tmp[2])
                            ey1.append(tmp[3])
                            ey2.append(tmp[4])
                            line=data.readline()
                        break
                break
        else:
            break
    data.close()
    x=[(float(xl[i])+float(xh[i]))/2 for i in range(len(xh))]
    ey=[float(ey1[i])+float(ey2[i]) for i in range(len(ey1))]
    y=[float(y[i]) for i in range(len(y))]
    ax=array("f",x)
    ay=array("f",y)
    return len(x),ax,ay

