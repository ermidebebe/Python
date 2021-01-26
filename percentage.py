if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    sum=0
    if query_name in student_marks:
        for key in student_marks:
            if key==query_name:
                for sub in student_marks[key]:
                    sum+=sub
        print(format(sum/len(student_marks[key]),'.2f'))
