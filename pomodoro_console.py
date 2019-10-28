import os
import time


class Pomodoro:
    def __init__(self):
        self.minutes = 25
        self.secs = 0
        self.brminutes = 30
        self.brsecs = 0
        self.times = 1
        self.rounds = 4
        self.clean = "clear" #For Linux
        #self.clean = "cls" #For Windows

    def main(self):
        input("Start timer ")
        Pomodoro.timer(self)

    def timer(self):
        while True:

            if self.minutes < 10 and self.secs < 10:
                os.system(self.clean)
                print(f"Round {self.times} of {self.rounds} : 0{self.minutes}-0{self.secs}")

            elif self.minutes < 10:
                os.system(self.clean)
                print(f"Round {self.times} of {self.rounds} : 0{self.minutes}-{self.secs}")

            elif self.secs < 10:
                os.system(self.clean)
                print(f"Round {self.times} of {self.rounds} : {self.minutes}-0{self.secs}")

            else:
                os.system(self.clean)
                print(f"Round {self.times} of {self.rounds} : {self.minutes}-{self.secs}")

            if self.secs == 0:
                self.minutes -= 1
                self.secs = 60

            if self.minutes < 0:
                self.times += 1
                self.minutes = 24

            if self.times > self.rounds:
                Pomodoro.br(self)

            self.secs -= 1
            time.sleep(1)

    def br(self):
        self.times = 1
        while True:
            if self.brminutes < 10 and self.brsecs < 10:
                os.system(self.clean)
                print(f"Break : 0{self.brminutes}-0{self.brsecs}")

            elif self.brminutes < 10:
                os.system(self.clean)
                print(f"Break : 0{self.brminutes}-{self.brsecs}")

            elif self.brsecs < 10:
                os.system(self.clean)
                print(f"Break : {self.brminutes}-0{self.brsecs}")

            else:
                os.system(self.clean)
                print(f"Break : {self.brminutes}-{self.brsecs}")

            if self.brsecs == 0:
                self.brminutes -= 1
                self.brsecs = 60

            if self.brminutes < 0:
                self.brminutes = 30
                self.minutes = 24
                Pomodoro.timer(self)

            self.brsecs -= 1
            time.sleep(1)


pomodoro = Pomodoro()
pomodoro.main()
