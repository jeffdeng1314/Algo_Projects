# Insertion Sort

def non_decreasing(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        prev = i-1

        while key < arr[prev] and prev >= 0:
            arr[prev+1] = arr[prev]
            prev = prev - 1
        arr[prev+1] = key
        
    return arr


def non_increasing(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        prev = i-1

        while key > arr[prev] and prev >= 0:
            arr[prev+1] = arr[prev]
            prev = prev - 1
        arr[prev+1] = key
    
    return arr

def main():
    a = [31,41,59,26,41,58,1]

    print('Non Decreasing: ' + str(non_decreasing(a)))
    print('Non Increasing: ' + str(non_increasing(a)))


if __name__ == "__main__":
    main()
