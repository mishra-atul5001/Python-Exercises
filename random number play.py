import random
r1 = random.randint(1,6)
r2 = random.randint(1,7)
def randomnumberplay(x):
	
	if x == r1 or x==r2:
		print ('This is matching' + ' Your number ' + str(x) + ' r1 is ' + str(r1) +' r2 is '+ str(r2))
	else:
		print('Not Macthed '+ ' r1 is '+ str(r1) + ' r2 is ' + str(r2))

randomnumberplay(4)	



def letsplaymore(r1,r2):
	if r1 >r2:
		print('"r1 is greater than r2" ' + str(r1) + ' <- r1||r2-> '+str(r2))
	else:
		print('"r2 is greater than r1" ' + str(r1) +' <- r1||r2->  '+ str(r2))

letsplaymore(r1,r2)

def pairs(r1,r2):
	stack=[]

	for i in range(r1):
		for j in range(r2):
			print (i,j)
			if i==j:
				 stack.append(i)
				 #print(sum(stack))
				 print('Common between ' + str(i) + ' and '+str(j))
			else:
				print('Nothing Common between ' + str(i) + ' and ' + str(j) )
	print(stack)
	y=(len(stack))
	z=y*2
	if y==1:
		print('Only one set was matching')
	else:
		print('No of matching pairs ' + str(z))
	print(stack)
	for i in stack:
		print('Pairs are: ' + str(stack[i])+ ' '+str(stack[i]))	
	

pairs(r1,r2)

