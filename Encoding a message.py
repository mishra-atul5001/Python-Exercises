#Write down an alphabet
alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m',
    'n','o','p','q','r','s','t','u','v','w','x','y','z']
#print(alphabet)
print('Provide the message you want to encrypt?')
inputString = input()
inputString = inputString.lower()
print('What shift do you want to use? Left/Right')
shift = int(input())

transAlphabet = {}
x = random.randInt(1,50)

for i in range(0,26):
    letter = alphabet[i]
    #key in dict           #enters value into dict
    transAlphabet[letter]=alphabet[(i+shift)%x]
    #this line is not necessary but it is nice to print
    #the whole dictionary in order 
    print(alphabet[i] + ':' + transAlphabet[letter])

#notice the standard print does not print the dictionary in order
print(cypherText)

#Atul Mishra
#SRM Univ.
