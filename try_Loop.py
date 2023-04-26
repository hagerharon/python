# #######global loop####
# # i = 5
# # j = 1
# # for x in range(i):
# #     print("\nfirstloop ",end='')
# #     while j <= 4:
# #         print("chiled loop  ",end='')
# #         j += 1
# ##############
# #######local loop####
# # for x in range(0, 5):
# #     print("\nfirstloop")
# #     for j in range(0, 4):
# #         print("chiled loop",end='')
# ###################################
# #make pyramids from * but n range
# # rangeStars = 8
# # userNumber = int(input("Enter number just in range 7 "))
# # for i in range(0, userNumber):
# #     if userNumber >= rangeStars:
# #         print("Your range unvalid")
# #         break;
# #     i += 1
# #     for x in range(0, i):
# #         print("*",end='')
# #     print()
# ###############################################
# # rangeStars = 8
# # userNumber = int(input("Enter number just in range 7 "))
# # for i in range(0, userNumber):
# #     if userNumber >= rangeStars:
# #         userNumber = int(input("Enter number just in range 7 Again "))
# #         for i in range(0, userNumber):
# #             #i += 1
# #             for y in range(0, i):
# #                 print("*", end='')
# #             print()
# #         continue
# #     else:
# #         i += 1
# #         for y in range(0, i):
# #             print("*",end='')
# #         print()
# #########program validtion ############
# import random
#
#
# # rangeStars = 8
# # userNumber = int(input("Enter number just in range 7 "))
# # i = 0
# #
# # def stars():
# #     for y in range(0, i):
# #         print("*", end='')
# #     print()
# #
# # def newstars():
# #     for w in range(0, userNumber):
# #         w += 1
# #         for x in range(0, w):
# #             print("*", end='')
# #         print()
# #
# # for i in range(0, userNumber):
# #     if userNumber >= rangeStars:
# #         userNumber = 0
# #         userNumber = int(input("This the last try to (enter number just in range 7) "))
# #         if userNumber >= rangeStars:
# #             userNumber = 0
# #             print("Game over")
# #             break
# #         else:
# #             newstars()
# #             break
# #     else:
# #         i += 1
# #         stars()
#
# ###############try global############
# # a = 'hager'
# # def koko():
# #     global a
# #     a = 'koki'
# # # *****must call function*****
# # koko()
# #
# # print (a)
# ##################
# # def add_sub(a, y):
# #     c = a * y
# #     j = a + y
# #     e = a - y
# #     return c, j, e
# # result1,result2, result3 = add_sub(9,4)
# # print(result2, result3)
#
# ##############array###########
# # from array import *
# # from random import *
# # random_m = random.
# # print(random_m)
# # x = 0
# # newarray = array('i', [1, 5, 7, -8, 19])
# # for i in range(len(newarray)):
# #     print(i)
# # for a in newarray:
# #     print(a)
# # while x < len(newarray):
# #     print("alla is beautful like beauty")
# #     x += 1
#
# # userArray = array('i', [])
# # lenArrUser = int(input("Enter your number of data free:  "))
# # b = 0
# # bb = 0
# # for b in range(lenArrUser):
# #     #for bb in range(b):
# #     valuesArrUser = int(input("Write value: "))
# #     userArray.append(valuesArrUser)
#
#     # *****it print all values of userArray ---- 2 5 8 25 ****
# # for c in userArray:
# #     print(c)
#
#     # *****it print all userArray ---- array('i', [])****
# # print(userArray)
#
# # ******* search value and get its index ******
# # d = 0
# # searchUser = int(input("Write your value to find its if exsited:  "))
# #
# # for d in userArray:
# #     if searchUser == d:
# #         print("Result your search= ", d, " & its index= ", userArray.index(d))
# #         break
# #
# # else:
# #     print("Sorry, your number not found")
# ###################### make function dictionary ####################################
# def tuplFun(**data):
#     for i, j in data.items():
#         print(i, j)
# tuplFun(nameUser='hager', age=30, city='egypt')
#
#
# def tuplFun2(*data2):
#     for u in data2:
#         print(u)
# tuplFun2('hager', 30, 'egypt')
############### make opertion on set of open numbers ####################
# def suum(a,*b):
#     c = a
#     for i in b:
#         c = c + i
#     print(c)
# suum(5,3,7,8)
########### print numbers of number double & single in list#################
# lst = [15, 20, 45, 30, 10, 15]
# def numberType (lst):
#     second = 0
#     singl = 0
#     for i in lst:
#         if i % 2 == 0:
#             second += 1
#         else:
#             singl += 1
#     return second, singl
#
# second,singl = numberType(lst)
# print("second number= {} single numbers= {}".format(second,singl))
################ fibonacci ###########################
# def fib(n):
#     a = 0
#     b = 1
#     if n == 1:
#         print(a)
#     else:
#         print(a)
#         print(1)
#         for i in range(2, n):
#             c = a + b
#             a = b
#             b = c
#             print(c)
# fib(10)
################# recurison function ###########################
# import sys
# n = int(input("enter num to fact"))
# sys.setrecursionlimit(1000)
# print(sys.getrecursionlimit())
# i = 1
# def fact(n):
#     global i
#     if i == n+1:
#         return 1
#     c = n * i
#     print(f"{n} * {i} = {c}")
#     i = i + 1
#     fact(n)
# fact(n)
#############filter/map/lambda##############
# lst = [20, 50, 2, 3, 35, 19, 100, 30]
# lst_filter = list(filter(lambda x: x %2==0,lst))
# print(lst_filter)
# lst_name = ['ziad','mahmoud','ahmed']
# lst_nameMap = list(map(lambda i:" "+i+" ",lst_name))
# print(lst_name)
# print(lst_nameMap)
##############decorate###########
# def diving(a, b):
#     if a < b:
#         a, b = b, a
#     return a/b
# print(diving(5,10))
##############inhrait################
# class A:
#     def __init__(self):
#         print('hello main class')
#
#     def mainffun1(self):
#         print('main function A')
#
# class b(A):
#     def __init__(self):
#         super().__init__()
#         super().mainffun1()
#         print('finmain child')
#
#     def featureb(self):
#         print('featureb')
#
# class F(b):
#     def __init__(self):
#         print('\nmainThird',)
#         super().mainffun1()
#
#     def thirdfun(self):
#         print('lallafdj')
# c = b()
# v= F()
################### memonzition ###############
# import time
# def saveIndex(idx, num=None):
#
#     if num is None:
#         num = {}
#     if idx in num.keys():
#         return num[idx]
#     if idx == 0:
#         print(0)
#     if idx == 1:
#         print(1)
#     a = 0
#     b = 1
#     print(a)
#     print(b)
#     startone = time.time()
#     for i in range(2, idx+1):
#         c = a + b
#         a = b
#         b = c
#         print(c)
#     endone = time.time()
#     print('time equal one', endone - startone)
#
#
# saveIndex(10)

