if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    first = second = -100
    for num in list(arr):
        if num > first:
            second = first
            first = num
        elif second < num < first:
            second = num
    print(second)

# Best Solution
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    print(sorted(set(arr))[-2])
