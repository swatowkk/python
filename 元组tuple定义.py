# tuple (元组) 定义元组使用小括号 '()' ,而且使用 , 号隔开各个元素, 元素可以是不同的数据类型 有序 可重复的
# (注意：元组一旦定义完成，就不可以修改 只读模式)


# 定义元组
tuple1 = (1, 2, 'hello', True)
tuple2 = ()                     # 空元组
tuple3 = tuple()                # 空元组
print(f'元组为{tuple1}, 其类型为{type(tuple1)}')
print(f'元组为{tuple2}, 其类型为{type(tuple2)}')
print(f'元组为{tuple3}, 其类型为{type(tuple3)}')

# 定义单个元素的元组
t1 = ('hello', )
print(f'单个元组为{t1}, 其类型为{type(t1)}')

# 元组的嵌套
t3 = ((1, 2, 3), ('a', 'b', 'c'))
print(f'单个元组为{t3}, 其类型为{type(t3)}')

# 元组的下标索引
tuple0 = (1, 2, 'hello', True)
value = tuple0[2]
print(f'元组中 下标2 的元素为{value}')

# 元组的操作：index查找方法
tuple4 = (1, 2, 'hello', True)
index1 = tuple4.index('hello')
print(f'hello在元组中的起始下标为{index1}')

# 元组的操作：count统计方法
tuple5 = (0, 1, 2, 1, 'hello', True, False) # Python中True数值等价于 1 , False数值等价于 0
count1 = tuple5.count(1)
print(f'元组中1出现的次数为{count1}')

# 元组的操作：len函数统计元组元素数量
tuple6 = (0, 1, 2, 1, 'hello', True, False)
num = len(tuple6)
print(f'元组中的元素为{num}')

# 元组的遍历：while
tuple7 = (0, 1, 2, 1, 'hello', True, False)
index = 0
while index < len(tuple7):
    print(f'元组中的元素分别为{tuple7[index]}')
    index += 1

# 元组的遍历：for...in...
tuple8 = (0, 1, 2, 1, 'hello', True, False)
for element in tuple8:
    print(f'元组中的元素分别为{element}')