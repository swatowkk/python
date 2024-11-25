# str(字符串) 定义字符串用 ' ' ,只可以存储字符串, 长度任意, 支持下标索引, 有序, 可重复的, 也是不可修改的, 只读模式

# 字符串的定义
my_str = 'hello world'
print(f'字符串{my_str}, 其类型为{type(my_str)}')

# 下标索引
value = my_str[6]
print(f'字符串中 下标6 的元素为{value}')

# index方法
index1 = my_str.index('world')
print(f'world在字符串中的起始下标为{index1}')

# replace方法 (替换) 语法：字符串.replace(字符串1, 字符串2) 功能： 将字符串1的全部内容替换为字符串2
# 注意： 不是修改字符串本身, 而是得到一个新字符串
my_str2 = my_str.replace('hello', 'Hi')
print(f'新字符串为 {my_str2}')

# split方法 (字符串的分割) 语法： 字符串.split(分隔符字符串) 功能： 按照指定的分隔符字符串, 将字符串划分为多个字符串, 并存入 列表 对象中
#注意： 字符串本身不变, 而是得到一个 列表 对象
my_list = my_str.split(' ') # ' ' 按照空格来切分
print(my_list)

# strip方法 (字符串的规整操作)  语法： 字符串.strip() (去前后空格) 或者 字符串.strip(字符串) (去前后指定字符串)
my_str1 = ' hello world '
my_str2 = '12hello world21'

new_str1 = my_str1.strip()
print(f'规整后的新字符串为{new_str1}')

new_str2 = my_str2.strip('12') # 注意： 传入的'12'其实就是 '1' '2' 都会移除, 是按照单个字符串
print(f'规整后的新字符串为{new_str2}')

# 统计字符串中某个字符串出现的次数
count1 = my_str.count('l')
print(f'字符串中 l 出现的次数为{count1}')

# 统计字符串的长度
num = len(my_str)
print(f'字符串的长度为{num}')

# while遍历字符串
index = 0
while index < len(my_str):
    print(f'字符串中的元素分别为 {my_str[index]}')
    index += 1

# for...in...遍历字符串
for element in my_str:
    print(f'字符串中的元素分别为 {element}')
