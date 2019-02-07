import random
class LNode(object):
	"""docstring for LNode"""
	def __init__(self, arg):
		self.data = arg
		self.next = None

def removeDup(head):
	"""
	有头节点
	"""
	if head.next is None:
		return head
	outerCur=head.next
	innerCur=None
	innerPre=None
	while outerCur is not None:
		innerCur=outerCur.next
		innerPre=outerCur
		while innerCur is not None:
			if innerCur.data == outerCur.data:
				innerPre.next=innerCur.next
				innerCur=innerCur.next
			else:
				innerPre=innerCur
				innerCur=innerCur.next
		outerCur=outerCur.next

	return  head
if __name__ == '__main__':
	i=1
	head=LNode(None)
	tmp=None
	cur=head
	while i<=10:
		n=random.randint(1,10)
		tmp=LNode(n)
		cur.next=tmp
		cur=tmp
		i+=1
	print("BeforeReverse:")
	cur = head.next
	while cur != None:
		print(cur.data)
		cur = cur.next

	head=removeDup(head)
	
	print("\nAfterReverse:")
	cur = head.next
	while cur != None:
		print(cur.data)
		cur = cur.next