class BiTNode(object):
	"""docstring for BiTNode"""
	def __init__(self,arg):
		self.data = arg
		self.left_child = None
		self.right_child = None

def print_tree_mid_order(root):
	#先判断二叉树是否为空,当左右节点都为空时
	if root.left_child is None and root.right_child is None:
		return root
	#中序遍历 左根右
	#遍历左子树
	if root.left_child is not None:
		print_tree_mid_order(root.left_child)
	#遍历根节点
	print(root.data)
	#遍历右子树
	if root.right_child is not None:
		print_tree_mid_order(root.right_child)
def print_tree_pre_order():
	#先判断二叉树是否为空
	if root.data == None:
		return root
	#先根
	print(root.data)
	#再左
	if root.left_child is not None:
		print_tree_mid_order(root.left_child)
	#再右
	if root.right_child is not None:
		print_tree_mid_order(root.right_child)

def print_tree_after_order():
	#先判断二叉树是否为空
	if root.data == None:
		return root
	#再左
	if root.left_child is not None:
		print_tree_mid_order(root.left_child)
	#再右
	if root.right_child is not None:
		print_tree_mid_order(root.right_child)
	#先根
	print(root.data)
	
#二叉树有顺序存储和链式存储两种，这里用的链式存储
if __name__ == '__main__':
	root=BiTNode(1)
	root.left_child=BiTNode(2)
	root.right_child=BiTNode(3)
	print("前序：",print_tree_pre_order(root))
	print("中序：",print_tree_mid_order(root))
	print("后序：",print_tree_after_order(root))
