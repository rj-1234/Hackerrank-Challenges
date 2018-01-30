def ransom_note(magazine, ransom):
    ransom = list(ransom)
    magazine = list(magazine)
    count = 0
    for i in ransom:
        if i in magazine:
            magazine.remove(i)
            count += 1
    if count == n:
        return(True)
    else:
        return(False)

m, n = map(int, input().strip().split(' '))
magazine = input().strip().split(' ')
ransom = input().strip().split(' ')
answer = ransom_note(magazine, ransom)
if(answer):
    print("Yes")
else:
    print("No")
