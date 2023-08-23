"""
Custom Wordle Solver

This module solves the word for any custom Wordle on mywordle.strivemath.com.
The URL of the custom Wordle includes a five character code at the end, which can then be
decrypted using the Vigenere cipher to reveal the word answer. The Vigenere cipher is a
method of encrypting alphabetic text by using a simple form of polyalphabetic substitution. 
Decryption requires knowledge of the keyword used during encryption, which in this case,
the keyword is WORDLE.

Functions:
    vigenere_decrypt(ciphertext, keyword):
        Decrypts a Vigenere cipher.
"""

KEY = "WORDLE"

def vigenere_decrypt(ciphertext, keyword):
    """
    Decrypts a Vigenere cipher.

    Args:
        ciphertext (str): The encrypted text to be decrypted.
        keyword (str): The keyword used for decryption.

    Returns:
        str: The decrypted text.
    """
    decrypted_text = ""
    keyword = keyword.upper()  # Convert keyword to uppercase for consistency
    keyword_length = len(keyword)

    for i, char in enumerate(ciphertext):
        if char.isalpha():
            keyword_shift = ord(keyword[i % keyword_length]) - ord('A')

            # Decryption logic for lowercase and uppercase letters
            if char.islower():
                decrypted_char = chr(((ord(char) - ord('a') - keyword_shift) % 26) + ord('a'))
            else:
                decrypted_char = chr(((ord(char) - ord('A') - keyword_shift) % 26) + ord('A'))

            decrypted_text += decrypted_char
        else:
            decrypted_text += char  # Keep non-alphabetic characters unchanged

    return decrypted_text

code = input("Enter the five characters at the end of the url: ")

print(vigenere_decrypt(code, KEY))
