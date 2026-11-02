'''
#if statement 
x = 300
y = 200
if x < y :
    print("x is less than y ")
#else statement 
else:
    print("x is greater than y ")
   
x = int(input("enter a number : "))
y = int(input("enter a number : "))
if x>0:
    print("the number is positive")
else:
    print("the number is negative ")
    #Find Biggest value of given 2 numbers from the command line by using Ternary Operator.
a = int(input("enter a number : "))
b = int(input("enter a number : "))
if a>b:
    print("a is greater than b")
else:
    print("b is greater than a")
#find the given number is even or odd
x = int(input("enter a number : "))
if x%2==0:
    print("the number is even")
else:
    print("the number is odd")          
#indentation error
marks = 20
if marks >= 33:
    print("Pass")
print("Result declared")
    
#Find Biggest value of given 3 numbers from the command line.
x = int(input("entar any number : "))
y = int(input("enter any number : "))
z = int(input("enter any number : "))
if x>y and x>z:
    print("x is greater ")
elif y>z:
    print("y is grater ")
else:
    print("z is gretaer ")
  
#creat a set
my_set = {"apple", "banana", "grapes","papaya","papaya"}
print(my_set)
#add an item to the set 
my_set.add("orange")
print("after adding an item to the set : ",my_set)
#update the set with multiple item 
my_set.update(["mango","kiwi","watermelon"])
print("after updating the set with multiple item : ",my_set)
#remove an item from the set 
my_set.remove("orange")

#set pop() method removes
my_set = {"anjali","sneha","sitanjali","gita"}
my_set.pop()
print(my_set)
#remove an item from the set using remove ()
my_set.remove("gita") 
#discard an item from the set using discard()
my_set.discard("annu")
print(my_set)
#clear the set using clear()
my_set.clear()
print(my_set)

grade = int(input("enter  a number : "))
if grade >= 90 :
    print("Grade: A")
elif grade >= 80 :
    print("Grade: B")
elif grade >= 70:
    print("Grade: C")
elif grade >= 60:
    print("Grade: D")
else:
    print("Grade: F")
'''
'''
x = 5
if x > 3:
    if x > 10:
        print("A")
    else:
        print("B")
        '''
'''
a = 10
b = 20
if a > 5:
    if b > 15:
        print("A")
    else:
        print("B")
else:
    print("C")
    '''
#Teen numbers mein sabse bada number nikalne ka program likho.
a = int(input("First: "))
b = int(input("Second: "))
c = int(input("Third: "))

if a > b:
    if a > c:
        print(a, " a is largest")
    else:
        print(c, " c is largest")
else:
    if b > c:
        print(b, " b is largest")
    else:
        print(c, " c is largest")
