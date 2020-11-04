def is_prime(num):
  """ Returns whether a number is Prime or not """
  # first prime number is 2 by definition, therefore anything less is False
  if num <= 0 or num == 1:
      return False
  # theres only one even number, therefore all evens will not be prime
  i = 2
  # using a while loop to make sure the sqrt of num is <= 2
  # could tidy this up by importing the sqrt function from the Math module
  while (i <= num ** 0.5 ):
      if num % i == 0:
          return False
      i += 1
  return True
