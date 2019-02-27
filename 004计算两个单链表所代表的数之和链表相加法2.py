class LNode:
	def __init__(self,arg):
		self.data=arg
		self.next =None
"""
题目描述：
将Head->1->1->3->3->5->7->7->8
与head->1->2->5->7->8相加
得Head->2->3->8->0->4->8->7->8
个位在前
方法：链表相加
"""
def add(h1,h2):
	if h1 is None or h1.next is None:
		return h2
	if h2 is None or h2.next is None:
		return h1
	c=0#用来记录进位
	sums=0#用来记录两个节点相加的值
	p1=h1.next#用来遍历h1
	p2=h2.next#用来遍历h2
	tmp=None#用来指向新创建的存储相加和的节点
	resultHead=LNode(None)#相加后链表头节点
	p=resultHead#用来指向链表resultHead最后一个节点
	#先考虑两个链表长度相同的情况
	while p1 is not None and p2 is not None:
		sums=p1.data+p2.data+c#两节点相加和

		tmp=LNode(sums%10)
		c=sums//10#进位  地板除

		p.next=tmp
		p=tmp
		p1=p1.next
		p2=p2.next
	#在考虑h2比h1长，接下来只需要考虑h2剩余节点 的值
	if p1 is None:
		while p2 is not None:
			sums=p2.data+c
			#c=sums/10
			if sums >= 10:
				c = 1
			else:
				c = 0
			tmp=LNode(sums%10)
			p.next=tmp
			p=tmp
			p2=p2.next
	#在考虑h1比h2长，接下来只需要考虑h1剩余节点 的值
	if p2 is None:
		while p1 is not None:
			sums=p1.data+c
			#c=sums/10
			if sums >= 10:
				c = 1
			else:
				c = 0
			tmp=LNode(sums%10)
			p.next=tmp
			p=tmp
			p1=p1.next
	if c==1:
		tmp=LNode(c)
		p.next=tmp
	return resultHead
if __name__ == '__main__':
	i=1
	head1=LNode(None)
	head2=LNode(None)
	tmp=None
	cur=head1
	addResult=None
	#构造第一个链表
	while i<7:
		tmp=LNode(i+2)
		cur.next=tmp
		cur=tmp
		i+=1
	cur=head2
	i=9
	while i>4:
		tmp=LNode(i)
		cur.next=tmp
		cur=tmp
		i-=1
	print("\nHead1:")
	cur=head1.next
	while cur is not None:
		print(cur.data)
		cur=cur.next
	print("\nHead2:")
	cur=head2.next
	while cur is not None:
		print(cur.data)
		cur=cur.next
	addResult=add(head1,head2)
	print("\n相加后:")
	cur=addResult.next
	while cur is not None:
		print(cur.data)
		cur=cur.next


