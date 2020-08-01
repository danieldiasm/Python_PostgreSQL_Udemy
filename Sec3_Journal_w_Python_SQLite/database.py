import sqlite3

connection = sqlite3.connect("data.db")
# We can change the way SQLite assemble the returning results
# connection.row_factory = sqlite3.Row
# Then the print results from a cursor will look like this:
# print(f"{entry['date']}\n{entry['content']}\n\n")
# getting as a dict we can look for a K:V pair, but it is slower


def create_table():
    with connection:
        connection.execute("CREATE TABLE IF NOT EXISTS entries(content TEXT, date TEXT);")

def add_entry(entry_content, entry_date):
    with connection:
        connection.execute(
            "INSERT INTO entries VALUES (?, ?);", (entry_content, entry_date)
        )

def get_entries():
    # - More obvious way:
    # cursor = connection.cursor()
    # cursor.execute("SELECT * FROM entries;")
    # - Shorter way:
    cursor = connection.execute("SELECT * FROM entries;")
    # cursor.fetchone() -> Get the first or next one
    # cursor.fetchall() -> Gives back a dict with all the results
    return cursor
