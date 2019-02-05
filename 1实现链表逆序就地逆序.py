class LNode:
	"""
	定义链表对象
	"""

	def __init__(self, x):
		self.data = x
		self.next = None

def Reverse(head):
	'''
	有头节点
	:param head:
	:return:
	'''
	# 判断链表是否为空
	if head is None or head.next is None:
		return
	pre = None
	cur = None
	next = None

	# 处理链表头
	cur = head.next
	next = cur.next
	cur.next = None
	pre = cur
	cur = next

	# 转变当前节点指向
	while cur.next != None:
		next = cur.next
		cur.next = pre
		pre = cur
		cur = next

	# 处理最后一个节点与倒数第二个节点
	cur.next = pre

	# 添加头节点
	head.next = cur

if __name__ == '__main__':
	i = 1
	head = LNode(None)
	# head.data=None
	# head.next=None
	cur = head
	tmp = None  # 用作添加新节点

	# 构造单链表

	while i <= 8:
		tmp = LNode(i)
		# tmp.data=i
		# tmp.next=None
		cur.next = tmp
		cur = tmp
		i += 1
	print("BeforeReverse:")
	cur = head.next
	while cur != None:
		print(cur.data)
		cur = cur.next
	print("\nAfterReverse:")
	Reverse(head)
	cur = head.next
	while cur != None:
		print(cur.data)
		cur = cur.next

