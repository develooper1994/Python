def string_length(mystring):
	if isinstance(mystring,(int,float)):
		raise("Sorry integers don't have length")
	else:
		return len(mystring)

print('string_length("selam")',string_length("selam"))
print('string_length("33")',string_length("33"))
print('string_length("33")',string_length(33))
print('string_length("33")',string_length(33.496))