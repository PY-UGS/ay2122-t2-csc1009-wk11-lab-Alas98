class clockTime:
    def __init__(self):
        self.Hours = 0
        self.Minutes = 0
        self.Seconds = 0

    def setHours(self):
        self.Hours = input("Enter number of hours:")

    def setMinutes(self):
        self.Minutes = input("Enter number of minutes:")

    def setSeconds(self):
        self.Seconds = input("Enter number of seconds:")

    def setTime(self):
        self.setHours()
        self.setMinutes()
        self.setSeconds()

    def showTime(self):
        print(self.Hours + ":" + self.Minutes + ":" + self.Seconds)


x = clockTime()
x.setHours()
x.setMinutes()
x.setSeconds()
x.showTime()