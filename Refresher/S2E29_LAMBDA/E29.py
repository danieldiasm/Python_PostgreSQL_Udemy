# 1- Using a lambda without a name
print((lambda x, y: x + y)(3,5))

# 2- Giving a name to a lambda function
mult = lambda x, y: x * y
# Then calling it
print(mult(2, 2))

# 3- Using a Map function
def double(x):
    return x * 2

sequence = [1, 2, 3, 4, 5]

# List comprehension is usually faster than Map
doubled_1 = [double(j) for j in sequence]
# MAP runs over each element of sequence applying as an argument on double
doubled_2 = map(double, sequence)

# 4 - LAMBDA!
# With list comprehension, quite confusing
doubled_3 = [(lambda x: x*2)(x) for x in sequence]
# With Map, is much easier to understand map(function_to_apply, list_to_run_through)
doubled_4 = list(map(lambda x: x*2, sequence))
# We must convert it into a list, otherwise we'll have a map object

print(doubled_1)
print(doubled_2)
print(doubled_3)
print(doubled_4)

