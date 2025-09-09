
# range function will from a to b-1. If u want to include even b, do b+1
sum = 0
for i in range(1, 101):
    sum += i
    
print(sum)

# Step or skip in pattern. In the below we are skipping by 2
for i in range(1, 20, 2):
    print(i)