#!/usr/bin/python3
import tkinter

import contact

class Application:
    def __init__(self):
        # Build a list that will hold Contact objects, an int to used when
        # we want to select a particular Contact, and a variable that will
        # point to our selected Contact once chosen.
        self.__contacts = []
        self.__selected_index = -1
        self.__selected_contact = None

        self.__window = tkinter.Tk()
        self.__window.title('Contact Manager')

        # Create four StringVar objects to be bound to the Entry widgets
        self.__first_name = tkinter.StringVar()
        self.__last_name = tkinter.StringVar()
        self.__email = tkinter.StringVar()
        self.__phone = tkinter.StringVar()

        # Build a Frame consisting of a Label and Entry widget for each field
        self.build_input_frame('First Name: ', self.__first_name)
        self.build_input_frame('Last Name: ', self.__last_name)
        self.build_input_frame('Email: ', self.__email)
        self.build_input_frame('Phone: ', self.__phone)

        # Build a new Frame and add three Buttons
        frame = tkinter.Frame(self.__window)
        self.__add_button = tkinter.Button(frame, text='Add Contact',
            anchor=tkinter.W, command=self.add_contact)
        self.__add_button.pack(side='left')
        self.__save_button = tkinter.Button(frame, text='Save Contact',
            anchor=tkinter.W, command=self.save_contact, state=tkinter.DISABLED)
        self.__save_button.pack(side='left')
        self.__delete_button = tkinter.Button(frame, text='Delete Contact',
            anchor=tkinter.W,
            command=self.delete_contact, state=tkinter.DISABLED)
        self.__delete_button.pack()
        frame.pack()

        # Now, we will use a Listbox widget to display our Contacts
        frame = tkinter.Frame(self.__window)
        label = tkinter.Label(frame, text='Your Contacts')
        self.__contacts_list = tkinter.Listbox(frame, width=120,
            selectmode=tkinter.SINGLE)
        # .bind is a special method that lets us connect a method in our
        # Application class definition with the user's action of clicking on
        # a row in our Listbox
        self.__contacts_list.bind('<<ListboxSelect>>', self.select_contact)
        label.pack()
        self.__contacts_list.pack()
        frame.pack()

    def build_input_frame(self, label, textvariable):
        """Build the top frames of the window for being able to enter data."""
        frame = tkinter.Frame(self.__window)
        label = tkinter.Label(frame, text=label, width=15, anchor=tkinter.W)
        entry = tkinter.Entry(frame, textvariable=textvariable, width=30)
        label.pack(side='left')
        entry.pack(side='right')
        frame.pack()

    def add_contact(self):
        """Get the values from the bound variables and create a new Contact."""
        c = contact.Contact(self.__first_name.get(), self.__last_name.get(),
            self.__email.get(), self.__phone.get())
        self.__contacts.append(c)

        # Add this Contact's __str__ output to the listbox
        self.__contacts_list.insert(tkinter.END, str(c))

    def select_contact(self, event):
        """Get the Contact at the index selected, and set the Entry fields
           with its values."""
        # Get the current selection from the Listbox. curselection() returns
        # a tuple and we want the first item
        # Get the current selection from the Listbox. curselection() returns
        # a tuple and we want the first item
        current_selection = self.__contacts_list.curselection()
        if current_selection:
            self.__selected_index = current_selection[0]

            # Grab the Contact object from self.__contacts at that index
            self.__selected_contact = self.__contacts[self.__selected_index]

            # Use it's values to set the StringVars
            self.__first_name.set(self.__selected_contact.get_first_name())
            self.__last_name.set(self.__selected_contact.get_last_name())
            self.__email.set(self.__selected_contact.get_email())
            self.__phone.set(self.__selected_contact.get_phone())

            # Make sure the Save button is enabled
            self.__save_button.config(state=tkinter.NORMAL)
            self.__delete_button.config(state=tkinter.NORMAL)

    def delete_contact(self):
        """Remov the Contact at the index selected then set the Entry fields
           to empty values."""
        if 0 <= self.__selected_index < len(self.__contacts):
            del self.__contacts[self.__selected_index]
            self.__contacts_list.delete(self.__selected_index)

            # Call the method to deselect the item, clear Entry fields, and
            # disable buttons.
            self.after_selected_operation()

    def save_contact(self):
        """Set the selected Contact's fields and then persist its __str__
           representation to the Listbox."""
        self.__selected_contact.set_first_name(self.__first_name.get())
        self.__selected_contact.set_last_name(self.__last_name.get())
        self.__selected_contact.set_email(self.__email.get())
        self.__selected_contact.set_phone(self.__phone.get())

        # Listbox widgets don't have a way of updating an item in place. So
        # We'll delete the item at a particular index and then add it
        self.__contacts_list.delete(self.__selected_index)
        self.__contacts_list.insert(self.__selected_index,
            str(self.__selected_contact))

        # Call the method to deselect the item, clear Entry fields, and
        # disable buttons.
        self.after_selected_operation()


    def after_selected_operation(self):
        """Clear the selected index, contact, and disable buttons."""
        self.__selected_index = -1
        self.__selected_contact = None

        self.__first_name.set('')
        self.__last_name.set('')
        self.__email.set('')
        self.__phone.set('')

        # Make sure the Save and Delete buttons are disabled
        self.__save_button.config(state=tkinter.DISABLED)
        self.__delete_button.config(state=tkinter.DISABLED)



    def start(self):
        """This method starts our GUI application."""
        tkinter.mainloop()


def main():
    app = Application()
    app.start()

main()

