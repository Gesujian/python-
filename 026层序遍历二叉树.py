#层序遍历二叉树，先遍历根节点，在遍历根节点的左右节点，在遍历根节点的左右子节点
#先定义二叉树节点，以及3种基本遍历方法
#定义二叉树结点类型
class BiTNode:
	"""docstring for BiTNode"""
	def __init__(self,arg):
		self.data = arg
		self.left_child = None
		self.right_child = None

#构造一个中序遍历有序的二叉树
def constructBitree(x):
	#x为二叉树节点个数
	arr=[]
	for i in range(10):
		arr.append(i)
	root=arrayToBiTree(arr)
	return root

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

#构造队列，
class LNode:
	def __init__(self,arg):
		self.data=arg
		self.next=None

class MyQueue:
	#模拟队列
	def __init__(self):
		#phead=LNode(None)
		self.data=None
		self.next=None
		self.front=self#指向队列首
		self.rear=self#指向队列尾
	#判断队列是否为空,如果为空返回True，否则返回false
	def isEmpty(self):
		return self.front==self.rear
	#返回队列的大小
	def size(self):
		p=self.front
		size=0
		while p.next!=self.rear.next:
			p=p.next
			size+=1
		return size
	#返回队列首元素
	def top(self):
		if not self.isEmpty():
			return self.front.next.data
		else:
			#print("队列为空")
			return None
	#返回队列尾元素
	def bottom(self):
		if not self.isEmpty():
			return self.rear.data
		else:
			#print("队列为空")
			return None
	#出队列
	def pop(self):
		if self.size()==1:
			data=self.front.next
			self.rear=self
			return data.data
		elif not self.isEmpty():
			data=self.front.next
			self.front.next=self.front.next.next
			#print("出队列成功")
			return data.data
		else:
			#print("队列已为空")
			return None
	#入队列
	def push(self,item):
		tmp=LNode(item)
		self.rear.next=tmp
		self.rear=self.rear.next
		#print("入队列成功")
	#清空队列
	def destroy(self):
		self.next=None
		#print("队列已清空")
	#打印队列
	def showQueue(self):
		if not self.isEmpty():
			p=self.front.next
			while p != self.rear.next:
				print(p.data)
				p=p.next
"""
队列，在遍历当前节点时，将节点的左右节点入队列，记录其子节点的顺序，
在遍历完当前层的节点数据后，按照当前队列中保存的节点顺序遍历节点，递归调用，遍历当前层的下一层
递归定义：将root节点如队列，然后将其左右子节点依次入队，然后打印队列头的元素，出队，
递归终止条件：队列为空
"""
# 层序遍历
def print_tree_layer_order(root):
	if root is None:
		return None

	#将当前节点以及其左右孩子依次存入队列，输出当前队列的头元素的data，
	#并弹出队头元素
	#queue.push(root)
	print(root.data)
	queue.pop()
	#print(root.left_child.data)
	#print(root.right_child.data)
	if root.left_child is not None:
		queue.push(root.left_child)
	if root.right_child is not None:
		queue.push(root.right_child)
	#当队列不为空时，递归调用该函数
	while not queue.isEmpty():
		print_tree_layer_order(queue.top())

if __name__ == '__main__':
	root=constructBitree(10)
	queue = MyQueue()
	print("中序遍历")
	print_tree_mid_order(root)
	print("前序遍历")
	print_tree_pre_order(root)
	print("层序遍历")
	print_tree_layer_order(root)