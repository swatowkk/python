# list (列表) 用 '[]' 作为标识 列表内每一个元素用 , 号隔开, 元素可以是不同的数据类型 有序 可重复的 (注意：列表可以修改)

list1 = [1, 2, 3, 'hello', [1, 2, 3, 4]]
print(list1)
print(type(list1))

# 列表的下标索引
#  列表从左到右从0开始，每次+1  (嵌套列表类型 先索引外层再到内层) (也可从右向左，从-1开始，每次-1)
list2 = [[1, 2, 3, 'hello'], [1, 2, 3, 4]]
print(list2[0])
print(list2[0][3])
print(list2[0][-1])

# 修改列表元素
list0 = [1, 2, 3, 'hello', 4]
list0[4] = 5
print(list0)

# 列表.index(元素) 查找指定元素在列表的下标
list3 = ['a', 'b', 'c', 'd', 'e', 'f']
index = list3.index('b')
print(index)

# 列表.insert(下标, 元素) 在指定下标处, 插入指定的元素
list4 = ['a', 'b', 'c', 'd', 'e', 'f']
list4.insert(1,'hello')
print(list4)

# 列表.append(元素) 向列表中追加一个元素(追加在最尾部)
list5 = ['a', 'b', 'c', 'd', 'e', 'f']
list5.append('hello')
print(list5)

# 列表.extend(容器)  将数据容器的内容依次取出, 追加到列表尾部
list6 = ['a', 'b', 'c', 'd', 'e', 'f']
list6.extend([1, 2, 3])
print(list6)

# del列表[下标] 删除列表指定下标元素 (方法一)
list7 = ['a', 'b', 'c', 'd', 'e', 'f']
del list7[2]  # del(翻译为 删除 )
print(list7)
# 列表.pop(下标) 删除列表指定下标元素 (方法二)
list8 = ['a', 'b', 'c', 'd', 'e', 'f']
element = list8.pop(2)  # element(翻译为 元素 )
print(f'通过pop方法取出元素后的列表内容为：{list8}, 取出的元素为：{element}')

# 列表.remove(元素) 从前向后, 删除此元素第一个匹配项
list9 = ['a', 'a', 'b', 'c', 'd', 'e', 'f']
list9.remove('a')
print(list9)

# 列表.clear() 清空列表
list10 = ['a', 'b', 'c', 'd', 'e', 'f']
list10.clear()
print(list10)

# 列表.count(元素) 统计此元素在列表中出现的次数
list11 = ['a', 'b', 'c', 'a', 'd', 'e', 'f']
count = list11.count('a')
print(count)

# len(列表) 统计容器内有多少元素
list12 = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
count = len(list12)
print(count)

# 用while或者for...ion...遍历列表

# while遍历（只能使用可下标索引的有序的）
list13 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 1, 2, 3]
index = 0
while index < len(list13):
    print(f'遍历list13中的元素为{list13[index]}')
    index += 1

# for...in... 遍历
list14 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 1, 2, 3]
for element in list14:
    print(f'遍历list14中的元素为{element}')