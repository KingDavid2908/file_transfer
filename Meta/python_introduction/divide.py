class divide:
    """A class for dividing numbers"""

    def __init__(self, name, type, classification):
        self.name = name
        self.type = type
        self.classification = classification

    def __str__(self):
        return f"{self.name} is of type {self.type} and can be classified under {self.classification}."

    def divide_two_numbers(self, num_1, num_2):
        '''try and except block to handle division by zero'''
        self.num_1 = num_1
        self.num_2 = num_2
        try:
            return round(self.num_1 / self.num_2, 2)
        # Added an except block to handle ZeroDivisionError cases
        except ZeroDivisionError:
            # checks if the numerator is negative
            if self.num_1 < 0:
                return float("-inf")
            # checks if the numerator is positive
            elif self.num_1 > 0:
                return float("inf")
            else:
                raise ValueError("undefined")

    def check_number(self, number):
        self.number = number
        '''Checks for the type and changes it to be workable'''
        # checks if the number is a string
        if isinstance(self.number, str):
            # assigns a default value of False to variable that confirms a number is negative.
            number_is_negative = False
            # Checks if a number is negative
            if self.number[0] == "-":
                self.number = self.number[1:]
                # since the number is negative it becomes true.
                number_is_negative = True
            # tries to turn the str to a float
            try:
                self.number = float(self.number)
            # raises an error if the string cannot be converted to a float
            except ValueError:
                raise ValueError(f"The number should be a float.")
            except Exception as error:
                print("The error rasied was:\n", error)
                print("The class of the error is", error.__class__)
            # converts a previously negative number to negative
            if number_is_negative:
                self.number = (0 - self.number)
        # If number is not a string leave the number unchanged.
        else:
            self.number = self.number
        return self.number

    def check_and_divide_numbers(self, divisor=None, divider=None):
        '''This function checks the type of number and divides them when it is done'''
        self.divisor = divisor
        self.divider = divider
        # If divisor was not given it gives the divisor a value
        if self.divisor == None:
            number_1 = input("Enter a divisor: ")
        else:
            number_1 = self.divisor
        # Checks the number 1 to ensure the type is correct
        number_1 = self.check_number(number_1)
        # If the divider was not given it gives the divider a number
        if self.divider == None:
            number_2 = input("Enter a divider: ")
        else:
            number_2 = self.divider
        # Checks the number 2 to ensure the type is correct
        number_2 = self.check_number(number_2)
        # divides the two numbers
        return self.divide_two_numbers(number_1, number_2)

    def continue_division(self, division):
        '''This function acts like a loop to either or end the function'''
        self.division = division
        print(self.division)
        continue_d = input("Do you want to continue your division(y/n): ")
        # if user chooses yes it asks for user to select a mode
        if continue_d[0].lower() == "y":
            print("Do you want to set previous result as divisor or divider? ")
            print("1. Divisor")
            print("2. Divider")
            print("New Calculation")
            selection = input("Enter your choice: ")
            # When user chooses divisor it assigns the previous result as the divisor
            if selection == "1":
                new_division = self.check_and_divide_numbers(
                    divisor=self.division)
            # When user chooses divider it assigns the previous result as the divider
            elif selection == "2":
                new_division = self.check_and_divide_numbers(
                    divider=self.division)
            # When user chooses New calculation, it doesn't assign the previous result.
            else:
                new_division = self.check_and_divide_numbers()
            # Continues the division
            return self.continue_division(new_division)
        # It ends the loop since the user chose end.
        else:
            return "Done"

    def divide_numbers(self):
        """It divides two numbers and serve as a loop that asks user for data."""
        print("Enter numbers to divide:")
        division = self.check_and_divide_numbers()
        return self.continue_division(division)


if __name__ == "__main__":
    print(divide.divide_numbers())
