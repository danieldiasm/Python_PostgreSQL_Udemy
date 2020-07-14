from database import create_table, add_entry, get_entries

menu = """Please select one of the following options:
1) Add new entry for today.
2) View Entries.
3) Exit.

Your selection:
"""

def prompt_new_entry():
    content = input("What have you learned today? ")
    date = input("Enter the date: ")
    add_entry(content, date)

def view_entries(entries):
    for entry in entries:
        print(f"{entry['date']}\n{entry['content']}\n\n")
welcome = "Welcome to the Programming Diary App"
create_table()

print(welcome)
user_input = input(menu)
# Walrus operator or assignment expressionm only Py 3.8 or greater
# while (user_input := input(menu)) != "3":
while user_input != "3":

    if user_input == "1":
        prompt_new_entry()
    elif user_input == "2":
        view_entries(get_entries())
    else:
        print("Invalid option, please try again")
    user_input = input(menu)