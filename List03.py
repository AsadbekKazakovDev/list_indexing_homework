def main(list1,list2):
    """
    lists list1 and list2 are given. Add them (combine) and return.
    Args:
        list1 (list): parameter
        list2 (list): parameter
    Returns:
        list: return answer
    """
    list3 = list1+list2
    return list3
list1,list2 = [1, 2, 3, 4, 5],[6, 7, 8, 9, 10] 
print(main(list1,list2))