# 4. Create a program that defines a function for sorting a list of names in alphabetical order.
# Allow the user to enter a list of names, and use the sorting function to display the names
# in sorted order.
def sort_names(names):
  """Sorts a list of names in alphabetical order.

  Args:
    names: A list of names.

  Returns:
    A list of names sorted in alphabetical order.
  """

  names.sort()
  return names

def main():
  """Prompts the user to input a list of names and displays the names in sorted order."""

  # Get the list of names from the user
  names = input("Enter a list of names, separated by commas: ").split(",")

  # Sort the names
  sorted_names = sort_names(names)

  # Display the sorted names
  print("The sorted names are:", sorted_names)

if __name__ == "__main__":
  main()
