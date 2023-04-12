class Stasc:
    def __init__(self) -> None:
        self.__date=[]
        self.__size=0
    def push(self,value):
        self.__date.append(value)
        self.__size+=1
    def empty(self)->bool:
        return self.__size==0
    def pop(self):
        if not self.empty():
            self.__size-=1
            return self.__date.pop()
        raise Exception("stack is empty")
    def top(self):
        if not self.empty():
            return self.__date[-1]
        raise Exception("stasc is empty")
    @property
    def Size(self):
        return self.__size
# if __name__=="__main__":
#         st=Stasc()
#         st.push("a")
#         st.push("b")
#         st.push("c")
#         while not st.empty():
#             print(st.pop())
class Solution:
     def removeKdigits(self, num: str, k: int) -> str:
         st=Stasc()
         for el in num:
             while k>0 and not st.empty() and st.top()>el:
                 st.pop()
                 k-=1
             st.push(el)
         while k>0 and st.empty():
             st.pop()
         ans=ans[::-1]
         if ans=="":
             ans="0"
         return str(int(ans))
    