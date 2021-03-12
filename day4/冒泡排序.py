li = [5, 2, 4, 7, 9, 1, 3, 5, 4, 0, 6, 1, 3]
for i in range(len(li)-1):
    for j in range(len(li)-1-i):
        if li[j] > li[j + 1]:
            li[j], li[j + 1] = li[j + 1], li[j]
            print(li)