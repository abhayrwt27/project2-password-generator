import random
import string

gen="yes"
print("Password Generator")

#generate password if user enter yes
while (gen == "yes"):
    length = int(input("Enter length of password to be generated: "))

    if (length < 6):
        #password of length less than 6 can not be generated
        print("Password too short")

    else:
        # if user wants to include symbols or not
        symb=input("Include symbols?(yes/no)")
        # if user wants to include number or not
        dgt=input("Include numbers?(yes/no)")

        if (symb == "yes" and dgt == "yes"):
            chars = string.ascii_letters + string.digits + string.punctuation

        elif (symb == "no" and dgt == "yes"):
            chars = string.ascii_letters + string.digits

        elif (symb == "yes" and dgt == "no"):
            chars = string.ascii_letters + string.punctuation

        else:
            chars = string.ascii_letters
            print("Not a strong password.")

        password=""

        # generating password of input length
        for i in range(length):
            password += random.choice(chars)

        # printing generated password
        print("Generated Password: ", password)

    # asking to generate one more password
    gen = input("Generate Another Password? (yes/no):")