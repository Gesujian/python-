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
class MyStack():
	def __init__(self):
		self.elemStack=Stack()#用来储存栈
		self.minStack=Stack()#用来保存栈中的最小值，当前栈的最小值即为栈顶元素
	#压栈
	def push(self,item):
		"""
		若当前元素的值比比minStack的栈顶元素小，或者“相等”！！都入栈
		这里是重点，网上很多文章，他们用的Java写的，但是同样没注意到这点！
		他们都只注意到当前元素要比minStack栈顶元素小，没注意到相等的情况。如果栈elemStack中为1-2-3-1-2-4，则minStack为：1-2-3-4(栈顶在前)，如果第一个1出栈，则elemStack:2-3-1-2-4,minStack:2-3-4,显而易见，最小值为1，但是minStack栈顶为2，所以出错了！！！！！！
		很多教材，和网上文章都没注意到。
		"""
		#先判断
		if self.minStack.isEmpty():
			return self.elemStack.push(item), self.minStack.push(item)
		if item<=self.minStack.top():
			#相等或小于，都入栈
			return self.elemStack.push(item),self.minStack.push(item)
		else:
			#大于,只存储在elemstack
			return self.elemStack.push(item)

	def pop(self):
		"""
		如果elemStack的栈顶元素等于minStack的栈顶元素，则两个都弹栈，如果elemStack的栈顶元素大于minStack的栈顶元素，则只有elemStack弹栈
		"""
		if self.elemStack.top()==self.minStack.top():
			return self.elemStack.pop(),self.minStack.pop()
		else:
			return self.elemStack.pop()
	def minitem(self):
		#返回最小值
		return self.minStack.top()
if __name__ == '__main__':
	s=MyStack()
	s.push(4)
	s.push(5)
	s.push(7)
	print("此时栈中的最小值为：",s.minitem())
	s.push(3)
	print("此时栈中的最小值为：",s.minitem())
	s.push(5)
	s.push(9)
	print("此时栈中的最小值为：",s.minitem())
	s.push(3)
	print("此时栈中的最小值为：",s.minitem())
	s.pop()
	print("此时栈中的最小值为：",s.minitem())
	



