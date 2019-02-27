import random
import time
class LNode:
	def __init__(self,arg):
		self.data=arg
		self.next=None

"""
题目描述：
给定链表Head->1->2->3->4->5->7->7->8
k=3
反转为链Head->3->2->1->7->5->4->8->7
要求：不足k个也翻转
方法：
"""
def creatLink(x):
	i = 1
	head = LNode(None)
	tmp = None
	cur = head
	while i <= x:
		n = random.randint(1, 9)
		tmp = LNode(n)
		tmp = LNode(i)
		cur.next = tmp
		cur = tmp
		i += 1

	return head
def Reverse(head):
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


def function(head,k):
	if head.next is None or head.next.next is None:
		return head
	pre = head  # 组前点
	slow = head.next  # 组的第一个节点
	fast = head.next  # 组的最后个节点
	p = k
	while p - 1 > 0:
		fast = fast.next  # 这里
		# fast = fast.next 究竟是放前面还是放后面，这里就非常讲究了，
		# 在这里放前面放后面作用是一样的，因为，前面第一条把只有一个节点的情况直接过滤了
		# 所以这里不会出现fast为None,而报出没有next属性的错误，但是在超过一组的情况中
		# 不能过滤掉还剩一个的情况，只能先判断后翻转，所以如果放前面就会出现直
		# 接把第一个节点直接跳过的情况
		if fast.next is None:
			# 不足一组
			Reverse(slow)
			head.next = fast
			return head
		# fast = fast.next
		p -= 1
	# 一组以上
	while True:
		# 用来指向下一组的第一个节点
		next = fast.next
		# 断开与上一组的链接 可以不用断，不断开的话在翻转时pre.next但是断开来理解更形象
		# pre.next=None
		# 断开与下一组的链接
		fast.next = None
		# 翻转当前组的链表
		Reverse(slow)
		# 将当前链表与链表尾部相连
		pre.next = fast
		# 将pre移至链表尾部，因为翻转fast指向了组中第一个节点，slow则指向了最后一个
		pre = slow
		# 链接当前组与下一组  这里也很精髓 ，可以直接去掉，可以连也可以不连，反正一会得断掉
		# pre.next=next
		# 判断next是否为空 这里是精髓，就像判断链表是否为空一格道理，一开始我忘了。
		if next is None:
			return head
		# 将slow指向下一组的第一个节点
		slow = next
		fast = slow
		# 判断后面是否还有一组
		p = k
		while p - 1 > 0:
			# 不够一组翻转并推出
			# fast = fast.next
			if fast.next is None:
				# pre.next = None
				# 翻转
				Reverse(slow)
				# 将当前组链接至链表尾部
				pre.next = fast
				return head
			fast = fast.next
			p -= 1

if __name__ == '__main__':
	head = creatLink(100000)
	#print("head:")
	#cur = head.next
	#while cur != None:
	#	print(cur.data)
	#	cur = cur.next
	k=int(input("请输入k值：\n"))
	#k=3
	start=time.time()
	head = function(head,k)

	end=time.time()
	print("用时",start-end)
	#print("\nAfterReverse:")
	#cur = head.next
	#while cur != None:
	#	print(cur.data)
	#	cur = cur.next