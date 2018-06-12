m = input()
a = eval(m)
b = a**0
c = a**1
d = a**2
e = a**3
f = a**4
g = a**365

print(b, c, d, e, f, g)

'''
eval函数将字符串当成有效Python表达式来求值，并返回计算结果
x = 1
eval('x+1')
eval('x==1')
与之对应的repr函数，它能够将Python的变量和表达式转换为字符串表示
repr(x==1)
repr(x+1)
'''