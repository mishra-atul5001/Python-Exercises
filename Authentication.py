print('My First Authentication Program....!!')
print('Please enter your username:')
username = input()
#username is Suyash or Kishan
if username == 'Suyash' or username =='Kishan':
    print('Welcome' + username) 
    print(' Please enter your password')
    password = input()
    if username == 'Suyash' and password == 'shukla':
        print('ACCESS GRANTED')
    elif username == 'Kishan' and password == 'Mokho':
        print('ACCESS GRANTED')
    else:
        print('Incorrect Password!')
        print('ACCESS DENIED')
else:
    print('No such username!')
    print('ACCESS DENIED')

    


#Atul Mishra
#SRM Univ.