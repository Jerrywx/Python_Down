

# 导入时间模块
import time



# 1、输出 time模块 帮助文档
print(help(time))

print("---------------------------")

# 2、获取时间戳
timeStamp = time.time()
print("时间戳:", timeStamp)

# 3、获取CPU执行时间
cpuTime = time.clock()
print("CPU执行时间:", cpuTime)

# 4、获取世界时间
gmTime = time.gmtime()
print("gTime:", gmTime)
# print("年份:", gmTime["tm_year"])

# 5、获取本地时间
localTime = time.localtime()
print("localTime", time.localtime())

# 6、将时间格式化字符串
strTime = time.strftime('%Y-%m-%d %H:%M:%S', gmTime)
print("格式化时间:", strTime)

# 7、将字符串格式化为时间
timeSturct = time.strptime('2017-11-04 10:41:53', '%Y-%m-%d %H:%M:%S')
print("时间:", timeSturct)
print(timeSturct.tm_year)
print(timeSturct.tm_mon)
print(timeSturct.tm_mday)


# 7、将时间戳转换为时间
time1 = time.ctime(time.time())
print(time1)

# 8、将时间转换为时间戳
time2 = time.mktime(time.localtime())
print(time2)





