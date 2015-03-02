#!/usr/bin/env python

import pyfits
import math

f = open('sample.dat','w')
hdu = pyfits.open('suzaku_nustar_magnetar_table_v150204.fits')
for extension in [hdu[5].data,hdu[6].data]:
	for line in extension:
		B  = line['Bsurf']
		xi = line['LxRatio']
		xi_el = line['LxRatio_ErrLow']
		xi_eu = line['LxRatio_ErrUp']
		if str(xi) != 'nan':
			print B, xi, xi_el, xi_eu
			dump  = '%.4f ' % (math.log10(float(B))-math.log10(float(4.414e+13)))
			dump += '%.4f ' % math.log10(float(xi))
			dump += '\n'
			f.write(dump)
f.close()		

error = 0.40
f = open('sample_werr.dat','w')
hdu = pyfits.open('suzaku_nustar_magnetar_table_v150204.fits')
for extension in [hdu[5].data,hdu[6].data]:
	for line in extension:
		B  = line['Bsurf']
		xi = line['LxRatio']
		xi_el = line['LxRatio_ErrLow']
		xi_eu = line['LxRatio_ErrUp']
		if str(xi) != 'nan':
			print B, xi, xi_el, xi_eu
			dump  = '%.4f ' % (math.log10(float(B))-math.log10(float(4.414e+13)))
			dump += '%.4f ' % math.log10(float(xi))
			dump += '%.4f ' % error
			dump += '\n'
			f.write(dump)
f.close()		