#Tuple
'''
tuple1,tuple2=('sam',10,6,22,77,90),(66,8,10)
print(tuple1[2])
print(tuple1[2:])
print(tuple2[0:])

print (tuple1[2:]+tuple2[0:])
'''
#Dictionary

'''
dic={'Name':'Blaze','Id':1097,'status':'Male'}
print (dic)
print(dic.values())
print(dic.keys())
print (dic['Name'])
'''
#TYpe

'''
a='man'
print(type(a))

str1='hello hoe are you doing?'
str2='if u r not well ,I dont care'

print(str1+' '+str2)
print(str1[2:4])
print(str1[:2]*2)

'''
#List
'''
a=["man",2,3]
print(a[1:])

#list is mutable where tuple is immutable


val=10
val2=None
print(val2)

'''



#bnary operator
"""Multi
line 
comments"""
'''Multi
comment'''
'''
a=7
b=6
i=bin(a)
j=bin(b)
print(bin(b))
print(bin(a))
print(a | b)
print(bin(a|b))
'''


#If else and user input
"""a=input("Enter a no")
b=input("Enter second no")
if(a>b):
    print(a)
else:
    exit(0)


c=input("Enter a no")
if(c==10):
    print("No is 10")
elif(c==50):
    print("No is 50")
else:
    print("Lol!")
"""

#For Loop

'''
i=0
for i in range(0,10,i+2):
    print(i,end=' ')
'''
'''num = int(input())
i=1
# To take input from the user
# num = int(input("Display multiplication table of? "))
# Iterate 10 times from i = 1 to 10
for i in range(1, 11,i+2):
   print(num,'*',i,'=',num*i)
'''

#While loop
'''
i=1
j=2
while i<10:
    print("%d * %d =%d"%(j,i,j*i))
    i=i+1
'''
#Front star pattern
'''a=int(input("Enter row"))
i=0
j=0
for i in range (0,a):
    print()
    for j in range (0,i+1):
        print("*",end='')
'''
'''
a=6
i=0
j=0
for i in range(6,0,-1):
    print(" ")
    for j in range(i,0,-1):
        print("*",end='')'''



'''
List={'Name','Blaze','value',1097,8,10}
count=1
for i in List:
    if i==10 :
        print('success')
        count=count+1
        break
print (count)
'''






'''
str="Pythonplus"
i=0
for i in str:
    if(i=='n'):
        continue
    print (i,end='')

'''




'''
num=2

while 1:
    i=1
    while i<=10:
        print(num ,'X' ,i, '=' ,num*i)
        i=i+1
    choice=(input("Do u want the table to continue?then press Y otherwise press N"))
    if(choice=='N'):
        break

    num=num+1
'''


#Pass Statement

'''
list=[1,2,3,4,5]
i=0
flag=0
for i in list:
    print("Current",i)
    if(i==3):
        pass
        print("Inside pass")
        flag=1
    if(flag==1):
        print("Come out")
        flag=0
        break

'''

#appending elemen in list

'''
l=[]
k=int(input("no of elements"))
for i in range(0,k):
    l.append(int(input("Enter items:")))
print("printing elements")
for i in  l:
    print(i,end='')
'''

'''
l=[1,3,6,9,15,18]

k=int(input("Enter the element u want to delete"))


if k  in l:
    l.remove(k)
else:
    exit(0)
for i in l:
        print(i)
'''


'''
k=(1,2,3,4,5,6)

b=int(input("Enter an integer"))
if b in k:
    print("Exist")
    print(k.index(b))
else:
    print(("does not"))
'''

#Python set k=set([a,b,c]) or k={a,b,c}
'''
k={1,2,3,4}
print(k)
k.add(5)
print(k)
k.update([6,7])
print(k)
'''

#discard and remove is used to delete...if item does not exists discard wont return error when remove will
#pop() is used to delete last item


#union of sets
'''
a={1,2,3,4}
b={5,6,7,8}
print(a|b)
c={12,14,15}
print(a.union(b).union(c))
'''


#intersection and intersectionupdate

#intersection will return common element
#intersectionupdate will remove items that are not present in both set

'''
a={1,2,3,4,6}
b={5,6,4,1}
c={6,9,1,10}
print(a&b&c)
(a.intersection_update(b,c))
print (a)

'''

#comparison operators will check if b is subset of a or not a>b
#in frozenset contents wont change  a=frozenset([1,2,3])

#Dictionary
'''
dic={"Name":"Reena","ID:":1097,"Roll:":112,"Salary":50000}
for i in dic:
    print(i)
for i in dic.values():
    print(i)

for i in dic.items():
    print(i)

for i,j in dic.items():
    print(i,j)
    
print(del dic["Name"])
'''

####FUNCTION

'''
def sum(a,b):
    return (a+b)

k=int(input("Enter 1st no"))
l=int(input("Enter 2nd no"))
print(sum(k,l))
'''
'''
list=[1,2,3,4]
def li(list1):
    list1.append(6)
    list1.append(7)
    return list

print(li(list))
'''

'''
def changestring(str):
    str=str+"will u marry me?"
    return  str

string1="Hi how are u"

print(changestring(string1))

'''
#Required arguments.....There should be all parameters
#keyword arguments....There should be all parameters with same name
#Default arg
'''
def func(name1,message,name2):
    print("printing the message with",name1,",",message,",and",name2)
func("John",message="hello",name2="David") #the first argument is not the keyword argument

'''

