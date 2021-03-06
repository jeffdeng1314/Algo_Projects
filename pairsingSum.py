# Check if any of the pairing sum is the power of two and return numbers of possible pairs

#condition:
# i <= j and sum of i and j is the power of two

def pairingSum(arr):
    counter = 0

    for i in range(len(arr)):
        for j in range(i,len(arr)):
            if arr[i] <= arr[j]:
                s = arr[i] + arr[j]

                # use bitwise operation to get power of two without using math library
                if (s) >= 0 and (s & (s-1)) == 0:
                    counter += 1
    
    return counter

if __name__ == '__main__':
    
    n = [-1, -6, -1, 2, 8, 6, 3, 3, 2, -5, 6, 5, 0, -9, 5, 6, 4, 5, -9, 3]
    print('Numbers of possible pairing sums that has the power of two: ',pairingSum(n))