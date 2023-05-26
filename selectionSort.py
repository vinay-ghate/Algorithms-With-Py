#SelectionSort is a sorting algorithm that sorts an array by repeatedly finding the minimum element (considering ascending order) from unsorted part and putting it at the beginning.
#The algorithm maintains two subarrays in a given array.
#1) The subarray which is already sorted.
#2) Remaining subarray which is unsorted.
#In every iteration of selection sort, the minimum element (considering ascending order) from the unsorted subarray is picked and moved to the sorted subarray.



def selectionSort(arr):  
    for i in range(len(arr)):
        min = arr[i]
        for j in range(len(arr)):
            if arr[j]>arr[i]:
                arr[i],arr[j] = arr[j],arr[i]
    
arr = [12,4,12,42,1,4,2,6,-2,54,-12,0,222]


selectionSort(arr)

print(arr)