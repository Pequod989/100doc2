student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)): 
    student_scores[n] = int(student_scores[n])
print(student_scores)

# Min and max functions
# print(max(student_scores))
# print(min(student_scores))

# Dummy scores so we don't have to type them in each time
student_scores = [78, 65, 89, 55, 91, 64, 89]

# loop through list of high scores to find highest one
high_score = 0
for score in student_scores:
    if score > high_score:
        high_score = score
        
print(f"The highest score in the class is: {high_score}")   