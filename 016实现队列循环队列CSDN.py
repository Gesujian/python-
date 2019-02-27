class SqQueue(object):
    def __init__(self, maxsize):
        self.queue = [None] * maxsize
        self.maxsize = maxsize
        self.front = 0
        self.rear = 0
    """
    ------------------
    队列的存储结构中使用的最多的是循环队列。循环队列包括两个指针， 
    front 指针指向队头元素， rear 指针指向队尾元素的下一个位置。 
    队列为空的判断条件是： 
    front == rear

    队列满的判断条件是： 
    (rear+1)%maxsize == front

    队列长度的计算公式： 
    (rear-front+maxsize)%maxsize
    ------------------
    """
    # 返回当前队列的长度
    def QueueLength(self):
        return self.rear - self.front
        #return (self.rear - self.front + self.maxsize) % self.maxsize

    # 如果队列未满，则在队尾插入元素，时间复杂度O(1)
    def EnQueue(self, data):
        if (self.rear + 1) % self.maxsize == self.front:
            #可以扩充
            print("The queue is full!")
        else:
            self.queue[self.rear] = data
           # self.queue.insert(self.rear,data)
            self.rear = (self.rear + 1) % self.maxsize
            print("EnQueue is done!")

    # 如果队列不为空，则删除队头的元素,时间复杂度O(1)
    def DeQueue(self):
        if self.rear == self.front:
            print("The queue is empty!")
        else:
            data = self.queue[self.front]
            self.queue[self.front] = None
            self.front = (self.front + 1) % self.maxsize
            print("DeQueue is done!")
            return data

    # 输出队列中的元素
    def ShowQueue(self):
        for i in range(self.maxsize):
            print(self.queue[i],end=',')
        print(' ')
# 测试程序
if __name__ == "__main__":
    # 建立大小为15的循环队列
    q = SqQueue(15)
    # 0~9入队列
    for i in range(10):
        q.EnQueue(i)
    q.ShowQueue()
    # 删除队头的5个元素：0~4
    for i in range(5):
        q.DeQueue()
    q.ShowQueue()
    # 从队尾增加8个元素：0~7
    for i in range(8):
        q.EnQueue(i)
    q.ShowQueue()
#--------------------- 
#作者：windwm 
#来源：CSDN 
#原文：https://blog.csdn.net/u012626619/article/details/80658397 
#版权声明：本文为博主原创文章，转载请附上博文链接！