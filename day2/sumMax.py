count = 0
sum = 0
_max = 0
ave = 0
while count < 10:
    num = input()
    num = int(num)
    if count == 0:
        _max = num
    sum += num
    count += 1
    if _max < num:
        _max = num
        ave = sum / 10
    print("第", count, "次", "和：", sum, "最大值:", _max, "平均数:", ave)