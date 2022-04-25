# --- Day 2: Dive! ---
# What do you get if you multiply your final horizontal position by your final depth?

input_dictionary = {'forward': 0, 'down': 0, 'up': 0}
# input_file = open("sample_input_02.txt","rt")
input_file = open("puzzle_02.txt","rt")

# depth, aim = 0; threw the error as below. I will have to understand why.
# TypeError: cannot unpack non-iterable int object

depth = 0 
aim = 0

for line in input_file:
  key, value = line.split()
  if key == 'forward':
    depth += int(value) * aim
  input_dictionary[key] += int(value)
  aim = input_dictionary['down'] - input_dictionary['up']


horizontal_position = input_dictionary['forward']
print(horizontal_position)

final_position = horizontal_position * depth
print(final_position)

input_file.close()