import random

num = 30
ragMin = 200
ragMax = 500
# ランダム
list1 = []
for x in range(0, num):
    list1.append(random.randint(ragMin*10, ragMax*10)/10)

# 累計ランダム
list2 = list1.copy()
for x in range(1, num):
    list2[x] += list2[x-1]

print(list1)
# print(list2)
