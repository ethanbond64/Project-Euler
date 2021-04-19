import os
import numpy as np
import time 

common_words = ['the','be','to','of','and','in','that','have','it','for','not','on','with','as','you','do','at','this']

def decrypt(ciphertext,key):
    plaintext = np.zeros(len(ciphertext),dtype='int')
    keylen = len(key)
    for i in range(int(len(ciphertext)/keylen)):
        plaintext[keylen*i:(keylen*i)+keylen] = np.bitwise_xor(ciphertext[keylen*i:(keylen*i)+keylen],key)

    return plaintext

file = open(os.path.split(os.path.abspath(__file__))[0] + '/p059_cipher.txt','r')

ciphertext = [int(s) for s in file.read().split(',')]

# Key = 3 lowercase letters
# Brute force all combinations SLOW AND NAIVE
# a-z = 97-122
max_words = 0
max_key = ()
max_ascii = []
max_ptext = ''
t0 = time.time()
for a in range(97,123):
    for b in range(97,123):
        for c in range(97,123):
            key = (a,b,c)
            # print(key)
            int_plaintext = decrypt(ciphertext,key)
            plaintext = ''.join(map(chr,int_plaintext))
            
            local_count = 0
            for word in common_words:
                local_count += plaintext.count(word)
            
            if local_count > max_words:
                
                max_words = local_count
                max_key = key
                max_ascii = int_plaintext
                max_ptext = plaintext

t1 = time.time()

print(max_key)
print(max_ptext)
print('ANSWER: ',sum(max_ascii))
print('Time elapsed: ',t1-t0)