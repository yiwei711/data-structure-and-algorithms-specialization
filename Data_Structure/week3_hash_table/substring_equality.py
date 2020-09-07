# python3

import sys
from random import randint

class Solver:
	def __init__(self, s):
		self.s = s
		self.hash1=[0]
		self.hash2=[0]
		
		self.x=randint(1,10**9)
		self.m1=10**9+7
		self.m2=10**9+9
		for i in range(len(s)):
                        self.hash1.append((self.x*self.hash1[-1]+ord(s[i]))%self.m1)
                        self.hash2.append((self.x*self.hash2[-1]+ord(s[i]))%self.m2)
                        
	def ask(self, a, b, l):
                mult1=self.x**l%self.m1
                mult2=self.x**l%self.m2
                one=(self.hash1[a+l]-self.hash1[b+l]-mult1*(self.hash1[a]-self.hash1[b]))%self.m1
                two=(self.hash2[a+l]-self.hash2[b+l]-mult2*(self.hash2[a]-self.hash2[b]))%self.m2
                if one==0 and two==0:
                        return True
                return False
                

s = sys.stdin.readline()
q = int(sys.stdin.readline())
solver = Solver(s)
for i in range(q):
	a, b, l = map(int, sys.stdin.readline().split())
	print("Yes" if solver.ask(a, b, l) else "No")
