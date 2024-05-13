# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from datetime import datetime  # https://www.w3schools.com/python/python_datetime.asp

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    if not hasattr(print_hi, "counter"):
        print_hi.counter = 0  # it doesn't exist yet, so initialize it
    print_hi.counter += 1

    # datetime object containing current date and time
    now = datetime.now()
    print(f'{print_hi.counter:3} {now} Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
    print(f'{print_hi.counter:3} {now} Bye, {name}')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    print_hi("Linux")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
