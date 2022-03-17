import sqlite3
import random
import clipboard
import secrets
import database as d
from os import path


# random password generator
def pas_gen():
    lower = 'abcdefghijklmnopqrstuvwxyz'
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    nums = str(secrets.randbits(35))
    symbols = '!@#$%^&*'
    string = lower + upper + nums + symbols
    stage_1 = ''.join(random.sample(string,15))
    stage_2 = ''.join(random.sample(stage_1,15))
    return stage_2
# master password creator
def master_pass_creator():
	if path.exists("passwords.db"):
		

		pass
	else:
		master = input('create a master pass: ')
		d.store_master(password=master)


# main function
def main():

	master_pass_creator()

	# looping the menu
	loop = True

	while loop == True:

		print("""
		1.Create new password
		2.Saved passwords
		3.Delete a password
		4.Quit
			""")
		print('-'*35)

		user_input = input('Enter Query: ')


		# Creating a db, password, copy to clipboard
		if user_input == '1':
			data = pas_gen()
			print('-'*35)
			user_key = input('Enter a key to store: ')
			print('-'*35)
			clipboard.copy(data)
			
			password = user_key, data   # packing key, password into a tuple
			d.store_pass(password)


		# showing all keys from db to query, copy to clipboard
		elif user_input == '2':

			master_db = d.query_master('mas')
			master_auth = input('Enter master pass: ')

			if master_auth == master_db[2]:
				queried_passwords = d.query_all()
 
				for i in queried_passwords:    
					print(i[1])
				print('-'*35)				

				user_key_choice = input('Enter key to copy: ')
				pass_out = d.query_pass(user_key_choice)
				clipboard.copy(pass_out[2])
				print('copied to clipboard..')

			else:
				print('Invalid password')



		# showing all keys from db to query, delete a key&pass from db
		elif user_input == '3':

			queried_passwords = d.query_all()

			for i in queried_passwords:
				print(i[1])
			print('-'*35)

			user_delete = input('Enter key to delete: ')
			d.delete_pass(user_delete)
			print('-'*35)
			print('Entry Deleted')


		# exiting the menu loop if input  = quit
		elif user_input == '4':
			print('Quiting.....')
			loop = False


# calling the main function			
if __name__ == '__main__':
	main()
