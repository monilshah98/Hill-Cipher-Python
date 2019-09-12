from math import *
import numpy as np
from os import *

a = list(input("Enter key: "))
b = list(input("Enter message: "))


lenKY=ceil(sqrt(len(a)))
lenpt=ceil(sqrt(len(b)))



def matcal(lengthkey,lenplain, ceilky):
    column = 0 
    if(lenplain%2==0):
    
            column = lenplain/ceilky;
            return int(ceil(column))
            
        
    
    else:
    
        lenplain+=1;
        column = lenplain/ceilky;
    return int(column)
        
    
column1 = matcal(len(a),len(b),lenKY)


km = [[0]*lenKY for i in range(lenKY)]
ptm = [[0]*column1 for i  in range(lenKY)]
cpm = [[0]*column1 for i in range(lenKY)]



z=97
for i in range(lenKY*lenKY):
    if((lenKY*lenKY)!=len(a)):
        a.append(chr(z))
        z=z+1


#Generate Key Matrix
def getkeymatrix(key):
    k = 0;
    for i in range(lenKY):
        for j in range(lenKY):
            km[i][j] = ord(a[k])%97
            k+=1
  
    


#Generate Cipher Matrix
def encrypt(plaintext):
    for i in range(lenKY):
        for j in range(column1):
            cpm[i][j] = 0
            for x in range(lenKY): 
                cpm[i][j] += (km[i][x] * ptm[x][j]) 
            cpm[i][j] = cpm[i][j] %26
    return cpm


def HillCipher(message, key): 
  
    # Get key matrix from the key string 
    getkeymatrix(a) 

    # Generate vector for the message
    mat_b=ptm
    for i in range(len(b)):
        mat_b[i%lenKY][floor(i/lenKY)] = ord(b[i]) % 97


    # Following function generates 

    # the encrypted vector
    cpm = encrypt(ptm)

    # Generate the encrypted text from the encrypted vector 
    cpt = []
    for i in range(column1):
        for j in range(lenKY):
            cpt.append(chr(cpm[j][i] + 97)) 


    # Finally print the ciphertext 
    print("Ciphertext: ", "".join(cpt))


def main(): 
  
    HillCipher(b, a)

if __name__ == "__main__": 
    main() 


