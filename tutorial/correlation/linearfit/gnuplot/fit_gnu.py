#!/usr/bin/env python

import os 

os.system('rm -rf out_woerr; mkdir out_woerr')
f = open('out_woerr/fit_gnu.plt','w')
lines = """plot "../data/sample.dat" usi 1:2
f(x) = a * x + b 
a = 1 
b = -1
fit f(x) "../data/sample.dat" usi 1:2 via a,b
set xlabel "X"
set ylabel "Y"
set term postscript eps color enhanced
set output "out_woerr/fit_gnu.ps"
plot "../data/sample.dat" usi 1:2, f(x)
set term x11
exit
"""
f.write(lines)
f.close()
os.system('gnuplot < out_woerr/fit_gnu.plt')
os.system('mv fit.log out_woerr')
os.chdir('out_woerr')
os.system('ps2pdf fit_gnu.ps')
os.chdir('../')


os.system('rm -rf out_werr; mkdir out_werr')
f = open('out_werr/fit_gnu.plt','w')
lines = """plot "../data/sample_werr.dat" usi 1:2:3 w yerrorbars
f(x) = a * x + b 
a = 1 
b = -1
fit f(x) "../data/sample_werr.dat" usi 1:2:3 via a,b 
set xlabel "X"
set ylabel "Y"
set term postscript eps color enhanced
set output "out_werr/fit_gnu.ps"
plot "../data/sample_werr.dat" usi 1:2:3 w yerr, f(x)
set term x11
exit
"""
f.write(lines)
f.close()
os.system('gnuplot < out_werr/fit_gnu.plt')
os.system('mv fit.log out_werr')
os.chdir('out_werr')
os.system('ps2pdf fit_gnu.ps')
os.chdir('../')

