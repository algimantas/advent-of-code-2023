def first_digit(str):
    for char in str:
        if char.isdigit():
            return int(char)
    return 0

def last_digit(str):
    return first_digit(str[::-1])

with open('input.txt', 'r') as file:
    lines = file.readlines()

sum = 0

for line in lines:
    sum += first_digit(line) * 10 + last_digit(line)

print(sum)
