def number_needed(a, b):
    l1 = list(a)   #typecasting string to a list
    l2 = list(b)	#typecasting string to a list
    
    c = len(l2)
    
    count = 0
    
    for i in l1:	#iterating for each element in l1
        if i in l2:	#checking membership of element in l2
            count += 1	
            l2.remove(i)	#removing element from l2 not l1
                   
    l = len(l1) + c -(2*count)
    return l

a = input().strip()
b = input().strip()

print(number_needed(a, b))     #calling number_needed(a, b )
