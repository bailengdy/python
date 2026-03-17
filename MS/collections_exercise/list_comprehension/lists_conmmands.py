# Solution 1
if __name__ == '__main__':
    N = int(input())
    res = []
    for _ in range(N):
        action, *number = input().split()
        line = list(map(int, number))
        match action:
            case "print":
                print(res)
            case "append":
                res.append(line[0])
            case "insert":
                res.insert(line[0], line[1])
            case "remove":
                res.remove(line[0])
            case "pop":
                res.pop()
            case "reverse":
                res.reverse()
            case "sort":
                res.sort()


# Solution 2
# 用字典存函数（function dispatch / 函数映射）
if __name__ == '__main__':
    N = int(input())
    res = []

    commands = {
        "append": lambda x: res.append(x[0]),
        "insert": lambda x: res.insert(x[0], x[1]),
        "remove": lambda x: res.remove(x[0]),
        "pop": lambda x: res.pop(),
        "reverse": lambda x: res.reverse(),
        "sort": lambda x: res.sort()
    }

    for _ in range(N):
        action, *number = input().split()
        line = [int(x) for x in number]

        if action == "print":
            print(res)
        else:
            commands[action](line)