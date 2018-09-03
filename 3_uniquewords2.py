#
import string
import sys
import collections

# empty dictionary
words = collections.defaultdict(int)
# all characters to ignore, returns a string with unwanted characters
strip = string.whitespace + string.punctuation + string.digits + "\'"
for filename in sys.argv[1:]:
    # iterate over each line in opened file mentioned in cmdl args
    for line in open(filename):
        # traversing each word in whitespace splitted string
        for word in line.lower().split():
            # clean up the word from unwanted characters
            word = word.strip(strip)
            if len(word) > 2:
                # fill up dictionary avoiding exception
                words[word] += 1

for word in sorted(words):
    # print dict content
    print("'{0}' occurs {1} times".format(word, words[word]))