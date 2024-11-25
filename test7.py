# 编写一个取款过程
account_balance = 200 # 账户余额
withdraw_money = int(input('请输入取款金额：')) # 取款金额

if withdraw_money <= account_balance :
    account_balance -= withdraw_money
    print(f'账户余额：{account_balance}')
    print(f'吐出钞票： {withdraw_money}')
else :
    print('余额不足')

operate = input('是否继续操作：')
if operate == '否' :
    print('退卡')
else :
    print('其他操作')

