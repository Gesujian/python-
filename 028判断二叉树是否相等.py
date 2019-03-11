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
		x=random.randint(-9,9)
		arr.append(x if x!=0 else 1)
	print(arr)
	root=arrayToBiTree(arr)
	return root

def isEqual(root1,root2):
	if root1 is None and root2 is None:
		return True
	if root1 is None and root2 is not None:
		return False
	if root1 is not None and root2 is None:
		return False
	if root1.data==root2.data:
		return isEqual(root1.left_child,root2.left_child) and isEqual(root1.right_child,root2.right_child)
	else:
		return False

if __name__ == '__main__':
	root1=constuctBiTree(10)
	root2=constuctBiTree(9)
	root3=root1
	root4=constuctBiTree(10)
	if isEqual(root1,root2):
		print("root1和root2相等")
	else:
		print("root1和root2不相等")
	if isEqual(root1,root3):
		print("root1和root3相等")
	else:
		print("root1和root3不相等")
	if isEqual(root1,root4):
		print("root1和root4相等")
	else:
		print("root1和root4不相等")
		