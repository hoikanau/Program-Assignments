# loopCounter = const(9)
# for x = 0 to loopCounter:
#     repeat
#         value = input("Enter a number between 1 and 10 inclusive")
#     until value > 0 and value < 11
#     print(calculate(value))
# next x
loopCounter = 19
def loopValue(Times):
    value = int(input("enter a number between 1 - 10"))
    for x in range (Times):
        value = value + 1
        print(value)
    return value

loopValue(loopCounter)