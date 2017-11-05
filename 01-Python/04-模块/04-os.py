
import os

# 1、获取当前目录
path = os.getcwd()
print(path)

# 2、修改当前目录
os.chdir("..")      # 切换到上一级目录
print(os.getcwd())

# 3、返回当前目录
path = os.curdir
print(path)

# 4、获取上一级目录
path = os.pardir
print(path)

# 5、生成多层文件夹
# os.makedirs('./test/test2')

# 6、删除空文件夹
# os.removedirs('./test/test2')

# 7、生成单个文件夹
# os.mkdir('./test')

# 8、删除单个文件
# os.rmdir('./test')

# 9、列出所有文件
files = os.listdir(path)
print(files)

# 10、删除一个文件  只能删除文件 不能删除文件夹
# os.remove('filePath')

# 11、重命名
# os.rename('oldName', 'newName')

# 12、获取文件信息
info = os.stat(path)
print(info)
print(info.st_size)

# 13、路径分隔符
print(os.sep)

# 14、换行分隔符
line = os.linesep
print(line)

# 15、路径分隔符
sep = os.pathsep
print(sep)

# 16、执行shell 命令
# print(os.system("cd"))

# 17、相对路径 转绝对路径
path = os.path.abspath(path)
print(path)

# 18、文件路径名 分割
fileName = os.path.split(path)
print(fileName)

# 19、上一级路径
print(os.path.dirname(path))