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
    



