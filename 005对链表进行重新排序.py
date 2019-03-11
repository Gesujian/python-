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
	#判断链表是否为空，或者只有一个元素，或者只有两个元素
	if head is None or head.next is None or head.next.next is None:
		return head
	# 寻找链表中间节点
	jump1 = head.next  # step为1的指针
	jump1Pre = head.next # 用于指向jump1的前驱节点
	jump2 = head.next  # step为2的指针
	mid = None # 用于指向链表的重点
	while jump2.next is not None:
		#这句是重点！！当链表长度为偶数，比如：1->2->3->4
		#在一次循环后jump2指向3，根据循环条件，此时是要再进入循环的，
		#这次循环是没问题的，也就是jump2指向None，但是此时来判断是否进循环就出了问题
		#因为jump2是空的，它没有next属性，程序在运行是会报错
		if jump2.next.next is None:
			break
		# 指向下一跳
		jump1Pre = jump1
		jump1 = jump1.next
		jump2 = jump2.next.next
	#这里接着上面的问题，无论是哪种情况退出循环
	# 其中间值我都设为jump1后一个，
	# 1）循环条件退出，说明个数为偶数，选jump1和jump1.next是一样的
	# 2）if语句退出，说明链表长度为奇数，但是jump2并没有到最后一个，
	#    所以其中间值应该是jump1的后一个，这是数学问题，大家自己画画图
	mid=jump1.next
	jump1Pre=jump1
	jump1Pre.next = None  # 切断

	#逆序后面的链表，这里就不多说了，前面都讲了三个方法了	
	cur=mid.next#用来逆序链表,指向第2个节点
	mid.next=None
	while cur is not None :
		next=cur.next
		cur.next=mid
		mid=cur
		cur=next

	# 这里是难点
	# 合并head和mid，mid无头节点
	curHead=head.next # 指向前半条链表的第一个节点
	curmid=mid # 指向后半条链表的第一个节点，从这里也可理解前面的mid节点的选取，
	#因为我要的是后半条，自然得要中间节点的后一个
	while curHead.next is not None:
		#因为取中间节点的原因，前半条链表的长度大于等于后半条
		nexthead = curHead.next #记录head的下一个节点
		#这里你看我前面画的图 
		curHead.next = curmid
		nextmid = curmid.next #记录mid的下一个节点
		curmid.next = nexthead
		curHead = nexthead
		curmid = nextmid
	# 这是前半条链表导等于后半条链表，
	# 也就是原链表产的长度为偶数的情况，因为前面循环只处理的
	# 只是将head连到mid，再从mid连到head，每次处理两个链接，
	# 但是偶数个节点之间应该有奇数个链接，这里是mid的最后一个节点没有处理
	if curmid is not None:
		curHead.next=curmid
	return head

if __name__ == '__main__':
	head=creatLink(10)
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