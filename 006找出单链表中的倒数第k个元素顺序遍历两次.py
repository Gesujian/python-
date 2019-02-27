import random
class LNode:
	def __init__(self,arg):
		self.data=arg
		self.next=None

"""
题目描述：
给定链表Head->1->1->3->3->5->7->7->8
单链表倒数第k=3个元素为7
要求：
方法：遍历链表计算链表长度n,然后求顺序第n-k+1个元素即可，再遍历一遍链表就可以得到结果
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
	cur=head.next
	if head.next is not None:
		while cur.next is not None:
			i+=1
			cur=cur.next
		n=i-k+1
		cur=head.next
		while n>0:
			cur=cur.next
			n=n-1
		return cur.data
	return None
if __name__ == '__main__':
	head=creatLink(10)
	print("head:")
	cur = head.next
	while cur != None:
		print(cur.data)
		cur = cur.next
	k=int(input("请输入k:\n"))
	item=FindLastButK(head,k)
	print("链表倒数第k个元素为：",item)


