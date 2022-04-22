#高级特征分为
#切片
#迭代列表
#生成式
生成器
#这里有个问题：
def odd():
    print('step 1')
    yield (1)
    print('step 2')
    yield(3)
    print('step 3')
    yield(5)
#输出如下：
#我就懵了：我的yield没啥用吗？
>>> next(odd())
step 1
1
>>> next(odd())
step 1
1
