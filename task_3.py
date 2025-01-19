import random
friends= ["Samiha", "Sajid", "Rifai"]

print(random.choice(friends)) #one way

res=random.randint(0,2)
print(friends[res])