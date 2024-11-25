# 字符串类型转换整型
num1 = '10'
num2 = '20'
result = int(num1) + int(num2)
print(f'result = {result},type(result) = {type(result)}')

n1 = int(num1)
n2 = int(num2)
result = n1 + n2
print(f'result = {result},type(result) = {type(result)}')

# float 浮点型 -> int
f1 = 55.55
f2 = 66.66
result = f1 + f2
print(f'result = {result},type(result) = {type(result)}')

g1 = int(f1)
g2 = int(f2)
result = g1 + g2
print(f'result = {result}')  # 浮点型转换整型直接丢弃掉小数部分

# int->float
a1 = 10
a2 = 30
result = float(a1) + float(a2)
print(f'result = {result}')

# float + int => float 只要有浮点数参与运算 输出都是浮点型 （保证运算的精确性）
b1 = 11.11
b2 = 22
result = b1 + b2
print(f'result = {result},type(result) = {type(result)}')
