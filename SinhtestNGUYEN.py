import sys
import random
sys.stdout=open("input_5.inp","w")
n=10**6
a = [random.randint(-1*10**9,10**9) for _ in range(n)]
print(n)
print(*a)