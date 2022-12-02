input_txt = open('./inputs/1.txt')

inventories = []

elf_index = 0
current_elf_calories = 0

for calories in input_txt.readlines():
    if calories == '\n':
        inventories.append(current_elf_calories)
        current_elf_calories = 0
        continue
    current_elf_calories += int(calories)

# First Half Answer
print(max(inventories))

# Second Half Answer
inventories.sort(reverse=True)
print(sum(inventories[:3]))