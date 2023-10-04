import tkinter as tk

class ContactBook:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")

        # Create a list to store contacts
        self.contacts = []

        # Create labels and entry widgets for name and phone
        tk.Label(root, text="Name:").pack()
        self.name_entry = tk.Entry(root)
        self.name_entry.pack()

        tk.Label(root, text="Phone:").pack()
        self.phone_entry = tk.Entry(root)
        self.phone_entry.pack()

        # Create buttons for adding and displaying contacts
        tk.Button(root, text="Add Contact", command=self.add_contact).pack()
        tk.Button(root, text="Show Contacts", command=self.show_contacts).pack()

        # Create a text widget to display contacts
        self.contacts_text = tk.Text(root, height=10, width=40)
        self.contacts_text.pack()

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        if name and phone:
            contact = f"Name: {name}, Phone: {phone}"
            self.contacts.append(contact)
            self.name_entry.delete(0, tk.END)
            self.phone_entry.delete(0, tk.END)
            self.contacts_text.insert(tk.END, contact + "\n")
        else:
            tk.messagebox.showerror("Error", "Please enter both name and phone.")

    def show_contacts(self):
        self.contacts_text.delete(1.0, tk.END)  # Clear the text widget
        for contact in self.contacts:
            self.contacts_text.insert(tk.END, contact + "\n")

def main():
    root = tk.Tk()
    contact_book = ContactBook(root)
    root.mainloop()

if __name__ == "__main__":
    main()
