#二叉树有顺序存储和链式存储两种，这里用的链式存储
#遍历二叉树的三种方法：前序、中序、后序
#构造二叉树节点类型
class BiTNode:
	"""docstring for BiTNode"""
	def __init__(self,arg):
		self.data = arg
		self.left_child = None
		self.right_child = None
"""
# 叶子节点：没有子节点，只有根节点，
# 如何判断其是否是叶子节点是个难点！！！
# **当该节点没有左右孩子，
# 很容易写成：
```
if root.left_child is None and root.right_child is None:
    return root
```
"""

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
	

if __name__ == '__main__':
	root=BiTNode(1)
	root.left_child=BiTNode(2)
	root.right_child=BiTNode(3)
	root.left_child.left_child=BiTNode(4)
	root.left_child.right_child = BiTNode(4)
	print("前序：\n")
	print_tree_pre_order(root)
	print("中序：\n")
	print_tree_mid_order(root)
	print("后序：\n")
	print_tree_after_order(root)
