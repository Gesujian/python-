import random
class LNode(object):
	"""docstring for LNode"""
	def __init__(self, arg):
		self.data = arg
		self.next = None

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
"""
题目描述：
将Head->1->1->3->3->5->7->7->8变
为head->1->2->5->7->8
方法：空间换时间，利用集合的无序性、唯一性
"""
def RemoveDup(head):
	"""
	空间换时间
	无头节点
	"""
	#先判断链表是否为空或者
	if head.next is None:
		return head
	Hashset=set()#保存已经遍历过的内容
	Hashset.clear()#初始化集合
	pre=head#指向当前节点的前驱节点，用于删除当前节点
	cur=head.next#用于遍历链表，指向当前节点
	#遍历链表
	while cur is not None:
		#如果当前节点的值不在HashSet中，则将其存到HashSet中
		if cur.data not in Hashset:		
			Hashset.add(cur.data)
			#遍历下一个节点
			cur=cur.next
			pre=pre.next
		else:
			#如果当前节点的值在HashSet中，则删除节点
			pre.next=cur.next
			cur=cur.next
	#返回处理完成的链表
	return head


if __name__ == '__main__':
	#构造链表
	head=construstLink(10)
	#打印处理之前的链表
	print("BeforeRemoveDup:")
	cur = head.next
	while cur != None:
		print(cur.data)
		cur = cur.next
	#调用算法，处理链表
	head = RemoveDup(head)
	# 打印处理之后的链表
	print("\nAfterRemoveDup:")
	cur = head.next
	while cur != None:
		print(cur.data)
		cur = cur.next