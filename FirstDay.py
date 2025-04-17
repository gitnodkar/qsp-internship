
# a=eval(input("Enter some value"))
# print(type(a))
# print("Hello World")

#WAP to check character length
# s="Python"
# if len(s)%2==0:
#     print("Its even length")

#WAp to check the given number is even and store into list
# a=10
# l=[]
# if a%2==0:
#     l.append(a)
#     print(l)

#WAp to check the given number is odd and store into list without using inbuilt function
# b=11
# k=[]
# if b%2!=0:
#     print("Its odd")
#     k+=[b]
#     print(k)

#WAP to check the given number is digit
# a='90'
# if a.isdigit():
#     print("Its a digit")
#
# a="h"
# a = a.upper()
# print(a)

# WAP to check the given datatype is iterable
# num=eval(input("Enter the datatype"))
# if type(num) in (str, list,set,tuple, dict):
#     print("Collection Data type")
# else:
#     print("Individual data type")

# 1.wap to check the number is odd (take user input)
# 2.wap to check the number is even (take user input)
# 3.wap to check if the student has scored 70% print "good luck "(take user input)
#
# a = eval(input("Enter a number "))
# if a%2!=0:
#     print("Its odd")
#
#
# b = eval(input("Enter a number "))
# if b%2==0:
#     print("Its even")
#
# c= eval(input("Enter your marks in percentage "))
# if c>=70:
#     print("Good Luck!")

# # 5.wap to check if the given string has even length of character
# d ="hey guys you all are Osamm"
#
# if len(d)%2==0:
#     print("Even numbers of characters are present")
# else:
#     print("Odd numbers of characters are present")

# 7.wap to check if the given programming is present in the list

# p=["java","python","c","c++","Ruby","golang"]
#
# e = str(input("Enter a language ")) #Mentioning eval will give error, user will have to give input always in double or single quotes
# if e in p:
#     print("Its in the list")

# 8.wap to check eligible to vote take user input as a age

# age =int(input("Enter your age "))
#
# if age >= 18:
#     print("you are elligible to vote")
#
# # 10.wap to check if the given string is palindrome (take user input)
# f = input("Enter a number or a word ") #Do not mention eval or any adatatype here
# if f==f[::-1]:
#     print("Its pal")
# else:
#     print("Not pal")

# 11.wap to check if the first letter in the given string is consonant

# s="Aahari is a good student"
#
# vowels = ["A","E","I","O","U","a","e","i","o","u"]
#
# if s[0] not in vowels: # you can also go like --> if s[0] not in "a", "e", "i", "o", "u":
#     print("String starting with a consonant")
# else:
#     print("String starting with a vowel")
#
# # 12.wap to check the given string is uppercase or not (take user input)
#
# g = str(input("Enter a string "))
# if g.isupper():
#     print("Its uppercase")
#
#
# # 14.wap to display "Python Coding" if the number is greater than 1 and less than 5 (take user input)
#
# h = int(input("Enter a number "))
# if 1<h<5:
#     print("Python Coding")




# 16.wap to check whether given input is divisible by 2 and 6 if condition is True ,convert the given number to complex number.(take user input)
#
# i = int(input("Enter a number "))
# if i%2 ==0 and i%6 ==0:
#     print("Its divisible by 2 and 6")
#     print("The complex is :",complex(i))


# wap to check whether the given number is even or not,if even store the value inside the list (take user input)

# j = int(input("Enter a number :"))
# k=[]
# if j%2 ==0:
#     print("Its even")
#     k.append(j) # another way --> k=[j]+k
#     print(k)    # print(k)
#
# # 19.wap to check whether a given value is divisible by 5 and 7,if the value is divisible then display the square of the values (take user input)
# l = int(input("Enter a number "))
# if l%5 ==0 and l%7 ==0:
#     print("Its divisible by 5 and 7")
#     print("The square is :",(l**2))
#
# 20.wap to check whether a given value is present in between 45 and 200 and the number should be divisible by 4 and 5 ,if satisfied,display the ascii characters (take user input
# m = int(input("Enter a number "))
# if 45<m<200 and m%4 ==0 and m%5 ==0:
#     print("The ascii character is", chr(m))

