plot "../data/sample.dat" usi 1:2
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
