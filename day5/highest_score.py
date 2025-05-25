student_scores = input("input a list of students!!\n").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

cnt = 0
for score in student_scores:
    if score > cnt:
        cnt = score

print(cnt)