#variable length arguments*********
'''
def valiu(*Name):
    
    for name in Name:   #here *Name works as tuple
        print(name)
print("Akash","Rahul")

'''


'''
sum = 0
def calculate(*args):
    sum=0
    for arg in args:
        sum = sum + arg
    print("The sum is", sum)



calculate(10, 20, 30)  # 60 will be printed as the sum
print("Value of sum outside the function:", sum)  # 0 will be printed

'''




#abs() returns absolute values
#all() function accepts iterable object like list and dictionary 0,false will return false
#any() will return true if any one is true #any(k) will false if k=[]
#empty iterable also returns true all(k) k=[]
#bin() returns binary expression
#print(bool(1))
#bytes() is used to create byte object
'''
str="hello new world"
arr=bytes(str,'utf-8')
print(arr)

l=[1,2,3,4]
arr1=bytearray(str,'utf-8')
print(arr1)

'''

# compile string source to code

'''
code_str = 'x=5\ny=10\nprint("sum =",x+y)'
code = compile(code_str, 'sum.py', 'exec')
print(type(code))
exec(code)

'''

#exec() takes large block of code and executes dynamically

'''
k=9
exec('print (k==9)') # Returns true
exec('print(k+4)') #Returns 13

'''
'''
#eval will evaluate program #unlike exec it will take single line
x=8
eval('print(x==8)')

#format() is used to format decimal,float and binary print(format(12,'f'))

# iter returns one element at a time
a=[1,2,3,4,5]
lik=iter(a)
print(next(lik))
print(next(lik))

#len() returns length of an object
#list() creates list list(string)
#f=open(full path) to open a file
#divmod(10,2) returns 5,0
#result=dict(a=1,b=2) creates dictionary
#map() function returns a list of result

def calculate(n):
    return n+n
num=(1,2,3,4)
k=map(calculate,num)


l=set(k)
print(l)


#memoryview returns an memoryview object

s=bytearray('abc','utf-8')
j=memoryview(s)
print(j[0])

'''
'''Python allows us to not declare the function in the standard manner, i.e., by using the def keyword. 
Rather, the anonymous functions are declared by using lambda keyword. However, Lambda functions can accept any number
 of arguments, but they can return only one value in the form of expression.

The anonymous function contains a small piece of code. It simulates inline 
functions of C and C++, but it is not exactly an inline function.'''

'''
x=lambda a:a+10
print("sum=",(x(20)))

#FILE................................................................................

k=open("TestPython",'r')
print(k.tell())
print(k.read())
print(k.tell())

print(k.seek(10))
'''
#import os.....os.rename(" "," ")...os.mkdir().....os.remove()
#check_call() method of module subprocess is used to execute a python script and write the script in a file
'''
temp=[1,34,-275,78]
def k(n):
    if(n<-273):
        return ("Does not makes sense")
    else:
        return n*9/5+32
for t in temp:
    print(k(t))

'''
#------------------------now write the script to a file in file file1.py

"""import subprocess

with open("output.txt","wb") as f:
    subprocess.check_call(["python","Python_practice.py"],stdout=f)

"""
#Exception Handling......................................................................................

'''
try:
    a=10
    b=0
    c=a/b
except ArithmeticError:
    print ("Exception is here")
else:
    print(a/b)

'''


#Raise in Exception.....................................
'''
try:
    
    a=10
    b=0
    c=int(input("Enter age"))
    if(c<18):
        raise ValueError
    else:
        print("age valid")
except ValueError:
    print("Error")
'''


#READ CUSTOMEXCEPTION...................................LATER







#TIME.....................................
'''
import datetime
print(datetime.datetime(2018,12,12,4,5,6))

'''


'''
import  time
print(time.localtime(time.time()))
print(time.asctime(time.localtime(time.time())))
for i in range(0,5):
    print(i)
    time.sleep(1);

'''

'''
from datetime import datetime as dt

if(dt.now())<dt(dt.now().year,dt.now().month,dt.now().day,20):
    print("hello")
else:
    exit(0)

'''

'''
import  calendar
print(calendar.prcal(2018))
'''


#Regular expression..............................................................

"""
import re
str="How are u. Hopefully good"
matches=re.search("How",str)
print(matches.group())
print(matches.span())
print(matches.string)

"""

#PYTHON SENDING EMAIL USING SMTP


'''
import smtplib
sender_mail = 'csoumyajit874@gmail.com'
receivers_mail = ['rinagandhi94@gmail.com']
message = """From: From Person %s 
To: To Person %s 
Subject: Sending SMTP e-mail  
This is a test e-mail message. 
"""%(sender_mail,receivers_mail)
try:
    password = input('Enter the password\n')
    smtpObj = smtplib.SMTP('gmail.com',587)
    smtpObj.login(sender_mail,password)
    smtpObj.sendmail(sender_mail, receivers_mail, message)
    print("Successfully sent email")
except Exception:
   print("Error: unable to send email")

'''


#CSV FILE..................................................................................
#Editing column header

'''
import pandas as pd
ufo=pd.read_csv('D:/Dataset/cars.csv')

print(ufo.columns)
ufo.columns=ufo.columns.str.replace('Car','Cars')
ufo.columns=ufo.columns.str.replace('MPG','MPGGas')
print(ufo.columns)
print(ufo)

'''

tuple1,tuple2=('sam',10,6,22,77,90),(66,8,10)
print(tuple1[2:4])
