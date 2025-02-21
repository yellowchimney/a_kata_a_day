"""
This function takes a text and returns the top 3 most frequent words.

It ignores non-alphabetical characters or uses them as delimiters. 
Words can contain apostrophes at any position (start, middle, end), 
but words can't contain only apostrophes.
"""

import re

def top_3_words(text):
    new_text = text.lower()
    split_text = re.split(r"[^a-z']", new_text)
    arr1 = [re.sub(r"[^a-z']", "", word) for word in split_text]
    count_dict = {word: arr1.count(word) for word in set(arr1) if any(char.isalpha() for char in word)}
    return  [key for key, _ in sorted(count_dict.items(), key=lambda item: item[1], reverse=True)[:3]]

