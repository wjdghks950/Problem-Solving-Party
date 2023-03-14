'''
https://www.hackerrank.com/challenges/2d-array/problem?isFullScreen=true

'''

def hourglassSum(arr):
    # Write your code here
    r = 3
    sum_arr = []
    for ptr in range(4):
        for i in range(4): # Col index
            hrglass_sum = 0
            for j in range(3): # Row index
                hrglass_sum += sum(arr[ptr+j][i:i+r])
                if j == 1:  # Second row (leave out the 0th, 2nd col for sum)
                    hrglass_sum -= arr[ptr+j][i]
                    hrglass_sum -= arr[ptr+j][i+2]
            sum_arr.append(hrglass_sum)
    return max(sum_arr)
            
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
