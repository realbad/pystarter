# 本题的关键在于，需要一个类似全局的变量记录函数生产了多少个。
#
# 方法一：相当于静态参数

# def createCounter():
#   def counter(i = [0]):
#       i[0] += 1
#       return i[0]
#   return counter
# 注意：参数不能写为 i = 0，因为这样是常量，无法执行 i += 1。<==

# 方法二：生成器

def createCounter(): 
  def counterGen(): #定义生成器
      i = 0
      while True:
          i += 1
          yield i

  callGen = counterGen() #创建生成器

  def counter(): #相当于函数工厂
      return next(callGen) #用生成器生成函数

  return counter
# 思路：由于要返回不同的函数，所以其实是要一个函数工厂。这里必须先有 callGen = counterGen()，然后有next(callGen)，不能直接写next(counterGen)。写counterGen()的话，没有一个直接的对象进行next，每次都是重新生成，generator必须有个对象。和对象一样，要创建后才能使用，def counterGen()只是定义，并没有创建。
# 测试:
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')