L = list(filter(lambda x: x%2==1, range(1, 20)))

print(L)
# 匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果。
#
# 用匿名函数有个好处，因为函数没有名字，不必担心函数名冲突。此外，匿名函数也是一个函数对象，也可以把匿名函数赋值给一个变量，再利用变量来调用该函数：
#
# >>> f = lambda x: x * x
# >>> f
# <function <lambda> at 0x101c6ef28>
# >>> f(5)
# 25
# 同样，也可以把匿名函数作为返回值返回，比如：
#
def build(x, y):
    return lambda: x * x + y * y
f=build(1,2)
print(f)
# >> <function build.<locals>.<lambda> at 0x0000020920EB4840>
print(f())
# >> 5