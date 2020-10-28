import random

def sort():
    sort_me = []

    for x in range(20):
        abc = random.randint(1, 100)
        sort_me.append(abc)

    n = len(sort_me)

    for z in range(n - 1):
        flag = 0
        for y in range(n - 1):
            if sort_me[y] >= sort_me[y + 1]:
                sss = sort_me[y]
                sort_me[y] = sort_me[y + 1]
                sort_me[y + 1] = sss
                flag = 1
        if flag == 0:
            break
    print(sort_me)

sort()
                