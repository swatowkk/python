# while 循环语句

i = 0   # 1. 定义循环变量

while i < 10 :  # 2. 定义循环条件

    i += 1   # 3. 定义循环增量

    print(i , end = '\t')


# 练习while使用

while True :   # 无限循环 (循环遇 False条件 结束 或者 遇到 'break' 结束)

    print('cmd')

    break   # 遇 break 结束无限循环

# 找出 1~100之间的偶数(之和)

num = 1

sum1 = 0   # 定义一个“框”变量 (求和必须）

while num <= 100 :

    if  num % 2 == 0 :
        sum1 += num
        print(num)

    num += 1

print(sum1)


# while循环类型：穷举 (无限循环 break结束)

# 一筐鸡蛋（至少有2个） 两个两个数，多一个 三个三个数，多一个 四个四个数，多一个 请问至少有多少个鸡蛋？

i = 2

while True :

    if i %2 == 1 and i %3 == 1 and i %4 == 1 :

         print(f'i ={i}')
         break # 条件成立就退出循环

    i += 1


# while循环类型：记数

# 统计 1 ~ 100 之间满足3倍数的数值个数

b = 1

count = 0 # 计数

while b <= 100 :

    if b % 3 == 0 :
        count += 1
        print(b , end = '\t')

    b += 1

print(f'count = {count}')
