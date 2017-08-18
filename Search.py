Stringy = '''
Suyash: Why are you wearing your pajamas?
Atul: [chuckles] These aren't pajamas! It's a warm-up suit.
Suyash: What are you warming up for Bro..!!?
Atul: Stuff.
Suyash: What sort of stuff?
Atul: Super-cool stuff you wouldn't understand.
Suyash: Like sleeping?
Atul: THEY ARE NOT PAJAMAS!
'''
print(Stringy)

def countWord(word,st):
    st = st.lower()
    count = st.count(word)
    return print(word + ' repeats ' + str(count) + ' times')

print('What word do you want to search for?')
userWord = input()
countWord(userWord,Stringy)
      


#Atul Mishra
#SRM Univ.