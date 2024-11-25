# 综合练习：发工资
'''

#某公司，账户余额有10000元，给20名员工发工资。
员工编号从1到20，从编号1开始，依次领工资，每人可领取1000元
领工资时，财务判断员工给绩效分（1-10）（随机生成），如果低于5，不发工资，换下一位
如果工资发完，结束发工资

'''

money = 10000

for i in range(1,21,1):

    import random
    num = random.randint(1,10)

    if num < 5 :
        print(f'编号{i}号员工，您的绩效分为{num}，不发工资,换下一位')

        continue

    if money >= 1000:
        money -= 1000
        print(f'编号{i}号员工，您绩效分为{num}，可领1000元，账户余额为{money}元')

    if money == 0:
        print(f'账户余额为{money}元，不足以发工资')

        break

