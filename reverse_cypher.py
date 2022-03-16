
#message = "This is program to explain reverse cipher"
message  = input("Enter a text to be encrypted:")
translated = ""
i = len(message) - 1

while i >= 0:
    translated = translated + message[i]
    i = i -1

print("The cipher text is: ", translated)
