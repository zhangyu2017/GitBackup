#! /usr/bin/env python
# -*- coding:utf-8 -*-

from ROOT import *
from  preprocess import preprocess

    

def fillFunc(Energy,Particle):
       
    hlist=[]
    n1,x1,y1=preprocess(Energy,Particle,"0-5%")
    hlist.append(TGraph(n1,x1,y1))
    n2,x2,y2=preprocess(Energy,Particle,"5-10%")
    for i in range(0,n2):
        y2[i]=y2[i]/2
    hlist.append(TGraph(n2,x2,y2))
    n3,x3,y3=preprocess(Energy,Particle,"10-20%")
    for i in range(0,n3):
        y3[i]=y3[i]/4
    hlist.append(TGraph(n3,x3,y3))
    n4,x4,y4=preprocess(Energy,Particle,"20-30%")
    for i in range(0,n4):
        y4[i]=y4[i]/6
    hlist.append(TGraph(n4,x4,y4))
    n5,x5,y5=preprocess(Energy,Particle,"30-40%")
    for i in range(0,n5):
        y5[i]=y5[i]/8
    hlist.append(TGraph(n5,x5,y5))
    n6,x6,y6=preprocess(Energy,Particle,"40-50%")
    for i in range(0,n6):
        y6[i]=y6[i]/10
    hlist.append(TGraph(n6,x6,y6))
    n7,x7,y7=preprocess(Energy,Particle,"50-60%")
    for i in range(0,n7):
        y7[i]=y7[i]/12
    hlist.append(TGraph(n7,x7,y7))
    n8,x8,y8=preprocess(Energy,Particle,"60-70%")
    for i in range(0,n8):
        y8[i]=y8[i]/14
    hlist.append(TGraph(n8,x8,y8))
    n9,x9,y9=preprocess(Energy,Particle,"70-80%")
    for i in range(0,n9):
        y9[i]=y9[i]/16
    hlist.append(TGraph(n9,x9,y9))

    for i in range(0,9):
        hlist[i].SetMarkerSize(1.1)
    hlist[0].SetMarkerStyle(20)
    hlist[0].SetMarkerColor(2)
    hlist[1].SetMarkerStyle(24)
    hlist[1].SetMarkerColor(1)
    hlist[2].SetMarkerStyle(20)
    hlist[2].SetMarkerColor(4)
    hlist[3].SetMarkerStyle(25)
    hlist[3].SetMarkerColor(6)
    hlist[4].SetMarkerStyle(20)
    hlist[4].SetMarkerColor(6)
    hlist[5].SetMarkerStyle(26)
    hlist[5].SetMarkerColor(1)
    hlist[6].SetMarkerStyle(20)
    hlist[6].SetMarkerColor(3)
    hlist[7].SetMarkerStyle(30)
    hlist[7].SetMarkerColor(4)
    hlist[8].SetMarkerStyle(28)
    hlist[8].SetMarkerColor(2)

    return hlist

