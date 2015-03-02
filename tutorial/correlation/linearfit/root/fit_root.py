#!/usr/bin/env python

import os 
import ROOT

os.system('rm -rf out_woerr; mkdir out_woerr')

tg = ROOT.TGraph()
for line in open('../data/sample.dat'):
	cols = line.split()
	x = float(cols[0])
	y = float(cols[1])
	tg.SetPoint(tg.GetN(),x,y)	

can = ROOT.TCanvas()	
can.SetMargin(0.1,0.02,0.13,0.02)
tg.SetMarkerStyle(20)
tg.SetMarkerSize(1.2)
tg.SetTitle(';X;Y')
tg.GetXaxis().SetLimits(-0.5,2.2)
tg.SetMinimum(-2.0)
tg.SetMaximum(2.0)
fit_result = tg.Fit('pol1', "SMEI")
fit_func   = tg.GetFunction('pol1')
tg.Draw('AP')
can.Print('out_woerr/fit_root.pdf')

f = open('out_woerr/fit_root.log','w')
lines  = 'p0 = %.5f +/- %.5f \n' % (fit_result.Parameter(0),fit_result.ParError(0))
lines += 'p1 = %.5f +/- %.5f \n' % (fit_result.Parameter(1),fit_result.ParError(1))
lines += 'chi2 / dof = %.4f (%d)\n' % (fit_func.GetChisquare(), fit_func.GetNDF())
lines += 'prob. = %.4e\n' % fit_func.GetProb()
f.write(lines)
f.close()



os.system('rm -rf out_werr; mkdir out_werr')

tg = ROOT.TGraphErrors()
for line in open('../data/sample_werr.dat'):
	cols = line.split()
	x = float(cols[0])
	y = float(cols[1])
	ye = float(cols[2])
	tg.SetPoint(tg.GetN(),x,y)	
	tg.SetPointError(tg.GetN()-1,0.0,ye)	

can = ROOT.TCanvas()	
can.SetMargin(0.1,0.02,0.13,0.02)
tg.SetMarkerStyle(20)
tg.SetMarkerSize(1.2)
tg.SetTitle(';X;Y')
tg.GetXaxis().SetLimits(-0.5,2.2)
tg.SetMinimum(-2.0)
tg.SetMaximum(2.0)
fit_result = tg.Fit('pol1', "SMEI")
fit_func   = tg.GetFunction('pol1')
tg.Draw('AP')
can.Print('out_werr/fit_root.pdf')

f = open('out_werr/fit_root.log','w')
lines  = 'p0 = %.5f +/- %.5f \n' % (fit_result.Parameter(0),fit_result.ParError(0))
lines += 'p1 = %.5f +/- %.5f \n' % (fit_result.Parameter(1),fit_result.ParError(1))
lines += 'chi2 / dof = %.4f (%d)\n' % (fit_func.GetChisquare(), fit_func.GetNDF())
lines += 'prob. = %.4e\n' % fit_func.GetProb()
f.write(lines)
f.close()


quit()