# for i in range(1,100):
#     if i%4 ==0 and i%5 ==0:
#         print(i)

# 21.wap to checking if a string contains a substring

# string="hello world"
# sub_string="world"
#
# if sub_string in string:
#     print("Its contains the given substring")
# else:
#     print("It does not contain the given substring")


#  22.wap to check whether a character is in the alphabet or not,if it is alphabet,store the value inside  a dict(key as a character and value as a ascii value)
# n = input("Enter a value ")
# d = {}
# if n.isalpha():
#     print("Its in the alphabet")
#     d[n] = ord(n) # Can also do by ---> d.update({n:ord(n)})
#     print(d)

# 23.wap to check whether a character is in uppercase or not,if uppercase,convert to lowercase and store the value inside the dictionary (character as key and ascii as value) take user input
# o = input("Enter a value ")
# d = {}
# if o.isupper():
#     print("Its in uppercase")
#     o = o.lower()
#     d[o] = ord(o) # Can also do by ---> d.update({n:ord(n)})
#     print(d)

# IF - ELSE PROGRAMS
#
# 2.wap to check whether the male and female are eligible for wedding (take user input)
#
# m = int(input("Enter the groom's age: "))
# f = int(input("Enter the bride's age: "))
#
# if m>21 and f>18:
#     print("Both are eligible")
# elif f<18 and m>21:
#     print("Bride is not eligible")
# elif m<21 and f>18:
#     print("Groom is not eligible")
# else:
#     print("Both are not eligible")



# 3.wap to return uppercase if the char is lower,else return same char (by taking user input)

# p = input("Enter a character :")
# if p.islower():
#     print(p.upper())
# else:
#     print(p)

# 5.wap to find greater value among the two number
# n1=34
# n2=54
#
# if n1>n2:
#     print(n1, "is greater")
# else:
#     print(n2, "is greater")

# 6.wap to check if the given number is even or not,if it is not even add+1 and make it even (take user input)

# q = int(input("Enter a number: "))
# if q%2 ==0:
#     print("It is even")
# else:
#     print(q+1)
#     print("Now its even")

# 7.wap to check whether the first character in the given string is starting with uppercase or Not if it is not Then capitalize it
# s="python"
#
# if s[0].isupper():
#     print(s)
#     print("The first letter is uppercase")
# else:
#     print(s.capitalize())
#     print("Now it is capitalized")


# 10.wap if the length of string is even then reverse else convert into upper case (take user input)

# t=str(input("Enter a string "))
# if len(t)%2==0:
#     print(t[::-1])
# else:
#     print(t.upper())

# 12.wap to check a data is individual or collection data type or not (take user input

# u=eval(input("Enter any value "))
# if type(u) in (float,bool,complex,int):
#     print("Its an individual data type")
# else:
#     print("Its collection data type")

#WAP to check which is greater number among 3

# a=10
# b=9
# c=88
#
# if a>b and a>c:
#     print("a is greater")
# elif b>a and b>c:
#     print("b is greater")
# elif c>a and c>b:
#     print("c is greater")

# wap if input is string print its length else input is list, pop the last element else if input is tuple, reverse the element, else print invalid datatype

# a=eval(input("Enter a value "))
#
# if isinstance(a,str):
#     print(len(a))
# elif isinstance(a,list):
#     a.pop()
#     print(a)
# elif isinstance(a,tuple):
#     print(a[::-1])
# else:
#     print("Invalid datatype")

