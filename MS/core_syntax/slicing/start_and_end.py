# Enter your code here. Read input from STDIN. Print output to STDOUT

S = input()
k = input()
l = len(k)
found = False

for i in range(len(S) - l + 1):
    if S[i:i+l] == k:
        if not found:
            found = True
        print((i, i + l - 1))

if not found:
    print((-1, -1))