#time equal 5.221366882324219e-05

# def fib(n):
#     a = 0
#     b = 1
#     if n == 0:
#         print(a)
#     if n == 1:
#         print(b)
#     else:
#         print(0)
#         print(1)
#     start = time.time()
#     for i in range(2, n):
#         c = a + b
#         a = b
#         b = c
#         print(c)
#     end = time.time()
#     print('time equal two', end - start)
#
#
# fib(10)
##########itrartor############
# class TryItrator:
#     def __init__(self):
#         self.num = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.num <= 10:
#             self.num += 1
#             return self.num
#         else:
#            raise StopIteration
#
# values= TryItrator()
# print(next(values))
##########generator#########
#******to save use itrator & next functions******
# def tryGenrt():
#     num = 0
#     while num <= 10:
#         sq = num * num
#         yield sq
#         num += 1
#
# values = tryGenrt()
# for i in values:
#     print(i)
############## try & exception ###########
# a = 5
# print('my number: ', a)
# try:
#     b = int(input('enter your numerber:'))
#     c = a/b
#     print('operation dividtion= ', a/b)
# except ValueError as e:
#     print('invalid type data')
# except ZeroDivisionError as e:
#     print('number must be != zero', e)
# except Exception as e:
#     print('try ya man')
# finally:
#     print('Good try')
################threading##############
# from time import sleep
# from threading import *
#
# class One(Thread):
#     def run(self):
#         for i in range(5):
#             print("hello")
#             sleep(1)
#
# class Two(Thread):
#     def run(self):
#         for i in range(200):
#             print('hiiii')
#             sleep(1)
# one = One()
# two = Two()
# one.start()
# sleep(0.2)
# two.start()
#
# one.join()
# two.join()
#
# print("byeeeee")
#################### mid######
# pos = -1
# def searchMid(list,n):
#     l = 0
#     u = len(list)-1
#     while l <= u:
#         mid = (l+u) // 2
#         if list[mid] == n:
#             global pos
#             pos = mid
#             return True
#         else:
#             if list[mid] < n:
#                 l = mid+1
#             else:
#                 u = mid -1
#     return False
# list=[9,8,7,10,11,12]
# n = 12
# if searchMid(list,n):
#     print('found')
# else:
#     print('not')
##########my bubble sort###############
# listt = [2,5,9,11,50,45,49]
# listt.sort(reverse=True)
# print(listt)
# for i in range(0,len(listt)):
#     outerlp = i
#     for j in range(i+1):
#         if listt[j] < listt[i]:
#             listt[i],listt[j] = listt[j],listt[i]
# print(listt)
#**************increadble*******
# listt = [3,2,9,11,50,45,49]
# listt.sort()
# print(listt)
# for i in range(len(listt)-1,0,-1):
#     outerlp = i
#     for j in range(i-1):
#         if listt[j] > listt[i]:
#             listt[i],listt[j] = listt[j],listt[i]
# print(listt)
################socket###############
# import socket
# s = socket.socket()
# print('create server')
# s.bind(('localhost',55555))
# #request , address = s.recv(1024)
# s.listen(3)
# print('waite for connection')
# while True:
#     request,address = s.accept()
#     print('connected with: ',address)
#     request.send(bytes('welcome in my site','utf-8'))
#         #, s.recv(1024)
#     #requesTrans = request.decode("UTF-8")
#     s.close()
################send email############
import smtplib

