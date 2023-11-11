def read_file(file_name):
    """ Reads in a file.

    Function:
        1. Open and read the given file into a variable using the File read()
           function
        2. Print the contents of the file
        3. Return the contents of the file

    Args:
        file_name: the name of the file to be read

    Returns:
        string: contents of the given file.
    """
    with open(file_name) as file:
        file_content = file.read()
        print(file_content)
        return file_content
    

def read_file_into_list(file_name):
    """ Reads in a file and stores each line as an element in a list

    Function:
        1. Open the given file
        2. Read the file line by line and append each line to a list
        3. Return the list

    Args:
        file_name: the name of the file to be read

    Returns:
        list: a list where each element is a line in the file.
    """
    with open(file_name) as file:
        file_list = []
        for line in file.readlines():
            file_list.append(line)
        return file_list


def write_first_line_to_file(file_contents, output_filename):
    """ Writes the first line of a string to a file.

    Function:
        1. Get the first line of file_contents
        2. Use the File write() function to write the first line into a file
           with the name from output_filename

        We determine the first line to be everything in a string before the
        first newline ('\n') character.

    Args:
        file_contents: string to be split and written into output file
        output_filename: the name of the file to be written to
    """
    ### WRITE SOLUTION HERE
    if "\n" in file_contents:
        first_line = file_contents[:file_contents.index("\n")]
    else:
        first_line = file_contents
    new_file = open(output_filename,"w")
    new_file.write(first_line)
    new_file.close()


def read_even_numbered_lines(file_name):
    """ Reads in the even numbered lines of a file

    Function:
        1. Open and read the given file into a variable
        2. Read the file line-by-line and add the even-numbered lines to a list
        3. Return the list

    Args:
        file_name: the name of the file to be read

    Returns:
        list: a list of the even-numbered lines of the file
    """
    even_numbered_lines = []
    with open(file_name) as file:
        x = 1
        for line in file.readlines():
            if x % 2 == 0:
                even_numbered_lines.append(line)
            x +=1
        return even_numbered_lines


def read_file_in_reverse(file_name):
    """ Reads a file and returns a list of the lines in reverse order

    Function:
        1. Open and read the given file into a variable
        2. Read the file line-by-line and store the lines in a list in reverse order
        3. Print the list
        4. Return the list

    Args:
        file_name: the name of the file to be read

    Returns:
        list: list of the lines of the file in reverse order.
    """
    file_list = []
    reverse_list = []
    with open(file_name) as file:
        for line in file.readlines():
            file_list.append(line)
        for x in range(len(file_list)):
            reverse_list.append(file_list[(len(file_list) - (x + 1))])
        print(reverse_list)
        return reverse_list

'''
Here are some sample commands to help you run/test your implementations.
Feel free to uncomment/modify/add to them as you wish.
'''
def main():
    file_contents = read_file("sampletext.txt")
    print(read_file_into_list("sampletext.txt"))
    write_first_line_to_file(file_contents, "online.txt")
    print(read_even_numbered_lines("sampletext.txt"))
    print(read_file_in_reverse("sampletext.txt"))

if __name__ == "__main__":
    main()