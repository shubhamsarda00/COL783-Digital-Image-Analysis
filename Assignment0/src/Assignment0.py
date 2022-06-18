# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 17:43:34 2021

@author: hp
"""
#############################Preprocessing########################################

import cv2
import numpy as np

a=cv2.imread('example.png',0)
cv2.imshow('j',a)
cv2.waitKey()
cv2.destroyAllWindows()
for i in range(1,106):
    if(abs(int(a[i][53])-int(a[i-1][53]))>50):
        print(a[i][53],a[i-1][53],abs(int(a[i][53])-int(a[i-1][53])))
        print(i)
for i in range(1,106):
    if(abs(int(a[53][i])-int(a[53][i-1]))>50):
        print(a[53][i],a[53][i-1],abs(int(a[53][i])-int(a[53][i-1])))
        print(i)        


s=0
b=0
for i in range(106):
    for j in range(106):
        if not (34<=i<72 and 34<=j<72):
            b+=1
            s+=int(a[i,j])
                
print(s/b)  

s=0
b=0
for i in range(34,72):
    for j in range(34,72):
            b+=1
            s+=int(a[i,j])
print(s/b)   

###################################PART1#####################################



for t in range(0,180,10):
    a=np.zeros((106,106))
    a = a.astype('float32')
    for m in range(106):
      for n in range(106):
        if (33<=m<72 and 34<=n<72):
           a[m,n]=172
        else:
           a[m,n]=75
    for i in range(106):
      for j in range(106):
        if not (33<=i<72 and 34<=j<72):
          a[i,j]=a[i,j]+t
    cv2.imwrite(str(t+75)+'.jpg', a)
    b=cv2.imread(str(t+75)+'.jpg',0)
    cv2.imshow('j',b)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    

#########################PART2###############################


import math
a=np.zeros((106,106))

for t in range(10,255,10):
    a=np.zeros((106,106))
    a = a.astype('float64')
    for m in range(106):
        for n in range(106):
            if not(33<=m<72 and 34<=n<72):
                a[m,n]=t 
        
    
    if(t>10):   
        for t1 in reversed(range(t,int(1.3*t))):
            for m in range(33,72):

                for n in range(34,72):
                    a[m,n]=t1             

            print(t,t1)


            cv2.imwrite('a.jpg', a)
            b=cv2.imread('a.jpg',0)
            cv2.imshow('j',b)




            cv2.waitKey(0)
            cv2.destroyAllWindows()
    else:
        for t1 in reversed(range(t,int(10+t))):
            for m in range(33,72):

                for n in range(34,72):
                    a[m,n]=t1             

            print(t,t1)


            cv2.imwrite('a.jpg', a)
            b=cv2.imread('a.jpg',0)
            cv2.imshow('j',b)




            cv2.waitKey(0)
            cv2.destroyAllWindows()    