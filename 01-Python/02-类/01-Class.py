

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

五、反射

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

f = Foo.get_instance()
print(f)
f1 = Foo.get_instance()
print(f)

