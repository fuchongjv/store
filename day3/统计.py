List = [1, 4, 7, 5, 8, 2, 1, 3, 4, 5, 9, 7, 6, 1, 10]

a = {}
for i in List:
    if List.count(i) > 1:
        a[i] = List.count(i)
print(a)