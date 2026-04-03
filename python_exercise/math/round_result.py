def average(array):
    # your code goes here
    distinct_array = set(array)
    return round(sum(distinct_array) / len(distinct_array), 3)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)