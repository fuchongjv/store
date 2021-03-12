names = [
    ["曹操", "56", "男", "106", "IBM", 500, "50"],
    ["大乔", "19", "女", "230", "微软", 501, "60"],
    ["小乔", "19", "女", "210", "Oracle", 600, "60"],
    ["许褚", "45", "男", "230", "Tencent", 700, "10"]
]
i = 0
ave = 0
age = 0
while i <= 3:
    names[i][1] = int(names[i][1])
    age += names[i][1]
    ave += names[i][5]
    i += 1
    if i == 4:
        print("平均薪资为：", ave // 4)
        print("平均年龄为：", age // 4)

names.append(["刘备", "45", "男", "220", "alibaba", 500, "30"])
print(names)

nan = 0
nv = 0

j = 0
while j <= 4:
    for i in range(0, len(names)):
        if names[i][2] == "男":
            nan += 1
            j += 1
        else:
            nv += 1
            j += 1

    print("男:", nan, "女：", nv)

for i in range(0, len(names)):
    dep = (names[i][4])
    print(dep, "1", end="  ")
