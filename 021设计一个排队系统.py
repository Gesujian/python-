# 人工客服排队系统，每个用户都能看到自己位置，如果有人退出，位置变动会通知用户，
# 中途能退出，
# 方法：用队列实现排队，用户为单独的对象，有入队，出队，查看位置，办理业务（用2秒时延代替）
# 的操作，
# 先构造队列类
import time  # 因为要用到时延
import random
class LNode:
	def __init__(self, arg):
		self.data = arg
		self.next = None


class Queue:
	# 模拟队列
	def __init__(self):
		# phead=LNode(None)
		self.data = None
		self.next = None
		self.front = self  # 指向队列首
		self.rear = self  # 指向队列尾

	# 判断队列是否为空,如果为空返回True，否则返回false
	def isEmpty(self):
		return self.front == self.rear

	# 返回队列的大小
	def size(self):
		p = self.front
		size = 0
		while p.next != self.rear.next:
			p = p.next
			size += 1
		return size

	# 返回队列首元素
	def top(self):
		if not self.isEmpty():
			return self.front.next.data
		else:
			#print("队列为空")
			return None

	# 返回队列尾元素
	def bottom(self):
		if not self.isEmpty():
			return self.rear.data
		else:
			#print("队列为空")
			return None

	# 出队列
	def pop(self):
		if self.size() == 1:
			data = self.front.next
			self.rear = self
			return data.data

		elif not self.isEmpty():
			data = self.front.next
			self.front.next = self.front.next.next
			#print("出队列成功")
			return data.data
		else:
			#print("队列已为空")
			return None

	# 入队列
	def push(self, item):
		tmp = LNode(item)
		self.rear.next = tmp
		self.rear = self.rear.next
		#print("入队列成功")

	# 清空队列
	def destroy(self):
		self.next = None
		#print("队列已清空")

	# 打印队列
	def showQueue(self):
		if not self.isEmpty():
			p = self.front.next
			while p != self.rear.next:
				print(p.data)
				p = p.next

class Users:
	def __init__(self):
		self.ID = GetID()  # 获取能唯一标识用户身份的ID,由系统分配
		self.UserName = Getname()  # 获取用户姓名，让用户能辨别自己
		self.Seq = 0  # 用户当前在队列中的位置

	# 加入排队
	def EnQueue(self):
		return self.ID

	# 退出队列
	def DeQueue(self):
		return self.ID

	# 查看当前自己在队列中的位置
	def ShowPosition(self, queue):
		return f"SYS:用户{self.UserName}\n当前共有：{queue.size()}人在排队\n你前面有：{self.Seq - 1}人"

	# 办理业务，这里用2秒时延代替。
	def Transaction(self):
		print("*"*50)
		print(self.UserName+"正在办理业务")
		for i in "abc":
			time.sleep(1)
			print(i)
		print(self.UserName + "办理业务成功，退出队伍")
		print("*"*50)


# 构造队伍的类:
class QueueUp:
	def __init__(self):
		self.queue = Queue()  # 队伍
		self.update = Queue()  # 用来处理前面有人中途退出的情况
		#self.userDeQueueTransaction()

	# 客户进入队伍,新建一个user对象入队，前面的客户不变,Seq为队长+1
	def userEnQueue(self):
		user = Users()
		user.Seq = self.queue.size() + 1

		self.queue.push(user)
		print(user.ShowPosition(self.queue))
		print("++++++++++++")
		print("新增一人入队：",user.UserName)
		print("\n")

	# 客户中途离开队伍，其前面的客户不变，后面的客户的Seq属性-1
	# 将其前面的用户存到栈中，然后让用户离开，然后在把保存在栈中的用户排在队伍后面
	# 但是队列是先进后出，所以全部出队列，将离开用户弹出，再重新排队
	def userDeQueueHalfway(self, UserName):
		while not self.queue.isEmpty():
			if self.queue.top().UserName == UserName:
				print("_____________________________")
				print(self.queue.top().UserName+"中途退出")
				self.queue.pop()
				time.sleep(2)
				print("\n")
			else:
				self.update.push(self.queue.pop())
		while not self.update.isEmpty():
			self.queue.push(self.update.pop())
			self.queue.top().Seq = self.queue.size()
			print(self.queue.bottom().ShowPosition(self.queue))

	# 客户正常办理完业务离开,其出列，其后所有人Seq-1
	def userDeQueueTransaction(self):
		if not self.queue.isEmpty():
			self.queue.top().Transaction()
			self.queue.pop()
			while not self.queue.isEmpty():
				self.update.push(self.queue.pop())
			while not self.update.isEmpty():
				self.queue.push(self.update.pop())
				self.queue.top().Seq = self.queue.size()
				print(self.queue.bottom().ShowPosition(self.queue))


def GetID():
	# 给用户选择一个唯一的ID
	ID = time.time()
	IDList.add(ID)
	return ID

def Getname():
	# 给用户选一个好记的名字
	return "user" + str(len(IDList))


if __name__ == '__main__':
	IDList = set()
	myqueue = QueueUp()
	for i in range(10):
		time.sleep(3)
		myqueue.userEnQueue()
	while not myqueue.queue.isEmpty():
		myqueue.userDeQueueTransaction()
		if random.randint(0,2)==1:
			myqueue.userDeQueueHalfway("user9")
		if random.randint(0,2)==1:
			myqueue.userEnQueue()

			

