import pickle
from pathlib import Path

class Contact:
	def __init__(self, name, email, address, telephone):
		self.name = name
		self.email = email
		self.address = address
		self.telephone = telephone

class ContactManager:

	def showAllContacts(self):
		print('\n----------------------------------All of the contacts----------------------------------')
		if len(self.contacts) == 0:
			print('No contacts, maybe you should add some...')
		i = 1
		for contact in self.contacts:
			print('{}. Name: {}   Email: {}   Address: {}   Telephone: {}'.format(i, contact.name, contact.email, contact.address, contact.telephone))
		print('------------------------------------------End------------------------------------------\n')

	def addContact(self, name, email, address, telephone):
		if len(name.strip()) == 0 and len(email.strip()) == 0 and len(address.strip()) == 0 and len(telephone.strip()) == 0:
			raise NotEnoughInfoException
		contact = Contact(name, email, address, telephone)
		self.contacts.append(contact)

	def modifyContact(self, idx, name, email, address, telephone):
		contact = self.contacts[idx]
		if len(name) > 0:
			contact.name = name
		if len(email) > 0:
			contact.email = email
		if len(address) > 0:
			contact.address = address
		if len(telephone) > 0:
			contact.telephone = telephone	

	def deleteContact(self, idx):
		try:
			del self.contacts[idx]
			return True
		except IndexError:
			print('\nThere\'s no such contact in the address book')
			return False

	def searchContact(self, keyword):
		resultlist = []
		for contact in self.contacts:
			if keyword in contact.name or keyword in contact.email or keyword in contact.address or keyword in contact.telephone:
				resultlist.append(contact)
		if len(resultlist) == 0:
			print('No results...')
		elif len(resultlist) > 0:
			print('\n----------------------------------Here is the results----------------------------------')
		for contact in resultlist:
			print('Name: {}   Email: {}   Address: {}   Telephone: {}'.format(contact.name, contact.email, contact.address, contact.telephone))
			print('------------------------------------------End------------------------------------------\n')

	def isContactsEmpty(self):
		if len(self.contacts) == 0:
			print('\nThere are no contacts in the address book.Please add some first...')
			return True
		return False

	def loadContacts(self):
		print('\nStart to load contacts from {}...'.format(ContactLoader.contactspath))
		cl = ContactLoader()
		self.contacts = cl.loadContacts()
		print('Finished!')

	def dumpContacts(self):
		print('\nDump data to {}...'.format(ContactLoader.contactspath))
		cd = ContactDumper()
		cd.dumpContacts(self.contacts)
		print('Finished!')

class ContactLoader:

	contactspath = 'contacts.data'

	def loadContacts(self):
		f = Path(ContactLoader.contactspath)
		if f.exists():
			contacts = pickle.load(open(f, 'rb'))
			return contacts
		else:
			return []

class ContactDumper:

	contactspath = ContactLoader.contactspath

	def dumpContacts(self, contacts):
		f = open(ContactLoader.contactspath, 'wb')
		pickle.dump(contacts, f)
		f.close()

class NotEnoughInfoException(Exception):
	pass
