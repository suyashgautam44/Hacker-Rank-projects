#Binary search Implementation recursive

def Binarysearch(a, low, high, x):
    if low > high:
        return -1
    mid = (low + high)/2
    if x == a[mid]:
        return mid
    elif x < a[mid]:
        return Binarysearch(a, low, mid - 1, x)
    else:
        return Binarysearch(a, mid +1, high, x)
    

a = int(raw_input('Enter how many elements you want in the list'))



elem_list = []
for i in range(a):
    elem = int(raw_input('enter element'))
    elem_list.append(elem)           

x = int(raw_input('enter search elemet'))

lenlist = len(elem_list)

result = Binarysearch(elem_list, 0, lenlist-1, x)
            
if result == -1:
    print "Not found"
else:
    print "Found it", elem_list[result] 