# wap to give discount to customer based on total price 1000 to 3000, 500 discount, 3001 to 5000, 1000 discount and more thyan 5001, 1200 discount. less than 1000 no discount
# you should purchase three products
#
# x=int(input("Enter the price of first product "))
# y=int(input("Enter the price of second product "))
# z=int(input("Enter the price of third product "))
# tot=x+y+z
# if tot<1000:
#     print("No Discount")
# elif 1000<=tot<=3000:
#     print("500 discount", tot-500)
# elif 3001<=tot<=5000:
#     print("1000 discount", tot-1000)
# elif tot>=5001:
#     print("1200 discount", tot-1200)

# 1.wap to check whether the given number is even and greater than 5
# num=20
#
# if num%2==0:
#     if num>5:
#         print("It is even and greater than 5")

#  2.wap to check the number is odd and check if the number is divisible by 7
# n=35
#
# if n%2!=0:
#     if n%7==0:
#         print("It is odd and divisible by 7")

# 4.wap to validate facebook username and password
# condition is:---> username-->"python"  and password="python masters"

# uid=input("Enter username ")
#
# pas=input("Enter password ")
#
# if uid=="python":
#     if pas=="python masters" :
#         print("Welcome to Facebook")
# if uid!="python":
#     if pas!="python masters":
#         print("Wrong Username and password")
# if uid=="python" and pas!="python masters":
#     print("Wrong password")
# if uid!="python" and pas=="python masters":
#     print("Wrong username")

# 5.wap to Book ticket in Book my show

# condition:---> first it should ask theaters name then it should display the movie available
# then it has to display ticket price and in the end ticket should be booked

# print("Welcome to BookMyShow")
# t=input("Enter the theatre name ")
#
# tdict={"PVR":("RRR","Kalki","KGF"), "CityPride":("KGF","Animal", "Kalki")}
# tktcategory=["Silver", "Gold", "Platinum"]
#
# if t in tdict:
#     print("Movies available :", tdict[t])
#     movie = input("Select Movie ")
#     if movie in tdict[t]:
#         print("Tickets :" ,tktcategory)
#         ticket=input("Select ticket ")
#         if ticket == "Silver":
#             print("Ticket price is 150")
#         elif ticket=="Gold":
#             print("Ticket price is 200")
#         elif ticket=="Platinum":
#             print("Ticket price is 300")
#         else:
#             print("Wrong Ticket Selected")
#
#
#         a=input("Book ticket? (Y/N)")
#         if a=="Y":
#             print("Ticket is booked")
#         elif a =="N":
#             print("Ticket is not booked")
#         else:
#             print("Error")
#     else:
#         print("Wrong Movie Selected")
# else:
#     print("Wrong theatre Selected")


# FOR LOOP
# a=[1,2,3,4,5,6,7]
# for i in a:
    # print(i, end=" ")



# wap to print think and convert it into dictionary
# a="Think"
# d={}
# for i in a:
#     d.update({i:ord(i)})
# print(d)

# 14.wap to check the length of dictionary and length of dictionary is even or Not if even
# print as it is or else add a item and make it even

# D={"a":"apple","b":"ball","c":"cat"}
# if len(D)%2==0:
#     print("Length is even")
# else:
#     D["d"]="dog"
#     print("Now its even", D)

# 8.wap to give 10% off only who is purchasing in credit card and min 3 product should purchase and each product price should be more than 500

# p1=eval(input("Enter 1st products price "))
# p2=eval(input("Enter 2nd products price "))
# p3=eval(input("Enter 3rd products price "))
# total=p1+p2+p3
#
# if p1 & p2 & p3 >= 500:
#     pay = ["Credit Card", "Debit Card", "Cash", "UPI", "NetBanking"]
#     print(pay)
#     userpay = str(input("Select payment option :"))
#     if userpay==pay[0]:
#
#         print("10 percent discount unlocked !!")
#         discount=total*0.1
#         print(F"The final price is {total}-{discount} = {total-discount}")
#     else:
#         print("Discount is only applicable for Credit Card payments")
#         print(F"The final price is {total}")
# else:
#     print("Each product price must be above 500")

