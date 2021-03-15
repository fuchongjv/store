def nxn(m):
    for i in range(1, m + 1):
        for j in range(i, m + 1):
            print(j, "x", i, "=", (j * i), end="  ")
        print()


n = input("请输入数字：")
n = int(n)

nxn(n)
