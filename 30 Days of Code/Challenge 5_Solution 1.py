def is_matched(expression):
    while (len(expression) > 0):
        temp = expression
        expression = expression.replace('()', '')
        expression = expression.replace('{}', '')
        expression = expression.replace('[]', '')
        #print(expression)
    
    
        if temp == expression:
            return False
    return True    

    

t = int(input().strip())
for a0 in range(t):
    expression = input().strip()
    if is_matched(expression) == True:
        print("YES")
    else:
        print("NO")
