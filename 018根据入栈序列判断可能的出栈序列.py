#栈：压栈、弹栈、取栈顶元素、判断栈是否为空、获取栈中元素个数、清空栈。先进后出
#方法：链表实现
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

"""
功能：输入序列pop，以及栈stack的引用，判断pop是否是stack的可能出栈序列。
"""
def isPopSerial(push,pop):
	"""
	输入：栈的引用，以及pop
	如果pop是出栈序列，打印“pop”是可能的出栈序列,如果不是则打印不是
	"""
	#先新建一个stack实例
	stack = MyStack()
	#先将push依次压栈，直到栈顶元素等于pop序列的第一个元素
	push_i=0#用来遍历序列push
	pop_i=0#用来遍历序列pop
	#这里用了无限循环，因为循环推出的条件比较复杂
	while True:
		#压栈
		stack.push(push[push_i])
		# 等栈顶元素等于当前pop_i的元素，则栈顶元素出栈，pop_i+=1
		# 如果栈顶元素还是等于pop_i的元素，则继续出栈，pop_i后移
		while stack.top()==pop[pop_i]:
			stack.pop()
			pop_i+=1
			# 如果pop遍历完了，而且栈是空的，则说明pop序列是可能的出栈序列
			if stack.isEmpty() and pop_i > len(pop) - 1:
				print(pop,"序列是可能的出栈序列")
				return True
		#否则继续入栈
		push_i+=1
		#如果push序列都入栈了，但pop还没有全部遍历，而栈顶元素也不等于当前pop_i的元素
		#则说明pop序列不是可能的出栈序列
		if push_i>len(push)-1 and \
				pop_i<=len(pop)-1 and \
				stack.top()!=pop[pop_i]:
			print(pop,"序列不是可能的出栈序列")
			return False
		# #如果pop遍历完了，而且栈是空的，则说明pop序列是可能的出栈序列
		# if stack.isEmpty() and pop_i>len(pop)-1:
		# 	print("pop序列是可能的出栈序列")
		# 	return True

	return
if __name__ == '__main__':
	#入栈序列
	push=["a","b","c","d","e"]
	print(push)
	#出栈序列
	#pop=["c","b","e","d","a"]
	#pop=["c","b","e","a","d"]
	pop = ["a","b","c","d","e"]
	print(pop)
	#pop = ["a", "b", "e", "c", "d"]
	#判断出栈序列是否是可能的出栈序列
	isPopSerial(push,pop)

