def MinToHours(minutes):
	hours=minutes/60
	return hours
def SecToHours(minutes):
	hours=MinToHours( minutes )/60 
	return hours
print("MinToHours:",MinToHours(30)); print(type( MinToHours(70) ))
print("SecToHours:",SecToHours(7200)); print(type( SecToHours(7200) ))

def minsecToHours(second,minutes):
	return MinToHours(minutes) + SecToHours(second)
print("minsecToHours(7200,70)",minsecToHours(7200,70))

def minsecToHours(second,minutes=70): #default argument
	return MinToHours(minutes) + SecToHours(second)
print("minsecToHours(7200)",minsecToHours(7200))

def minsecToHours(minutes=70,second): #default argument at first parameter
	return MinToHours(minutes) + SecToHours(second)
	#print("minsecToHours(7200)",minsecToHours(7200)) #SyntaxError: non-default argument follows default argument



