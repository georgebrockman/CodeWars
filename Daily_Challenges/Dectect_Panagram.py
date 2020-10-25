import string

def is_pangram(s):
    # create an empty set
    set = []
    # convert all letters in string to lowercase
    s = s.lower()
    # loop through the input string
    for i in s:
        # if element in s is in the alphabet
        if i.isalpha():
            # if element is not yet in list, add to list
            if i not in set:
                set.append(i)
    # return true if length of set is 26
    return len(set) == 26
