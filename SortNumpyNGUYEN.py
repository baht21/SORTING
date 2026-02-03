import numpy as np
import sys
import time
sys.stdin=open("input_1.inp","r")
sys.stdout=open("output.out","w")
start=time.perf_counter()
n=int(input())
a=np.array(input().split(),dtype=int)
b=np.sort(a)
end=time.perf_counter()
print(round((end-start)*1000,6))