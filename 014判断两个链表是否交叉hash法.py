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
方法：建立一个Hashset,先遍历head1，并将链表的节点的Next域存储在hashset表中，
然后遍历head2中的链表，并将当前的节点的Next域与hashset表中的值作比较，如果存在相同的值，则表明两条链表相交
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
def JudgeX(head1,head2):
	if head1 is None or head2 is None or head1.next is None or head2.next is None:
		return None
	hashset=set()#存储链表的Next域
	hashset.clear()
	p=None#用来遍历链表
	p=head1.next
	while p.next is not None:
		hashset.add(p.next)
		p=p.next
	p=head2.next
	while p is not None:
		if p.next in hashset:
			return 1#香蕉
		p=p.next
	return 0#不香蕉


if __name__ == '__main__':
	head1=creatLink(7)
	head2=creatLink(5)
	q = head1.next.next.next
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
	if JudgeX(head1,head2)==1:
		print("两个链表相交")
	elif JudgeX(head1,head2)==0:
		print("两个链表不相交")



