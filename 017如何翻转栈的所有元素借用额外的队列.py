class LNode:
	def __init__(self,arg):
		self.data=arg
		self.next=None
class MyStack:
	#模拟栈
	def __init__(self):
		#phead=LNode(None)
		self.data=None
		self.next=None
	#判断栈是否为空,如果为空返回True，否则返回false
	def isEmpty(self):
		if self.next is None:
			return True
		else:
			return False
	#返回栈的大小
	def size(self):
		size=0
		p=self.next
		while p is not None:
			size+=1
			p=p.next
		return size
	#返回栈顶元素
	def top(self):
		if not self.isEmpty():
			return self.next.data
		else:
			print("栈为空")
			return None

	#返回栈底元素
	def bottom(self):
		if not self.isEmpty():
			p=self.next
			while p.next is not None:
				p=p.next
			return p.data
		else:
			print("栈为空")
			return None
	#弹栈
	def pop(self):
		if not self.isEmpty():
			p=self.next
			self.next=self.next.next
			print("弹栈成功")
			return p.data
		else:
			print("栈已为空")
			return None
	#压栈
	def push(self,item):
		tmp=LNode(item)
		p=self.next
		self.next=tmp
		tmp.next=p
		print("入栈成功")
	#清空栈
	def destroy(self):
		self.next=None
		print("栈已清空")

	# 打印栈
	def showStack(self):
		p = self.next
		while p is not None:
			print(p.data)
			p = p.next
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
	stack=MyStack()
	a="abcdefg"
	#将“abcdefg"存栈中
	for i in a:
		stack.push(i)
	#打印栈中元素---从后往前
	stack.showStack()
	# 将栈中的元素压出，并存入队列中
	queue=MyQueue()
	while not stack.isEmpty():
		queue.push(stack.pop())
	print("\n")
	# 将队列中的元素出队列，并存入栈中
	while not queue.isEmpty():
		stack.push(queue.pop())
	#打印栈中元素---从后往前
	stack.showStack()