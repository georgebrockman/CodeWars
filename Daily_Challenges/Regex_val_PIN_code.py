# import the regex module
import re
def validate_pin(pin):
    """ Return True if the PIN string is four or six digits, else return false """
    # use an if statement and the fullmatch function to check pin has four or six digits exactly
    if re.fullmatch("\d{4}|\d{6}", pin):
        return True
    else:
        return False
