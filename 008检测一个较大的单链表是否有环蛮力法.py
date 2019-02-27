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
	HashSet=set()
	HashSet.clear()
	tmp=head.next
	while tmp.next is not None:
		if tmp.next not in HashSet:
			HashSet.add(tmp.next)
			tmp=tmp.next
		else:
			return 0
	return 1
if __name__ == '__main__':
	start = time.time()
	head = creatLinkwithAnnulation(1000000)
	end = time.time()
	print("创建用时：", end - start)

	cur = head.next
	start=time.time()
	buer=judgeAnnulation(head)
	end=time.time()
	print("判断用时：",end-start)
	if buer == 0:
		print("head中有环")
	elif buer == 1:
		print("head中没环")
	else:
		print("head为空")
"""
创建用时： 6.576046466827393
判断用时： 0.7184720039367676
head中没环7
"""

