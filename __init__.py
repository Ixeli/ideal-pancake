# Text analyzer
# Analyzes a .txt (ASCII) fjle for letter frequencies, string and word counts.

import sys # For argument processing

if __name__!="__main__": # This is a CLI tool
    raise ImportError("This tool is not meant to be run as a module.")

abc=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'] # Do you know your ABC's?

def count_char_frequency(charlist,string): # Find frequencies of characters
    count_list=[] # In the beginning, there are no letters

    for i in range(0,len(charlist)):
        count_list.append(0) # Fill the list with zeroes

    for char in string.lower(): # Make sure the chars are lowercase
        if char in charlist: # Repeat on every char
            count_list[abc.index(char)]+=1 # Count up

    return count_list

def count_string_frequency(string_list): # Find frequencies of strings
    frequency_table={} # Empty frequency table

    for string in string_list: # Repeat for every string
        stringl=string.lower()
        if stringl in frequency_table:
            frequency_table[stringl]+=1 # Count up
        else:
            frequency_table[stringl]=1 # If it doesn't exist, make it exist

    return frequency_table

def count_words(string,dict): # Significantly harder than counting strings, because it checks the "dictionary" file
    list_strings=string.split() # Compile list of strings
    list_words=[] # Start with an empty list

    for string in list_strings: # Iterate over every string
        string=string.lower()
        if string in dict:
            list_words.append(string) # Add to list

    return list_words

args=sys.argv # Find CLI args

if '-h' in args: # If the -h flag is enabled
    with open('help.txt','r') as help_file: # Open help.txt
        print(help_file.read()) # Read it
        sys.exit() # Close the prostring

file_name=args[1] # File name is here, is not put in a try/except because it would fail anyway
with open(file_name,'r') as f: # Open main file
    txt=f.read() # Read it

dict=False # Dictionary mode is, by default, off.

try:
    if args[2]=='-d': # If the -d flag is enabled
        dict_name=args[3] # Set the location of the dictionary file
        dict=True
        with open(dict_name,'r') as dict_file: # Open dictionary
            dict_words=dict_file.read() # Read it
    else:
        raise ValueError("Invalid command-line option.") # It's your fault, not mine
except IndexError:
    pass

# Data printout
print("Size:",len(txt)) # Document size
print()

print("String count:",len(txt.split())) # Count all the strings
print()

print("Letter frequency distribution (letter -> counts):") # Letter frequency distribution, useful in cryptanalysis
for a in range(0,26):
    print(abc[a],"->",count_char_frequency(abc,txt)[a])
print()

print("String frequency distribution (string -> counts):") # String frequency distribution, also useful in cryptanalysis
for string in count_string_frequency(txt.split()):
    print(string,"->",count_string_frequency(txt.split())[string.lower()])
print()

if dict: # If dictionary mode is enabled, continue spitting out data
    print("Word count:",len(count_words(txt,dict_words)))
    print()

    print("Words per string:",len(count_words(txt,dict_words))/len(txt.split()))
    print()

    print("Word frequency distribution (word -> counts):")
    for word in count_string_frequency(count_words(txt,dict_words)):
        print(word,"->",count_string_frequency(txt.split())[word])
    print()

print("Done.")
