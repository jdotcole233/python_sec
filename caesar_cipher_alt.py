def encrypt(plain_text, shift):
    result = ""

    for i in range(len(plain_text)):
        char = plain_text[i]
        uni = ord(char)
        #print(i , " ", uni)
        #print("\n")
        if (char.isupper()):
            result += chr((uni + shift - 65) % 26 + 65)
        else:
            result += chr((uni + shift - 97) % 26 + 97)

    return result


def decrypt(cipher_text, shift):
    plain_text = ""

    for i in range(len(cipher_text)):
        char = cipher_text[i]
        uni = ord(char)

        if (char.isupper()):
            plain_text += chr((uni + shift  + 65) % 26 + 65)
        else:
            plain_text += chr((uni + shift +  97) % 26 + 97)

    return plain_text


#text = "CEASER CIPHER DEMO"
#shift = 4

text = input("Enter text to be encrypted using Ceaser Cipher: ")
shift = int(input("Enter Number of shifts: "))

cipher = encrypt(text, shift)

print("Plain text: ",  text)
print("Shift pattern:",  str(shift))
print("Cipher ", cipher)
print("decrypt ", decrypt(cipher, shift))
