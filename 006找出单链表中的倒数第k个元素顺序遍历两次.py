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
#先构造链表
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
#函数开始
#输入链表头以及k值
def FindLastButK(head,k):
	#如果链表非空则执行
	if head.next is not None:
		cur=head #因为这里是计算链表长度，需要将第一个节点也算上
		i=0 #用于记录链表长度
		while cur.next is not None:
			i+=1
			cur=cur.next
		#将问题转化为求 正序数第n-k+1个元素
		n=i-k+1
		cur=head
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


