x = 2

try:
  if not type(x) is str:
    raise TypeError('Only strings are allowed.')
except NameError:
  print('Error means something is probably undefined.')
except ZeroDivisionError:
  print('Please do not divide by zero.')
except Exception as error:
  print(error)
else:
  print('No errors.')
finally:
  print("I'm going to print with or without an error.")