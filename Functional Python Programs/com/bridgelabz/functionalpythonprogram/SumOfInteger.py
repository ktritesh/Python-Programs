"""""
*author - Ritesh KT
*date - 28-07-2021
*time - 07:30 PM
*title - Sum Of Integer Add to zero
"""""
from array import *

class SumOfInteger():
    def __init__(self, size):
        self.size = size  #Initialize the constructor using parameters


    def sumOfdigit(self):  #Defining sumOfDigit method
        arr = array('i', [])
        for i in range(self.size):
            print("Enter the number: ")
            num = int(input())
            arr.append(int(num))

        print("you have entered: ")
        print(arr)
        x = len(arr)
        for i in range(x):
            fno = arr[i]
            i = i + 1
            for j in range(x):
                sno = arr[j]
                j = j + 1
                for k in range(x):
                    tno = arr[k]
                    k = k + 1
                    sum = fno + sno + tno
                    if sum == 0:
                        print(fno, sno, tno)
try:
    size = int(input("Enter the no of element you want add : "))
    sumofintegerobject = SumOfInteger(size)
    fno, sno, tno = sumofintegerobject.sumOfdigit()
except:
    print("No triples")



