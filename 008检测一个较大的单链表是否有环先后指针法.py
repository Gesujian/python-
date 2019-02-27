import random
import time
class LNode:
	def __init__(self,arg):
		self.data=arg
		self.next=None

"""
题目描述：
链表中的某个节点的next域指向的是链表中在他之前的某一个节点，这样在链表尾部形成了环的结构。如何判断链表中是否有环的结构
要求：
方法：HashSet蛮力法
"""
def creatLinkwithAnnulation(x):
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
	start = time.time()
	head = creatLinkwithAnnulation(100)
	end = time.time()
	print("创建用时：", end - start)
	cur = head.next
	start1=time.time()
	buer=judgeAnnulation(head)
	end1=time.time()
	print("判断用时：",end1-start1)
	if buer == 0:
		print("head中有环")
	elif buer == 1:
		print("head中没环")
	else:
		print("head为空")
"""
创建用时： 6.560430526733398
判断用时： 0.718552827835083
head中有环
"""
