"""""
*author - Ritesh KT
*date - 27-07-2021
*time - 05:45 PM
*title - Flip coin
"""""
import random

tailCount = 0
headCount = 0
coinResult = 0

count = int(input("Enter number of times you want to flip the coin: "))

class FlipCoin:
    for i in range(1, count):
        coinResult = random.uniform(0, 1)
        print(coinResult)
        if coinResult < 0.5:
            tailCount += 1
        else:
            headCount += 1
    headPercentage = (headCount / count) * 100
    print("Head Percentage is: ", headPercentage)
    tailPercentage = (tailCount / count) * 100
    print("Tail percentage is: ", tailPercentage)
