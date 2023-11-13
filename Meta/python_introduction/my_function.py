print(sum(range(1, 5)))

def range_of(*args): 
    """
    Function:
        This function creates a list with the first value being the start value, and the difference between the first and second value in the list is the end value. The list ends before the end value.
    Arguments:
        1. The start value would be first item on the list created. By default it is 0.
        2. The end value would be the value the last item on the list should not reach up to.
        3. The step is the differnce between the second item on the list and first item om the list. By default it is 1
    Returns:
        A list that contains a range of values starting from the start value but less than the end value.  
    """
    if len(args) == 1:
        end_value = args[0]
        start_value = 0
        step = 1
    elif len(args) == 2:
        start_value = args[0]
        end_value = args[1]
        step = 1
    elif len(args) == 3:
        start_value = args[0]
        end_value = args[1]
        step = args[2]
    elif len(args) > 3:
        raise TypeError(f"range expected at most 3 arguments, got {len(args)}")
    elif len(args) < 1:
        raise TypeError(f"range expected at least one argument, got {len(args)}")

    list_of_values = []
    while start_value < end_value:
        list_of_values.append(start_value)
        start_value += step
    return list_of_values


def sum_of(*args):
    """
    Function:
        Adds all the items in the list. 
    Arguments:
        Recieves a list as an argument
    Returns:
        Returns an integer equal to the sum of all the items in the list.
    """
    if len(args) == 1:
        iterable = args[0]
    elif len(args) == 2:
        iterable = args[0]
        arg = args[1]
        iterable.append(arg)
    elif len(args) < 1:
        raise TypeError(f"sum_of() takes at least 1 positional argument ({len(args)} given)")
    elif len(args) > 2:
        raise TypeError(f"sum_of() takes at most 2 arguments ({len(args)} given)")


    sum = 0
    for item in iterable:
        sum += item
    return sum

print(sum_of(range_of(1, 5)))
print(sum_of([1, 4, 7, 11]))