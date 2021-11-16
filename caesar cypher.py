def shift_amount(i):
    # Will determine the shift, taking into account the length of the alphabet
    return i % 26


def encrypt(text, required_shift):
    out_string = ""
    text = text.lower()
    for char in text:
        if char not in alphabet:
            out_string = out_string + char
        else:
            alpha_index = alphabet.find(char)
            out_string = out_string + alphabet[shift_amount(alpha_index + required_shift)]
    return out_string


alphabet = "abcdefghijklmnopqrstuvwxyz"
input_text = input("Please write the text to be coded")
input_code = int(input("Please insert the number to be used as a cypher"))

result = encrypt(input_text, input_code)
print(result)