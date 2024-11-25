# for...in range() 循环语句

'''

range() ：什么的范围  “Python的内置函数： range(start,stop,step)"
作用：生成指定范围的序列 序列：多个数值 1，2，3，4，5，6...这个有序的整体称为序列
start:开始 (可以不填 不填默认为 0 ）
stop:结束 (不包括所填数值 必填）
step:步长 (可以不填 不填默认为 1 )

'''

# 生成一个 1~10 的序列

for i in range(1,11,1) :
    print(i,end = '\t')


# 使用for循环，求1~100之间所以整型的累加和

count = 0

for num in range(1,101,1) :
    count += num

print(count)


# for循环的嵌套特点

# 查看count1的计数

count1 = 0 # 计数

for a in range(10) :      # 外套循环（外套循环执行1次内套循环执行10次）
    for b in range(10) :  # 内套循环
        count1 += 1

print(count1) # 总共 10 * 10 = 100


# 练习：地球公转和自转 （公转1圈 自转365圈）

for g in range(1,2,1) :
    for z in range(1,366,1) :

        print(z)


# 练习：用 * 打印一个五行五列正方形

for j in range(5) : # 控制了 行

    for k in range(5) : # 控制了 列

        print('*', end = ' ')

#内套循环出循环需要换行
    print()

# 练习：用 * 打印一个五行五列正直角三角形

for m in range(1,6,1) :

    for n in range(1,m + 1,1) :

        print('*', end = ' ')
        
    print()

# 练习：用 * 打印一个五行五列倒直角三角形

for c in range(1,6,1) :

    for d in range(1,7 - c,1) :

        print('*', end = ' ')

    print()


# for循环流程控制（break和continue)

# break 往循环外面跳出
# continue 往循环条件位置跳

# 练习：列出整数 1~10 的序列 (忽略 '5')

for i in range(10) :

    if i == 5 :

        continue # 往循环条件位置跳

    print(i,end = '\t')


# 练习：用户输入密码，有三次机会，如果正确。登陆成功。如果三次机会都错误，冻结此账户

for a in range(3) :

    password = input('请输入密码：')

    if password == '123' :

        print('登录成功')

        break

    else :
        print(f'密码错误，还有{2 - a}次机会')

else :
    print('密码错误，账户已被冻结')


