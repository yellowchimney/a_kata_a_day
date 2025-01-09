from preloaded import MORSE_CODE
"""
Function takes a string of dots and dashes and converts it to a string of words 
using morse_code dictionary. 
"""

def decode_morse(morse_code):
    list_of_words = morse_code.split("   ")
    decoded_message = []
    for word in list_of_words:
        temp = word.split()
        decoded_word = []
        for letter in temp:
            decoded_letter = MORSE_CODE[letter]
            decoded_word.append(decoded_letter)
        final_word = "".join(decoded_word)
        decoded_message.append(final_word)
    
    final_message = " ".join(decoded_message)
    return final_message.strip()
        