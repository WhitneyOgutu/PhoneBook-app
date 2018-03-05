class Phonebook:
    def __init__(self):
        self.phonebook = []
    
    def add_contact(self, fullname, number):
        contact = {}
        contact["fullname"] = fullname
        contact["number"] = number   
        self.phonebook.append(contact)     
        return {"message": "Contact added successfully"}
    
    def view_contact(self, contact):
        for contact in self.phonebook:
            return contact

    def delete_contact(self, contact):
        if contact in self.phonebook:
            self.phonebook.remove(contact)
        return{"message": "Deleted contact successfully"}

    def update_contact(self,contact):
        if contact in self.phonebook:
            self.phonebook.update(contact)
        return {"message": "Updated contact successfully"}