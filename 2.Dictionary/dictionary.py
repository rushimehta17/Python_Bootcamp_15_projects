import json
from difflib import get_close_matches
"""
json to open json data file
from difflib get_close_matches to get close match
so that minor spelling error of user can be corrected
"""

data = json.load(open("2.Dictionary\data.json"))

def translate(word):
"""
    get the word from user,
    check in lower case for match,
    other wise check for title and then in uppercase.

    if there is minor smelling mistake that can be also corrected.
"""
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word , data.keys())) > 0 :
        print("did you mean %s instead" %get_close_matches(word, data.keys())[0])
        decide = input("press y for yes or n for no")
        if decide == "y":
            return data[get_close_matches(word , data.keys())[0]]
        elif decide == "n":
            return("pugger your paw steps on wrong keys ")
        else:
            return("You have entered wrong input please enter just y or n")
    else:
        print("pugger your paw steps on wrong keys")



word = input("Enter the word you want to search")
output = translate(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
