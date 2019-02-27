import random
class LNode(object):
	"""docstring for LNode"""
	def __init__(self, arg):
		self.data = arg
		self.next = None


"""
题目描述：
将Head->1->1->3->3->5->7->7->8变
为head->1->2->5->7->8
方法：递归法1
"""
def RemoveDup(head):
	"""
	无头结点
	"""
	if head.next is None:
		
		return head
	pointer=None
	cur=head
	head.next=RemoveDup(head.next)
	pointer=head.next
	while pointer is not None:
		if head.data == pointer.data:
			cur.next=pointer.next
			pointer=cur.next
		else:
			pointer=pointer.next
			cur=cur.next
	return head
		
def HaveFirstNodeRemoveDup(head):
	"""
	有头节点
	"""
	if head.next is None:
		return head
	else:
		firstnode=head.next
		newhead=RemoveDup(firstnode)
		return newhead
if __name__ == '__main__':
	i = 1
	head = LNode(None)
	tmp = None
	cur = head
	while i <= 10:
		n = random.randint(1, 10)
		tmp = LNode(n)
		cur.next = tmp
		cur = tmp
		i += 1
	print("BeforeReverse:")
	cur = head.next
	while cur != None:
		print(cur.data)
		cur = cur.next

	head = RemoveDup(head)

	print("\nAfterReverse:")
	cur = head.next
	while cur != None:
		print(cur.data)
		cur = cur.next