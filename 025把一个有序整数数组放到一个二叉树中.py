#定义二叉树结点类型
class BiTNode:
	"""docstring for BiTNode"""
	def __init__(self,arg):
		self.data = arg
		self.left_child = None
		self.right_child = None

#前序遍历
def print_tree_pre_order(root):
	#先判断二叉树是否为空
	#if root.left_child is None and root.right_child is None:
	if root is None:
		return root
	#先根
	print(root.data)
	#再左
	if root.left_child is not None:
		print_tree_pre_order(root.left_child)
	#再右
	if root.right_child is not None:
		print_tree_pre_order(root.right_child)

#中序遍历二叉树
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

#后序遍历
def print_tree_after_order(root):
	#先判断二叉树是否为空
	if root is None:
		return root
	#再左
	if root.left_child is not None:
		print_tree_after_order(root.left_child)
	#再右
	if root.right_child is not None:
		print_tree_after_order(root.right_child)
	#先根
	print(root.data)

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


		

#将[0,1,2,3,4,5,6,7,8,9,10]存储到二叉树
if __name__ == '__main__':
	#先构造一个有序数组、链表
	arr=[]
	for i in range(10):
		arr.append(i)
	print(arr)
	#调用函数
	BT=arrayToBiTree(arr)
	#前序遍历二叉树
	print("前序")
	print_tree_pre_order(BT)
	# 中序遍历二叉树
	print("中序")
	print_tree_mid_order(BT)
	# 后序遍历二叉树
	print("后序")
	print_tree_after_order(BT)

