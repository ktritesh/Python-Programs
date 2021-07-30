"""""
*author - Ritesh KT
*date - 30-07-2021
*time - 07:00 AM
*title - Write a Stopwatch Program for measuring the time that elapses between
         the start and end clicks
"""""
from time import time

class SimulateStopWatch:
    startTime = 0
    stopTime = 0
    elapsTime = 0

    def inputStartTime(self):
        self.startTime = int(time() * 1000)               # input start time in millisecond

    def inputStopTime(self):
        self.stopTime = int(time() * 1000)                # input stop time in millisecond

    def elapsedTime(self):
        self.elapsTime = self.stopTime - self.startTime   # calculate elapsed time and display
        print(int(self.elapsTime) / 1000, "sec")          # print elapsed time in second

if __name__ == '__main__':                                # main method
    sWatch = SimulateStopWatch()                          # creating object of the class
    while True:
        try:                                              # exception handling
            startInput = int(input("Enter 1 for start: "))
            if startInput != 1:
                print("Wrong input !! Enter 1 only")
                continue
            sWatch.inputStartTime()                       # inputStartTime method call

            stopInput = int(input("Enter 2 for stop: "))
            if stopInput != 2:
                print("Wrong input !! Enter 2 only")
                continue
            sWatch.inputStopTime()                        # inputStopTime Method call
            sWatch.elapsedTime()                          # elapsedTime Method call
            break
        except ValueError:
            print("You are giving wrong input !!!  Enter 1 for start and 2 for stop")