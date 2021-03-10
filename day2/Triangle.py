a = input()
a = int(a)

b = input()
b = int(b)

c = input()
c = int(c)

print(a, b, c)
while True:

    if a == b == c:
        print("等边直角")
        break
    elif a == b or a == c or b == c:
        print("等腰")
        break
    elif a + b > c and a + c > b and b + c > a:
        print("普通三角")
        break
    else:
        print("不能组成三角")
        break
