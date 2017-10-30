# Bubble sort
#While running through the array, if the element you encounter is 
#greater than its successor, you need to swap

a = [1,4,2,7,3]
print "Original", a
n = len(a)
temp  = 0
numswaps = 0
for i in range(n, 0, -1):
    for j in range(0, i-1):
        if a[j] > a[j+1]:
            temp = a[j]
            a[j] = a[j+1]
            a[j+1] = temp
            numswaps += 1
            
print "Sorted", a
print "swaps", numswaps