
# Get student heights and display them.
student_heights = input("Input a list of student heights").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

# count length of list function
total_height = 0
for height in student_heights:
    total_height += height
#print(total_height)

# calculate sum of list
number_of_students = 0
for student in student_heights:
    number_of_students += 1
#rint(number_of_students)

# calculate average and dsiplay it
average_height = total_height // number_of_students

print(round(average_height))

# check if code works
# print("len:" , len(student_heights))
# print("sum: ", sum(student_heights))
# print("Average: ", round(sum(student_heights)/len(student_heights)))