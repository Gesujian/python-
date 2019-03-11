class LNode(object):
	"""docstring for LNode"""
	def __init__(self, arg):
		self.data = arg
		self.next = None

"""
题目描述：
将Head->1->2->3->4->5->6->7->8逆序输出，但不能改变原有链表结构
输出8->7->6->5->4->3->2->1
Head->1->2->3->4->5->6->7->8
方法：递归
"""
def ReversePrint(head):
	if head is None:
		return
	ReversePrint(head.next)
	print(head.data)
	return head

def printHaveFirstNodeREverseLink(head):
	'''
	带头节点
	'''
	if head.next is None:
		return head
	firstNode = head.next
	newhead = ReversePrint(firstNode)
	head.next = newhead
	return head


		

if __name__ == '__main__':
	i = 1
	#有头节点
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
	#逆序输出但是不改变链表结构
	print("\nprintHaveFirstNodeREverseLink:")
	head=printHaveFirstNodeREverseLink(head)
	print("\nAfterReverse:")
	cur = head.next
	while cur != None:
		print(cur.data)
		cur = cur.next
