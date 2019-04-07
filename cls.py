class Contact:
	def __init__(self, name, email, address):
		self.name = name
		self.email = email
		self.address = address

class ContactManager:
	def __init__(self, contacts):
		self.contacts = contacts

	def showAllContacts(self):
		print('\n----------------------------------All of the contacts----------------------------------')
		if len(self.contacts) == 0:
			print('No contacts, maybe you should add some...')
		for contact in self.contacts:
			print('Name:',contact.name, 'Email:', contact.email, 'Address:', contact.address)
		print('------------------------------------------End------------------------------------------\n')

	def addContact(self, name, email, address):
		if len(name.strip()) == 0 and len(email.strip()) == 0 and len(address.strip()) == 0:
			raise NotEnoughInfoException
		contact = Contact(name, email, address)
		self.contacts.append(contact)
		print('Success.')

class NotEnoughInfoException(Exception):
	pass
