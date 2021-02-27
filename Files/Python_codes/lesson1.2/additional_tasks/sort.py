arr = [4, 5, 3, 6, 2]

def my_sort(arr):
    for i in range(1,len(arr)):
        if(arr[i-1] > arr[i]):
            j = i
            while(arr[j] < arr[j-1]):
                if(j!=0):
                    arr[j], arr[j-1] = arr[j-1], arr[j]
                    j -= 1
                else:
                    break

my_sort(arr)
print(arr)

my_str = ["cd", "az", "fq", "qh"]

def my_sort(arr):
    for i in range(1,len(arr)):
        if(arr[i-1] > arr[i]):
            j = i
            while(arr[j] < arr[j-1]):
                if(j!=0):
                    arr[j], arr[j-1] = arr[j-1], arr[j]
                    j -= 1
                else:
                    break

my_sort(my_str)
print(my_str)
