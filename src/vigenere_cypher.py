"""
The Vigenère cipher is a type of polyalphabetic substitution cipher. 
It uses a keyword to shift the letters of the plaintext.

The alphabet is shifted by the keyword, and the keyword is repeated as many times as needed.

The class takes a key and an alphabet as input.

The encode method takes a text and returns the encoded text.

The decode method takes a text and returns the decoded text.

Both methods ignore non-alphabetical characters.

"""

class VigenereCipher(object):
    def __init__(self, key, alphabet):
        self.key = key
        self.alphabet = alphabet
        self.shifts = [alphabet.index(char) for char in key]
    
    def encode(self, text):
        counter = 0
        encrypted = []
        for i,char in enumerate(text):
            if char not in self.alphabet:
                encrypted.append(char)
                counter+=1
            else:
                new_index = self.alphabet.index(char) + self.shifts[counter%len(self.key)]
                new_char = self.alphabet[new_index%len(self.alphabet)]
                counter+=1
                encrypted.append(new_char)
        return ''.join(encrypted)
    
    def decode(self, text):
        counter = 0
        decrypted = []
        for i,char in enumerate(text):
            if char not in self.alphabet:
                decrypted.append(char)
                counter+=1
            else:
                new_index = self.alphabet.index(char) - self.shifts[counter%len(self.key)]
                new_char = self.alphabet[new_index%len(self.alphabet)]
                counter+=1
                decrypted.append(new_char)
        return ''.join(decrypted)