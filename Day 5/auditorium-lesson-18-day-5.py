target = int(input()) # Enter a number between 0 and 1000
# 🚨 Do not change the code above ☝️

# Write your code here 👇
even_number = 0 
for number in range(0, target + 1, 2):
  even_number += number
print(f"{even_number}")