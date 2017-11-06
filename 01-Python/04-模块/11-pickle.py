
import pickle


def test():
    print("This is a Test")


# 写入 函数
# data = pickle.dumps(test)
#
# f = open("pickel_txt", "wb")
# f.write(data)
# f.close()

# 读出函数

f = open("pickel_txt", "rb")
data = f.read()
data = pickle.loads(data)
data()
