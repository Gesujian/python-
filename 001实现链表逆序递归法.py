import time
class LNode:
    def __init__(self,x):
        self.data=x
        self.next=None

"""
题目描述：
将Head->1->2->3->4->5->6->7->8逆序
为head->8->7->6->5->4->3->2->1
方法：递归法
"""
def RecursiveReverese(head):
    '''
    没有头节点
    '''
    if head is None or head.next is None:
    	return head
    else:
    	newhead = RecursiveReverese(head.next)
    	head.next.next = head
    	head.next = None
    return newhead

def Reverese(head):
	'''
	带头节点
	:param head: 带头节点链表
	:return: 逆序后的
	'''
	if head.next is None:
		return
	firstNode=head.next
	newhead=RecursiveReverese(firstNode)
	head.next=newhead
	return head

if __name__=='__main__':
	starttime=time.time()
	i=1
	tmp=None
	head=LNode(None)#链表头
	cur=head
	while i<=999:
		tmp=LNode(i)
		cur.next=tmp
		cur=tmp
		i+=1
	#逆序前
	print("BeforeReversehead:")
	cur = head.next
	while cur != None:
		print(cur.data)
		cur = cur.next
	print("\nAfterReversehead:")
	head=Reverese(head)
	cur = head.next
	while cur != None:
		print(cur.data)
		cur = cur.next
	endtime = time.time()
	#print(str(endtime - starttime))