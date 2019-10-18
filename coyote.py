def os(settings, login_user, logo, os):
	while True:
		try:
			from time import sleep
			from termcolor import cprint, colored
			import cio as io
			from os import system as run
			dfault = {
				'username' : 'Cinco',
				"password" : 'Coyote',
				'prompt_color' : "green"
			}
			errors = {
				1 : "Command not implmented" 
			}

			commands =['exit', 'help',  'cconfig', 'logout']
			try:
				command = input(colored("DEV@coyote ~$ ", settings['prompt_color']))
			except KeyError:
				print("We don't have that color yet.")
				settings['prompt_color'] = 'green'
			def save_settings():
				ledger = f'{login_user}.ledger'
				#io.ulock(ledger)
				local_table = open(ledger,'w')
				local_table.write(str(settings))
				local_table.close()
				#io.lock(ledger)
			def error(code):
				print(f"ERROR: {errors[code]}")
				
			if command in commands:
				
				if command == 'exit':
					print('Exiting Coyote')
					sleep(0.314)
					save_settings()
					exit()
				elif command == 'help':
					print(commands)
				elif command == 'cconfig':
					print("Your current settings are:")
					print(settings)
					print('[1] Change Username\n[2] Change password\n[3]Change prompt color\n[4] Add a user\n[5] Delete a user')
					setting = input("")
					if setting == '1':
						user = input("What is the new username? ")
						settings['username'] = user
					elif setting == '2':
						pas = input("What is your new password? ")
						settings['password'] = pas
					elif setting == '3':
						print("Colors can be: \ngrey\nred\ngreen\nmyellow\nblue\nmagenta\ncyan\nwhite")
						color = input("What is the new color? ")
						try:
							settings['prompt_color'] = color
						except:
							print("Oops... We don't have that color yet.")
					elif setting =='4':
						ledger_new = dfault
						use = input("What will be the new user's username? ")
						ledger_new['username'] = use
						pas = input('What is the new user\'s password? ')
						ledger_new['password'] = pas
						led = open(f"{use}.ledger", 'x')
						led.write(str(ledger_new))
						led.close()
						ledger_new = {}
					elif setting == '5':
						confirm = input(colored("Do you what to contine? [Y/N] "))
						if confirm == 'Y' or confirm == 'y':
							pass
						else:
							continue
						use = input("What user do you want to delete?")
						run(f'rm {use}')


				elif command == 'logout':
					save_settings()
					break
					



			if command not in commands:
				error(1)
		except KeyboardInterrupt:
			save_settings()
		continue