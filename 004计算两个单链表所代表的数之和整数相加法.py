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
方法：整数相加，先求h1的和，再求h2的和，然后相加，最后根据和新建链表
"""
#构造链表
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
#用于求和
def fn(x,y):
	return x*10+y
#求链表所代表的数	
def sumlink(head):
	Sum=0#保存和
	cur=head.next
	List=[]#用于保存链表的每一个节点
	while cur is not None:
		#将节点保存在第一位
		List.insert(0,cur.data)
		cur=cur.next
	if head is not None or head.next is not None:
		Sum=reduce(fn,List)
	print("head's Sum :",Sum)
	return Sum

def function(head1,head2):
	Sum=sumlink(head1)+sumlink(head2)
	print("sum is ",Sum)
	Sum=str(Sum)
	head=LNode(None)
	cur=head
	tmp=None
	for i in Sum:
		tmp=LNode(i)
		cur.next=tmp
		cur=cur.next
	# 判断链表是否为空
	if head is None or head.next is None:
		return

	# 处理链表头
	cur = head.next
	next = cur.next
	cur.next = None
	pre = cur
	cur = next

	# 转变当前节点指向
	while cur.next != None:
		next = cur.next
		cur.next = pre
		pre = cur
		cur = next

	# 处理最后一个节点与倒数第二个节点
	cur.next = pre

	# 添加头节点
	head.next = cur

	return head

if __name__ == '__main__':
	head1=creatLink(10)
	head2=creatLink(10)
	
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

	head = function(head1,head2)

	print("\nAfteplus:")
	cur = head.next
	while cur != None:
		print(cur.data)
		cur = cur.next