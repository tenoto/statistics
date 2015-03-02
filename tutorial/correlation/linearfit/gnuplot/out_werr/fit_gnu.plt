plot "../data/sample_werr.dat" usi 1:2:3 w yerrorbars
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
