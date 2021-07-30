"""""
*author - Ritesh KT
*date - 30-07-2021
*time - 12:20 PM
*title - Simulates a gambler who start with $stake and place fair $1 bets until 
         he/she goes broke (i.e. has no money) or reach $goal.
"""""
import random
import stake

class Gambler:

    def gamePlay(self): #find average of win and loss in gambler game
        winCount = 0
        loosCount = 0
        playCount = 0
        makeMoney = self.stake
        while 0 < makeMoney < self.goal and playCount < self.numberOfTimes:
            radomNumber = random.randint(0,1)
            playCount += 1
            if radomNumber == 0:
                makeMoney = makeMoney - 1
                loosCount = loosCount + 1
            else:
                winCount = winCount + 1
                makeMoney = makeMoney + 1

            winPercentage = (winCount / playCount) * 100
            loosePercentage = (loosCount / playCount) * 100
            print("Win Percentage: ", winPercentage)
            print("Loss Percentage: ", loosePercentage)

    def setCondition(self): # Taking input from user
        while True:
            try:
                self.stake = int(input("Enter the amount to start gambling: "))
                self.goal = int(input("Enter amount for win: "))
                self.numberOfTimes = int(input("How many times you want to play: "))
                break
            except ValueError:
                print("You have enter a wrong value")

if __name__ == '__main__': # main method to execute several methods
    gambler = Gambler()    # Creating object of gambler class
    gambler.setCondition() # calling setCondition method using reference variable
    gambler.gamePlay()     # callig gamePlay method to play gambling




