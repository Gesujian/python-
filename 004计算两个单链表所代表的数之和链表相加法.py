import random
#定义链表节点类型
class LNode:
	"""docstring for LNode"""
	def __init__(self, arg):
		self.data = arg
		self.next = None
"""
题目描述：
将Head->1->1->3->3->5->7->7->8
与head->1->2->5->7->8相加
得Head->2->3->8->0->4->8->7->8
个位在前
方法：链表相加
"""
#构造链表
def creatLink(x):
	i = 1
	head = LNode(None)
	tmp = None
	cur = head
	while i <= x:
		n = random.randint(0, 9)
		tmp = LNode(n)
		cur.next = tmp
		cur = tmp
		i += 1
	return head

#输入两个链表，计算链表代表整数的和，并将其存入链表返回
def function(head1,head2):
	#判断两个链表是否都为空为空，为空则返回空链表
	if head1.next is None and head2.next is None:
		return head1
	cur1=head1.next # 指向head1的第一个节点
	cur2=head2.next # 指向head2的第一个节点
	c=0#用来记录进位
	newhead=LNode(None)#这是相加之后产生的新链表，这里称为和
	cur=newhead#指向和
	#当两个链表至少有一个还没有遍历完时，循环
	#这里比较复杂，有三种情况
	#（1）当head1遍历完了
	#（2）当head2遍历完了
	#（3）两个都没有遍历完
	while cur1 is not None or cur2 is not None:
		#head1遍历完了
		if cur1 is None:
			#此时head2是有数据的，head1没有，这里注意加上进位
			sumL = cur2.data + c
		#head2遍历完了
		elif cur2 is None:
			#此时head1是有数据的，head2没有，这里注意加上进位
			sumL = cur1.data + c
		# 都没遍历完
		else:
			#这时两个都有数据，加上进位
			sumL = cur1.data + cur2.data + c
		#判断是否产生进位
		if sumL>=10:
			c=1
		else:
			c=0
		#将该位的和的个位存储为一个节点，并接在总和链表的后面
		n=sumL%10
		tmp=LNode(n)
		cur.next=tmp
		cur=tmp
		#这里是用于循环的语句，这里是需要判断一下的，
		#因为，如果有一个链表先遍历完了，也就是短的那条
		#此时cur是None，如果运行cur1=cur1.next,会报错
		#提示cur为空类型，没有next属性
		#所以这里要先判断，如果为空，就不做变化
		#前面的循环判断语句while cur1 is not None or cur2 is not None:
		#这里我用的 OR 所以要两个都为空才能出循环，这样就省去了判断谁长谁短的步骤了
		if cur1 is not None:
			cur1=cur1.next
		if cur2 is not None:
			cur2=cur2.next
	# 注意！！！！假如两个链表一样长，最后的一位相加大于10，
	# 程序是直接存储了个位，就直接退出了，并没有考虑c进位
	# 所以这里单拿出来判断下
	if c==1:
		tmp=LNode(1)
		cur.next = tmp
		cur = tmp
	#结束后直接返回存储着两个链表的和的链表
	return newhead

if __name__ == '__main__':
	#构造链表，这里可以多试几次，用不同的长度
	head1 = creatLink(1000000)
	head2 = creatLink(1000000)
	#打印head1head2
	print("head1:")
	cur = head1.next
	while cur != None:
		print(cur.data)
		cur = cur.next
	print("head2:")
	cur = head2.next
	while cur != None:
		print(cur.data)
		cur = cur.next
	#调用求和函数
	head = function(head1, head2)
	#打印和链表
	print("\nAfteplus:")
	cur = head.next
	while cur != None:
		print(cur.data)
		cur = cur.next