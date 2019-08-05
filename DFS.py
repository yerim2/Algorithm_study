number = [1,1,1,1,1]
target = 3
def solution(numbers,target):
    answer=[0]
    for a in numbers:
        temp=[]
        for b in answer:
            temp.append(b+a)
            temp.append(b-a)
        answer=temp
    result = answer.count(target)
    return result
print(solution(number,target))