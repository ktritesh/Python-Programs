"""""
*author - Ritesh KT
*date - 30-07-2021
*time - 12:20 PM
*title - Simulates a gambler who start with $stake and place fair $1 bets until 
         he/she goes broke (i.e. has no money) or reach $goal.
"""""
import random

class Gambler:
    def __init__(self,start_amount,goal_amount): #initialize constructor using parameter
        self.start_amount=start_amount
        self.goal_amount=goal_amount

    def calculateAverageCount(self):  #define method for calculate percentage of loss and wins
        countBet=0
        winCount=0
        lossCount=0
        while True:
            if self.start_amount==0 or self.start_amount==self.goal_amount:
                break
            else:
                random_value=int(random.choice([0,1]))
                countBet=countBet+1
                if random_value==1:
                    self.start_amount=self.start_amount+1
                    winCount=winCount+1
                else:
                    self.start_amount=self.start_amount-1
                    lossCount=lossCount+1

        return winCount,lossCount,countBet

while True:
    try:
        stake_value=int(input("Enter the start amount : "))
        if stake_value<0:
            print("Please Enter Positive Value")
            continue
        goal_value=int(input("Enter goal amount you want : "))
        if goal_value<0:
            print("Please Enter Positive Value")
            continue

        gambler_object=Gambler(stake_value, goal_value)
        winCount,lossCount,countBet=gambler_object.calculateAverageCount()
        print("Percentage of win count", (winCount / countBet) * 100)
        print("Percentage of loss count", (lossCount / countBet) * 100)
        '''
             return the value and calculate the percentage of win,loss count
        '''
    except ValueError:
        print("Please Enter Digit Value")
    except:
        print("Exception Occured ")

