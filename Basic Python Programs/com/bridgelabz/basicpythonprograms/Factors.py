"""""
*author - Ritesh KT
*date - 27-07-2021
*time - 07:00 PM
*title - Prime Factorization
"""""

f = 0
num = int(input("Enter the number: "))

for i in range(2, num + 1):
    if num%i == 0:
        for j in range(2, int(i/2)):
            if i%j == 0:
                f = 1
                break
        if f == 0:
            print(i)