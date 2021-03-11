'''


'''
# 1. 循环10次来做:实现输入10个数字，并打印10个数的求和结果
# i = 1
# sum = 0
# a = 0
# while i <= 10:
#
#     num = input("请输入数：")
#     num = int(num)
#     if i == 1:
#         a = num
#     if num > a:
#         a = num
#     sum = sum + num
#
#     i = i + 1
# print("最大的数是",a,"10次数据的和：",sum,"平均数是：",(sum / 10))


# 2.等腰，等边，直角，普通
# a = int(input("输入第一边："))
# b = int(input("输入第二边："))
# c = int(input("输入第三边："))
#
# if a + b > c and a + c > b and b +c >a:
#     if a ==  b  == c:
#         print("等边三角形！")
#     elif (a == b != c) or (a == c !=  b)  or (b == c  != a):
#         print("等腰三角形！")
#     elif (a *a + b * b == c * c)  or (a * a +  c  * c == b * b) or (b * b  +  c *c == a *a):
#         print("直角三角形！")
#     else:
#         print("普通三角形！")
# else:
#     print("无法形成三角形！")

# a = 56
# b = 78
#
# a = a + b # 将和放入a中
# b = a - b # 总和减去b =a ,然后将a赋值b
# a = a - b # 将总和减去b(a) =  b,赋值给a
#
# print(a,b)

#
# name = "root"
# password = "admin"
#
# i = 1
# while True:
#     if i == 4:
#         print("系统已锁定！")
#         break
#     username = input("请输入用户名：")
#     passwd = input("请输入密码：")
#     if name != username or password !=  passwd:
#         print("用户名或密码错误，请重新输入！")
#     else:
#         print("登陆成功！")
#         break
#     i = i + 1


# # 打印等腰三角形
# num = int(input("请输入层数："))
# i = 1
# while i <= num:
#
#     # 先打印空格
#     j = 1
#     while  j <= (num - i):
#         print(" ",end="")  # end="" 不换行
#         j =  j + 1
#     # 打印星号
#     k = 1
#     while k <= i:
#         print("* ",end="")
#         k = k +1
#     print() #  换到下一行
#
#     i = i +1

'''
1x1=1
1x2=2   2x2=4
1x3=3   2x3=6   3x3=9
.....

1x9=9   2x9=18  3x9=27    .........  9x9=81    
'''
# num = int(input("请输入n层："))
# i = 1
# while i <= num: # 控制整体层数走向
#     # 每一层打印
#     k = 1
#     while k <= i: # 控制每层打印
#         print(k,"x",i,"=",(i*k),"\t",end="")
#         k = k +1
#     print()
#
#     i = i + 1

# h = 20
# sum = 0
# day = 0
#
# while True:
#
#     day = day + 1  # 先进来就加1天
#
#     sum = sum + 3 # 白天先爬3米
#     if sum >= h: # 然后判断是否爬出来
#         print("爬出来了")
#         break
#     else: # 没有就下滑2米
#         sum = sum  - 2
# print(day)

i = 1
sum = 0
while i <= 6:

    k = 1
    s = 1
    while k <= i:
        s = s * k
        k = k + 1
    sum = sum + s
    i = i + 1
print("阶乘和：",sum)

'''
1! = 1
2!= 1 * 2 = 2
3! = 1*2*3 = 6
4! = 1*2*3*4 = 24
5! = 1*2*3*4*5 = 120
6!=1*2*3*4*5*6=720
1+2+6+24+120 +720 = 153+720

'''












