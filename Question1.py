class Calculator:
    def __init__(self, input1, input2):
        self.input1 = input1
        self.input2 = input2

    def adder(self):
        return self.input1 + self.input2

    def subtractor(self):
        return self.input1 - self.input2

    def multiplier(self):
        return self.input1 * self.input2

    def divider(self):
        return self.input1 / self.input2

    def clear(self):
        self.input1 = 0
        self.input2 = 0


input1 = int(input("First number: "))
input2 = int(input("Second number: "))

x = Calculator(input1, input2)
print("Addition: ", x.adder())
print("Subtraction: ", x.subtractor())
print("Multiply: ", x.multiplier())
print("Division: ", x.divider())
x.clear()