from random import *
from time import perf_counter







































# class Solution:
#     def strStr(self, hay: str, ne: str) -> int:
#         if  ne in hay:
#             for i in range(0,len(hay)):
#                 h=''
#                 for j in range(len(ne)):
#                      if hay[i+j]==ne[j]:
#                          h+=ne[j]
#                      else:
#                          break
#                 if h==ne:
#                     return i




# def tub(n):
#     sm=0
#     if n==1:
#         return False
#     for i in range(2,int(n**(0.5))+1):
#         if n%i==0:
#             return False
#     return True



# ms=list()
# a,b=map(int,input().split())


# for i in range(a,b):
#     if tub(i):
#         ms.append(i)
# if ms:
#     print(max(ms,key=lambda x: sum(map(int,list(str(x))))))
# else : print(-1)


# a,k,l,r=map(int,input().split())
# s=0
# for i in range(l,r+1):
#     if i%a==k:
#         s+=1
# print(s)


# n=int(input())
# ms=map(int,input().split())
# st=""
# for i in ms:
#     if n//i==2:
#         st=i
# print(st)

# class Solution:
#     def lengthOfLastWord(self, s: str) -> int:

# s=input().split()
# ms=list()
# for i in s:
#     if i !=" ":
#         ms.append(i)
# sm=max(ms)
# print(len(sm))