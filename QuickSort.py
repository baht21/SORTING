import sys
import time
import numpy as np
sys.stdin=open("input_1.inp","r")
sys.stdout=open("output.out","w")
n=int(input())
a=np.array(list(map(float,input().split())))
def quicksort(a,l,r):
    if l>=r: return
    pivot=a[(l+r)//2]
    i,j=l,r
    while i<j:
        while a[i]<pivot: 
            i+=1
        while a[j]>pivot: 
            j-=1
        if i<=j:
            a[i],a[j]=a[j],a[i]
            i+=1
            j-=1
    quicksort(a,i,r)
    quicksort(a,l,j)   
start=time.perf_counter()
quicksort(a,0,n-1)
end=time.perf_counter()
print(round((end-start)*1000,6))
