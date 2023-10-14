# Initialize an empty list to store 10 numbers
numbers = []


# Function to display the current list
def display_list():
    print("Current list:", numbers)


# Function to add a number to the end of the list
def add_number():
    num = float(input("Enter a number to add to the end of the list: "))
    numbers.append(num)
    display_list()


# Function to remove the first occurrence of a specific number
def remove_number():
    num = float(input("Enter a number to remove from the list: "))
    if num in numbers:
     numbers.remove(num)
    print(f"{num} has been removed from the list.")
    else:
    print(f"{num} is not in the list.")
    display_list()

    # Function to calculate the sum of all numbers in the list


def calculate_sum():
    total = sum(numbers)
    print("Sum of all numbers:", total)


# Function to find the min and max value in the list
def find_min_max():
    if len(numbers) == 0:
        print("The list is empty.")
    else:
        min_value = min(numbers)
        max_value = max(numbers)
        print("Minimum value:", min_value)
        print("Maximum value:", max_value)


# Function to sort the list in descending order
def sort_descending():
    numbers.sort(reverse=True)
    display_list()


# Function to create a sublist based on user input
def create_sublist():
    user_input = input(
        "Enter 'index' to create a sublist based on an index or 'item' to create a sublist based on an item: ")
    if user_input == 'index':
        index = int(input("Enter the index to start the sublist: "))
        sub_list = numbers[index:]
        print("Sublist:", sub_list)
    elif user_input == 'item':
        item = float(input("Enter an item to create a sublist: "))
        sub_list = [num for num in numbers if num == item]
        print("Sublist:", sub_list)
    else:
        print("Invalid input.")


# Main program loop
while True:
    print("\nOptions:")
    print("a) Add a new number to the end of the list")
    print("b) Remove the first occurrence of a specific number from the list")
    print("c) Calculate the sum of all the numbers in the list")
    print("d) Find the min and max value of the list")
    print("e) Sort the list in descending order")
    print("f) Create a sub list based on user input")
    print("q) Quit")

    choice = input("Enter your choice: ").lower()

    if choice == 'a':
        add_number()
    elif choice == 'b':
        remove_number()
    elif choice == 'c':
        calculate_sum()
    elif choice == 'd':
        find_min_max()
    elif choice == 'e':
        sort_descending()
    elif choice == 'f':
        create_sublist()
    elif choice == 'q':
        break
    else:
        print("Invalid choice. Please select a valid option.")

# End of the program
print("Goodbye!")
