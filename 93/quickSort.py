L = [3,9,5,1,8,6,7,4,2]


def QuickSort(myList, start_Index, end_Index):
      def partition(myList, start, end):
            pivot = myList[end]
            index = start
            for i in range(start, end):
                  if myList[i] <= pivot:
                        myList[i], myList[index] = myList[index], myList[i]
                        index += 1
            myList[index], myList[end] = myList[end], myList[index]
            return index

      if start_Index<end_Index:
            new_Pivot_Index = partition(myList, start_Index, end_Index)
            QuickSort(myList, start_Index, new_Pivot_Index-1)
            QuickSort(myList, new_Pivot_Index+1, end_Index)

print(L, "\n")
QuickSort(L, 0,  len(L)-1)
print(L)
