#File handling program
# will call functions to break words
def break_words(stuff):
    """This function will break words"""
    # 3 quotes will also be used as a comment
    words = stuff.split(' ')
    return words

def sort_words(words):
    return sorted(words)

def print_first_word(words):
    first_word = words.pop(0)
    print(first_word)

def print_last_word(words):
    last_word = words.pop(-1)
    print(last_word)

def sort_sentence(sentence):
    return sorted(sentence)

def print_first_and_last(words):
    firstWord = words.pop(0)
    lastWord = words.pop(-1)
    print('first word is ', firstWord , 'last word is ', lastWord)

def print_first_and_last_sorted(words):
    sorted(words)
    first_Word = words.pop(0)
    last_Word = words.pop(-1)
    print('first word after sorting is ', first_Word , 'last word AFTER sorting is ', last_Word)