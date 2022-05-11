from time import sleep as s
import time
import calendar
from datetime import datetime as samay
from datetime import date as tarik
status = time.localtime()
s(0.2)
print(f"Day:  {samay.today().strftime('%A')} ")
print(f"Date: {tarik.today()}")
print(f"Time: {status.tm_hour}hrs,{status.tm_min}min")
print("\r")
s(0.3)
for x in range(20,0,-10):
 print(x*"*")
s(0.1)
print("built by Akash with <3(love)".center(65))
for x in range(0,21,10):
 print(x*"*")
s(0.6)
 
print("\r")
print("\r")
s(0.3)

opr=["(+)add","(-)sub","(÷)divide","(*)multiply","(%)percent","(^)power",'(!)factorial',"(√)sqrt"]


#start
class calc:
	def add(a,b):
		c=a+b
		return c
	def sub(a,b):
		c=a-b
		return c
	def div(a,b):
		if b==0:
			print("Cant divide by 0")
			c=a
			return c
		c=a/b
		return c
	def mul(a,b):
		c=a*b
		return c
	def power(a,b):
		c=a**b
		return c
	def percent(a,b):
		c=(a*(b/100))
		return c
	def sqrt(a):
		import math
		if a>=0:
			c=math.sqrt(a)
			return c
		else:
			print("complex no. detected ")
			print("NOTE: python represents i as--> j")
			import cmath
			c=cmath.sqrt(a)
			return c
	def fact(a):
			import math
			if a<0:
				print("factorial isnt defined for negative no.	")
				c=a
				return c
			a=abs(int(a))
			c=math.factorial(a)
			return c
	
	def id():
		a= float(input("•enter 1st no: "))
		print("\r")
		for f in opr:
			print(f)
		print("\r")
		e= input("•enter operation: ")
		print("\r")
		if e=="√":
				d=calc.sqrt(a)
				j=calc.choice(d)
				return j
	
		elif e=="!":
			d=calc.fact(a)
			j=calc.choice(d)
			return j
		b= float(input("•enter 2nd no: "))
		print("\r")
		k=calc.op(e,a,b)
		return k
	def choice(d):
		z=d
		print("\r")
		for j in range(4):
			print(j*"#",end='')
		print("\r")
		print("RESULT=:", z)
		for j in range(4):
			print(j*"#",end="")
		print("\r")
		print("\r")
		print("#press enter to stop!")
		s(0.8)
		print("#Ignore above statement if you want to continue: ")
		print("\r")
		for j in opr:
				print(j)
		print("\r")
		k=input(f"•input --> ")
		if k=="":
			return z
			
		else:
			o=calc.con(k,z)
			return o
			
	def op(e,a,b):
		if e=="+":
			d=calc.add(a,b)
			j=calc.choice(d)
			return j
			
		elif e=="-":
			d=calc.sub(a,b)
			j=calc.choice(d)
			return j
		elif e=="*":
			d=calc.mul(a,b)
			j=calc.choice(d)
			return j
		elif e=="÷":
			d=calc.div(a,b)
			j=calc.choice(d)
			return j
		elif e=="^":
			d=calc.power(a,b)
			j=calc.choice(d)
			return j
		elif e=="%":
			d=calc.percent(a,b)
			j=calc.choice(d)
			return j
			
			
	def con(e,a):
		if e=="√":
				d=calc.sqrt(a)
				j=calc.choice(d)
				return j
	
		elif e=="!":
			d=calc.fact(a)
			j=calc.choice(d)
			return j
		print("\r")
		b= float(input("•enter 2nd no: "))
		print("\r")
		n=calc.op(e,a,b)
		return n
		
		def huh(e,a):
			k=calc.con(e)
			return k
#end
			
v=calc.id()
if status.tm_hour <15 and status.tm_hour >6:
 wish = "MORNING"
elif status.tm_hour >15 and status.tm_hour <19:
 wish = "EVENING"

else:
    wish = "NIGHT"
print("\r")
for k in range(12):
	print(k*".",end="")
print("\r")
print("\r")
print("\r")
print("\r")
print(f"HAVE A GREAT  {wish}!!!".center(70))
print("\r")
print("\r")
print('\r')
print("~Akash".center(125))
for k in range(12):
	print(k*".",end="")
s(0.3)
print("\r")







		
			