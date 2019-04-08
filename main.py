from cls import ContactManager
from cls import NotEnoughInfoException
import time

choices = {
	1 : 'View the address book',
	2 : 'Add a contact',
	3 : 'Modify a contact',
	4 : 'delete a contact',
	5 : 'search in address book',
	6 : 'Quit'
}



print('\nWelcome! ')
cm = ContactManager()
cm.loadContacts()
print('\nChoose a number to use this program!')

while True:
	print('\n-----------------------------------------Menu------------------------------------------')
	for choice, desc in choices.items():
		print('\t\t\t\t',choice,'.',desc)
	no = int(input('Your choice:'))

	if no == 1:
		cm.showAllContacts()
		k = input('Press \'Enter\' to continue:')
		continue

	if no == 2:
		name = input('\nName:')
		email = input('Email:')
		address = input('Address:')
		telephone = input('Telephone:')
		try:
			cm.addContact(name, email, address, telephone)
			print('\nSuccess.')
		except NotEnoughInfoException as ex:
			print('Please input one of info below : name or email or address.')

	if no == 3:
		if cm.isContactsEmpty():
			continue
		cm.showAllContacts()
		select = input('Select the number before a contact to modify it(\'q\' to quit):')
		if select == 'q':
			continue
		name = input('\nName(Nothing for not modifying):')
		email = input('Email(Nothing for not modifying):')
		address = input('Address(Nothing for not modifying):')
		telephone = input('Telephone(Nothing for not modifying):')
		cm.modifyContact(int(select)-1, name, email, address, telephone)
		print('\nSuccess.')

	if no == 4:
		if cm.isContactsEmpty():
			continue
		cm.showAllContacts()
		select = input('Select the number before a contact to delete it(\'q\' to quit):')
		if select == 'q':
			continue
		success = cm.deleteContact(int(select)-1)
		if success:
			print('\nSuccess.')
		else:
			continue

	if no == 5:
		if cm.isContactsEmpty():
			continue
		keyword = input('Input a keyword to search:')
		cm.searchContact(keyword)
		k = input('Press \'Enter\' to continue:')
		continue

	if no == 6:
		cm.dumpContacts()
		print('\nExit now...')
		break
	print('\nPlease make an another choice')







