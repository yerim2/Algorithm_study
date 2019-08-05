from collections import Counter
list1 = [1,2,3,4,5,6,7,5,4,3,5,6,7,8,5,5,3,3,3,3]
counter_each_num = Counter(list1)
print counter_each_num
print counter_each_num.most_common()
print counter_each_num[3]

list2 = [["A","a"],["B","b"],["C","c"],["D","c"]]
counter_each_char = Counter([key for _, key in list2])
print counter_each_char
for key,val in dict(counter_each_char).items():
    print(key,val)

s = 'How many words in this'
words = s.split()
counter_each_word = Counter(words)
print counter_each_word

print(counter_each_char+counter_each_word)
