"""""
*author - Ritesh KT
*date - 27-07-2021
*time - 07:00 PM
*title - power of two
"""""

i = 0
power = 1

p = int(input("Enter the no to calculate its power: "))

while i <= p:
    print(i , " " ,power)
    power = 2 * power
    i = i + 1