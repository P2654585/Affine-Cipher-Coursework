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
    arr_alphabet = list(string.ascii_uppercase) # ['A', 'B', 'C'...]
    arr_plainText = list(map(lambda x: x.upper(),plainText)) #separated & converted to upper#
    length_plainText = len(arr_plainText) #length of plaintext
    
    for x in range (length_plainText):
        y=arr_alphabet.index(arr_plainText[x]) # searching for the index of given character
        affine_output = (((key_a * y) + key_b) % 26) #formula for affine cipher
        #print(x,affine_output,arr_plainText[x], ord(arr_plainText[x])) #used for debugging
        encrypted_output.append(arr_alphabet[affine_output]) #create a new arrau from the chosen letters
        
    encrypted_output = "" .join(encrypted_output) #combine everything in the array without delimiter
    arr_plainText_raw = "" .join(arr_plainText) #combine everything in the array without delimiter
    print("Your Input was '" + arr_plainText_raw + "'")
    print("Your generated cipher text is: ",encrypted_output)
    main() #call menu

def decrypt(cipherText, key_a, key_b):
    try:
        decrypted_output=[] #create new array
        arr_alphabet= list(string.ascii_uppercase) #create alphabet list
        arr_cipherText = list(map(lambda x: x.upper(),cipherText)) 
        
        length_cipherText = len(arr_cipherText)
        multiplicative_Inverse = pow(key_a, -1, 26) #using pow function to get multiplicitive inverse
        for x in range(length_cipherText):
            y=arr_alphabet.index(arr_cipherText[x])
            affine_output = ((multiplicative_Inverse*(y-key_b)) % 26)
            #print(x,affine_output,arr_cipherText[x], ord(arr_cipherText[x])) #used for debugging
            decrypted_output.append(arr_alphabet[affine_output]) #
            
        arr_cipherText_raw = "".join(arr_cipherText)
        decrypted_output = "".join(decrypted_output)
        print("Your ciphertext was '" + arr_cipherText_raw + "'") #combine everything in the array without delimiter
        print("Your decrypted output is '" + decrypted_output + "'") #combine everything in the array without delimiter
        main()
    except ValueError:
        print("Error, Unable to decrypt correctly! REASON: key_a is not prime | Returning to menu... ") #error handling
        main()


def main(): 
    while True:
        try: #try input

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
                print("Exiting the program...")
                quit()
        except ValueError: #Error handle if not in range
            print("Error, you did not select one of the displayed choices, try again!")
        else:
            quit()

main() #runs the program
    
