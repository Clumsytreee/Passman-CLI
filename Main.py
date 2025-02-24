import string

print("Welcome to Passman")
print("0:Encrypt / 1:Decrypt / 2:Fetch password / 3:Exit")


#input repeater
def cmd_chk():
    char = list(" " + string.punctuation + string.ascii_letters + string.ascii_lowercase + string.ascii_uppercase)
    key = " ~bZAMoDfOSTaDnTUMWjdwCPCuIvFVKHkhnm!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}NmqtlczwIgjAyplsPHGubykEEiKYatQWzLvxRFciGJxBeZhNsrYfqegdOJQVBXSoLUrXRp"
    
    i = 1
    while i < 10:
        cmd_lst = ["0", "1", "2", "3"]
        cmd = input("Enter command : ")
        for x in cmd_lst:
            #Encrypt
            if cmd == cmd_lst[0]:
                plain_text_input = input("Enter your pass : ")
                cipher_text = ""
                for letter in plain_text_input:
                    index = char.index(letter)
                    cipher_text += key[index]
                print(f"Your encrypted message : {cipher_text}")
                storing_value = input("Enter a unique index for current password : ")
                global update_passfile
                update_passfile = open("encrypted/passwords.txt", "a")
                update_passfile.write(f"{storing_value} : {cipher_text}\n")
                update_passfile.close()
                
                break
            #Decrypt
            elif cmd == cmd_lst[1]:
                cipher_text_input = input("Enter your cipher : ")
                plain_text = ""
                for letter in cipher_text_input:
                    index = key.index(letter)
                    plain_text += char[index]
                print(f"Your decrypted message : {plain_text}")
                break
            #Fetch Password
            elif cmd == cmd_lst[2]:
                index_value = input("Enter the unique index value : ")
                fetch_file = open("encrypted/passwords.txt", "r")
                res = {key.strip(): value.strip() for key, value in (line.split(':', 1) for line in fetch_file)}
                stored_cipher_txt = res.get(index_value)
                plain_txt = ""
                for letter in stored_cipher_txt:
                    index = key.index(letter)
                    plain_txt += char[index]
                print(f"Your decrypted message : {plain_txt}")
                break
            elif cmd == cmd_lst[3]:
                i = 11
cmd_chk()