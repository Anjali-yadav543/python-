#Level 1 – Basic Mathematical Questions
#Write a Python program to add two numbers.
'''
a =  10
b = 20
#c = a+b
print(a+b)
'''
'''
#userinput
a = int(input("enter a first number : "))
b = int(input("enter a second number : "))
print("add to number result : ",a+b)
'''
'''
#Write a program to subtract two numbers.
a = 12
b = 8
c = a-b
print(c) #print(a-b)
'''
'''
#userinput
a = int(input("enter a first number : "))
b = int(input("enter a second number : "))
print("subtract  result two numbers : ",a-b)
'''
'''
#Write a program to multiply two numbers.
a = 56
b = 45
c = a*b
print(c)
'''
'''
#userinput
num_1 = int(input("enter a first number : "))
num_2 = int(input("enter a second number : "))
num_3 = int(input("enter a third number : "))
print(num_1*num_2*num_3 )
'''
'''
#Write a program to divide two numbers.
div_1 = int(input("enter a number first : "))
div_2 = int(input("enter a number second : "))
print(div_1/div_2 )
'''
'''
#Write a program to find the square of a number.
s = int(input("enter a number : "))
print(s**2)
'''
'''
#Write a program to find the cube of a number.
q = int(input("enter a number : "))
#q_ = q*q*q
#print(q_)
print(q**3)
'''
'''
#Write a program to calculate the remainder.
r = int(input("enter a Dividend  number : "))
r_1 = int(input("enter a Divisor number : "))
print(r%r_1)
'''
'''
#Write a program to calculate the Floor division.
r = int(input("enter a Dividend  number : "))
r_1 = int(input("enter a Divisor number : "))
print(r//r_1)
'''
'''
#Write a program to calculate the area of a rectangle.
l = int(input("enter a lenght : "))
w = int(input("enter a width : "))
print(l*w)
'''
#Write a program to calculate the average of three numbers.
'''
num_1 = int(input("enter a first number : "))
num_2 = int(input("enter a second number :"))
num_3 = int(input("enter a third number :"))
print(num_1+num_2+num_3/)3)
'''
'''
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
print("Average =", sum([a,b,c])/3)
'''
'''
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
total = a+b+c
avg = total/3
print("Average =", avg)
'''
'''
#Level 2 – Mathematical Logic
#Write a program to check whether a number is even or odd.
a = 78
if a % 2==0:
	print("number is even")
else : 
	print("number is odd ")
'''
'''
#Write a program to find the largest of two numbers.
a = int(input("enter a first number :"))
b = int(input("enter a second number : "))
if a> b :
	print("largest number : ",a)
else:
	print("largest number : ", b)
'''
'''
#Write a program to find the largest of three numbers.
a = int(input("enter a first number :"))
b = int(input("enter a second number : "))
c = int(input("enter a third number : "))
if a>b and a>c :
	print("largest number :",a)
elif b>a and b>c :
	print("largest number : ", b)
else:
	print("largest number : ",c)
'''
'''
#Write a program to calculate the simple interest.
p = int(input("enter a principal : "))
r  = int(input("enter a rate : "))
t = int(input("enter time : "))
si = p*r*t
print("simple interest : ",si)
'''
'''
#Write a program to calculate the percentage of five subjects.
num1 = int(input("enter a first sucbject number : "))
num2 = int(input("enter a second sucbject number : "))
num3 = int(input("enter a third sucbject number : "))
num4 = int(input("enter a fourth sucbject number : "))
num5 = int(input("enter a fifth sucbject number : "))
total = num1+num2+num3+num4+num5 
per = (total/500)*100
print("percentage of five subjects : ",per)
'''
'''
#Write a program to calculate the area of a circle.
a = int(input("enter a  range : "))
c = a**2
p = 3.14*c
print(p)
'''
'''
#Write a program to convert Celsius into Fahrenheit.
c = int(input("enter a celsius : "))
f =c*1.8+32
print("Celsius into Fahrenheit :",f)
'''
'''
#Write a program to calculate the factorial of a number.
n = 5
fact = 1
for i in range(1,n+1):
	fact = fact*i
print("factorial : ",fact)
'''
'''
#Write a program to check whether a number is positive, negative or zero.
n = int(input("enter a number : "))
if n>0:
	print("number is positive")
elif n<0:
	print("number is negative ")
else:
	print("number is zero")
'''
#Print numbers from 1 to 10.
# Print numbers from 1 to 10 using while loop.
i = 1
while i <= 10:
    print(i)
    i = i + 1
    




	