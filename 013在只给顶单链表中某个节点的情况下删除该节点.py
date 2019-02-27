import random
class LNode:
	def __init__(self,arg):
		self.data=arg
		self.next=None

"""
题目描述：
给Head->1->2->2->4->5->5->6
				 ^
				 |
				 p	
只给定p指针删除节点

要求：
方法：

"""
def creatLink(x):
	i = 1
	head = LNode(None)
	tmp = None
	cur = head
	while i <= x:
		n=random.randint(1,9)
		tmp = LNode(n)
		cur.next = tmp
		cur = tmp
		i += 1
	return head

def DelNode(head,p):
	if head is None or head.next is None or head.next.next is None:
		return head
	p.data=p.next.data
	p.next=p.next.next
	return head
if __name__ == '__main__':
	head=creatLink(10)
	p=head.next.next.next.next.next
	print("BeforeReverse:")
	cur = head.next
	while cur != None:
		print(cur.data)
		cur = cur.next

	print("p->",p.data)
	head=DelNode(head,p)
	print("\nAfterReverse:")
	cur = head.next
	while cur != None:
		print(cur.data)
		cur = cur.next
	