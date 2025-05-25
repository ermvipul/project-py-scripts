student_heights = input("Input a list of student heights\n").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

total = 0
cnt = 0
for student_height in student_heights:
    total += student_height
    cnt += 1
avg_height = round(total / cnt)

print(total)
print(cnt)
print(avg_height)