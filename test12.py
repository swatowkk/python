
money = 5000000

# 主菜单函数

i = 0

while i < 3 :                     #  使用while一个循环条件规避 while Ture和for...in...嵌套带来的程序混乱BUG
    password = input('请输入您的密码：')
    if password == 'kali':
        print(f'请选择操作项目')
        select = input('')
        i = 0                    # 利用每次循环 i = 0 使 i < 3 永远成立 从而达到无限循环操作
    else:
        if 2 - i != 0:
            print(f'输入错误, 您还有{2 - i}次机会')
            i += 1
            continue
        else:
            print('您已被锁卡, 请联系工作人员')
            break



    if select == '查询':
        # 查询余额函数
        def mon(money3):
            '''

            :param money3:  当前余额
            :return:  返回’空‘
            '''
            print(f'当前余额为{money3}')
            return None
        mon(money)
        continue


    if select == '存款':
        # 存款函数
        a = int(input(f'请输入存款金额：'))
        def mon1(money1, a1):
            '''

            :param money1: 上一级的余额
            :param a1: 存入金额
            :return: 存入后的余额
            '''
            money1 += a1
            return money1
        money = mon1(money, a)
        print(f'当前余额为{money}')
        continue


    if select == '取款':
        # 取款函数
        b = int(input(f'请输入取款金额：'))
        def mon2(money2, b1):
            '''

            :param money2: 上一级的余额
            :param b1: 取款金额
            :return: 取款后的余额
            '''
            money2 -= b1
            return money2
        money = mon2(money, b)
        print(f'当前余额为{money}')
        continue

    if select == '退卡':
        print('请收好您的卡片')
        break
