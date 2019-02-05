class LNode:
	"""
	定义链表对象
	"""

	def __init__(self, x):
		self.data = x
		self.next = None

def Reverse(head):
	'''
	链表逆序插入法
	带头节点
	:param head: 链表头
	:return: 逆序后的链表头
	'''
	cur = None
	next = None
	tmp = LNode(None)
	cur = head
	head=tmp
	head.next=cur
	if head is None or head.next is None:
		return head
	cur = None
	next = None
	cur = head.next.next
	head.next.next = None
	while cur is not None:
		next=cur.next
		cur.next=head.next
		head.next = cur
		cur = next
	return head


if __name__=='__main__':
	i=1
	tmp=None
	head=LNode(None)#链表头
	cur=head
	while i<=7:
		tmp=LNode(i)
		cur.next=tmp
		cur=tmp
		i+=1
	#逆序前
	print("BeforeReverse:")
	cur = head.next
	while cur != None:
		print(cur.data)
		cur = cur.next
	print("\nAfterReverse:")
	head=Reverse(head)
	cur = head.next
	while cur != None:
		print(cur.data)
		cur = cur.next