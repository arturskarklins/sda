# implementing lambdas as funciton and using them
# not a good practice, avoid it, use "normal" functions with def
func = lambda x, y: x + y

print(func(3, 4))
print(func(4, 7))

# lambda with if/else as ternary operator
func = lambda x: True if x % 2 == 0 else False


# sort list by elements second char
profiles = ['bob', 'anna', 'tom', 'tim']
profiles.sort(key=lambda x: x[1])
print(profiles)

# map with "hello {}" prefix each element in list
print(list(map(lambda x: f'hello {x}', profiles)))

# filter only persons which profile starts with "t"
print(list(filter(lambda x: x.startswith('t'), profiles)))

# smaple of reduce
import functools
print(functools.reduce(lambda x, y: x + y, profiles))
# 1 - x=bob, y=anna, return bobanna;
# 2 - x=bobanna, y=tom, return bobannatom;
# 3 - x=bobannatom, y=tim, return bobannatomtim;

# get min and max out of tuples, with multi elements
tuples_numbers = [(2, 3), (4, 1), (5, 7), (6, 3)]
print(min(tuples_numbers, key=lambda x: x[0] + x[1]))
print(max(tuples_numbers, key=lambda x: x[1]))
