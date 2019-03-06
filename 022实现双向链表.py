# 题目描述：双向链表，每个节点有三个属性，一个pre域，指向其前驱节点，
# 一个data域，存储节点数据，一个next域。
#单链表的节点只有一个指向其next域的指针，由此从某个节点出发的话，只能顺着指
#针查其后继节点，若要查其前驱节点，则需要从头结点开始遍历，为了克服单链表的
#这种缺点，我们引入双向链表
class LNode:
	def __init__(self,arg):
		self.data=arg
		self.prior=self # 指向其先驱节点
		self.next=self # 指向其后继节点

def createLink(x):
	head=LNode(None)
	tmp=None
	cur=head
	i=1
	while i<x:
		tmp=LNode(i)
		cur.next=tmp
		tmp.prior=cur
		cur=tmp

if __name__ == '__main__':
	head=createLink(10)

