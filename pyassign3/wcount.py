#Assignment3, word count
#韦宗乐, 1700011705
#2017.12.19

"""Module for word count

This module use several string and dictionary functions to count the most
common words in an url which point to a txt file, and output he topn (word
count), each in one line.
To use this module, open it in a command tool. It will show the way to
use if users do not input any parameters.
If users input an invalid parameter, it will return an error description."""


import string
import sys
from urllib.request import urlopen


def wcount(lines, topn=10):
    """count words from lines of text string, then sort by their counts
    in reverse order, output the topn (word count), each in one line. 

    Parameter lines: the text to count.
    Precondition: lines is a string

    Parameter topn: the numbers of the most common words to output. If not
    given, default is 10. 
    Precondition: topn is an int
    """
    wd_list = c_wd_list(lines)
    count_result = histogram(wd_list)
    sorted_result = sort_dict(count_result)
    print_result(sorted_result, topn)
    pass


def c_wd_list(s):
    """Returns: a word list, without punctuations

    This function change a string into word list, taking out punctuations.

    The value returned has type list.
    
    Parameter s: the text to be changed into a word list
    Precondition: s is a string
    """
    s = s.replace("-", ' ')
    wd_list = s.split()
    clear_wd_list = []
    
    for i in wd_list:
        i = i.strip(string.punctuation + string.whitespace)
        i = i.lower()
        clear_wd_list.append(i)
    
    return clear_wd_list


def histogram(alist):
    """Returns: a dictionary, which keys are words, values are frequencies.

    This function count all words appeared and save the result in a
    dictionary, which keys are words, values are their frequencies.
    
    The value returned has type dict.

    Parameter alist: the word list to count.
    Precondition: alist is a list.
    """
    d = dict()
    
    for c in alist:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    
    return d


def sort_dict(adict): 
    """Returns: a sorted list, which elements are tuples(value, key).

    This function create a list of items(value, key) of a dictionary,
    then sort the list in the order of values, from large to small.

    The value returned has type list.
    Parameter adict: the dictionary to sort.
    Precondition: adict is a dictionary
    """
    t = []
    for key, value in adict.items():
        t.append((value, key))
    
    t.sort(reverse=True)
    return t


def print_result(alist, topn):
    """Returns: None.

    This function output the topn (word count), each in one line. But if
    there are more than one words have the same frequency, this function
    may not output all of them.

    Parameter alist: the word list to print
    Precondition: alist is a list.

    Parameter topn: the numbers of the most common words to output. But it
    do not have a default, unlike topn in the function wcount.
    Precondition: topn is an int.
    """
    for (value, key) in alist[:topn]:
        print(key + ' ' * (15 - len(key)), value)


if __name__ == '__main__':

    if  len(sys.argv) == 1:
        print('Usage: {} url [topn]'.format(sys.argv[0]))
        print('  url: URL of the txt file to analyze ')
        print('  topn: how many (words count) to output. If not given, will output top 10 words')
        sys.exit(1)

    try:
        topn = 10
        if len(sys.argv) == 3:
            topn = int(sys.argv[2])
    except ValueError:
        print('{} is not a valid topn int number'.format(sys.argv[2]))
        sys.exit(1)

    try:
        with urlopen(sys.argv[1]) as f:
            contents = f.read()
            lines   = contents.decode()
            wcount(lines, topn)
    except Exception as err:
        print(err)
        sys.exit(1)
