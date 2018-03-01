import unittest

import app.phonebook as phonebook

class Testphonebook(unittest.TestCase):
    
    def test_add_contact(self):
        response = phonebook.addContact("Brian", "Ouma", "0734576890")
        self.assertEqual(response["message"], "Contact created successfully")

    def test_update_contact(self):
        response = phonebook.updateContact({"Jane", "Doe", "0721947689" },{"John", "Doe", "0721949689"})
        self.assertEqual(response["message"], "Contact updated successfully")

    def test_delete_contact(self):
        response = phonebook.deleteContact("Mike", "James", "0721947689")
        self.assertEqual(response["message"], "Contact deleted successfully")

    def test_view_contact(self):
        response = phonebook.viewContact("Brian", "Mwathi", "0734473456")
        self.assertEqual(response["message"], "Contact found successfully")

