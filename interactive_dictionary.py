'''
   Author: Naveen B N
   Aug 18 - 2017
   Interactive dictionary 
   Input :- Pre-defined (data.json) mapping of word to definition
   Output :- Provide meaning for word input.
	     Suggestions based on user input.
'''

import json
#import difflib
from difflib import get_close_matches

data = json.load(open("data.json"))

def interactive_dictionary(word_input):
    word_input = word_input.lower()
    if word_input in data:
        return data[word_input]
    elif len(get_close_matches(word_input, data.keys())) > 0:
        response = input("Did you mean %s instead ?" % get_close_matches(word_input, data.keys())[0])
        if response == "Y":
            return data[get_close_matches(word_input, data.keys())[0]]
        elif response == "N":
            return "Word doesn't exist. Double check."
        else:
            return "Not able to recognize the input"
    else:
        return "word doesn't exist. Double check."

word_input = input("Enter a word:")
output = interactive_dictionary(word_input)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
