'''
https://www.hackerrank.com/challenges/2d-array/problem?isFullScreen=true

'''
def hourglassSum(arr):
    # Write your code here
    max_val = -9 * 9
    for i in range(1, 5):
        for j in range(1, 5):
            cur_val = arr[i][j] + sum(arr[i-1][j-1:j+2]) + sum(arr[i+1][j-1:j+2])
            if max_val < cur_val:
                max_val = cur_val
    return max_val


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
