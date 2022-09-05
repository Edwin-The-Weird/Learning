import random

num25 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
guess = int(random.choice(num25))


odd = [1, 3, 5, 7, 9]
even = [2, 4, 6, 8, 10]
odd_even = [odd, even]
odd_or_even = str(random.choice(odd_even)

greater_msg = """The value you entered is greater than the secret number
"""
less_msg = """The value you entered is less than the secret number
"""
odd_msg = """
"""

#guess = 20
greater = True
attempts = 0

print("Any Number Between 1 and 30(including 1 and 30)(no decimal also)")
while guess != usr_guess:
	message = ""
	usr_guess = int(input("Number:"))
	attempts += 1
	is_odd_or_even_value = 0



	is_odd = False
	if usr_guess % 2 == 0:
		is_odd = False
	else:
		is_odd =True

	if is_odd == True and odd_or_even == "odd":
		is_odd_or_even_value = usr_guess + int(random.choice(odd))
		





	if usr_guess > guess:
		greater = True
		message += greater_msg
	else:
		greater = False
		message += less_msg

	

	
			
	
	
	
	
	
print(f"""
Congratulation You have found the Secret Number!
The number was {guess}
It took you {attempts} attempts

""")
