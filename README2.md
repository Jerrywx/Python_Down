###分支和循环
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
        
###数组
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
    