#wap to reverse a list

# a=[1,2,3,4]
# l=[]
#
# for i in a:
#     l=[i]+l
# print(l)
#
# m=[1,2,3,4,5]
# m.reverse()
# print(m)

# d={1:"a",2:"b"}
# for i in reversed(d):
#     print(i, d[i])

# 6.wap to find middle element is even or odd
# s=list(input("Enter a list"))
# if s%2==0:
#     print("Its even")
# else:
#     print("Its odd")


# # 1.wap to print the number form 1 -20 segregate even and odd number into list
#
# a=[]
# b=[]
# for i in range(1,21):
#     if i%2==0:
#         a.append(i)
#     else:
#         b.append(i)
# print(a)
# print(b)

# 2.wap to extract vowels and digits in a string
# s="hello123"
#
# for i in s:
#     if i in ["a","e","i","o","u"] or i.isdigit() :
#         print(i)

# 3.wap to capitalize only the first letter of every word in the given list
# l=["vaidegi","rahul","shivam","kapil","patil"]
#
# for i in range(len(l)):
#     l[i]=l[i].capitalize() #takes the index and capitalizes it
# print(l)

# 5.wap to extract only individual data types from the list and sum all the individual data types

# l=["hello",1,23.4,5+6j,"guys",[2,3,4],True,False]
# sum=0
# for i in l:
#     if type(i) in [int, complex, bool, float]:
#         print(i)
#         sum+=i
# print(sum)

# 6.wap to print the count of alphabets and numbers and space in the given string

# s="india got the independence in the year 1947"
# sum1=0
# sum2=0
# sum3=0
# for i in s:
#     if i.isalpha():
#         sum1+=i.count(i)
#     if i.isdigit():
#         sum2+=i.count(i)
#     if i.isspace():
#         sum3+=i.count(i)
#
# print("The alphabets are", sum1)
# print("The numbers are", sum2)
# print("The spaces are", sum3)

# 7.wap to check how many words are present in the given sentence
#
# s="hello world sentence"
# sum1=0
# x=s.split()
# for i in x:
#     print(i)
#     sum1+=i.count(i)
# print("The words present are",sum1)


# 10.wap to print series of factorial(take user input)
# a=int(input("Enter a number to calculate its factorial and display the series"))
# result=1
# for i in range(a,0,-1):
#     print(i, end=" ")
#     result*=i
# print()
# print("The factorial is :", result)


# 8.wap to create a dictionary and print the characters
# and its Ascii value pair

# output:--> {"h":ascii value,"e":ascii value........}
# s="hello world"
#
# d={}
# for i in s:
#     d.update({i:ord(i)})
# print(d)

# 9.wap to create a dictionary and traverse into it and if the length is even print as it else reverse it

# names=["apple","google","yahoo","microsoft","gmail","walmart"]
#
# d={}
# for i in names:
#     if len(i)%2==0:
#         d[i]=i
#     else:
#         d[i]=i[::-1]
# print(d)


# 11.wap to create a dictionary with element and its count pair
# output:--> {'yellow': 2, 'red': 2, 'black': 1, 'pink': 2, 'orange': 1, 'green': 1}
# l=["yellow","red","black","pink","orange","green","red","pink","yellow"]
#
# d={}
# for i in l:
#     if i in d:
#         d[i]+=1
#     else:
#         d[i]=1
# print(d)

# 12.wap to find the length of the string without using inbuilt function
# s="Never Give Up"
#
# sum=0
# for i in s:
#     sum+=1
# print(sum)

# 13.wap to reverse a string without using inbuilt function
# x="you did it guys"
#
# print(x[::-1])

# 14.wap to print alternative character from a given string
#
# s = "hello python"
# print("Alternate characters:", s[::2])

# s = "tomorrow is weekend and non-veg special"
#
# d = {}
# for index, word in enumerate(s.split()):
#     d[index] = word
# print(d)



