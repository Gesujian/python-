import random
class LNode:
	def __init__(self,arg):
		self.data=arg
		self.next=None

"""
题目描述：
链表中的某个节点的next域指向的是链表中在他之前的某一个节点，这样在链表尾部形成了环的结构。
找到链表环的入口点
要求：
方法：
"""
def creatLinkwithAnnulation(x):
	i = 1
	head = LNode(None)
	tmp = None
	cur = head
	while i <= x:
		n = random.randint(1,99)
		tmp = LNode(n)
		cur.next = tmp
		cur = tmp
		i += 1
	m = random.randint(1, x-1)
	if random.randint(0,1)==1:
		Annulation=head.next
		while m<0:
			Annulation=Annulation.next
			m-=1
		cur.next=Annulation
		return head
	elif random.randint(0,1)==0:
		return head
	return head
def Finddoor(head):
	if head.next is None or head.next is None:
		return None
	slow=head.next
	fast=head.next.next
	while fast.next is not None:
		if slow.next==fast.next:
			print("链表有环")
			return slow.data
		slow=slow.next
		fast=fast.next.next
	print("链表无环")
	return None

if __name__ == '__main__':
	head=creatLinkwithAnnulation(10000)
	cur = head.next
	door=Finddoor(head)
	print(door)

