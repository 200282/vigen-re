
print("vigenere algorithm")

# 3%26 ==>  3/26=0   0*26+3=3 

def generate_key(plaintext, keyword):
    plaintext=plaintext.replace(" ", "")
    key = list(keyword)
    if len(plaintext) == len(key):
        return key
    else:
        for i in range(len(plaintext) - len(key)):
            key.append(key[i % len(key)])
    return "".join(key)




def vigenere_cipher_Enc(text, k):
    result = ""
    text=text.replace(" ", "")
    # Traverse the text  loop in text for each char
    for i in range(len(text)):
        
           char = text[i]
           key=k[i]
        
        
          # Encrypt uppercase characters    65+3-65=3%26=3+65=68(D)
           if char.isupper():
             result += chr(((ord(char)-65) + (ord(key) - 65)) % 26 + 65)
           # Encrypt lowercase characters
           elif char.islower():
             result += chr(((ord(char)-97) + (ord(key) - 97)) % 26 + 97)
           else:
             result +=''  # Non-alphabetic characters remain the same
    
    return result



def vigenere_cipher_Dec(text, k):
    result = ""
    text=text.replace(" ", "")
    # Traverse the text  loop in text for each char
    for i in range(len(text)):
        
           char = text[i]
           key=k[i]
            # Encrypt uppercase characters   ascii of A --> 65     
           if char.isupper():
                result += chr(((ord(char)-65) - (ord(key) - 65)) % 26 + 65)
            # Encrypt lowercase characters  ascii of a --> 97
           elif char.islower():
               result += chr(((ord(char)-97) - (ord(key) - 97)) % 26 + 97)
           else:
               result += ''  # Non-alphabetic characters remain the same
    
    return result

# Example usage

while 1:
    
  ch=input("if you want encrept enter EN if you want decrypt enter DE ")

  if ch=="EN":
    plain=input("enter your plaintext :")
    
    key = input("enter key : ")
   
    key=generate_key(plain,key)
    print(key)
    encrypted_text = vigenere_cipher_Enc(plain, key)
    print("Encrypted:", encrypted_text)


  elif ch=="DE":
     cipher=input("enter your ciphertext :")
     text = "sa"
     key = input("enter key : ")
     key=generate_key(cipher,key)
     decrypted_text = vigenere_cipher_Dec(cipher, key)
     print("decrypted:", decrypted_text)

  else :
     print("invalid input")
    
    
    
    
    
    
    
    
    
    
    
    
   
   
