"""
给定一个数组[3,4,7,10,20,9,8],可以找出两个数队(3,8),(4,7)=>3+7=8+4
"""
import random
class Pair:
	"""docstring for pair"""
	def __init__(self,first,second):
		self.first=first
		self.second=second

def findPairs(arr):
	Dict={}
	i=0
	n=len(arr)
	while i<n:
		j=i+1
		while j<n:
			pair=Pair(arr[i],arr[j])
			sum=arr[i]+arr[j]
			if sum not in Dict:
				Dict[sum]=pair
			else:
				p=Dict[sum]
				print("数队：("+str(pair.first)+","+str(pair.second)+")与("+str(p.first)+","+str(p.second)+")符合题目要求")
				Dict[sum] = pair
			j+=1
		i+=1
	return False
if __name__ == '__main__':
	arr=[]
	for i in range(6):
		arr.append(random.randint(0,9))
	print(arr)
	findPairs(arr)
	print(arr)
