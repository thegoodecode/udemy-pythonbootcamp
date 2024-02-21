import random

random_integer = random.randint(1, 10)
print(random_integer)


random_float = random.random() * 5
print(random_float)

love_score = random.randint(1, 100)
print(f"Your love score is {love_score}")


states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia"] 

states_of_america[1] = "Penniesalvania"

print(states_of_america)

states_of_america.append("Anneland")

print(states_of_america)