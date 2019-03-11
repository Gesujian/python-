import random
class LNode:
	def __init__(self,arg):
		self.data=arg
		self.next=None

"""
题目描述：
给定链表 
Head->1->1->3->3->5->7->7->8
k=4
Head->5->7->7->8->1->1->3->3
要求：
方法：先后指针法
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

def RotatingLastButK(head,k):
	slow=head.next
	fast=head.next
	#处理fast节点
	while k-1>0:
		fast=fast.next
		k-=1
	#pre用来指向slow的前驱节点
	pre=None
	#判断链表是否为空，不为空执行
	if head.next is not None:
		#开始循环，直到fast指向最后一个节点。
		while fast.next is not None:
			pre=slow
			slow=slow.next
			fast=fast.next
		pre.next=None # 断开链表
		cur=head.next
		head.next=slow # 头结点指向slow
		fast.next=cur # 将前N-k个节点接在尾部
	#返回头结点
	return head
	
if __name__ == '__main__':
	head=creatLink(10)
	print("beforewhirlhead:")
	cur = head.next
	while cur != None:
		print(cur.data)
		cur = cur.next
	k=int(input("请输入k:\n"))
	item=RotatingLastButK(head,k)
	#print("链表倒数第%d个元素为："%k,item)
	print("afterwhirlhead:")
	cur = head.next
	while cur != None:
		print(cur.data)
		cur = cur.next


