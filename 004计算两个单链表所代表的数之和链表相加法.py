import random
from functools import reduce
class LNode:
	"""docstring for LNode"""
	def __init__(self, arg):
		self.data = arg
		self.next = None

"""
题目描述：
将Head->1->1->3->3->5->7->7->8
与head->1->2->5->7->8相加
得Head->2->3->8->0->4->8->7->8
个位在前
方法：链表相加
"""
def creatLink(x):
	i = 1
	head = LNode(None)
	tmp = None
	cur = head
	while i <= x:
		n = random.randint(0, 9)
		tmp = LNode(n)
		cur.next = tmp
		cur = tmp
		i += 1
	return head

def fn(x,y):
	return x*10+y

def function(head1,head2):
	if head1.next is None and head2.next is None:
		return head1
	cur1=head1.next
	cur2=head2.next
	c=0
	newhead=LNode(None)
	cur=newhead
	while cur1 is not None or cur2 is not None:
		if cur1 is None:
			sumL = cur2.data + c
		elif cur2 is None:
			sumL = cur1.data + c
		else:
			sumL = cur1.data + cur2.data + c
		n=sumL%10
		if sumL>=10:
			c=1
		else:
			c=0

		tmp=LNode(n)
		cur.next=tmp
		cur=tmp
		if cur1 is not None:
			cur1=cur1.next

		if cur2 is not None:
			cur2=cur2.next
	if c==1:
		tmp=LNode(1)
		cur.next = tmp
		cur = tmp
	return newhead
if __name__ == '__main__':
	head1 = creatLink(5)
	head2 = creatLink(9)

	print("head1:")
	cur = head1.next
	while cur != None:
		print(cur.data)
		cur = cur.next
	print("head2:")
	cur = head2.next
	while cur != None:
		print(cur.data)
		cur = cur.next

	head = function(head1, head2)

	print("\nAfteplus:")
	cur = head.next
	while cur != None:
		print(cur.data)
		cur = cur.next