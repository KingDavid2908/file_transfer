print(sum(range(1, 5)))

def range_of(start_value, end_value): 
    list_of_values = []
    while start_value < end_value:
        list_of_values.append(start_value)
        start_value += 1
    return list_of_values


def sum_of(list):
    sum = 0
    for item in list:
        sum += item
    return sum

print(sum_of(range_of(1, 5)))