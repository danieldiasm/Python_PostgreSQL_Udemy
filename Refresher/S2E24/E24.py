def greeting():
    print("Welcome to the age in seconds program!");

def user_age_in_seconds():
    user_age = int(input("Insert your age:"))
    user_age_in_seconds = user_age * 365 * 24 * 60 * 60
    print(f'Your age in seconds is: {user_age_in_seconds}')

# Yes, I've just did it. Just for the lolz!
print(f'{greeting()}')
# Yes it prints that strange None
user_age_in_seconds()
