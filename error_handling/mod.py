def modulus_four(n):
	r = n % 4
	if r == 0:
		print("Multiple of 4")
	elif r == 1:
		print("Remainder 1")
	elif r == 2:
		print("Remainder 2")
	elif r == 3:
		print("Remainder 3")
	else:
		assert False, "This should never happen"

# Notes on Assertion Errors:

# Use assertions to check that your 
# implementation is correct 

# In other words, check if the 
# programmer has made a mistake 

# Do not use assertions to validate arguments