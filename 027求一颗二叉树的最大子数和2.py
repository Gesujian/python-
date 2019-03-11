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
class LastChoose:
	def __init__(self):
		self.maxSum=-2**31

	def constuctBiTree(self,x):
		# 构造一个没有零的二叉树
		arr = []
		for i in range(x):
			x = random.randint(-9, 9)
			arr.append(x if x != 0 else 1)
		print(arr)
		root = arrayToBiTree(arr)
		return root

	def SumChildTree(self,root, maxSumRoot):
		# maxSum是是保存最大和的子树根节点
		# 空节点返回其左右子树和为0
		if root is None:
			return 0
		# 求左子树和
		sum_left_childTree = self.SumChildTree(root.left_child, maxSumRoot)
		# 求右子树和
		sum_right_childTree = self.SumChildTree(root.right_child, maxSumRoot)
		# 求当前节点的左右子树和
		sum = sum_left_childTree + sum_right_childTree + root.data
		# 与当前找到的最大和做比较，如果更大则复制之
		print("sum==",sum)
		if sum > self.maxSum:
			self.maxSum = sum
			maxSumRoot.data = root.data
			maxSumRoot.left_child = root.left_child
			maxSumRoot.right_child = root.right_child
		return sum

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

if __name__ == '__main__':
	test=LastChoose()
	root=test.constuctBiTree(7)
	maxSumRoot=BiTNode(None)
	test.SumChildTree(root,maxSumRoot)
	print("字数和",str(test.maxSum))
	print("节点",str(maxSumRoot.data))
	print_tree_mid_order(maxSumRoot)