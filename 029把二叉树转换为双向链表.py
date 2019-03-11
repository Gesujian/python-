import random
class BiTNode:
	"""docstring for BiTNode"""
	def __init__(self,arg):
		self.data = arg
		self.left_child = None
		self.right_child = None

def arrayToBiTree(array):
	#判断arr是否为空
	if len(array)==0:
		return BiTNode(array[0])
	mid=len(array)//2 # 有序数组的中间元素的下标
	#print(mid)
	#start=0 # 数组第一个元素的下标
	#end=-1 # 数组最后一个元素的下标
	if len(array)>0:
		#将中间元素作为二叉树的根
		root=BiTNode(array[mid])
		#如果左边的元素个数不为零，则递归调用函数，生成左子树
		if len(array[:mid])>0:
			root.left_child = arrayToBiTree(array[:mid])
		#如果右边的元素个数不为零，则递归调用函数，生成左子树
		if len(array[mid+1:])>0:
			root.right_child = arrayToBiTree(array[mid+1:])
	return root	

def constuctBiTree(x):
	#构造一个没有零的二叉树
	arr=[]
	for i in range(x):
		x=random.randint(0,9)
		arr.append(x)
	print(arr)
	root=arrayToBiTree(arr)
	return root

#中序遍历
def print_tree_mid_order(root):
	#先判断二叉树是否为空,当左右节点都为空时
	if root is None:
		return
	#中序遍历 左根右
	#遍历左子树
	if root.left_child is not None:
		print_tree_mid_order(root.left_child)
	#遍历根节点
	print(root.data)
	#遍历右子树
	if root.right_child is not None:
		print_tree_mid_order(root.right_child)

def BiTreeToDLink(root):
	global pHead
	global pEnd
	if root is None:
		return
	#左子树
	BiTreeToDLink(root.left_child)
	#根节点的左孩子指向pEnd,pEnd的有孩子指向root
	root.left_child=pEnd
	if None == pEnd:
		pHead=root
	else:
		pEnd.right_child = root
	#右子树
	pEnd=root
	BiTreeToDLink(root.right_child)
if __name__ == '__main__':
	root=constuctBiTree(12)
	print("中序遍历：")
	print_tree_mid_order(root)
	pHead=None
	pEnd=None
	BiTreeToDLink(root)
	cur=pHead
	print("双向链表正序:")
	while cur is not None:
		print(cur.data)
		cur=cur.right_child
	cur = pEnd
	print("双向链表倒序:")
	while cur is not None:
		print(cur.data)
		cur = cur.left_child