# i=ord("a")
# while i<=ord("z"):
#     print(chr(i)+chr(i-32), end=" ")
#     i=i+1

# x=[11,3.4,"hii",[1,2,3],{2,3},True]
# i=0
# while i<len(x):
#     if isinstance(x[i], (int,float,complex,bool)):
#         print(x[i])
#     i=i+1

# y=["apple","phone","pen","light","right","sim","java"]
#
# i=0
# while i<len(y):
#     if len(y[i])%2!=0:
#         print(y[i])
#     i=i+1

# i=1
# while i <=20:
#     print(i, end=" ")
#     i=i+1

# i=20
# while i>=1:
#     if i%2==0:
#         print(i, end=" ")
#     i=i-1
# WAP to check the occurences of each letter in a sentence

# i=0
# s="Hello guys Good Morning python is a programming language"
# d={}
#
# while i < len(s):
#     if s[i] in d:
#         d[s[i]]+=1
#     else:
#         d[s[i]]=1
#     i+=1
# print(d)

# Functions
# def Greet():
#     print("Good morning")
# print(Greet())



#wap to check the given number is even
# a=10
# if a%2==0:
#     print("its even")
#
# else:
#     print("its odd")

# def Even_odd(a):
#     if a%2==0:
#         print("its even")
#
#     else:
#         print("its odd")
# Even_odd(10)
# Even_odd(11)



# def Pal(b):
#     if b==b[::-1]:
#         print("its pal")
#
#     else:
#         print("its not")
# Pal("mom")
# Pal("DaD")
# Pal

#
# a = eval(input("enter the element"))
# def Check():
#     # a=eval(input("enter the element"))
#     if a==a[::-1]:
#         print("its pal")
#
#     else:
#         print("its not")
# Check()



# a=100    #---------> global
# def Check():
#     global a
#     b=200  #-------> local
#     a=a+400
#     print(a)
#
# Check()
# print(a)
# # a=a+900
# # print(a)



# def check():
#     b=100
#     return b
# # print(check())
# check()

#wap add sum numbers/----->??


# def Operation(a,b):
#     x=a+b
#     y=a-b
#     z=a*b
#     print(x,y,z)
# Operation(3,4)

# def Operation(a,b):
#     print(a+b,a-b,a*b)
# Operation(3,4)



# def Operation(a,b):
#     x=a+b
#     y=a-b
#     z=a*b
#     return x,y,z
# q=Operation(3,4)
# print(q)





# def Operation(a,b):
#    return a+b,a-b,a*b
# q=Operation(3,4)
# print(q)

"""
def function_name(parameter):
     statement
     statement
     statement
     return data1,data2,data3....

new_var=function_name(argument)
print(new_var)

"""

#positional argument----->

# def check(a,b):
#     print(a+b)
#
# check(1,2)
# check(1,2)




#variable positional argument----->(*args)


# def Fun(*args):
#     print(*args)
#
# Fun(1,2,3,4,5)
# Fun(1)
# Fun()
#
#
# #keyword argument---->(=)------>parameter=argument
#
# def Hiii(a,b,c):
#     print(a+b+c)
#
# Hiii(a=10,b=20,c=30)
# Hiii(a=10)
# Hiii(a=10,b=20)


#variable keyword argument(**kwargs)---->


# def Demo(**kwargs):
#     print(kwargs)
# Demo()
# Demo(a=90)
# Demo(b=89,c="hi",d=100)


#
# def spam(*args,**kwargs):
#     print(args,kwargs)
#
# spam()
# spam(1,2,3,a=900,b=888)

# wap to perform addition and subtraction if "a" is greater than "b" return sum else return difference

# def addorsubtract(a ,b):
#     if a> b:
#         print(a + b)
#     else:
#         print(b - a)
#
#
# addorsubtract(20, 25)

# 2.waf to check string is palindrome or not (take user input)

