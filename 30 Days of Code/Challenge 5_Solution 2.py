def is_matched(expression):
    s = []
    
    pair = {'(' : ')', '{' : '}', '[' : ']'}
    
    for c in expression:
        if c in pair:
            s.append(pair[c])
            #print(s)
        elif len(s)>0 and c == s[-1]:
            s.pop()
        else:
            return (False)
 
    return not s

    

t = int(input().strip())
for a0 in range(t):
    expression = input().strip()
    if is_matched(expression) == True:
        print("YES")
    else:
        print("NO")
