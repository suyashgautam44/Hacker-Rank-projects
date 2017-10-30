import sys

#h = map(int, raw_input().strip().split(' '))
word = raw_input().strip()

h = [1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 
     5, 5, 5, 5, 5, 5]
new_list = []
alphabets = ['a','b','c','d','e','f','g','h','i','j',
             'k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
ld = dict(zip(alphabets, h))
#for every element in dictionary, if that element is also in word, get its keys 
x = [ld[x] for x in ld if x in word]
y = max(x)*len(word)

print y
