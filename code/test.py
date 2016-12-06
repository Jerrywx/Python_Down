# coding=utf-8

class Dog(object):
	def __init__(self, name, color):
		self.name = name
		self.color = color

	def printDog(self):
		print("Dog:" + self.name + self.color)

d = Dog("小白", "白色")
d.printDog()

bol = hasattr(d, "name")
print(bol)
