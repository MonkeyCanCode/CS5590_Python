#!/usr/bin/python3
# Lab assignment 1: part 2


def get_middle_word(sentence):
    """
    Get the middle word(s) of the sentence
    """
    words = sentence.strip().split()
    middle_pos = int(len(words) / 2)
    return words[middle_pos] if len(words) % 2 else words[middle_pos - 1:middle_pos + 1]


def get_longest_word(sentence):
    """
    Get the longest word of the sentence
    """
    words = sentence.strip().split()
    return max(words, key=len)


def get_reverse_sentence(sentence):
    """
    Get the sentence with reverse words
    """
    return " ".join(word[::-1] for word in sentence.strip().split())


# When input_sentence contains and old number of words, it will return only one word as middle words
input_sentence = "My name is Jacqueline Fernandez"
print("The middle word for [", input_sentence, "] is {", get_middle_word(input_sentence), "}")
# When input_sentence contains an even number of words, it will return two words as middle words
input_sentence = "My name is Jacqueline Fernandez Dsouza"
print("The middle words for [", input_sentence, "] are {", get_middle_word(input_sentence), "}")
# Get longest word
print("The longest word for [", input_sentence, "] is {", get_longest_word(input_sentence), "}")
# Get reversed word in the sentence
print("The reversed words [", input_sentence, "] are {",   get_reverse_sentence(input_sentence), "}")
