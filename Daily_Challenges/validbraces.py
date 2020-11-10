def validBraces(string):
    """ Return True if braces in string match correctly """
    # Use a while loop to check if closed braces in string
    while '{}' in string or '()' in string or '[]' in string:
        # replace closed brackets with empty string
        string=string.replace('{}','')
        string=string.replace('[]','')
        string=string.replace('()','')
    # if string is empty, returns True
    return string==''
