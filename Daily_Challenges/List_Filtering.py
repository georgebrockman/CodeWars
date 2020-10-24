def filter_list(l):
    """ Return a new list with the strings filtered out """
    new_list = [] # assign a new list variable
    # use for loop to loop through the elements in the list and check type is integer
    for i in range(len(l)):
        if type(l[i]) == int:
            # if int, append new_list
            new_list.append(l[i])
    # return the new_list
    return new_list
