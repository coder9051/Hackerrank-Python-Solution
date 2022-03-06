if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for i in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    s = 0
    for i in student_marks[query_name]:
        s = s +i
        av = s/3
    print("%.2f"%av)
