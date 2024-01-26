string = input("Enter a string: ")
stringCopy = string.lower()
reversedString = stringCopy[::-1]
reversedString = reversedString.capitalize()
print(f"The string {string} was reversed to {reversedString}.")