def main():
    gROOT.SetBatch(1)
    gStyle.SetOptStat(kFALSE)

    c = TCanvas("c","c",800,600)
    c.cd()
    pad = TPad("p","p",0.08,0.08,0.98,0.98)
    pad.Divide(3,2,0,0.08)
    
    pad.SetFillColor(kWhite)
    pad.Draw()

    pad.cd(1)
    gPad.SetRightMargin(0.07) 
    gPad.DrawFrame(0,0.00005,2.04,600)
    gPad.SetLogy(1)
    hlist1=fillFunc("39 GeV","pi+")
    hlist1[0].Draw("p")
    for i in range(1,9):
        hlist1[i].Draw("psame")

    pad.cd(2)
    gPad.SetLeftMargin(0.07)
    gPad.SetRightMargin(0.07) 
    gPad.DrawFrame(0,0.00003,2.04,60)
    gPad.SetLogy(1)
    hlist2=fillFunc("39 GeV","ka+")
    hlist2[0].Draw("p")
    for i in range(1,9):
        hlist2[i].Draw("psame")

    pad.cd(3)
    gPad.SetLeftMargin(0.07) 
    gPad.DrawFrame(0,0.00004,2.04,30)
    gPad.SetLogy(1)
    hlist3=fillFunc("39 GeV","proton")
    hlist3[0].Draw("p")
    for i in range(1,9):
        hlist3[i].Draw("psame")

    pad.cd(4)
    gPad.SetRightMargin(0.07) 
    gPad.DrawFrame(0,0.0001,2.04,600)
    gPad.SetLogy(1)
    hlist4=fillFunc("39 GeV","pi-")
    hlist4[0].Draw("p")
    for i in range(1,9):
        hlist4[i].Draw("psame")

    pad.cd(5)
    gPad.SetLeftMargin(0.07)
    gPad.SetRightMargin(0.07) 
    gPad.DrawFrame(0,0.00003,2.04,20)
    gPad.SetLogy(1)
    hlist5=fillFunc("39 GeV","ka-")
    hlist5[0].Draw("p")
    for i in range(1,9):
        hlist5[i].Draw("psame")

    pad.cd(6)
    gPad.SetLeftMargin(0.07) 
    gPad.DrawFrame(0,0.00001,2.04,6)
    gPad.SetLogy(1)
    hlist6=fillFunc("39 GeV","pbar")
    hlist6[0].Draw("p")
    for i in range(1,9):
        hlist6[i].Draw("psame")
    
    c.cd()
    xtitle=TLatex(0.51,0.081,"p_{T} (GeV/c)")
    xtitle.SetTextSize(0.025)
    xtitle.Draw("psame")
    ytitle=TLatex(0.07,0.45,"#frac{1}{2#pi} #frac{d^{2}N}{p_{T}dp_{T}dy} [(GeV/c)^{-2}]")
    ytitle.SetTextSize(0.025)
    ytitle.SetTextAngle(90)
    ytitle.Draw("psame")

    pad.cd(1)
    t1=TLatex(0.42,0.93,"Au+Au 39 GeV") 
    t1.SetTextSize(0.053)
    t1.SetNDC()
    t1.Draw("same")
    t11=TLatex(0.8,0.93,"#pi^{+}")
    t11.SetTextSize(0.073)
    t11.SetNDC()
    t11.Draw("same")
    pad.cd(2)
    t2=TLatex(0.8,0.93,"K^{+}")
    t2.SetTextSize(0.073)
    t2.SetNDC()
    t2.Draw("same")
    
    
    leg=TLegend()
    leg.AddEntry(hlist1[0],"0-5%","p")
    leg.AddEntry(hlist1[1],"5-10% / 2","p")
    leg.AddEntry(hlist1[2],"10-20% / 4","p")
    leg.AddEntry(hlist1[3],"20-30% / 6","p")
    leg.SetX1NDC(0.14)
    leg.SetY1NDC(0.04)
    leg.SetX2NDC(0.42)
    leg.SetY2NDC(0.24)
    leg.SetFillColor(kWhite)
    leg.SetLineColor(0)
    leg.SetTextSize(0.053)
    leg.Draw("psame")

    pad.cd(3)
    t3=TLatex(0.84,0.93,"p")
    t3.SetTextSize(0.073)
    t3.SetNDC()
    t3.Draw("same")
    leg1=TLegend()
    leg1.AddEntry(hlist1[4],"30-40% / 8","p")
    leg1.AddEntry(hlist1[5],"40-50% / 10","p")
    leg1.AddEntry(hlist1[6],"50-60% / 12","p")
    leg1.AddEntry(hlist1[7],"60-70% / 14","p")
    leg1.AddEntry(hlist1[8],"70-80% / 16","p")
    leg1.SetX1NDC(0.14)
    leg1.SetY1NDC(0.04)
    leg1.SetX2NDC(0.42)
    leg1.SetY2NDC(0.26)
    leg1.SetFillColor(kWhite)
    leg1.SetLineColor(0)
    leg1.SetTextSize(0.053)
    leg1.Draw("psame")


    pad.cd(4)
    t4=TLatex(0.8,0.93,"#pi^{-}")
    t4.SetTextSize(0.073)
    t4.SetNDC()
    t4.Draw("same")

    pad.cd(5)
    t5=TLatex(0.8,0.93,"K^{-}")
    t5.SetTextSize(0.073)
    t5.SetNDC()
    t5.Draw("same")

    pad.cd(6)
    t6=TLatex(0.84,0.93,"#bar{p}")
    t6.SetTextSize(0.073)
    t6.SetNDC()
    t6.Draw("same")



    c.Print("pTSpectra_39.pdf")


if __name__=="__main__":
    main()
