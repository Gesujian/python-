import random
class LNode:
	def __init__(self,arg):
		self.data=arg
		self.next=None

"""
题目描述：
给定链表Head->1->2->3->4->5->7->7->8
反转为链Head->2->1->4->3->7->5->8->7
要求：
方法：只用一个cur,用pre和next辅助反转。
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
def function(head):
	if head is None or head.next is None:
		return head
	cur=head.next#当前遍历节点
	pre=head#当前遍历节点的前驱节点
	next=None#当前节点后继节点的后继节点
	while cur is not None and cur.next is not None:
		next=cur.next.next
		pre.next=cur.next
		cur.next.next=cur
		cur.next=next
		pre=cur
		cur=next
	return head
if __name__ == '__main__':
	head = creatLink(11)
	print("head:")
	cur = head.next
	while cur != None:
		print(cur.data)
		cur = cur.next
	head = function(head)
	print("\nAfterReverse:")
	cur = head.next
	while cur != None:
		print(cur.data)
		cur = cur.next