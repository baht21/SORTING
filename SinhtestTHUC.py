import sys
import random
sys.stdout=open("input_6.inp","w")
n=10**6
a= [round(random.uniform(-1*10**9,10**9),4) for _ in range(n)]
print(n)
print(*a)