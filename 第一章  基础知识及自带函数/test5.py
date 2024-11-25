# input 输入函数

num : str  = input('输入')
print(f'结果为%s' % num)

# 输入一个数字密码以启动程序 （密码为07）

num = input('请输入密码')

if num == '07' :
    print('程序启动成功')
else :
    print('程序启动失败')
