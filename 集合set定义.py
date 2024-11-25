# set(集合) 定义集合用 '{元素, 元素, ...}' 可容纳多个数据, 可以容纳不同类型的数据, 可以修改(增加或删除元素)
# 数据是无序存储(不支持下标索引), 不允许重复数据存在(去重复) '注意：因为不支持下标索引只能用for循环'

# 定义集合
set1 = {1, 2, 3, 'a', 'b', 'c', True}
print(f'定义集合为{set1}, 其类型为{type(set1)}')

# 添加元素 语法： 集合.add(元素)
set2 = {1, 2, 3}
set2.add(4)
set2.add(1)    # 集合会去掉重复
print(f'添加元素后的新集合为{set2}')

# 移除元素 语法：集合.remove(元素)
set3 = {1, 2, 3, 'hello'}
set3.remove('hello')
print(f'移除元素后的新集合为{set3}')

# 随机取出一个元素 语法： 集合.pop() 注意：因为集合不支持下标索引 所以pop()为空 即随机取出
set4 = {'hello', 'world', 1, 2, 3}
element = set4.pop()
print(f'取出元素后的新集合为{set4}, 取出的随机元素为{element}')

# 清空集合 语法： 集合.clear()
set5 = {'hello', 'world', 1, 2, 3}
set5.clear()
print(f'清空集合为{set5}')

# 取出2个集合的差集
# 语法： 集合A.difference(集合B), 功能： 取出集合A和集合B的差集(集合A有而集合B没有的) ( A-B={x|x属于A且x不属于B} )
# 结果：得到一个新集合, 集合A和集合B不变
set6 = {1, 2, 3}
set7 = {1, 4, 5}
set8 = set6.difference(set7)
print(f'两个集合的差集为{set8}')  # ( A-B={x|x属于A且x不属于B} )
print(set6)
print(set7)

# 消除2个集合的差集
# 语法：集合1.difference_update(集合2), 功能： 对比集合1和集合2, 在集合1内, 删除和集合2相同的元素
# 结果：集合1被修改, 集合2不变
set6 = {1, 2, 3}
set7 = {1, 4, 5}
set6.difference_update(set7)
print(f'消除差集后,集合1为{set6}')
print(f'消除差集后,集合2为{set7}')

# 2个集合合并为1个
# 语法：集合1.union(集合2), 功能：将集合1和集合2组合成新集合
# 结果：得到新集合, 集合1和集合2不变
set6 = {1, 2, 3}
set7 = {1, 4, 5}
set9 = set6.union(set7)
print(f'两个集合合并新集合为{set9}') # 集合里的元素不允许重复
print(set6)
print(set7)

# 统计集合元素的数量
num = len(set9)
print(f'集合set9元素的数量为{num}')

# 集合的遍历
for element in set9:
    print(f'遍历集合set9里的元素为{element}')