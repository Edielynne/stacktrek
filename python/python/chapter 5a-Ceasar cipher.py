word = input()
cipher = int(input())
array_word = []
array_cipher = []
ciphered_word = ""


for x in word:
    if x.isalpha() == True:
        array_cipher.append(ord(x) + cipher)
    else:
        array_cipher.append(x)
    
for i in array_cipher:
    if str(i).isnumeric() == True:
        if i <= 122:
            array_word.append(chr(i))
        else:
            i = (i-122) + 96
            array_word.append(chr(i))
    else:
        array_word.append(i)


ciphered_word = "".join(array_word)

print (ciphered_word)
