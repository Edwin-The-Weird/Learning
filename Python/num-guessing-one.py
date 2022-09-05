import random

num25 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
guess = int(random.choice(num25))
usr_guess = int(input("Any Number Between 1 and 30(including 1 and 30)(no decimal also): "))
greater = True
attempts = 0
while guess != usr_guess:
	attempts += 1
	
	if usr_guess > guess:
		greater = True
	else:
		greater = False
		
	
	
	
	
	
print(f"""
Congratulation You have found the Secret Number!
The number was {guess}
It took you {attempts} attempts

""")
