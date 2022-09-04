#Collatz Conjecture

num = int(input("Number: "))
is_odd = False
hey = True
#while hey == True:
while num != 1:
#for i in range(1,3):
	if num % 2 != 0:
		is_odd = True
		num = (num*3)+1
		print(num)
	else:
		is_odd = False
		num = num/2
		print(num)
