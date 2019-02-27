class LNode:
	def __init__(self,x):
		self.data = x
		self.next = None
"""
题目描述：
将Head->1->2->3->4->5->6->7->8逆序
为head->8->7->6->5->4->3->2->1
方法：插入法
"""
def NFirstNodeReverse(head):
	'''
	链表逆序插入法
	不带头节点
	先将不带头节点的链表加入一个头节点
	直接套用带头结点的函数即可
	在返回时再删去
	:param head: 链表头
	:return: 逆序后的链表头
	'''
	#增加头节点
	cur = None
	next = None
	tmp = LNode(None)
	cur = head
	head=tmp
	head.next=cur
	if head is None or head.next is None:
		return head
	cur = None
	next = None
	cur = head.next.next
	head.next.next = None
	while cur is not None:
		next=cur.next
		cur.next=head.next
		head.next = cur
		cur = next
	#删去头节点
	head=head.next
	return head

if __name__ == '__main__':
	#无头结点
	i=1
	head=LNode(i)
	cur=head
	n=8
	tmp = None
	while i<=n-1:
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
	head=NFirstNodeReverse(head)
	cur = head
	while cur != None:
		print(cur.data)
		cur = cur.next

		