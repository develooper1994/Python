import json
from difflib import SequenceMatcher  # finding difference in strings, SequenceMatcher gives a ratio
from difflib import get_close_matches #getting most similar word

data=json.load(open("data.json")) #'r' mode is default
print("type(data): ",type(data))
print("data['rain'']: ",data["rain"])
print('SequenceMatcher(None,"rainn","rain").ratio()',SequenceMatcher(None,"rainn","rain").ratio())
print('get_close_matches("rainn",["help,pyramid","rain"])',get_close_matches("rainn",["help,pyramid","rain"]))
print('get_close_matches("rainn",data.keys())',get_close_matches("rainn",data.keys()))
print('get_close_matches("rainn",data.keys())[0]',get_close_matches("rainn",data.keys())[0]) #most similar is first elemetn

def translate(w):
    w=w.lower()
    if w in data:
        return data[w] # access values
    elif w.title() in data:  # if user entered "texas" this will check for "Texas" as well.
        return data[w.title()]
    elif w.upper() in data:  # in case user enters words like USA or NATO
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys()))>0:
        yn= input( "Did you mean %s instead?Enter Y if yes or N if no:" % get_close_matches(w, data.keys())[0] ).lower()
        if yn in ['y','ye','yes','Y']:
            return data[ get_close_matches(w, data.keys())[0] ]
        elif yn in ['n','no','N']:
            return "The word doesn't exist, Please do double check it"
        else:
            return "we didn't understand your entry."
    else:
        return "The word doesn't exist. Please double check it."
word=input("Enter Word: ")
output=translate(word)
#print(output) #prints python list we don't want to see like that at output

if type(output)==list:
    for w in output:
        print(w)
else:
    print(output)

