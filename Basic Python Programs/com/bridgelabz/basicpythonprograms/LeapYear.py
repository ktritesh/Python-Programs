"""""
*author - Ritesh KT
*date - 27-07-2021
*time - 07:00 PM
*title - Leap year or not
"""""

year = int(input("Enter Year: "))

if year % 4 == 0 and year % 100 != 0:
    print(year, "is a Leap Year")
elif year % 100 == 0:
    print(year, "is not a Leap Year")
elif year % 400 == 0:
    print(year, "is a Leap Year")
else:
    print(year, "is not a Leap Year")