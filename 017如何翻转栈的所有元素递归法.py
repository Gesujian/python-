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

"""
功能：将栈底元素移至栈顶
"""
def MoveBottomToTop(stack):
	#保存栈顶元素
	StackTop=stack.top()
	#弹出栈顶元素
	stack.pop()
	#处理不包含栈顶元素的子栈
	if not stack.isEmpty():
		MoveBottomToTop(stack)
		SonStackTop=stack.top()
		stack.pop()
		#交换栈顶与子栈顶元素
		stack.push(StackTop)
		stack.push(SonStackTop)
	else:
		stack.push(StackTop)
"""
功能：递归调用除栈顶以外的子栈
"""
def RecursionInvokoingSonStark(stack):
	if not stack.isEmpty():
		#保存栈顶元素
		MoveBottomToTop(stack)
		StackTop=stack.top()
		#弹出栈顶元素
		stack.pop()
		print("\n")
		#递归调用除栈顶以外的子栈
		RecursionInvokoingSonStark(stack)
		stack.push(StackTop)
	else:
		return
if __name__ == '__main__':
	stack=MyStack()
	a="abcdefg"
	#将“abcdefg"存栈中
	for i in a:
		stack.push(i)
	#打印栈中元素---从后往前
	stack.showStack()
	#递归调用
	RecursionInvokoingSonStark(stack)
	print("\n")
	#打印栈中元素---从后往前
	stack.showStack()