server = smtplib.SMTP('smtp.gmail.com',587)
server.ehlo()
server.starttls()
server.login('haronhager19@gmail.com','*ALLA*akbr100')
try:
    subject='important message'
    body='Hello my bst friend gogo'
    message='Subject: {}\n\n'.format(subject,body)
    server.sendmail('haronhager19@gmail.com','haronhager19@gmail.com',message)
    print('success')
except Exception as e:
    print('failed',e)
##################private -- protect -- public ##########
# class Person:
#     def __init__(self, first_name, last_name, age):
#         self.__first_name = first_name
#         self._last_name = last_name
#         self.age = age
#         self.__fullname = ''
#         self.__update_fullname()
#     def __update_fullname(self):
#         self.__fullname = self.__first_name + " " + self._last_name
#
#     def last_name(self,val):
#         if type(val) != str or val == "":
#             raise ValueError('first name must not empty')
#         self._last_name = val
#         self.__update_fullname()
#         print(self.__fullname, self.age)
# p = Person('hager','haron',30)
# p.last_name('hageeer')
#########json file#########
import json
# data = {
#     "P1":{"name":"hager", "age":30, "city":"minia"}, "P2":{"name":"zozo", "age":43, "city":"giza"}, "P3":{"name": "mohamed", "age": 50, "city": "mokatm"}
# }
# fileCreate = open('myJson.json','w')
# json.dump(data,fileCreate)
# fileCreate.close()

#***********open*************
# insetData = "OpenmyJson.json"
# getData = open(insetData,'r')
# loadData = json.load(getData)
# getData.close()
# print(loadData)
#############jypter##########




