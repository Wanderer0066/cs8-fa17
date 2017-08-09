#!/usr/bin/python3

# Here's a simple use of two dimensional lists. Here, we're going
# to keep track of 4 students' grades on 3 exams.
student_scores = [
  [68, 77, 98],
  [88, 86, 89],
  [91, 92, 94],
  [99, 89, 90]
]

# Loop over student_scores by index
for r in range(len(student_scores)):
    print('Student', r)
    total = 0
    for c in range(len(student_scores[r])):
        print('Score', c)
        total += student_scores[r][c]
    avg = total / len(student_scores[r])
    print('Avg: {:.2f}'.format(avg))

print('Current score', student_scores[2][1])
student_scores[2][1] = 93
print('After adjustment', student_scores[2][1])

# Here's a slightly modified version that doesn't use indices
# but rather just loops directly over the lists' items.
for s in student_scores:
    total = 0
    for sc in s:
        total += sc
    avg = total / len(s)
    print('Avg: {:.2f}'.format(avg))

print(student_scores)
