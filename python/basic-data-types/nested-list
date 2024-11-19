lowest = float('inf')
runnerup = float('inf')
students = []

if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        student = [name, score]
        students.append(student)
        if score < lowest:
            runnerup, lowest = lowest, score
        elif lowest < score < runnerup:
            runnerup = score

target = [x for x in students if x[1] == runnerup]
target.sort()

for x in target:
    print(x[0])
