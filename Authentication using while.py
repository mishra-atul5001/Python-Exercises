

accessGranted = False
while accessGranted == False:
    dict = {'Suyash':'abc123','Kishan':'mokho','Radhe':'Maxx','Punnu':'#shreyashi'}
    print('Please enter your username')
    username = input()
    if username in dict:
        print('Hey Buddy' + username)
        print('Enter Password')
        password = input()
        #dict[username] gives the value as password
        if password == dict[username]:
            print('ACCESS GRANTED')
            accessGranted = True
        else:
            print('Incorrect Password!')
            print('ACCESS DENIED')
    else:
        print('No such username!')
        print('ACCESS DENIED')







#Atul Mishra
#SRM Univ.