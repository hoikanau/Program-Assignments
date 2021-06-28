Bob = {
    "test0" : 75,
    "test1" : 65,
    "test2" : 42,
    "test3" : 73
}

Helen = {
    "test0" : 62,
    "test1" : 65,
    "test2" : 67,
    "test3" : 79
}

Vic = {
    "test0" : 13,
    "test1" : 17,
    "test2" : 19,
    "test3" : 17
}

def scoreSearch(student, testNum):
    score = student[testNum]
    print("This student's score for " + str(testNum) + " is: " + str(score))

scoreSearch(Vic, "test0")