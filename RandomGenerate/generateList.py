import random

# ランダム
def generateList(num, ragMin, ragMax):
    list1 = []
    for x in range(0, num):
        list1.append(random.randint(ragMin*10, ragMax*10)/10)
    return list1

# 累計ランダム
def generateAddedList(num,ragMin,ragMax):
    list2 = generateList(num, ragMin, ragMax)
    for x in range(1, num):
        list2[x] += list2[x-1]
    return list2

# list to string
def strList(list1):
    for x in range(0, len(list1)):
        list1[x] = str(list1[x])
    return list1