import random as rand
import numpy as np

# pi = 0
# while pi < 100:
#     print(pi)
#     pi+= 1

# for i in range (0,100,1):
#     print(i)
#     i+= 1

def fibanacciExe(max):
    i = 0
    j = 1
    k = 0
    while i < max:
        print(k)
        k = i + j
        i = j
        j = k

print(fibanacciExe(30))
print(" ")
print(" ")
print(" ")
def primeFinder(max):
    for i in range (2, max):
        for j in range(2,i):
            if i % j == 0:
                break
        else:
            print(i)
    return(max)

print(primeFinder(30))

def triangleArea(base, height):
    area = base*height/2
    return area

print(triangleArea(3,9))

n = 5
m = 5
areaList = []
for b in range (0,n):
    for h in range (0,m):
        areaList.append(triangleArea(b,h))

print(areaList)
Menu = {
    "Burgers": 12.99,
    "Fries": 3.99,
    "Shakes":1.50
}

def foodSum(Dict, item1, item2):
    sum = Dict[item1] + Dict[item2]
    print("The total price of your order of " + item1 + " and " + item2 + " is $" + str(sum))
    sum += 1.0925
    print("With tax that will be $ " + str(sum))

foodSum(Menu, "Burgers", "Fries")

listPlayers = [1,2,3,4,5,6,7]
length = len(listPlayers)
for i in range (length):
    length = len(listPlayers)
    randomNumber = rand.randint(0,length-1)
    listPlayers.pop(randomNumber)
    print(listPlayers)

#add things = append, extend, insert
# take over things = pop, remove, clear

# food = {
#     "chicken":1.59,
#     "beef":1.99,
#     "cheese":1.00,
#     "milk":2.50
# }

# def totalPrice(Dict, food1, food2):
#     grandTotal = Dict[food1] + Dict[food2]
#     print("The total price of your order of " + food1 + " and " + food2 + " is " + str[grandTotal])

# totalPrice(food,"cheese","beef")

listNumbers = []
size = 5
for i in range(size):
    listNumbers.append(10*np.random.random())

print(listNumbers)
listNumbers.sort()
print(listNumbers)


listCities = ["New York", "Los Angeles", "Oakland", "Chicago", "Paris"]
listCities.sort(key=len)