import random
class LNode:
	def __init__(self,arg):
		self.data=arg
		self.next=None

"""
题目描述：
给定链表Head->1->1->3->3->5->7->7->8
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
def FindLastButK(head,k):
	i=0
	slow=head.next
	fast=head.next
	while k-1>0:
		fast=fast.next
		k-=1
	#exec('''"fast=head.next"+".next"*(k-1)''')
	pre=None
	if head.next is not None:
		while fast.next is not None:
			#print("s",slow.data)
			#print("f",fast.data)
			pre=slow
			slow=slow.next
			fast=fast.next
		pre.next=None
		cur=head.next
		head.next=slow
		fast.next=cur
		return head
	return head
if __name__ == '__main__':
	head=creatLink(10)
	print("beforewhirlhead:")
	cur = head.next
	while cur != None:
		print(cur.data)
		cur = cur.next
	k=int(input("请输入k:\n"))

	item=FindLastButK(head,k)
	#print("链表倒数第%d个元素为："%k,item)
	print("afterwhirlhead:")
	cur = head.next
	while cur != None:
		print(cur.data)
		cur = cur.next


