import time

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
		tmp = LNode(i)
		cur.next = tmp
		cur = tmp
		i += 1
	return head

def xReverese(head):
	# 有头节点
	if head is None or head.next is None or head.next.next is None:
		return head
	# 寻找链表中间节点
	jump1 = head.next  # step为1的指针
	jump1Pre = head.next
	jump2 = head.next  # step为2的指针
	mid = None
	while jump2.next is not None:
		if jump2.next.next is None:
			break
		jump1Pre = jump1
		jump2 = jump2.next.next
		jump1 = jump1.next

	if jump2 is None:
		mid=jump1#长度为偶数
		jump1Pre.next = None  # 切断
	else:
		mid=jump1.next#长度为奇数
		jump1Pre=jump1
		jump1Pre.next = None  # 切断
	#逆序后面的链表

	cur=mid.next#用来逆序链表,指向第2个节点
	mid.next=None
	while cur is not None :
		next=cur.next
		cur.next=mid
		mid=cur
		cur=next
	#合并head和mid，mid无头节点
	curHead=head.next
	curmid=mid

	while curHead.next is not None:
		nexthead = curHead.next
		curHead.next = curmid
		nextmid = curmid.next
		curmid.next = nexthead
		curHead = nexthead
		curmid = nextmid
	if curmid is not None:
		curHead.next=curmid
	return head
if __name__ == '__main__':
	starttime = time.time()
	head=creatLink(20)
	print("BeforeReverse:")
	cur = head.next
	while cur != None:
		print(cur.data)
		cur = cur.next
	head=xReverese(head)
	print("\nAfterReverse:")
	cur = head.next
	while cur != None:
		print(cur.data)
		cur = cur.next
	endtime=time.time()
	print(str(endtime-starttime))