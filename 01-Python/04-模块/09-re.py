
import re

'''
元字符:
    .   ^   $   *   +   ?   {}  []   |   ()   \
    
    1. "."
        标识一个任意的字符 换行除外
    2. "^"
        只在开头匹配
    3. "$"
        只在结尾匹配
    4. "*"
        重复匹配 0 到无穷次
    5. "+"
        重复匹配 1 到无穷次   0 个不可以  
    6. "?"
        匹配 0-1 个
    
    7. "{}"
        指定匹配次数  {5}匹配5个
        
    7. "[]" 字符集
        指定要匹配的字符集
        
    8. "\"
        
        
    
'''

# 匹配所有结果
# re.findall()
# 匹配第一个符合条件的结果
# re.search()

# ret = re.findall('w...o', 'asdasdwxiaos,asdsadwxiaosadasdsaxwxiao')
# print(ret)


str = "hello world This he is hello Of helllllll Myworld happo"

# 1. "."
ret = re.findall('h...o', str)
print(ret)

# 2. "^"
ret = re.findall('h...o$', str)
print(ret)

# 3. "$"
ret = re.findall('h...o$', str)
print(ret)

# 4. "*"
ret = re.findall('hel*', str)
print(ret)

# 5. "+"
ret = re.findall('hel+', str)
print(ret)

# 6. "?"
ret = re.findall('hel?', str)
print(ret)

# 7. "{}"
ret = re.findall('el{1,5}', str)
print(ret)

# 8. "[]"
ret = re.findall('t[e,s]t', "test text tttt tst tet")
print(ret)

ret = re.findall('t[e,s]*t', "test text tttt tst tet")
print(ret)


ret = re.findall('t[e,s]t', "test text tttt tst tet")
print(ret)

