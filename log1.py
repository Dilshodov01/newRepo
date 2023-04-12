from time import perf_counter
from random import randint
from typing import Union ,Optional

class Oopp:
    def __init__(self,mk:Optional[Union[list,tuple]]) -> None:
        self.ms=tuple(mk)
    def serch(self,key):
        l=0
        r=len(self.ms)-1
        while l<r:
            orta=(l+r)//2
            if self.ms[orta]<key:
                l=orta+1
            else:
                r=orta
        return r

ms=list()
for i in range(1,10**3):
    ms.append(i)
db=Oopp(ms)
key=14
uz=db.serch(key)
if ms[uz]==key:
    print(f"{key}-->{ms[uz]}hammai joyida")
else:
    print(f"{ms[uz]}natija natogri")


        




