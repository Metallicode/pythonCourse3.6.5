L = [3,9,5,1,8,6,7,4,2]

def visualizer(indx, length, symb):
      ls = [symb for x in range(0, length)]
      ls[indx] = int(not symb)
      return tuple(ls)

def partition(myList, start, end):
      pivot = myList[end]
      index = start
      for i in range(start, end):
            print(myList, f"\tpivot is: {pivot}")
            print(visualizer(i, len(myList), 1))
            print(visualizer(index, len(myList), 0))
            if myList[i] <= pivot:
                  myList[i], myList[index] = myList[index], myList[i]
                  print(f"swaped  {myList[i], myList[index]}\t new index is {index+1}")
                  index += 1

      myList[index], myList[end] = myList[end], myList[index]
      print(f">>>swaped  {myList[index], myList[end]}, return index {index}")
      print(myList)
      return index

def QuickSort(myList, start_Index, end_Index):
      if start_Index<end_Index:
            new_Pivot_Index = partition(myList, start_Index, end_Index)
            print(f"{myList[start_Index:new_Pivot_Index]}  < {myList[new_Pivot_Index]} < {myList[new_Pivot_Index+1:end_Index+1]}")
            QuickSort(myList, start_Index, new_Pivot_Index-1)
            QuickSort(myList, new_Pivot_Index+1, end_Index)

def QuickSortCaller(lst):
      QuickSort(lst, 0, len(lst)-1)

print(L, "\n")
QuickSortCaller(L)
print(L)
