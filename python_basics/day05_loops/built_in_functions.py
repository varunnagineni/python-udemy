student_scores = [50, 142, 160, 189, 96, 78, 90, 77, 65, 36]

print(sum(student_scores))

sum = 0
for score in student_scores:
    sum += score
    
print("Score: ", sum)

print(max(student_scores))

max_value = 0
for score in student_scores:
    if score > max_value:
        max_value = score
        
print(max_value)


