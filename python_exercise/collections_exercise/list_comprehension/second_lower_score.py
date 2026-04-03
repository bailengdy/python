if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        students.append([input(), float(input())])

    second = sorted({score for _, score in students})[1]
    for name in sorted(name for name, score in students if score == second):
        print(name)