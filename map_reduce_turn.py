from functools import reduce
def dict(i):
 a={'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'0':0}
 return a[i]
def turn(a,b):
 return a*10+b
s='123.456'
def re(s):
 val,frc=s.split(".")
 return reduce(turn,map(dict,val))+reduce(turn,map(dict,frc))*10**(-len(frc))

if re(s)-123.456<0.00001:
    print("yes!")

编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
