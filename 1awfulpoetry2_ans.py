import sys
import random

#Declare part
articles = ["a", "the", "another", "one", "other", "precious", "brave", "determined", "cautious"]
subjects = ["cloud rapper", "misanthrope", "rock star", "bear", "mammal", "sloth", "devil"]
verbs = ["sang", "ran", "jumped", "attacked", "protected", "laughed", "cried", "died", "born"]
adverbs = ["loudly", "quietly", "badly", "carefully", "obviously", "deadly", "friendly", "smoothly"]

lines = 0
try:
    lines = int(sys.argv[1])
except IndexError:
    lines = 5
except ValueError as err:
    print(err)

#random.randint(x,y) choose between x and y inclusively
i = 0
while i < lines:
    if random.randint(0, 1) == 1:
        print(random.choice(articles), random.choice(subjects), random.choice(verbs), random.choice(adverbs))
    else:
        print(random.choice(articles), random.choice(subjects), random.choice(verbs))
    i += 1