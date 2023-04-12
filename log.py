from queue import Queue
from time import sleep

class MyStack:
    def __init__(self) -> None:
        self.data =[]
        self.size = 0
    def push(self,value):
        self.data.append(value)
        self.size += 1
        return None
    def empty(self):
        return self.size == 0
    def pop(self):
        if not self.empty():
            self.size -= 1
            return self.data.pop()
        raise Exception("Queue is empty")         
    def top(self):
        if not self.empty():
            return self.data[-1]

class Solution:
    def calPoints(self, operations: list[str]) -> int:
        a=[]
        for i in operations:
            if i=="+":
               a.append(a[-1]+a[-2])
            elif i=="D":
                a.append(a[-1]*2)
            elif i=="C":
                a.pop()
            else:
                a.append(int(i))
        return sum(a)
        





# class Solution:
#     def firstUniqChar(self, s: str) -> int:
#         dc={}
#         cnt=0
#         for i in s:
#             if i in dc:
#                 dc[i]+=1
#             else:
#                 dc[i]=1
#         for i in range(dc):
#             if dc[s[i]]==1:
#                 return i
#         return -1
        

