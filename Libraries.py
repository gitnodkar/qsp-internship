import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pandas.io.clipboard
from PIL.TiffImagePlugin import DATE_TIME
from pandas import to_datetime

# x = np.array([11,14,15,99,100])
# print(x)
# print(x[1])
# y=x.view()


# x=np.array([1,2,3,4,5,6,7,9])
# w=np.array_split(x,4)
# y=np.split(x,2)
# print(y)
# print(w)

# x = np.array([1, 2, 3, 4, 5])
# y = np.array([6, 7, 9, 2, 3])
# print(np.concatenate((x,y)))
# print(np.stack((x,y)))
# print(np.hstack((x,y)))
# print(np.vstack((x,y)))
# print(np.dstack((x,y)))

# print(np.add(x,y))
# print(np.subtract(x,y))
# print(np.divide(x,y))
# print(np.mod(x,y))
# print(np.power(x,y))


# Pandas Date and Time
# x=pd.DataFrame({"DATE_Time":["2025-03-06 10:02:25","2025-02-25 03:24:45"]})
# x["DATE_Time"]=pd.to_datetime(x["DATE_Time"])
#
# x["HOUR"]=x["DATE_Time"].dt.hour
# x["Minute"]=x["DATE_Time"].dt.minute
# x["Second"]=x["DATE_Time"].dt.second
# x["Day"]=x["DATE_Time"].dt.day
# x["Month"]=x["DATE_Time"].dt.month
# x["Weekday"]=x["DATE_Time"].dt.weekday (0=monday, 6=Sunday)
# print(x)

# Alternative Method
# DATE_TIME=["2025-03-06 10:02:14","2024-05-20 12:45", "2025-01-05"]
# x={"DATE_TIME":DATE_TIME}
# data=pd.DataFrame(x)
# data["DATE_TIME"]=pd.to_datetime(data["DATA_TIME"])
# data["HOUR"]=data["DATA_TIME"].dt.hour
# print(data)

# DT=["10:02","11:45","09:30"]
# x={"DT":DT}
# data=pd.DataFrame(x)
#
# data["Hour"]=data["DT"].str.slice(0,2).astype(int)
# print(data)

# EID=[9,10,11,12,29]
# sal=[1000,1500,2000,2100,1600]
# combined={"EID":EID,"SALARY":sal}
# x=pd.DataFrame(combined)
# print(x.sort_index())
# print(x.sort_values(by='EID'))
# print(x)



# GENERATOR
# It will generate the sequence of elements. WE can save the memory, as oppose to a function.
# The return keyword terminates the condition cannot be use multiple times
# The yield keyword pauses the execution. multiple uses
# next keyword in generator is used to print.

# s=[1,2,3,4,5,6]
#
# def square(s):
#     for i in s:
#         print(i**2)
#
# square(s)
#
#
# def square(s):
#     for i in s:
#         yield (i**2)
#
# x=square(s)
# print(next(x))
# print(next(x))
# print(next(x))

# WAP to do opeartons add, subtraction, multipliacation

# def operation(a,b):
#     yield a+b,a-b,a*b
#
# print(operation(9,4))
#
# x = operation(10,25)
# print(next(x))


# def check(t):
#     for i in t:
#         if len(i)%2==1:
#             yield (i)
#
# x = check(["sunny","mohan","java","python"])
# print(next(x))

# MATPLOTLIB

# x = ["Python", "Java", "C++"]
# rank = [80,75,70]
#
# plt.pie(rank, labels=x, autopct="%1.2f%%", explode = [0.1,0,0], colors = ["r","y","c"], shadow=True, radius=1.5, labeldistance=1.5, startangle=0, counterclock = True, rotatelabels=True, textprops ={"fontsize":5}, wedgeprops={"linewidth":2, "edgecolor":"y"})
# plt.legend(loc="lower left")
# plt.show()
#
# y = [1,2,3,4,5,6,7]
# z = [50,55,60,65,74]
# plt.plot(y,z,c="r", ls="dotted",marker="o",lw=10,ms=5,mec=2)
# plt.xlabel("x-axis")
# plt.ylabel("y-axis")
# plt.legend()
# plt.show()


a = [1,2,3,4,5,6,7,8]
b = [2,5,6,4,3,2,7,8]
color=["r","y","m","y","g","b","c","r"]
size=[100,50,10,20,40,10,15,20]
plt.scatter(a,b,c=color,s=size,marker="*",alpha=0.2,label="Information",edgecolors="y")
plt.title("Scatter Plot")
plt.legend()
plt.show()

name = ["Rahul","Rohit","Virat","David"]
score = [100,200,600,400]
iplscore = [50,125,300,200]
championscore = [250,50,200,100]
width=0.3
p=np.arange(len(name))
p1=[i+width for i in p]
p2=[i+width for i in p1]
print(p1)
plt.bar(p,score,color="g",width=0.3, edgecolor, linestyle, label="Score")
plt.bar(p1,iplscore,color="r",width=0.3, edgecolor, linestyle, label="IPL Score")
plt.bar(p2,championscore,color="b",width=0.3, edgecolor, linestyle, label="Champions Trophy Score")
plt.xlabel("Player name")
plt.ylabel("Score")
plt.tile("The scores of diff players")
plt.legend()
plt.xticks(p1,name)s
plt.show()
