# Create a program that takes a user&#39;s input string and performs following string operations.
# The program should ask the user to input a string, then let user select an operation to
# manipulate the string and display the outcome at the end of program.
i=(input("enter the given string: "))
print("-----MENU-----"
      "\na. Capitalize the String"
      "\nb. Reverse the String"
      "\nc. Display the Length of the String"
      "\nd. Find the Specific word in a String"
      "\ne. Replace a Specific word with a new word"
      "\nf. Extend the String")
ans=input("Enter the option: ")

if ans =="a":
      print(" Capitalize the String is:\n",i.upper())
elif ans == "b":
      print("Reverse the String is:\n",i.i[::-1])
elif ans =="c":
      print("Display the Length of the String is:\n",i.len(i))
elif ans =="d":
      word=input("enter the word: ")
      print("the word find at index:\n",i.find(word))
elif ans == "e":
    a = input("Enter Original : ")
    b = input("Enter Modified : ")
    nw = i.replace(a,b)
    print("The Replacing of Specific word with a new word :")
    print(f"Original = {i} \nModified = {nw}")
elif ans=="f":
    c= input("enter the string to be added: ")
    print("the exten of the string is:\n",i+c)
else:
    print("invalid option")




