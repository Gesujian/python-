#队列：入队列、出队列、查看队列首尾元素、查看队列是否为空、查看队列大小等功能、清空栈。先进先出
#方法：数组实现
class Queue:
	"""docstring for Queue"""
	def __init__(self):
		self.items = []

	#入队列
	def push(self,item):
		self.items.append(item)
		print("入队列成功")
	#出队列
	def pop(self):
		if len(self.items)>0:
			print("出队列成功")
			return self.items.pop(len(self.items)-1)
		else:
			print("队列已为空")
			return None

	#查看列表是否为空
	def isEmpty(self):
		return len(self.items)==0
	#查看队列首元素
	def head(self):
		if not self.isEmpty():
			return self.items[len(self.items)-1]
		else:
			return None
	#查看队列尾元素
	def end(self):
		if not self.isEmpty():
			return self.items[0]
		else:
			return None
	#查看队列大小
	def size(self):
		return len(self.items)
	#清空队列
	def destroy(self):
		self.items=[]
		print("队列已清空")
	
if __name__ == '__main__':
	s=Queue()
	s.push(4)#end
	s.push(5)
	s.push(6)
	s.push(1)
	s.push(2)
	s.push(3)#head
	print("size:",s.size())
	print("head:",s.head())
	print("end:", s.end())
	s.pop()
	s.pop()
	print("size:",s.size())
	print("head:",s.head())
	print("end:", s.end())
	s.pop()
	s.pop()
	s.pop()
	print("size:", s.size())
	print("head:", s.head())
	print("end:", s.end())
	s.destroy()
	print("size:",s.size())
