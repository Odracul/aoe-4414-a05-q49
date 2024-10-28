# full_ops.py

# Usage: python3 pool_ops.py c_in n_wv

import sys
import math

# Arguements 
# c_in: input channel count
# n_wv: number of weight vectors


# Parse script arguments
if len(sys.argv) == 8:
    c_in = int(sys.argv[1])
    n_wv = int(sys.argv[2])
else:
    print('Usage: python3 full_ops.py c_in n_wv')
    exit()

muls = n_wv*c_in

adds = n_wv*c_in

divs = 0

c_out = n_wv

h_out = 1 

w_out = 1

print(int(c_out)) # output channel count
print(int(h_out)) # output height count
print(int(w_out)) # output width count
print(int(adds))  # number of additions performed
print(int(muls))  # number of multiplications performed
print(int(divs))  # number of divisions performed