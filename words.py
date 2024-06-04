# def print_upper_words(strArray):
#     for str in strArray :
#       if str[0]=='h' or str[0] == 'y': 
#         print(str.upper())

#
def print_upper_words(strArray, must_start_with):
    """Given list of strings, return the words that starts with 'h' or 'y' and convert them to the upper words.
    """      
    for str in strArray:
        if str[0].lower() in must_start_with:
            print(str.upper())

print_upper_words(["hello", "hey", "goodbye", "yo", "yes"],
                   must_start_with={"h", "y"})