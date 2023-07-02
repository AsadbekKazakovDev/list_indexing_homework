def main(list_num):
    """
    A list of numbers consisting of several elements is given. Return the largest between the first and last elements.
    Args:
        list_num (list): parameter
    Returns:
        int: return answer
    """
    if len(list_num) == 0:
        return None

    largest = list_num[0]
    index = 1

    while index < len(list_num):
        if list_num[index] > largest:
            largest = list_num[index]
        index += 1

    return largest
list_num=[4, 32, 1, 4, 3]
print(main(list_num))