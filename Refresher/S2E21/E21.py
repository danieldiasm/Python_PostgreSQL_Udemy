# List Comprehension

numbers = [1, 2, 3, 4, 5]
doubled = [num * 2 for num in numbers]
print(doubled)

friends = ["Rolf", "Sam", "Samantha", "Samuel", "Jessica"]

starts_s = [friend for friend in friends if friend.startswith('S')]

print(starts_s)

print(f'friends: {id(friends)}, starts_s: {id(starts_s)}')