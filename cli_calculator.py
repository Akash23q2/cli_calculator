from time import sleep as s
import time
import calendar
from datetime import datetime
from datetime import date
status = time.localtime()
s(0.2)
print(f"Day:  {datetime.today().strftime('%A')} ")
print(f"Date: {date.today()}")
print(f"Time: {status.tm_hour}hrs,{status.tm_min}min")
print("\r")
s(0.3)
for x in range(20,0,-10):
 print(x*"*")
s(0.1)
print("built by Akash with <3(love)".center(66))
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
			print("##Cant divide by 0")
			calc.behave()
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
			print("##complex no. detected ")
			print("##NOTE: python represents i as--> j")
			import cmath
			c=cmath.sqrt(a)
			return c
	def fact(a):
			import math
			if a<0:
				print("##factorial isnt defined for negative and float no.	")
				calc.behave()
			a=abs(int(a))
			c=math.factorial(a)
			return c
	
	def id():
		a= input("•enter 1st no: ")
		try:
			a=float(a)
		except ValueError or NameError:
			calc.behave()
		for f in opr:
			print(f)
		print("\r")
		e= input("•enter operation: ")
		try:
			e=int(e)
			calc.behave()
		except ValueError or NameError:
			if e=="√":
				d=calc.sqrt(a)
				j=calc.choice(d)
				return j
			elif e=="!":
				d=calc.fact(a)
				j=calc.choice(d)
				return j
			print("\r")
			b= input("•enter 2nd no: ")
			try:
				b=float(b)
				print("\r")
				k=calc.op(e,a,b)
				return k
			except ValueError or NameError:
					calc.behave()
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
			try:
				z=calc.con(k,z)
				return z
			except ValueError or NameError:
				return z
			
		
	def op(e,a,b):
		try:
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
		except NameError or ValueError:
			calc.behave()
			
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
				b= input("•enter 2nd no: ")
				try:
					b=float(b)
					print("\r")
					h=calc.op(e,a,b)
					return h
				except ValueError or NameError:
					calc.behave()
					
			
			
	def behave():
			print("\r")
			s(1)
			print("•Please Input With Care!!")
			s(1.4)
			print("\r")
			print("#Restarting....")
			for b in range(3):
				for x in range(4):
					print(x*"*",end="")
			s(1)
			print("\r")
			s(1)
			print("\r")
			v=calc.id()
#end

v=calc.id()
if status.tm_hour <15 and status.tm_hour >6:
 wish = "DAY"
elif status.tm_hour >15 and status.tm_hour <19:
 wish = "EVENING"

else:
    wish = "NIGHT"
print("\r")
for k in range(12):
	print(k*".",end="")
print(("\r")*(4))
print(f"HAVE A GREAT  {wish}!!!".center(70))
print(("\r")*(4))

print("~Akash".center(127))

for k in range(12):
	print(k*".",end="")
s(0.3)

print("\r")







		
		
