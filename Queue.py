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
for i in range(0,len(progresses)):
    end.append(math.ceil((100-progresses[i])/speeds[i]))
    print end
answer = []

test = Queue()

test.Enqueue(end[0])

for i in range(0,len(end)-1):
    count = 1;
    if end[i+1]<=end[i]:
        test.Enqueue(end[i+1])
        count += 1
    else:
        while(test.isEmpty()==False):
            test.Dequeue()
    answer.append(count)
print(answer)
