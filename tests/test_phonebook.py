import unittest

from app.phonebook import Phonebook

class Testphonebook(unittest.TestCase):
    def test_add_contact(self):
        phonebook = Phonebook()
        response = phonebook.add_contact("John Doe", "0789567456")
        self.assertEqual(response["message"], "Contact added successfully")

    def test_view_contact(self):
        phonebook = Phonebook()
        response = phonebook.add_contact("Jane Dorothy", "0728987856")
        response = phonebook.view_contact(phonebook)
        self.assertEqual(response, {'fullname':"Jane Dorothy", 'number':"0728987856"})

    def test_delete_contact(self):
        phonebook = Phonebook()
        response = phonebook.delete_contact(phonebook)
        self.assertEqual(response["message"], "Deleted contact successfully")

    def test_update_contact(self):
        phonebook = Phonebook()
        response = phonebook.update_contact(phonebook)
        self.assertEqual(response["message"], "Updated contact successfully")