#方法一：利用指针原理：直接在改变本身来实现。闭包内修改普通类型会报错，但是可以lying改变复杂类型的值，而不
def createcounter() :
    a=[0]
    def counter():
     a[0]=a[0]+1
     return a[0]
    return counter
cc=createcounter()
print(cc())
print(cc())
#方法二：利用nonlocal声音一个非内部函数的局部变量。从而进行修改。
def createCounter():
  n = 0               # 先定义一个变量作为初始值
  def counter():      # 定义一个内部函数用来计数
    nonlocal n        # 声明变量n非内部函数的局部变量，否则内部函数只能引用，一旦修改会视其为局部变量，报错“局部变量在赋值之前被引用”。
    n += 1            # 每调用一次内部函数，对n + 1
    return n          # 返回n的值
  return counter
#方法三：利用生成器：此方法比较奇妙
def createCounter():
    def num_generator():
        num = 0
        while True:
            num += 1
            yield num

    int_num = num_generator()

    def counter():
        return next(int_num)

    return counter
c=createCounter()
print(c(),c(),c())

