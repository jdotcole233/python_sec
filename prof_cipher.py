import string

def caesar(text, shift, alphabets):

    def shift_alphabet (alphabet):
        return alphabet[shift:] + alphabet[:shift]

    ma = map(shift_alphabet, alphabets)
    shifted_alphabets = tuple(ma)
    final_alphabet = ''.join(alphabets)
    final_shifted_alphabet = ''.join(shifted_alphabets)
    table = str.maketrans(final_alphabet, final_shifted_alphabet)
    t = text.translate(table)
    return t



plain_text = "This is a new test, Hello World!"
print(caesar(plain_text, 7, [string.ascii_lowercase, string.ascii_uppercase, string.punctuation]))