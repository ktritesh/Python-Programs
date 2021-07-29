"""""
*author - Ritesh KT
*date - 27-07-2021
*time - 07:00 PM
*title - Harmonic Number
"""""

def harmonic(num):
    if num <= 0:
        print("Enter the number greater than Zero")
        return
    i = 1
    total = 0
    while i <= num:
        print(f"1/{i}")
        total += 1 / i
        i += 1
    print(f"Harmonic number is {total}")


harmonic(int(input("Enter the number to find harmonic: ")))