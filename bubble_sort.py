#bubble sort algorithm
def bubbleSort(array):
	isSorted=False
	while(not isSorted):
		isSorted=True
		for i in range(0,len(array)-1):
			if array[i]>=array[i+1]:
				x=array[i]
				array[i]=array[i+1]
				array[i+1]=x
				isSorted=False
	return array


arr=input("Enter your array:").split()
for i in range(0,len(arr)):
	arr[i]=int(arr[i])
print(arr)
print(bubbleSort(arr))

