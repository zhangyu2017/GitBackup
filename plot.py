#!/usr/bin/env python
# -*- coding:utf-8 -*-
import ROOT
from ROOT import *
import math

def calcRapidity(line):
    tmp = line.split()
    px = float(tmp[1])
    py = float(tmp[2])
    pz = float(tmp[3])
    m  = float(tmp[4])
    pt = math.sqrt(pow(px,2)+pow(py,2))
    p  = math.sqrt(pow(pt,2)+pow(pz,2))
    E  = math.sqrt(pow(p,2)+pow(m,2))
    y  = 0.5*math.log((E+pz)/(E-pz))
    return y


dir = ['a'+str(1.5),'a'+str(3.2),'a'+str(9)]
dirList = []
histList = []
n = 1
for j in range(0,3):
    for i in range(1,11):
        data = open(dir[j]+'/'+str(i)+'/ana/ampt.dat','r')
        line = data.readline()
        while(True):
            if line != "":
                pid = line.split()[0]
                if pid == str(n):
                    histList.append(TH1D("hist"+str(j)+str(i)+str(n),"k^{+}",50,-6,6))
                    while(True):
                        line = data.readline()
                        if line != "" and line.split()[0]!= str(n+1):
                            if line.split()[0] == "321":
                                histList[(i-1)*100+n-1].Fill(calcRapidity(line),50/12.)
                                # (i-1)*100+n-1 projected to i-th directory , n-th event 's histogram
                                # all these histograms in same a-value are stored in histList
                        else:
                            n+=1
                            break
                    #print(histList[j][n-1].GetEntries())
            else:
                break
        n = 1
        data.close()
    dirList.append(histList)
    histList = []
tp = []
for i in range(0,3):
    tp.append(TProfile("tp"+str(i),"",50,-6,6,'s'))
startx = -5.88                
width = 0.24      
for k in range(0,3):
    for i in range(len(dirList[0])):          
        for j in range(1,51):     
            tp[k].Fill(startx+width*(j-1),dirList[k][i].GetBinContent(j))
c = TCanvas("c1","title",800,350)
gROOT.SetBatch(1)
gStyle.SetOptStat(kFALSE)
pad = TPad("pad","pad title",0.08,0.08,0.98,0.98)
c.cd()
pad.Draw()
pad.Divide(3,1)
pad.cd(1)
pad.SetLeftMargin(0.1)
tp[0].SetMarkerStyle(24)
tp[0].SetMarkerColor(1)
tp[0].SetMarkerSize(0.9)
tp[0].SetLineColor(1)
tp[0].Draw()
pad.cd(2)
tp[1].SetMarkerStyle(25)
tp[1].SetMarkerColor(2)
tp[1].SetMarkerSize(0.9)
tp[1].SetLineColor(2)  
tp[1].Draw("same")
pad.cd(3)
pad.SetRightMargin(0.1)
tp[2].SetMarkerStyle(26)
tp[2].SetMarkerColor(4)
tp[2].SetMarkerSize(0.9)
tp[2].SetLineColor(4)  
tp[2].Draw("same")

xtitle = TLatex(0.5,0.05,"y")
xtitle.SetNDC()
xtitle.SetTextSize(0.05)
c.cd()
xtitle.Draw("psame")

ytitle = TLatex(0.05,0.5,"dN/dy")
ytitle.SetTextAngle(90)
ytitle.SetNDC()
ytitle.SetTextSize(0.05)
ytitle.Draw("psame")

title = TLatex(0.06,0.9,"K^{+}")
title.SetNDC()
title.SetTextSize(0.08)
title.Draw("psame")

pad.cd(1)
t1 = TLatex(0.45,0.93,"a = 1.5")
t1.SetNDC()
t1.SetTextSize(0.05)
t1.Draw("psame")
pad.cd(2)
t2 = TLatex(0.45,0.93,"a = 3.2")
t2.SetNDC()
t2.SetTextSize(0.05)
t2.Draw("psame")
pad.cd(3)
t3 = TLatex(0.45,0.93,"a = 9")
t3.SetNDC()
t3.SetTextSize(0.05)
t3.Draw("psame")

c.Print("7.7kp.pdf")
