def main(list1,i):
    """
    A list of several elements is given. i Return the item in the index.
    Args:
        list1 (list): parameter
        i (int): parameter
    Returns:
        list: return answer
    """
    return list1[i]
list1,i = [5,3,'a',1,2],3
print(main(list1,i))