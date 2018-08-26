from pprint import pprint

L1 = [1,2,3]
L2 = [4,5,6,7]
L3 = [8,9]
L4 = [10,11,12,13,14]
L5 = [15,16,17,18]
L6 = []
L7 = [19,20,21,22]
L8 = [23]

jaggedArray = []

jaggedArray.append(L1)
jaggedArray.append(L2)
jaggedArray.append(L3)
jaggedArray.append(L4)
jaggedArray.append(L5)
jaggedArray.append(L6)
jaggedArray.append(L7)
jaggedArray.append(L8)

for i in jaggedArray:
      for k, v in enumerate(i):
            print(k, " ", v)

        











