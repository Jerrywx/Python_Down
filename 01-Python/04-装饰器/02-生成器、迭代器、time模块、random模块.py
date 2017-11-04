

'''

一、生成器

# 1. 列表生成器

1. 生成器的创建方式
    a. s = (x * 2 for x in range(5))
    b. yield 关键字

2. 实现 费波纳茨 数列


二、迭代器



三、time, random, json, pickle


'''


# 生成器 1
# s = (x * 2 for x in range(5))
#
# print(s)
#
# print(next(s))
# print(next(s))
# print(next(s))
# print(next(s))
# print(next(s))
# print(next(s))
# print(next(s))

# 生成器 2

def ye():
    # print("111")
    yield 1
    # print("222")
    yield 2

y = ye()

# print("--------------")
# print(next(y))
# print("--------------")
# print(next(y))
# print("--------------")

for i in y:
    print(i)
