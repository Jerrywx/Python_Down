

'''
一、成员修饰符
    1.公共属性
    2.私有属性
        使用"__"双下换线收拾的变量就是 私有属性



二、特殊成员

    1. __init__     : 初始化时调用        ClassName()
    2. __call__     : 对象被执行之调用     obj()
    3. __int__      : 强转为int时调用     int()
    4. __str__      : 强转为str时调用     str()
    5. __add__      : 两个对象相加时       obj + obj
    6. __del__      : 对象被销毁的时候回执行
    7. __dict__     : 将对象中封装的所有内容 通过字典的形式返回  可以使用 类/对象 调用
    8. __getitem__  : obj[0]            执行指定的 __getitem__ 方法
    9. __setitem__  : obj[0] = 100      执行指定的 __setitem__ 方法
    10. __delitem__ : del obj[0]        执行指定的 __delitem__ 方法
    11. __iter__    : 在 for in 中执行



三、metaclass 元类



四、异常处理

# ------------- 异常处理简单流程 1
try:
    # 代码逻辑
    pass
except Exception as e:
    # 错误处理
    pass

# ------------- 异常处理完整流程 2
try:
    # 异常代码
    pass

except IndexError as e:
    print("IndexError")

except ValueError as e:
    print("ValueError")

except Exception as e:
    print("ExceptionError")

else:
    # 如果异常代码没有出现错误
    print("else")

finally:
    # 最终都会执行
    print("finally")

# ------------- 主动触发异常 3
# 主动触发异常
raise Exception('出现异常')

# ------------- 自定义异常 4
# 自定义异常类
class MyError(Exception):

    def __init__(self, msg):
        self.message = msg

    def __str__(self):
        return self.message

# 抛出自定义异常
try:
    raise MyError("我错了...")
except MyError as e:
    print(e)

# ------------- 断言 5
# 条件不成立时报错
assert 1 == 2


五、反射
# 通过字符串 操作对象中的成员

# 通过字符串 获取对象中的成员属性
1. getattr(p, "age")

# 通过字符串 设置对象中的成员属性
2. setattr(p, "name", "wx")

# 通过字符串 删除对象中的成员属性
3. delattr(p, "name")

六、单粒模式

--------------------------------- 单粒模式
class Foo:

    __instance = None

    @classmethod
    def get_instance(cls):
        if cls.__instance

        
            return cls.__instance

        else:
            cls.__instance = Foo()
            return cls.__instance

# 通过使用 f = Foo.getinstance() 获取对象
---------------------------------

'''

# # 异常完整处理 2
# try:
#     # 异常代码
#     pass
#
# except IndexError as e:
#     print("IndexError")
#
# except ValueError as e:
#     print("ValueError")
#
# except Exception as e:
#     print("ExceptionError")
#
# else:
#     # 如果异常代码没有出现错误
#     print("else")
#
# finally:
#     # 最终都会执行
#     print("finally")
#
#
# numb = input("请输入一个数字:")
#
# try:
#     n = int(numb)
#
# except Exception as e:
#     print(e)
#     n = 1
#
# print(n)

class Person:

    __haha

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def log(self):
        print("name %s age:%d" % (self.name, self.age))

p = Person("wxioa", 26)

print(getattr(p, "name"))
setattr(p, "age", 22)
print(getattr(p, "age"))


print(getattr(p, "log"))
print(getattr(Person, "log"))


delattr(p, "name")







# ---- 自定义异常
class MyError(Exception):

    def __init__(self, msg):
        self.message = msg

    def __str__(self):
        return self.message

try:
    raise MyError("我错了...")
except MyError as e:
    print(e)



class Person:
    '''人类'''
    def __init__(self, name, age):
        self.name = name
        self.__age = age


    def say(self):
        print(self.name)
        print(self.__age)

    def __call__(self, *args, **kwargs):
        print("Person __call__ 方法")

    def __int__(self):
        print("Person __int__ 方法")
        return 111

    def __str__(self):
        print("Person __str__ 方法")
        return "asds"

    def __getitem__(self, item):

        if type(item) == slice:
            print("用户使用切片操作")
        else:
            print("用户使用索引操作")

    def __iter__(self):
        return iter(["one", "two", "three"])


class Student(Person):

    def log(self):
        Person.say(self)
        print(self.name)


p = Person("wxiao", 26)

# print(int(p))
# str(p)

# print(p.__dict__)
# print(Person.__dict__)

# s = Student("wxiao", 26)
# s.log()
# s.say()


# p[3]
# p[1:2]

# for item in p:
#     print(item)



class Foo:

    __instance = None

    @classmethod
    def get_instance(cls):
        if cls.__instance:
            return cls.__instance

        else:
            cls.__instance = Foo()
            return cls.__instance

# f = Foo.get_instance()
# print(f)
# f1 = Foo.get_instance()
# print(f)

