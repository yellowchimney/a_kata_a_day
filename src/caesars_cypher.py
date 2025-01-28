def counter_intelligence(encrypted_str):
    decrypted_message = ''
    if len(encrypted_str) == 0:
        return decrypted_message
    secret_message = encrypted_str.upper()
    shift = ord('X') - ord(secret_message[-1])
    for char in secret_message:
        if char.isupper():
            decrypted_message += chr((ord(char) + shift - 65)%26 +65)
        else:
            decrypted_message += char
        
    return decrypted_message


def encrypter(message):
    secret_message = ''
    for char in message:
        if char.isupper():
            secret_message += chr((ord(char) - 5 +65)%26 +65)
        else:
            secret_message +=char
    return secret_message 