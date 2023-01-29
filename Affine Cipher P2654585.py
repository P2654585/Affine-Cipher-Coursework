#Affine Cipher P2654585

#1.take plaintext -> convert to uppercase
#2. take keys, key a and key b.
#3. use formula y = a * x + b
#4. output to user.

import string

#y = a * x + b (mod 26)

def encrypt(plainText, key_a, key_b):
    
    
    print("text") #test
    encrypted_output=[]
    arr_alphabet = list(string.ascii_uppercase) # ['a', 'b', 'c'...]
    #print(arr_alphabet) #26 chars
    arr_plainText = list(map(lambda x: x.upper(),plainText)) #separated & converted to upper#
    length = len(arr_plainText) #length of plaintext
    for x in range (length):
        #current = arr_plainText[x] #redundant
        affine_output = (((key_a * x) + key_b) % 26)
        print(x,affine_output,arr_plainText[x], ord(arr_plainText[x]))
        encrypted_output.append(arr_alphabet[affine_output])
        
        
        
        
        

    
    encrypted_output = "" .join(encrypted_output)
    arr_plainText_a = "" .join(arr_plainText)
    print("Your Input was '"+ arr_plainText_a + "'")
    print("Your generated cipher text is: ", encrypted_output)
    #print(encrypted_output)
    main()

def decrypt(cipherText, key_a, key_b):
    print("text")

def main():
    choice = 0

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
        exit()



main()
    
