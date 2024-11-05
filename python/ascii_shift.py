'''
https://www.codewars.com/kata/56e9ac87c3e7d512bc001363/python

Ascii Shift Encryption/Decryption

The goal of this kata is to create a very simple ASCII encryption and decryption. 
The encryption algorithm should shift each character's charcode by the character's 
current index in the string (0-based).

The input strings will never require to go outside of the ASCII range.

Example:
   p | a | s | s | w | o | r | d  Plaintext
 + 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7  Shift (add)
   p | b | u | v | { | t | x | k  Ciphertext
 The decryption should reverse this:

   p | b | u | v | { | t | x | k  Ciphertext
 - 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7  Shift (subtract)
   p | a | s | s | w | o | r | d  Plaintext
'''

def ascii_encrypt(plaintext):
    
    return "".join(chr(ord(letter) + index) for index, letter in enumerate(plaintext))
    
def ascii_decrypt(encrypted):
    
    return "".join(chr(ord(letter) - index) for index, letter in enumerate(encrypted))

# Like I've said before, I love any chance for a one-liner.
