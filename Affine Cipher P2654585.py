#Affine Cipher P2654585

#1.take plaintext -> convert to uppercase
#2. take keys, key a and key b.
#3. use formula y = a * x + b
#4. output to user.

import string
import contextlib

#y = a * x + b (mod 26)


def encrypt(plainText, key_a, key_b):
    encrypted_output=[]
    arr_alphabet = list(string.ascii_uppercase) # ['a', 'b', 'c'...]
    arr_plainText = list(map(lambda x: x.upper(),plainText)) #separated & converted to upper#
    length_plainText = len(arr_plainText) #length of plaintext
    
    for x in range (length_plainText):
        y=arr_alphabet.index(arr_plainText[x]) # searching for the index of given character
        affine_output = (((key_a * y) + key_b) % 26) #formula for affine cipher
        print(x,affine_output,arr_plainText[x], ord(arr_plainText[x])) #test
        encrypted_output.append(arr_alphabet[affine_output]) #create a new arrau from the chosen letters
        
    encrypted_output = "" .join(encrypted_output)
    arr_plainText_raw = "" .join(arr_plainText)
    print("Your Input was '"+ arr_plainText_raw +"'")
    print("Your generated cipher text is: ", encrypted_output)
    main() #call menu

def decrypt(cipherText, key_a, key_b):
    try:
        decrypted_output=[]
        arr_alphabet= list(string.ascii_uppercase)
        arr_cipherText = list(map(lambda x: x.upper(),cipherText))
        
        length_cipherText = len(arr_cipherText)
        multiplicitive_Inverse = pow(key_a, -1, 26)
        for x in range(length_cipherText):
            y=arr_alphabet.index(arr_cipherText[x])
            affine_output = ((multiplicitive_Inverse*(y-key_b)) % 26)
            print(x,affine_output,arr_cipherText[x], ord(arr_cipherText[x]))
            decrypted_output.append(arr_alphabet[affine_output])
            
        arr_cipherText_raw = "".join(arr_cipherText)
        decrypted_output = "".join(decrypted_output)
        print("Your ciphertext was '"+ arr_cipherText_raw+"'")
        print("Your decrypted output is '" + decrypted_output +"'")
        main()
    except:
        print("Error, Unable to decrypt correctly!") #suppression error handling
        main()






def main():
    choice = 0 #assign
    choice = int(input("Enter Option\n1. Encrypt\n2. Decrypt\n3. Exit the Program\nChoice: "))

    if choice == 1:
        plainText=str(input("Enter plaintext: "))
        key_a = int(input("Enter key_a: "))
        key_b = int(input("Enter key_b: "))
        encrypt(plainText, key_a, key_b)
    elif choice == 2:
        cipherText=str(input("Enter ciphertext: "))
        key_a = int(input("Enter key_a: "))
        key_b = int(input("Enter key_b: "))
        decrypt(cipherText, key_a, key_b)
    elif choice == 3:
        print("exit")
        quit()

main()
    
