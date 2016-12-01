
print("---------------  Change My Games ---------------")
temp = input("输入一个数字:")
number = 8
guess = int(temp)

while guess != number:
        temp = input("猜错了请重新输入:")
        guess = int(temp)
        if guess == number:
                print("猜对了")
        else:
                print("猜错了")

                if guess > number :
                        print("大了")
                else :
                        print("小了")

print("游戏结束")

