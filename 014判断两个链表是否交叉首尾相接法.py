import random
class LNode:
	def __init__(self,arg):
		self.data=arg
		self.next=None

"""
题目描述：
给定链表 Head1->1->1->3->3->5->7->7->8
						^
						/
						/
	    Head2->1->1->3->3
判断两个链表是否交叉，
要求：
方法：将head1的尾节点接到hea2的第一个节点，然后判断以head1链表是否有环
"""
def creatLink(x):
	i = 1
	head = LNode(None)
	tmp = None
	cur = head
	while i <= x:
		n = random.randint(1, 9)
		tmp = LNode(n)
		cur.next = tmp
		cur = tmp
		i += 1
	return head
def creatannulation(head1,head2):
	if head1 is None or head2 is None or head1.next is None or head2.next is None:
		return None
	last=None#用于指向链表最后一个节点
	head1first=None#用于指向head2的第一个节点
	last=head1.next
	head1first=head2.next
	while last.next is not None:
		last=last.next
	last.next=head1first
	return head1
def judgeAnnulation(head):
	if head.next is None or head.next is None:
		return None
	slow=head.next
	fast=head.next.next
	while fast.next is not None:
		if slow.next==fast.next:
			return 0
		slow=slow.next
		fast=fast.next.next
	return 1
if __name__ == '__main__':
	head1=creatLink(6)
	head2=creatLink(4)
	q = head1.next.next.next.next
	print("q->", q.data)
	cur=head2.next
	while cur.next is not None:
		cur=cur.next
	if random.randint(0,2)==1:
		cur.next=q
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
	head=creatannulation(head1,head2)
	buer=judgeAnnulation(head)

	if buer==0:
		print("两个链表相交")
	elif buer==1:
		print("两个链表不相交")



