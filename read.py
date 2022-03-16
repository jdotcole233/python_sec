input = open('file.txt', 'r')
print(input.read());


for line in input:
    print(line)



print("testing the read line")
print(input.readlines())

input.close()

