#先引入random库
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
方法：顺序删除
"""
#这里!前几篇的create我写错了，少了个e,
#这里改用construct 构造的意思
def construstLink(x):
	i = 1
	head = LNode(None)
	tmp = None
	cur = head
	while i <= x:
		#这里与之前不同，先生成一个随机数，作为节点值
		n = random.randint(0, 9)
		tmp = LNode(n)
		cur.next = tmp
		cur = tmp
		i += 1
	return head
def removeDup(head):
	"""
	有头节点
	"""
	#先判断链表是否为空
	if head.next is None or head is None:
		return head
	outerCur=head.next # 用于遍历整个链表
	innerCur=None  # 用于遍历当前节点的子链表
	innerPre=None # 用于保存内部遍历的当前节点的前驱节点
	while outerCur is not None:
		#inner指向当前节点的后后继节点 用于遍历
		innerCur=outerCur.next
		#innerpre 用来保存当前节点的前驱节点
		innerPre=outerCur
		#这里开始内部遍历，直到链表为空
		while innerCur is not None:
			#判断内部遍历的当前节点的值是否与外部遍历的当前节点的值相同
			if innerCur.data == outerCur.data:
				#相同则删除节点
				innerPre.next=innerCur.next
				innerCur=innerCur.next
			else:
				#不同则继续遍历下一个节点，直到子链表为空
				innerPre=innerCur
				innerCur=innerCur.next
		#遍历下一个节点
		outerCur=outerCur.next
	#返回处理完成的链表
	return  head
if __name__ == '__main__':
	#构造链表
	head=construstLink(8)
	#打印函数
	print("Before-removeDup-head:")
	cur = head.next
	while cur != None:
		print(cur.data)
		cur = cur.next
	#调用函数
	head=removeDup(head)
	#查看完成后的链表
	print("After-removeDup-head:")
	cur = head.next
	while cur != None:
		print(cur.data)
		cur = cur.next
