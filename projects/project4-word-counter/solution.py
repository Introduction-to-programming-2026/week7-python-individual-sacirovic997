# Project 4 - Word Counter
# Author: Sacirovic
# Date: 30.04.2026

sentence = input("Enter a sentence: ")
words = sentence.lower().split()

total_words = len(words)
total_chars = len(sentence.replace(" ", ""))

frequency = {}
for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

print(f"Total words: {total_words}")
print(f"Total characters (no spaces): {total_chars}")
print(f"Word frequency: {frequency}")
