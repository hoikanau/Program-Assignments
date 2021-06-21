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

food = {
    "chicken":1.59,
    "beef":1.99,
    "cheese":1.00,
    "milk":2.50
}

def totalPrice(food1,food2):
    grandTotal = food1 + food2
    return grandTotal

print(totalPrice(food["chicken"], food["beef"]))

       