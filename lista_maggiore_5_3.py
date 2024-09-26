from random import random

def lunghezza_froci(v):
    lt = 0
    index = 0
    for r in range(len(v)):
        c3 = 0
        c5 = 0
        # Settiamo c3 e c5 se il primo numero della lista è 3 o 5
        if v[r] == 3:
            c3+=1
        elif v[r] == 5:
            c5+=1
        # Per ogni elemento succesivo a r
        for j in range(r+1, len(v)):
            if v[j] == 3:
                c3+=1
            elif v[j] == 5:
                c5+=1
        if c3 == c5:
            if len(v) - r > lt:
                lt = len(v) - r
        else:
            for x in range(len(v) -1, r, -1):
                if v[x] == 3:
                    c3-=1
                elif v[x] == 5:
                    c5-=1
                if c3 == c5:
                    temp = x - r
                    if temp > lt:
                        lt = temp
                    break
    print(index)
    return lt

# Codice che si esegue quando avviamo
array = []
for i in range(2000):
    array.append(int(random() * 10))
print(array)
print(lunghezza_froci(array))