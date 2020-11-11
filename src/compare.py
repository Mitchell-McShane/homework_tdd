# compare.py
def compare(num_1, num_2):
    return f"{num_1} is greater than {num_2}"

def compare(num_1, num_2):
    # ADDED
    if num_1 < num_2:
        return f"{num_1} is less than {num_2}"
    #
    return f"{num_1} is greater than {num_2}"

def compare(num_1, num_2):
    # SAME
    if num_1 == num_2:
        return f"numbers are the same"
    # 
    if num_1 < num_2:
        return f"{num_1} is less than {num_2}"
    return f"{num_1} is greater than {num_2}"

# Refactoring
def compare(number_1, number_2):
    if number_1 == number_2:
        return f"numbers are the same"
    elif number_1 < number_2:
        return f"{number_1} is less than {number_2}"
    else:
        return f"{number_1} is greater than {number_2}"