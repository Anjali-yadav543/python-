'''
i = 50 #
while i>=1:
    print(i)
    i -= 1
    '''
'''
#printing table to any number using while loop
i = 1
while i<=10:
    print(i*2)
    i +=1
    '''
'''
#printing text using while loop
count = 1
while count<=10:
   # print("ANJALI YADAV")
    count +=1
    print("ANJALI YADAV _______")
    '''
'''
#printing letter of string using while loop 
i = 6
s = "ANJALI YADAV"
while i < len(s):
    print(s[i])
    i +=1 
   ''' 
'''
# printing  value of list using while loop
i = 3
l = [1,3,5,8,23,45]
while i < len(l):
    print(l[i])
    i += 1 
     '''
'''
i = 10
while i > 4:
   print(i)
   i += 1
   '''
'''
i = 1
while i < 10:
    print(i)
    if i == 10:  
        break
    i+=1
   ''' 
'''
i = 0
while i<20:
        i+=1
        if i ==18:
            continue
        print(i)
        '''
'''
for i in range(1, 6):
    if i == 3:
        pass
    print(i)
    '''
'''
#for loop statement
s = "ANJALIYADAV"
for i in s :
    print(i)
#for loop break statement 
fruits = ["apple","banana","guava","mango"]
for i in fruits:
    if i =="guava":
            break
    print(i)
    '''
'''
#for loop continue statement 
f = ["apple","banana","orange","mango"]
for i in f:
     if i == "orange":
        continue
     print(i)
   '''
'''
#for loop nested loop statement 
s = ["anjali","annu","sneha","shweta"]
d = ["yadav","sharma","singh","verma"]
for x in s :
    for y in d :
        print(x,"*",y)
        '''
'''
#assert staement 
a = 10
assert a == 10, "a is not equal to 10"
print("a is equal to 10")
'''
'''
for i in range (1,6):
    print(i)
    pass
'''
for i in range(5,0,-1):
    print(i)