# def pal(a):
#     if a==a[::-1]:
#         print("Its a palindrome")
#     else:
#         print("Its not a palindrome")
#
# pal(input("Enter a string: "))

# 3.wap to return length of variable keywords arguments

# def lenofkwargs(**kwargs):
#     print("The length of keyword arguments you passed is :", len((kwargs)))
#
# lenofkwargs(a=200,b=600,c=700)


# 4.wap to return length of the variable positional arguments

# def lenofargs(*args):
#     print("The length of keyword arguments you passed is :", len((args)))
# lenofargs(4,5,6,"hii",2.14,5+4j)

# 5.waf to search for character in a given string and return corresponding index
# string="coding part is done"
#
# def findchar(a):
#     if a in string:
#         print("Its index is:", string.index(a))
# findchar("z")

# 6.wap to squaring of the element in the given list
# 7.wap to fetch last digit number

# l = [1, 2, 3, 4, 5]
#
#
# def squareandlastdigit():
#
#     for i in l:
#         print(i*i, end=" ")
#
#     print()
#     print(F"The last digit is {l.pop()}")
#
# squareandlastdigit()

# 8.wap to read 3 numbers from the user,first two numbers should be added and the result of addition should be subtracted by third number

# def addsubtract3(a,b,c):
#     res1=a+b
#     print("The addition of first two numbers is", res1)
#     print("The final result is after subtracting from third number is",res1-c)
#
# addsubtract3(int(input("Enter first number ")), int(input("Enter second number ")), int(input("Enter third number ")))

# 9.wap to find square,cube,square root and cube root of a number
#
# def squarecuberoot(a):
#     print(a*a)
#     print(a*a*a)
#     print(math.sqrt(a))
#     print(math.cbrt(a))
#
# squarecuberoot(int(input("Enter a number ")))

# 10.wap to check the given characters is alphabets or digit or special characters

# def checktype():
#     a=input("Enter a character")
#     if a.isalpha():
#         print("Its a alphabet")
#     elif a.isdigit():
#         print("Its a digit")
#     else:
#         print("Its a special character")
#     return a
#
# print(F"Your character is {checktype()}")


# #Binary Search (always use sorted list)
# w=[3,5,9,15,17]
#
# def binary_search(w,key):
#     li=0
#     hi=len(w)-1
#
#     while li<=hi:
#         mid=(li+hi)//2
#         if w[mid]==key:
#             return mid
#         elif key>w[mid]:
#             li=mid+1
#         else:
#             hi=mid-1
#
# print(binary_search(w,1))
#
# #Linear Search
#
# def linear_search(x,key):
#     n=len(x)
#     for i in range(n):
#         if x[i]==key:
#             return i
#
#     return None
#
# x=[3,5,9,15,17]
# print(linear_search(x,3))


#List Comprehension

# 1) Whenever we dont want have any condition only for loop
#     variable=[expression(print()) for loop condition]
#
# 2) Whwenever we have if and for loop conditions:
#     variable=[TSB(True state block) for loop cndition if condition]
#
# 3) Whenever we have if else and for loop:
#     variable=[TSB if condition else for loop condition]


a=[1,2,3,4,5,6]
k=[]
for i in a:
    k.append(i**2)

print([i**2 for i in a])

print([i for i in a if i%2==0])

x=[1,3,7,8,9,10,11]
y=[]
for i in x:
    if i%2==0:
        y.append(i*i)
    else:
        y.append(i*i*i)
print(y)

print([i**2 if i%2==0 else i**3 for i in x])


#Dictionary comprehension
# 1) variable={key:value for loop condition}
# 2) variable={key:value for loop condition if condition}
# 3) variable={key:value if condition else for loop condition}

x=["python","java","c","c++","sql","pen","copy","no"]

print({i:i[::-1] for i in x if len(i)%2==0})
print({i:i[::-1] if len(i)%2==0 else i for i in x})
