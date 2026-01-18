'''print("Hello World")
print(max(10,20,30))
num1=int(input("Enter first number"))
num2=int(input("Enter second number"))
result=num1+num2
print("Sum of nums: ",result)
print(pow(2,3))
# Coding Practice.
#Find the area of triangle when all 3 sides are known.
a=int(input("Enter first side :"))
b=int(input("Enter second side :"))
c=int(input("Enter third side :"))
s=(a+b+c)/2
area= (s*(s-a)*(s-b)*(s-c))**0.5
print("Area of the triangle: ",round(area,2))
# Simple Intrest.
p=float(input("Enter Principal Amount: "))
r=float(input("Enter Rate of Interest: "))
t=float(input("Enter Time in years: "))
s=p*r*t/100
#print("The simple intrest = ",s)
a=p*(1+r/100)**t
print("Amount =",round(a,3))
c=a-p
print("Compound Interest = ",round(c,3))'''
# Area of triangle with base and height
a=float(input("Enter first side :"))
b=float(input("Enter second side :"))
area=0.5*a*b
print("Area of the triangle: ",round(area,2))
