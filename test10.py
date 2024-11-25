# 练习：用户输入密码，有三次机会，如果正确。登陆成功。如果三次机会都错误，冻结此账户

for a in range(3) :

    password = input('请输入密码：')

    if password == '123' :

        print('登录成功')

        break

    if 2 - a != 0 :

        print(f'密码错误，还有{2 - a}次机会')

        continue
    else :

        print('密码错误，账户已被冻结')


