import random
class LNode(object):
	"""docstring for LNode"""
	def __init__(self, arg):
		self.data = arg
		self.next = None

"""
题目描述：
将Head->1->1->3->3->5->7->7->8变
为head->1->2->5->7->8
方法：递归法2
"""
def RemoveDup(head):
	"""
	无头结点
	"""
	if head.next is None:
		return head
	#这里的if语句只是为了判断递归是否到了最后第二个节点，所以下面不需要else语句
	#直接写在if同一层就行。
	pre=head
	cur=head.next
	head.next=RemoveDup(head.next)
	# 注意是head.next 因为这里是去掉与head相同的值，但是head还是留下来的
	while cur is not None:
		if cur.data == head.data:
			pre.next=cur.next
			cur=cur.next
			#删除重复节点的操作：
			#  pre   cur
			#  |      |
			#  |______|______
			#  \             >
			#   \           /
			#    \_________/
		else:
			cur=cur.next
			pre=pre.next
	return head
		
def HaveFirstNodeRemoveDup(head):
	"""
	有头节点
	"""
	if head.next is None:
		return head
	else:
		firstnode=head.next
		newhead=RemoveDup(firstnode)
		return newhead
if __name__ == '__main__':
	i = 1
	head = LNode(None)
	tmp = None
	cur = head
	while i <= 10:
		n = random.randint(1, 10)
		tmp = LNode(n)
		cur.next = tmp
		cur = tmp
		i += 1
	print("BeforeReverse:")
	cur = head.next
	while cur != None:
		print(cur.data)
		cur = cur.next

	head = RemoveDup(head)

	print("\nAfterReverse:")
	cur = head.next
	while cur != None:
		print(cur.data)
		cur = cur.next