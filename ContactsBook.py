import tkinter as tk
from tkinter import messagebox

contacts = {}

# Function to add a new contact
def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get(1.0, tk.END).strip()  
    
    if name == '':
        messagebox.showerror("Error", "Please enter a name.")
        return
    
    if phone == '':
        messagebox.showerror("Error", "Please enter a phone number.")
        return
    
    contacts[name] = {
        'Phone': phone,
        'Email': email,
        'Address': address
    }
    
    update_contact_list()
    clear_entries()

# Function to update the contact list display
def update_contact_list():
    contact_listbox.delete(0, tk.END)  # Clear current list
    
    for name, contact_info in contacts.items():
        contact_listbox.insert(tk.END, f"{name}: {contact_info['Phone']}")

# Function to clear input entries after adding or updating
def clear_entries():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(1.0, tk.END)

# Function to search for a contact
def search_contact():
    search_term = search_entry.get().strip().lower()
    
    contact_listbox.delete(0, tk.END)  # Clear current list
    
    for name, contact_info in contacts.items():
        if search_term in name.lower() or search_term in contact_info['Phone']:
            contact_listbox.insert(tk.END, f"{name}: {contact_info['Phone']}")

# Function to display full contact details when selected from list
def view_contact_details(event):
    try:
        index = contact_listbox.curselection()[0]
        selected_contact = contact_listbox.get(index)
        selected_name = selected_contact.split(':')[0].strip()
        
        contact_info = contacts[selected_name]
        messagebox.showinfo("Contact Details", 
                            f"Name: {selected_name}\nPhone: {contact_info['Phone']}\nEmail: {contact_info['Email']}\nAddress: {contact_info['Address']}")
    except IndexError:
        pass

# Function to update a contact's details
def update_contact():
    try:
        index = contact_listbox.curselection()[0]
        selected_contact = contact_listbox.get(index)
        selected_name = selected_contact.split(':')[0].strip()
        
        # Update contact details
        contacts[selected_name]['Phone'] = phone_entry.get()
        contacts[selected_name]['Email'] = email_entry.get()
        contacts[selected_name]['Address'] = address_entry.get(1.0, tk.END).strip()
        
        update_contact_list()
        clear_entries()
    except IndexError:
        pass

# Function to delete a contact
def delete_contact():
    try:
        index = contact_listbox.curselection()[0]
        selected_contact = contact_listbox.get(index)
        selected_name = selected_contact.split(':')[0].strip()
        
        del contacts[selected_name]
        update_contact_list()
        clear_entries()
    except IndexError:
        pass

root = tk.Tk()
root.title("Contact Management System")

tk.Label(root, text="Name:").grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Phone:").grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
phone_entry = tk.Entry(root)
phone_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Email:").grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
email_entry = tk.Entry(root)
email_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Address:").grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)
address_entry = tk.Text(root, height=4, width=30)
address_entry.grid(row=3, column=1, padx=10, pady=5)

add_button = tk.Button(root, text="Add Contact", command=add_contact)
add_button.grid(row=4, column=0, padx=10, pady=10)

update_button = tk.Button(root, text="Update Contact", command=update_contact)
update_button.grid(row=4, column=1, padx=10, pady=10)

delete_button = tk.Button(root, text="Delete Contact", command=delete_contact)
delete_button.grid(row=4, column=2, padx=10, pady=10)

search_entry = tk.Entry(root)
search_entry.grid(row=5, column=0, padx=10, pady=5)

search_button = tk.Button(root, text="Search", command=search_contact)
search_button.grid(row=5, column=1, padx=10, pady=5)

contact_listbox = tk.Listbox(root, height=10, width=50)
contact_listbox.grid(row=6, column=0, columnspan=3, padx=10, pady=5)

contact_listbox.bind("<Double-Button-1>", view_contact_details)

root.mainloop()
