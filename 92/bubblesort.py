L = [45,7,32,5,3,3,5,6,78,4,3,456,76,6]

for i in range(0, len(L)-1):
      for j in range(0, (len(L)-1) -i):
            if L[j] > L[j+1]:
                  L[j], L[j+1] = L[j+1], L[j]

print(L)
