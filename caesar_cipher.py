def encrypt(plain_text, shift):
    result = ""

    for i in range(len(plain_text)):
        char = text[i]
        result += chr((ord(char) + shift - 65) % 26 + 65)

    return result


#text = "CEASER CIPHER DEMO"
#shift = 4

text = input("Enter text to be encrypted using Ceaser Cipher: ")
shift = int(input("Enter Number of shifts: "))

print("Plain text: ",  text)
print("Shift pattern:",  str(shift))
print("Cipher ", encrypt(text, shift))
