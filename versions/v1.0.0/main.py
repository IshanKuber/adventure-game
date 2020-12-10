# Importing keyboard module
import keyboard

# Adventure Game
print('Adventure Game v1.0.0')
print('\nWelcome to the adventure game!')
name = input('\nEnter your name: ')

# Each Player is given 10 lives
lives = 3

# Actual Game started
print(f'\nHello {name}! Your have {lives} lives')
print('\nYou are on the top of a green hill.')
choice = input('Enter a direction to go (left / right): ')

# If user chooses to go left
if choice == 'left':
	print('\nThere is a river in front of you.')
	print('You have 2 options')
	print('1) Cross the river and go ahead')
	print('2) Go along the bank of river')
	choice = input('What do you want to do? (cross / along): ')

	# If user chooses to swim across the river
	if choice == 'cross':
		print('\nYour crossed the river successfully!')
		print('But unfortunately 2 fishes bit you.')
		print('You lost 2 lives because of that.')
		lives -= 2
		print(f'\nYou have {lives} lives remaining now.')
		print('\nYou now see a big lake in front of you.')
		choice = input('What do you want to do? (drink water / go ahead): ')

		# If user chooses to drink water
		if choice == 'drink water':
			print('\nAlas! The water was poisonous!')
			print('\nYou lost all your lives!')

		# If user chooses to go ahead
		elif choice == 'go ahead':
			print('\nYou went ahead and entered a forest.')
			print('But suddenly a tiger attacked you.')
			print('You still have some more time to think.')
			choice = input('What do you want to do? (fight / run): ')

			# If user chooses to fight
			if choice == 'fight':
				print('\nThe tiger killed you!')
				lives -= 1
				print(f'\nYou have {lives} lives remaining now')

			# If user chooses to run away
			elif choice == 'run':
				print('\nThe tiger was faster than you.')
				print('So he catched up quickly and killed you!')
				lives -= 1
				print(f'\nYou have {lives} lives remaining now')

			# If user chooses to do something else
			else:
				print('\nThat was not a valid choice!')

		# If user chooses to do something else
		else:
			print('\nThat was not a valid choice!')
	
	# If user chooses to go along the river
	elif choice == 'along':
		print('\nYou went along the river.')
		print('After some time you saw some people coming.')
		choice = input('What do you want to do? (run away / meet them): ')

		# If the user chooses to run away
		if choice == 'run away':
			print('\nYou started running away.')
			print('But you see that those people are running after you!')
			print('They were on some fast vehicles so they were fast.')
			print('They were successful in catching you!')
			print('You realise that they were murderers.')
			print('3 people stabbed you 3 times')
			lives -= 3
			print(f'\nYou have {lives} lives remaining now')
		
		# If user chooses to meet them
		elif choice == 'meet them':
			print('\nYou realise that they were murderers.')
			print('3 people stabbed you 3 times')
			lives -= 3
			print(f'\nYou have {lives} lives remaining now')
		
		# If user chooses to do something else
		else:
			print('\nThat was not a valid choice!')
	
	# If user chooses to do something else
	else:
		print('\nThat was not a valid choice!')

# If user chooses to go right
elif choice == 'right':
	print('\nYou saw a huge mountain range.')
	choice = input('Do you want to go in? (yes / no): ')

	# If user chooses to go in
	if choice == 'yes':
		print('\nYou were trekking for a long time...')
		print('Finally you reached on a top of a big mountain.')
		print('The mountain is steep from all sides.')
		print('You could climb up,')
		print('but no way you can climb down the same way.')
		print('You have only 2 options left:')
		print('a) Try making a parachute to land with less materials you have')
		print('b) Give up the game')
		choice = input('Enter choice (a / b): ')

		# If user chooses to make parachute
		if choice == 'a':
			print('\nYou can only make a small parachute with your jacket and some rope you have got.')
			print('You tried making one, and succeeded! You jumped down and opened the parachute')
			print('Unfortunatey, te parachute did not work well, and you fell down with a bang!')
			print('There was no chance of your survival.')
			print('\nGame Over')
		
		# If user chooses to give up
		elif choice == 'b':
			print('\nGame Over')
		
		# If user chooses to do something else
		else:
			print('\nThat was not a valid choice!')

# If user chooses to do something else
else:
	print('\nThat was not a valid choice!')

# Prompting the user to exit
print('Press Esc to exit...')
keyboard.wait('esc')
