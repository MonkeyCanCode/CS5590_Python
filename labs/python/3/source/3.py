#!/usr/bin/python3
# Lab assignment 3: part 3

import collections
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.util import bigrams


def generate_word_tokens(text):
    """
    Generated lemmatized tokens for each word
    """
    lemmatizer = WordNetLemmatizer()
    return [lemmatizer.lemmatize(x.lower()) for x in word_tokenize(text) if x.isalpha()]

# Generate lemmatized tokens from input file
all_tokens = generate_word_tokens(open("input.txt").read())

# Generate all bigram from lemmatized tokens
all_bigrams = [bigram for bigram in bigrams(all_tokens)]

# Calcualte bigram frequency
print("=====Top 5 most frequent Bigram=====")
counter = {}
for bigram in all_bigrams:
    counter[bigram] = 1 if bigram not in counter else counter[bigram] + 1

# Top 5 most frequent bigram
output = collections.Counter(counter).most_common(5)
output_keys = set()
for key, value in output:
    print(key, "->", value)
    output_keys.add(key)

# Concatenate all sentences which contain top 5 most frequent biagram
print("=====Output=====")
output = ""
with open("input.txt") as infile:
    for line in infile:
        for sentence in sent_tokenize(line):
            current_key_set = set(bigram for bigram in bigrams(generate_word_tokens(sentence)))
            if output_keys & current_key_set:
                output += sentence + " "
                continue

print(output)
