#队列：入队列、出队列、查看队列首尾元素、查看队列是否为空、查看队列大小等功能、清空栈。先进先出
#方法：数组实现书上的方法，会出现数组前面的部分不能被充分利用的情况，可以用数组实现。
class Queue:
	"""docstring for Queue"""
	def __init__(self):
		self.items = []
		self.front = 0#队列首
		self.rear = 0 #队列尾
	#入队列
	def push(self,item):
		self.items.append(item)
		self.rear+=1
		print("入队列成功")
	#出队列
	def pop(self):
		if self.rear>self.front:
			p=self.front
			self.front+=1
			print("出队列成功")
			return self.items[p]
			#return self.items.pop(len(self.items)-1)
		else:
			print("队列已为空")
			return None

	#查看列表是否为空
	def isEmpty(self):
		return self.front==self.rear
	#查看队列首元素
	def head(self):
		if not self.isEmpty():
			return self.items[self.front]
		else:
			return None
	#查看队列尾元素
	def end(self):
		if not self.isEmpty():
			return self.items[self.rear-1]
		else:
			return None
	#查看队列大小
	def size(self):
		return self.rear-self.front
	#清空队列
	def destroy(self):
		self.items=[]
		self.front=0
		self.rear=0
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
	print("front:",s.head())
	print("rear:", s.end())
	s.pop()
	s.pop()
	print("size:",s.size())
	print("front:",s.head())
	print("rear:", s.end())
	s.pop()
	s.pop()
	s.pop()
	print("size:", s.size())
	print("front:", s.head())
	print("rear:", s.end())
	s.destroy()
	print("size:",s.size())