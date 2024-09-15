from collections import Counter


def num_students(students, sandwiches):
    count = Counter(students)
    total_students = len(students)

    for s in sandwiches:
        if count[s] == 0:
            return total_students

        count[s] -= 1
        total_students -= 1

    return total_students


def num_students_2(students, sandwiches):
    while students:
        if students[0] == sandwiches[0]:
            students.pop(0)
            sandwiches.pop(0)
        else:
            # move the student to the end of the queue
            students.append(students.pop(0))

        # breaking from the loop condition
        # if there's only a single student available but the sandwiches are still remaining
        if len(set(students)) == 1 and sandwiches[0] != students[0]:
            return len(students)

    return 0


# res = num_students([1, 1, 1, 0, 0, 1], [1, 0, 0, 0, 1, 1])
res = num_students_2([1, 1, 1, 0, 0, 1], [1, 0, 0, 0, 1, 1])
print(res)
