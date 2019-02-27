import time
import random
class LNode:
	def __init__(self,arg):
		self.data=arg
		self.next=None

"""
题目描述：
给定链表L0->L2->L3……->Ln-1->Ln
把链表重新排序为L0->Ln->L2->Ln-1->L3->Ln-2……
要求：（1）在原来链表的基础上进行排序，即不能申请新的节点；（2）只能修改节点的next域，不能修改数据域
方法：
先找到链表的中间节点，并将原链表拆分成两个子链表，将后面的子链表逆序，在将两个子链表合成最终链表
"""
def creatLink(x):
	i = 1
	head = LNode(None)
	tmp = None
	cur = head
	while i <= x:
		#n=random.randint(1,9)
		tmp = LNode(i)
		cur.next = tmp
		cur = tmp
		i += 1
	return head

def xReverese(head1,head2):
	# 有头节点
	if head1 is None or head1.next is None or head1.next.next is None:
		return head1
	if head2 is None or head2.next is None or head2.next.next is None:
		return head2
	#合并head和mid，mid无头节点
	curHead=head1.next
	curmid=head2.next
	p=curHead
	while curHead.next is not None:
		nexthead = curHead.next
		curHead.next = curmid
		nextmid = curmid.next
		curmid.next = nexthead
		curHead = nexthead
		curmid = nextmid
	if curmid is not None:
		curHead.next=curmid
	return head1

	
if __name__ == '__main__':
	starttime = time.time()
	head1=creatLink(5)
	head2=creatLink(6)
	print("BeforeReverse:")
	cur = head1.next
	while cur != None:
		print(cur.data)
		cur = cur.next
	print("BeforeReverse:")
	cur = head2.next
	while cur != None:
		print(cur.data)
		cur = cur.next
	head=xReverese(head1,head2)
	print("\nAfterReverse:")
	cur = head.next
	while cur != None:
		print(cur.data)
		cur = cur.next
	endtime=time.time()
	print(str(endtime-starttime))