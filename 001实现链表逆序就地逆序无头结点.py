class LNode:
	"""
	定义链表对象
	"""

	def __init__(self, x):
		self.data = x
		self.next = None
"""
题目描述：
将Head->1->2->3->4->5->6->7->8逆序
为head->8->7->6->5->4->3->2->1
方法：就地逆序
"""
def NofirstNodeReverse(head):
	if head is None or head.next is None:
		return
	cur = None
	pre = None
	next = None
	#处理第一个节点
	cur = head
	next = cur.next
	cur.next = None
	pre = cur
	cur = next

	while cur.next != None:
		next = cur.next
		cur.next = pre
		pre = cur
		cur = next
	#添加头节点
	cur.next = pre
	head=cur
	return head

if __name__ == '__main__':
	i=1
	head=LNode(i)
	cur=head
	tmp = None
	while i<=8:
		i+=1
		tmp=LNode(i)
		cur.next=tmp
		cur=tmp
	print("BeforeReverse:")
	cur = head
	while cur != None:
		print(cur.data)
		cur = cur.next
	print("\nAfterReverse:")
	head=NofirstNodeReverse(head)
	cur = head
	while cur != None:
		print(cur.data)
		cur = cur.next
