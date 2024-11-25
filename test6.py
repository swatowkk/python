# 根据用户输入的月份判断在哪个季节

month = int(input('请输入月份:'))

if 1 <= month <= 12 :
    if 1 <= month <= 3 :
        print('现在是春季')
    elif 4 <= month <= 6 :
        print('现在是夏季')
    elif 7 <= month <= 9 :
        print('现在是秋季')
    elif 10 <= month <= 12 :
        print('现在是冬季')
else :
        print('输入无效')
