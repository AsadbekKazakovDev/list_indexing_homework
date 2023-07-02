def main(list1):
    """
    A list of several elements is given. True if all items are the same, otherwise return False.
    Args:
        list1 (list): parameter
    Returns:
        bool: return answer
    """
    if len(list1) == 0:
        return True
    
    first_item = list1[0]
    index = 1
    
    while index < len(list1):
        if list1[index] != first_item:
            return False
        index += 1
    
    return True
list1=[1, 1, 1, 1, 7]
print(main(list1))
list1=[1, 1, 1, 1, 1]
print(main(list1))