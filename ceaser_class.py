import string
import time
import os


def characters_all():
    return [string.ascii_lowercase, string.ascii_uppercase, string.punctuation]

def reformatCharacters(chars, shift):
    return [x[shift:] + x[:shift] for x in chars]


def caesar_encryption (text, shift = 4):
    characters_as_list = characters_all()
    characters_as_string = ''.join(reformatCharacters(characters_as_list, shift))
    character_trans = str.maketrans(''.join(characters_as_list), characters_as_string)
    return text.translate(character_trans)



def read_file(file_name):
    lines = []
    try:
        print("Preparing file content for encryption...")
        exisiting_file = open(file_name, 'r')
        begin_read = True
        while begin_read:
            line = exisiting_file.readline()
            if not line:
                begin_read = False
            else:
                lines.append(line)
        exisiting_file.close()
    except IOError:
        print("File Not found")
    # finally:
    #     if exisiting_file:
    #         exisiting_file.close()
    
    print("Completed file preparation...")
    return lines

def write_file(file_name, contents, shift):
    file_parts = os.path.splitext(file_name)
    encrypted_file_name = file_parts[0] + "_encrypted" + file_parts[1]

    try:
        if not bool(contents):
            print("Content of file seems empty")
            return
        
        print("Creating encrypted file")
        create_enc_file = open(encrypted_file_name, 'a')

        for line in contents:
            cipher = caesar_encryption(line, shift)
            create_enc_file.write(cipher)
        
        print("Encrypted file name [{}] completed".format(encrypted_file_name))
        create_enc_file.close()
    except IOError:
        print("File can not be created")
    # finally:
    #     if create_enc_file:
    #         create_enc_file.close()


def encrypt_file(file_name, shift):
    contents = read_file(file_name)
    write_file(file_name, contents, shift)


def main():
    program = True
    while program:
        try:
            print("Encrypt from:\n1. File\n2. Terminal\n3. Terminate")
            choice =  int(input("choice > "))
            time.sleep(0.5)
            if choice == 1:
                try:
                    # dir_listing = os.getcwd()
                    # print("Select file using the number")
                    # for i in range(len(dir_listing)):
                    #     print("{}. {}".format(i, dir_listing[i]))
                    file_name = input("Enter file name: ")
                    sk = int(input("Enter number of shifts expected (default=4): "))
                    encrypt_file(file_name, sk)
                except ValueError:
                    print("Wrong value entered")
            elif choice == 2:
                try:
                    text = input("Enter something nice: ") 
                    sk = int(input("Enter number of shifts expected (default=4): "))
                except:
                    print("wrong key entered")
                cipher = caesar_encryption (text, sk)
                time.sleep(0.5)
                print("Cipher Text generated: {}".format(cipher))
                print("Share key {} securely with third party".format(sk))
                print("\n")
            elif choice == 3:
                print("Ending program. Good bye!")
                time.sleep(0.5)
                program = False
            else:
                print("wrong choice. Try Again")
        except ValueError:
            print("Wrong value inputted.")
        except KeyboardInterrupt:
            print("\nEnding program. GoodBye!")
            program = False




if __name__ == '__main__':
    main()




