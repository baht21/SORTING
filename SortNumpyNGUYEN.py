import sys
import time
import numpy as np
sys.stdin=open("input_1.inp","r")
sys.stdout=open("output.out","w")
n=int(input())
a=np.array(list(map(int,input().split())))
start=time.perf_counter()
a.sort()
end=time.perf_counter()
print(round((end-start)*1000,6))
