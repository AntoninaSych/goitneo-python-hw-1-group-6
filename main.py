from datetime import datetime
import list_people
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# Приклад використання функції зі списком користувачів
users = [
    {"name": "Bill Gates", "birthday": datetime(1955, 10, 28)},
    {"name": "Steve Jobs", "birthday": datetime(1955, 2, 24)},
    {"name": "Mark Zuckerberg", "birthday": datetime(1984, 5, 14)},
    {"name": "Elon Musk", "birthday": datetime(1971, 6, 28)},
    {"name": "Tim Cook", "birthday": datetime(1960, 11, 1)},
]


list_people.get_birthdays_per_week(users)
list_people.get_birthdays_per_week(users)