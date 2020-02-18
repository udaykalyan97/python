#bubble sort algorithm
import time
def bubbleSort(arr):
    print ("##BubbleSort algorithm##")
    isSorted = False 
    while (not isSorted):
        isSorted = True 
        for i in range (0, len (arr) - 1):
            if arr[i] > arr[i + 1]:
                x = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = x
                isSorted = False 
        print (arr) 
        time.sleep(1) 
print ("enter the array:")
array=list(map(int,input().split()))
bubbleSort (array)
