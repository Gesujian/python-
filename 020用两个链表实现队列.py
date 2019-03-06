#栈：压栈、弹栈、取栈顶元素、判断栈是否为空、获取栈中元素个数、清空栈。先进后出
#方法：链表实现
class LNode:
	def __init__(self,arg):
		self.data=arg
		self.next=None
class Stack:
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
			self.next=self.next.next
			print("弹栈成功")
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
	#打印栈
	def showStack(self):
		p=self.next
		while p is not None:
			print(p.data)
			p=p.next
class MyQueue:
	def __init__(self):
		self.EnQueue=Stack()# 用来进行入队列操作
		self.DeQueue=Stack()# 用来进行出队列操作

	#判断队列是否为空
	#队列长度
	#入队列
	#出队列
	#清空队列
	#返回队首元素
	#返回队尾元素
	#打印队列