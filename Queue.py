import math
class Queue:
    def __init__(self):
        self.Queue_item =[]

    # Enqueue
    def Enqueue(self,x):
        self.Queue_item.append(x)
        return None

    # Dequeue
    def Dequeue(self):
        item_length = len(self.Queue_item)
        if item_length < 1:
            print("Queue is empty!")
            return False
        result = self.Queue_item[0]
        del self.Queue_item[0]
        return result
    # isEmpty
    def isEmpty(self):
        return  not self.Queue_item

end = []
progresses = [93,30,55]
speeds=[1,30,5]
answer =[]
progresses = [math.ceil((100-a)/b) for a,b in zip(progresses,speeds)]

front = 0
for i in range(len(progresses)):
    print i
    if progresses[front]<progresses[i]:
        answer.append(i-front)
        front = i
answer.append(len(progresses)-front)
print answer