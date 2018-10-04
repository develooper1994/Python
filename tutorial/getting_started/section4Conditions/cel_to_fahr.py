def cel_to_fahr(c):
	if c<-273.15:
		raise "That temperature doesn't make sense!"
	else:
		f = c * 9/5 + 32
		return f
print(cel_to_fahr(-273))
print(cel_to_fahr(-273.4))
print(cel_to_fahr(-274))