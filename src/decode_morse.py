from preloaded import MORSE_CODE

"""
Function takes a string of bits ('0100100111010100001010') and converts it
to a string of dashes and dots ('.... . .-.. .-.. ---'). 
The key to decoding:
    "Dot" – is 1 time unit long.
    "Dash" – is 3 time units long.
    Pause between dots and dashes in a character – is 1 time unit long.
    Pause between characters inside a word – is 3 time units long.
    Pause between words – is 7 time units long.
The function should treat zeros in the beginning and in the end of the string.
The function should accomodate for variety of time units, as everyone types at a different speed.
"""

def find_rate(splits):
    rate_list = [len(string) for string in splits if string]
    return min(rate_list)

def decode_bits(bits):
    bits = bits.strip('0')
    print(bits)
    if len(bits)== 1:
        rate = 1
    else:
        if '0' not in bits:
            rate = len(bits)
        else:
            rate = min(find_rate(bits.split('0')), find_rate(bits.split('1')))
        
    meaningful_bits = ''.join(bits[i] for i in range(0,len(bits), rate))
    words = meaningful_bits.split('0000000') 
    decoded_message = []
    bits_to_chars = {'111': '-','1': '.'}
    for word in words:
        letters = word.split('000')
        decoded_word = []
        for letter in letters:
            decoded_letter_list = [bits_to_chars[char] for char in letter.split('0')]
            decoded_letter_string = ''.join(decoded_letter_list)
            decoded_word.append(decoded_letter_string)
        final_word = " ".join(decoded_word)
        decoded_message.append(final_word)
    
    final_message = "   ".join(decoded_message)
    return final_message
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
        