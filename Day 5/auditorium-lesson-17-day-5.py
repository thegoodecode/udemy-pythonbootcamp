# Input a list of student scores
student_scores = input().split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

# Write your code below this row 👇
sorted_scores = sorted(student_scores, reverse=True)

highest_score = sorted_scores[0]

print(f"The highest score in the class is: {highest_score}")


#------------------------------------------------------------------------------

# Solution given:

# Input a list of student scores
student_scores = input().split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

# Your code below this row 👇
highest_score = 0
for score in student_scores: #looping through every score in the list of student_scores
  if score > highest_score: #if the score is higher than the set highest_score (=0) then keep that as highest score. Keeps looping until the list is finished and sets the then highest score as highest_score
    highest_score = score
    # print(highest_score)

print(f"The highest score in the class is: {highest_score}")

