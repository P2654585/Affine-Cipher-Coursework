#Affine Cipher P2654585

#1.take plaintext -> convert to uppercase
#2. take keys, key a and key b.
#3. use formula y = a * x + b
#4. output to user.

import string

#y = a * x + b (mod 26)

def encrypt(plainText, key_a, key_b):
    
    
    print("text")#
    encrypted_output=[]
    arr_alphabet = list(string.ascii_uppercase) # ['a', 'b', 'c'...]
    print(arr_alphabet) #26 chars
    arr_plainText = list(map(lambda x: x.upper(),plainText)) #separated & converted to upper#
    length = len(arr_plainText)
    for x in range (length):
        #current = arr_plainText[x]
        print(x,arr_plainText[x], ord(arr_plainText[x]))
        
        affine_output = (((key_a * x) + key_b) % 26)
        encrypted_output.append(arr_alphabet[affine_output])
        print(affine_output)
        

    
    
    print(arr_plainText)
    print(encrypted_output)

def decrypt(cipherText, key_a, key_b):
    print("text")

x = True

choice = int(input("Enter Option\n1. Encrypt\n2. Decrypt\n3. Exit the Program\nChoice: "))

if choice == 1:
    print("a")
    plainText=str(input("Enter plaintext: "))
    key_a = int(input("Enter key_a: "))
    key_b = int(input("Enter key_b: "))
    encrypt(plainText, key_a, key_b)
elif choice == 2:
    print("b")
elif choice == 3:
    print("exit")
    
