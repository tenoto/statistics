#!/usr/bin/env python

# Spearman's Rho 
# http://www2.warwick.ac.uk/fac/sci/moac/people/students/peter_cock/python/rank_correlations/#Spearman
# http://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.spearmanr.html

import scipy.stats

x = [5.05, 6.75, 3.21, 2.66]
y = [1.65, 26.5, -5.93, 7.96]
print scipy.stats.stats.spearmanr(x, y)[0]
