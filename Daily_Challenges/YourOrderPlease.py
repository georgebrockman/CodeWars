import operator
def order(sentence):
    """ Returns the input string in the order of the numbers inside each word """
    # set variable toReturn as an empty string
    toReturn = ""
    # split the string up into seperate words (.split()) [returns a list]
    sentence = sentence.split()
    # create a dictionary with 1-9 as keys
    dict = {'1':'None', '2':'None', '3': 'None', '4':'None', '5': 'None', '6': 'None', '7':'None', '8':'None', '9':'None'}
    # loop through the list of words
    for word in sentence:
        # loop through the characters in each element
        for char in word:
            # if char is a digit and an integer less or equal to nine update value of dict to word
            if(char.isdigit() and int(char) <= 9):
                dict[char] = word
    # sort the dictionary into numberical order
    # .items returns the key value pairs as tuples
    sorted_dict = sorted(dict.items())
    # loop through the tuples
    for sort in sorted_dict:
        # if index one does not equal one add value to toReturn plus a space
        if(sort[1] != 'None'):
            toReturn = toReturn +sort[1] + " "
    # update the toReturn value by removing the last space at the end
    toReturn = toReturn[:-1]
    # return the string
    return toReturn
