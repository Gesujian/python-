#队列：入队列、出队列、查看队列首尾元素、查看队列是否为空、查看队列大小等功能、清空队列。先进先出
#方法：链表实现
#front指向队列首，rear指向队列尾
#新元素加在链表尾部，出队列时将第一个节点的值返回并删掉该节点
class LNode:
	def __init__(self,arg):
		self.data=arg
		self.next=None
class MyQueue:
	#模拟队列
	def __init__(self):
		#phead=LNode(None)
		self.data=None
		self.next=None
		self.front=self#指向队列首
		self.rear=self#指向队列尾
	#判断队列是否为空,如果为空返回True，否则返回false
	def isEmpty(self):
		return self.front==self.rear
	#返回队列的大小
	def size(self):
		p=self.front
		size=0
		while p.next!=self.rear.next:
			p=p.next
			size+=1
		return size
	#返回队列首元素
	def top(self):
		if not self.isEmpty():
			return self.front.next.data
		else:
			print("队列为空")
			return None
	#返回队列尾元素
	def bottom(self):
		if not self.isEmpty():
			return self.rear.data
		else:
			print("队列为空")
			return None
	#出队列
	def pop(self):
		if self.size()==1:
			data=self.front.next
			self.rear=self
			return data.data

		elif not self.isEmpty():
			data=self.front.next
			self.front.next=self.front.next.next
			print("出队列成功")
			return data.data
		else:
			print("队列已为空")
			return None
	#入队列
	def push(self,item):
		tmp=LNode(item)
		self.rear.next=tmp
		self.rear=self.rear.next
		print("入队列成功")
	#清空队列
	def destroy(self):
		self.next=None
		print("队列已清空")
	#打印队列
	def showQueue(self):
		if not self.isEmpty():
			p=self.front.next
			while p != self.rear.next:
				print(p.data)
				p=p.next


if __name__ == '__main__':
	s=MyQueue()
	s.push(4)
	s.push(5)
	s.push(7)
	s.push(4)
	s.push(5)
	s.push(9)
	print("size:",s.size())
	print("front:",s.top())
	print("rear:", s.bottom())
	s.pop()
	print("size:",s.size())
	print("front:",s.top())
	print("rear:", s.bottom())
	s.showQueue()
	while not s.isEmpty():
		print(s.pop())
	s.pop()
	s.pop()
	s.pop()
	s.destroy()
	print("size:",s.size())



