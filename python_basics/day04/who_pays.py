import random

# One way
friends = ["Abc", "Def", "Ghi", "Jkl", "Mno"]
random_friend = random.choice(friends)
print(random_friend)

# Other way
rand_int = random.randint(0, 4)
print(rand_int)
print(friends[rand_int])

print(len(friends))