from collections import Counter

def ransom_note(magazine, ransom):
    counter = 0
    ransom_dict = Counter(ransom)
    c = int(len(ransom))
    magazine_dict = Counter(magazine)
    
    for key in ransom:
        if ((key in magazine_dict) and (magazine_dict.get(key)>0)):
            magazine_dict[key] -= 1
            counter += 1
    if counter == c:return(True)
    else:return(False)
            
m, n = map(int, input().strip().split(' '))
magazine = input().strip().split(' ')
ransom = input().strip().split(' ')
answer = ransom_note(magazine, ransom)
if(answer):
    print("Yes")
else:
    print("No")
