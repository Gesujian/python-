#栈：压栈、弹栈、取栈顶元素、判断栈是否为空、获取栈中元素个数、清空栈。先进后出
#方法：数组实现
class MyStack:
	#模拟栈
	def __init__(self):
		self.items = []
	#判断栈是否为空
	def isEmpty(self):
		return len(self.items)==0
	#返回栈的大小
	def size(self):
		return len(self.items)
	#返回栈顶元素
	def top(self):
		if not self.isEmpty():
			return self.items[len(self.items)-1]
		else:
			return None
	#返回栈底元素
	def bottom(self):
		if not self.isEmpty():
			return self.items[0]
		else:
			return None
	#弹栈
	def pop(self):
		if len(self.items)>0:
			print("弹栈成功")
			return self.items.pop()
		else:
			print("栈已为空")
			return None
	#压栈
	def push(self,item):
		self.items.append(item)
		print("入栈成功")
	#清空栈
	def Del(self):
		self.items=[]
		print("栈已清空")
if __name__ == '__main__':
	s=MyStack()
	s.push(4)
	s.push(5)
	s.push(7)
	s.push(4)
	s.push(5)
	s.push(7)
	print("size:",s.size())
	print("top:",s.top())
	print("bottom:", s.bottom())
	s.pop()
	print("size:",s.size())
	print("top:",s.top())
	s.pop()
	s.pop()
	s.pop()
	s.Del()
	print("size:",s.size())


