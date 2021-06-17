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


        