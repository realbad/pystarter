# def triangles():
#
#     c=[1]
#     while True:
#
#         if len(c) > 2:
#             buf = c[:]
#             for j in range(len(c)-2):
#                 c[j+1]=buf[j]+buf[j+1]
#             d = c[:]
#             c.append(1)
#
#             yield d
#             # c = c[:1] + buf
#         else:
#             d=c[:]
#             c.append(1)
#             yield d
            # 实在是太蠢了！下面的巧妙很多
 # 原因不是因为yield的问题，二十因为用c.append(1)会对c的值进行改变，这是一个相对复制,即使已经append到了另一个列表中,凡是对c进行的修改作为list的相对应用都会被copy过来
# def triangles():
#     N = [1]
#     while True:
#         yield N
#         S=N[:]
#         S.append(0)
#         N = [S[i-1] + S[i] for i in range(len(S))]
# 可以是-1，代表代数第一个
def triangles():
    Y = [1]
    while 1:
        yield Y
        Y = [0] + Y + [0]
        Y = [(Y[i] + Y[i + 1]) for i in range(len(Y) - 1)]
# 这种写法比较巧妙的通过Y建立了另一个列表，同时又可以不引入另一个列表的具体名称，以Y代替,由于Y发生了整体替代，每次的都不再是相对引用，另外关键点还有引入两个[0]后可以以[i]+[i+1},避免了需要buf，所以相对自己写的少了两个引入的变量
# 期待输出:
# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
# [1, 5, 10, 10, 5, 1]
# [1, 6, 15, 20, 15, 6, 1]
# [1, 7, 21, 35, 35, 21, 7, 1]
# [1, 8, 28, 56, 70, 56, 28, 8, 1]
# [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
n = 0
results = []
for t in triangles():
    print(t)
    results.append(t)
    n = n + 1
    if n == 10:
        break
print(results)
if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')
