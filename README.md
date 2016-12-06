# Python_Down
Python_Down
##002用Python设计第一个游戏
1、什么是 BIF
2、查看 Python中的BIF
    dir(__builtins__)
3、查看帮助文档
    help(input)
##003小插曲之变量和字符串
1、原始字符串
    str = r'This a String'
2、跨越多行的字符串
    ‘’‘ 内容 ’‘’ 或者 “”“ 内容 ”“”
    
    
###004改进我们的小游戏
1、while 循环
    
###005闲聊之Python的数据类型
1、type("字符串")
    
2、isinstance("content", str)
    返回 BOOL 是否符合类型

###006Pyhon之常用操作符
1、基本运算符
    + 、- 、*、 /、 **、//、 %
2、比较
    >、 <、 >=、 <=、 ==、 !=
3、逻辑运算符
    or、and、not

###007分支和循环
1、else 悬挂
2、while 循环
3、for 循环
    语法:
    for 目标 in 表达式:
        循环体
    a. break    
    b. continue
4、range
    语法:
    range([start,] stop [, step=1])
    - 包含三个参数 中括号中的参数可选
    - step=1 表示第三个参数的默认值是1
    - range 可以生成从start参数值开始到stop惨呼是值结束的数字序列
        
###008数组
1、创建列表
    a. 普通类型列表
    ```
        member = ["one", "two", "three"]
    ```
    b. 混合列表
    ```
        list = ["one", 1, [2, 3, 4, 5]]
    ```    
    c.空列表
    ```
        empty = []
    ```

2、向列表添加元素
    a. 追加元素
        append(元素) 在列表末尾添加元素
        extend(列表) 拓展列表中的元素
    b. 插入元素
        insert(index, 元素)
        
3、从列表中获取元素
    a. 索引
        member[0]
4、从列表中删除元素    
    a. remove(元素)
    b. del 列表名[index]
    c. pop() 去除最后一个 并 删除
       pop(1)
       
5、列表分片
    member[1:3]
    member[:3]
    member[1:]
    member[:]
    
6、列表使用操作符
    比较运算符
    + * in

7、list BIF
    dir(list)
    count(元素)   出现次数
    index(元素)   获得索引
    reverse()    翻转
    sort()       排序
    
    
###009元组
    

###014字符串


###017函数
1、定义函数 使用 def 关键字
```
def MyFirstFunction() :
    print("MyFirstFunction!")
    print("这是我创建的第一个函数!")
```
2、函数调用
```
MyFirstFunction()
```
3、定义带参数函数
```
# 定义一个参数函数
def hello(name):
    print("Hello " + name + "!")
    
# 调用
hello("Test")
```

```
# 定义多个参数函数
def add(num1, num2):
    print(num1 + num2)
    
# 调用
add(2, 3)
```

4、定义返回值函数
```
# 定义带返回值函数
def add(num1, num2):
    return (num1 + num2)
    
# 调用
print(add(2, 3))
```

5、函数文档
```
# 定义一个带注释文档的函数
def testFunc():
    '这是函数的注释'
    print("This is testFunc")

# 获取注释
testFunc.__doc__
# 注: help 可获取函数帮助文档
```

6、关键字参数
```
# 定义一个函数
def func(param1, param2):
    print(param1 + " " + param2)
# 调用函数使用关键字参数
func(param2 = "two", param1 = "one")

```

7、默认参数
```
# 定义一个默认参数函数
def add(num1=4, num2=6):
    print(num1 + num2)

# 调用函数
add(3)
# 结果9
```

8、收集参数 (多个参数 存放在数组中)
```
# 定义收集参数
def testFunc(*param):
    print("参数个数:" + len(param))
    print("第一个参数" + param[0])
    
# 调用函数
testFunc(1,2,3,4,5)
# 注: 如果要包含其他参数使用 默认参数
```
9、函数变量作用域
    a. 局部变量
    b. 全局变量 
    global 关键字  修改全局变量时使用
    

10、嵌套函数 (在函数中创建另一个函数)
```
# 定义嵌套函数
def func1():
    print("func1 Runing")
    def func2():
        print("func2 Runing")
    func2()
# 调用
func1()
```

11、闭包
> lisp语言


12、匿名函数 
```
# 匿名函数 lambda
func = lambda x: x * x

# 调用
func(5)
```

13、BIF filter()
>help(filter)
>filter(function or None, iterable) --> filter object
14、BIF map()
>help(map)
>map(func, *iterables) --> map object

###022递归

###025字典
1、定义字典
```
dict = {"aa":"one", "bb":"two", "cc":"three"}
dict["bb"]
```

    
###028文件


###036面向对象编程
1、定义一个类
```
# 定义学生类
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
        
    def print_score(self):
        print("%s : %s", (self.name, self.score))

# 使用学生类
s = Student("wxiao", "100")
s.print_score()
```
2、类和实例
######a. 创建类和实例
```
>>> class Student(object):
...     pass
... 
>>> s = Student()
>>> s
<__main__.Student object at 0x10c972a10>
>>> Student
<class '__main__.Student'>
>>> 
```

######b.给实例绑定属性
```
>>> s.name = "pName"
>>> s.name
'pName'
>>> s.age = 24
>>> s.age
24
>>> 
```
######c.初始化方法 __init__
>__init__方法，在创建实例的时候调用
>注意到__init__方法的第一个参数永远是self，表示创建的实例本身


3、访问限制
>在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问

4、继承和多态


5、获取对象信息
######a. 使用 type()
    获取对象类型
    type(123) == type(456)
    

#######b. 使用 isinstance()
    判断某个实例是否属于某类型
    isinstance(dog, Dog)
    
#######c. 使用 dir() 
获得一个对象的所有属性和方法
dir(list)

######d. 获取实例信息
hasattr(obj, "x")       # 是否包含 x 属性
setattr(obj, 'y', 19)   # 设置一个属性'y' 
getattr(obj, 'y')       # 获取属性'y'
getattr(obj, 'z', 404)  # 获取属性'z'，如果不存在，返回默认值404

6、实例属性和类属性

```
# 实例属性
class Student(object):
    def __init__(self, name):
        self.name = name

s = Student('Bob')
s.score = 90

# 类属性
class Student(object):
    name = 'Student'
```

>当我们定义了一个类属性后，这个属性虽然归类所有，但类的所有实例都可以访问到。
>在编写程序的时候，千万不要把实例属性和类属性使用相同的名字，因为相同名称的实例属性将屏蔽掉类属性，但是当你删除实例属性后，再使用相同的名称，访问到的将是类属性。

