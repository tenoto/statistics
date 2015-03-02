#!/usr/bin/env python


import os 

os.system('rm -rf out; mkdir out')
f = open('out/fit_qdp.pco','w')
lines = """r x -0.5 2.2
r y -2 2 
mark 17 on 2 
mark size 2 on 2
mo ?
mo cons linr 
-1 
1
plot 
fit 
plot 
/xw 
time  off 
la f 
hard  out/fit_qdp.ps/cps
we    fit_qdp
exit
"""
f.write(lines)
f.close()
cmd  = 'qdp ../data/sample.dat >& out/fit_qdp.log <<EOF\n'
cmd += '/xw\n'
cmd += '@out/fit_qdp.pco\n'
cmd += 'EOF\n'
print cmd
os.system(cmd)
os.system('mv -f fit_qdp.pco fit_qdp.qdp out')
os.chdir('out')
os.system('ps2pdf fit_qdp.ps')
os.chdir('../')

