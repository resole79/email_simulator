class Email:
    def __init__(self, from_address, subject_line, email_contents):
        # Instance variable
        self.from_address = from_address
        self.subject_line = subject_line
        self.email_contents = email_contents
        self.has_been_read = False
        self.is_spam = False

    def __str__(self):
        return f"from:{self.from_address} | subject:{self.subject_line} "

    # Method mark email read
    def mark_as_read(self):
        self.has_been_read = True

    # Method mark email spam
    def mark_as_spam(self):
        self.is_spam = True


class Inbox:

    def __init__(self):
        self.inbox = []

    # Method put an image if email is read or spam
    def imagine_read_spam(self, i):
        if self.inbox[i].has_been_read:
            read_email = f"{green} Ⓡ "
        else:
            read_email = " "
        if self.inbox[i].is_spam:
            spam_email = f"|{red} Ⓢ "
        else:
            spam_email = " "

        return read_email, spam_email

    # Method check email is in Inbox
    def check_email(self, email_to_check):
        email_check = False
        for i, email_arrive in enumerate(self.inbox):
            if email_arrive.from_address == email_to_check:
                email_check = True

        return email_check

    # Method view all email inside Inbox
    def view_all(self):
        message_to_use = "Ⓐ All Emails"
        print(header(message_to_use))

        for i, send_email in enumerate(self.inbox):
            read_email, spam_email = self.imagine_read_spam(i)
            if i % 2 == 0:
                print(f"{bold}{italic}{i}. {send_email.__str__()} {read_email} {spam_email}{endc} ")
            else:
                print(f"{revers}{bold}{italic}{i}. {send_email.__str__()} {read_email} {spam_email}{endc} ")

        print(f"\n ◙ You have: {revers}{bold}{italic} {len(self.inbox)} {endc} emails in total")

    # Method add email inside the Inbox
    def add_email(self, from_address, subject_line, email_contents):
        email_object = Email(from_address, subject_line, email_contents)
        self.inbox.append(email_object)

    # Method list all email from sender
    def list_messages_from_sender(self, sender_address):
        message_to_use = f"email from: {sender_address}"
        print(header(message_to_use))

        count_email_arrive_from = 0
        for i, email_arrive in enumerate(self.inbox):
            if email_arrive.from_address == sender_address:
                read_email, spam_email = self.imagine_read_spam(i)
                if i % 2 == 0:
                    print(f"{bold}{italic}{i}. {email_arrive.__str__()}{read_email}{spam_email}{endc} ")
                else:
                    print(f"{revers}{bold}{italic}{i}. {email_arrive.__str__()}{read_email}{spam_email}{endc} ")
                count_email_arrive_from += 1

        print(f"\n ◙ You have: {revers} {count_email_arrive_from} {endc} emails from {revers} {sender_address} {endc} in total\n")

    # Method to see email request
    def get_email(self, sender_address, index):
        output = ""
        email_to_view = self.inbox[index]
        message_to_use = f"Email Index: {[index]}"
        print(header(message_to_use))

        if email_to_view.from_address == sender_address:
            output = f"  Email From: \t{email_to_view.from_address}\n"
            output += f"  Email Subject: {email_to_view.subject_line}\n"
            output += f"  Email Content:\n"
            output += f"  {email_to_view.email_contents}\n"
            output += "\n"
            # Call method "mark_as_read"
            email_to_view.mark_as_read()
        else:
            print(f"\n{red}{bold} Ⓔ Sorry, your index is incorrect.{endc}\n")

        return output

    # Method mark spam the email request
    def mark_as_spam(self, sender_address, index):
        count_spam = 0
        for i, email_to_spam in enumerate(self.inbox):
            if email_to_spam.from_address == sender_address and i == index:
                if not email_to_spam.is_spam:
                    email_to_spam.mark_as_spam()
                    print(f"\n{green}{bold} Email has been marked as spam.{endc}\n")
                    count_spam += 1

        if count_spam == 0:
            print(f"\n{red}{bold} Ⓔ Sorry, your email can't mark to spam.{endc}\n")

    # Method to show the unread email
    def get_unread_emails(self):

        message_to_use = "Ⓤ Unread Emails"
        print(header(message_to_use))

        count_unread_email = 0
        for i, unread_email in enumerate(self.inbox):
            read_email, spam_email = self.imagine_read_spam(i)
            if not unread_email.has_been_read:
                if i % 2 == 0:
                    print(f"{bold}{italic}{i}. {unread_email.__str__()}{spam_email}{endc}")
                else:
                    print(f"{revers}{bold}{italic}{i}. {unread_email.__str__()}{spam_email}{endc}")
                count_unread_email += 1

        print(f"\n ◙ You have: {revers} {count_unread_email} {endc} unread emails in total")

    # Method to show the spam email
    def get_spam_emails(self):

        message_to_use = "Ⓢ Spam Emails"
        print(header(message_to_use))

        count_spam_email = 0
        for i, email_spam in enumerate(self.inbox):
            read_email, spam_email = self.imagine_read_spam(i)
            if email_spam.is_spam:
                if i % 2 == 0:
                    print(f"{bold}{italic}{i}. {email_spam.__str__()}{read_email}{endc}")
                else:
                    print(f"{revers}{bold}{italic}{i}. {email_spam.__str__()}{read_email}{endc}")
                count_spam_email += 1

        print(f"\n ◙ You have: {revers} {count_spam_email} {endc} spam emails in total")

    # Method to delete email
    def delete(self, sender_address, index):
        count_delete = 0
        for i, email_to_delete in enumerate(self.inbox):
            if email_to_delete.from_address == sender_address and i == index:
                self.inbox.pop(index)
                print(f"\n{green}{bold} Email has been delete.{endc}\n")
                count_delete += 1

        if count_delete == 0:
            print(f"\n{red}{bold} Ⓔ Sorry, your email can't delete.{endc}\n")


# Function
# Function to create header of email
def header(message):
    header_email = "╔══════════════════════════════════════════════════════════════╗\n"
    header_email += f"                         {message}                          \n"
    header_email += "╚══════════════════════════════════════════════════════════════╝\n"

    return header_email


# Function to check empy item
def check_empty(item_to_check):
    if item_to_check == "":
        empty_check = True
    else:
        empty_check = False

    return empty_check


# Declare Variable
# Color use for program
green = "\u001b[32m"
red = "\u001b[31m"
bold = "\033[1m"
italic = "\033[3m"
revers = "\u001b[7m"
endc = '\033[0m'

user_choice = ""

# User Menu
usage_message = "\nWelcome to the email system! What would you like to do?\n"
usage_message += f"{green}(S){endc}end - {green}(R){endc}ead - {green}(M){endc}ark spam - {green}(D){endc}elete"
usage_message += f" - {green}(L){endc}list from a sender - {green}(GU){endc}Get Unread - {green}(GS){endc}Get Spam"
usage_message += f" - {green}(E){endc}xit : "

# An Email Simulation
# Call class "Inbox()"
conteiner_email = Inbox()
# Call method "add_email"
conteiner_email.add_email("example@hello.com", "hello", "This is a test email!")


while True:
    # Show all email in my Inbox
    conteiner_email.view_all()
    # Ask user to choose a voice from menu
    user_choice = input(usage_message).strip().lower()

    if user_choice == "s":
        pass
        # Ask user to insert email address, subject of email and contents of email
        sender_address = input("Please enter the address of the sender : ").lower()
        while check_empty(sender_address):
            print(f"\n{red}{bold} Ⓔ Sorry, your email is empty.{endc}\n")
            sender_address = input("Please enter the address of the sender : ").lower()

        subject_line = input("Please enter the subject line of the email : ").capitalize()
        while check_empty(subject_line):
            print(f"\n{red}{bold} Ⓔ Sorry, your email subject is empty.{endc}\n")
            subject_line = input("Please enter the subject line of the email : ").capitalize()

        contents = input("Please enter the contents of the email : ").strip()
        while check_empty(contents):
            print(f"\n{red}{bold} Ⓔ Sorry, your email content is empty.{endc}\n")
            contents = input("Please enter the contents of the email : ").strip()

        # Call method "add_email"
        conteiner_email.add_email(sender_address, subject_line, contents)

        print(f"\n{green}{bold} Email has been added to inbox.{endc}\n")

    elif user_choice == "l":
        pass
        # Ask user to insert email address
        sender_address = input("Please enter the address of the sender : ").lower()

        # "while" cycle: condition to exit email is in Inbox
        while not conteiner_email.check_email(sender_address):
            print(f"\n{red}{bold} Ⓔ Sorry, I can't find this email sender.{endc}\n")
            sender_address = input("Please enter the address of the sender : ").lower()

        # Call method "list_messages_from_sender"
        conteiner_email.list_messages_from_sender(sender_address)

    elif user_choice == "r":
        pass
        try:
            # Ask user to insert "sender_address"
            sender_address = input("Please enter the address of the sender : ").lower()

            # "while" cycle: condition to exit email is in Inbox
            while not conteiner_email.check_email(sender_address):
                print(f"\n{red}{bold} Ⓔ Sorry, I can't find this email sender.{endc}\n")
                sender_address = input("Please enter the address of the sender : ").lower()

            # Call method "list_messages_from_sender"
            conteiner_email.list_messages_from_sender(sender_address)

            # Ask user to insert "email_index"
            email_index = int(input("Please enter the index of the email that you would like to read : "))

            # Call method "get_email"
            print(conteiner_email.get_email(sender_address, email_index))

        except ValueError as value_error:
            print(f"\n{red}{bold} Ⓔ ValueError: {value_error}{endc}\n")
        except IndexError as index_error:
            print(f"\n{red}{bold} Ⓔ IndexError: {index_error}{endc}\n")

    elif user_choice == "m":
        try:
            # Ask user to insert "sender_address"
            sender_address = input("Please enter the address of the sender of the email : ").lower()

            # "while" cycle: condition to exit email is in Inbox
            while not conteiner_email.check_email(sender_address):
                print(f"\n{red}{bold} Ⓔ Sorry, I can't find this email sender.{endc}\n")
                sender_address = input("Please enter the address of the sender of the email : ").lower()

            # Call method "list_messages_from_sender"
            conteiner_email.list_messages_from_sender(sender_address)

            # Ask user to insert "email_index"
            email_index = int(input("Please enter the index of the email to be marked as spam : "))

            # Call method "mark_as_spam"
            conteiner_email.mark_as_spam(sender_address, email_index)

        except ValueError as value_error:
            print(f"\n{red}{bold} Ⓔ {value_error}{endc}\n")
        except IndexError as index_error:
            print(f"\n{red}{bold} Ⓔ {index_error}{endc}\n")

    elif user_choice == "gu":
        pass
        # List all unread emails
        print(conteiner_email.get_unread_emails())

    elif user_choice == "gs":
        pass
        # List all spam emails
        print(conteiner_email.get_spam_emails())

    elif user_choice == "d":
        pass
        try:

            # Ask user to insert "sender_address"
            sender_address = input("Please enter the address of the sender of the email : ").lower()

            # "while" cycle: condition to exit email is in Inbox
            while not conteiner_email.check_email(sender_address):
                print(f"\n{red}{bold} Ⓔ Sorry, I can't find this email sender.{endc}\n")
                sender_address = input("Please enter the address of the sender of the email : ").lower()

            # Call method "list_messages_from_sender"
            conteiner_email.list_messages_from_sender(sender_address)

            # Ask user to insert "email_index"
            email_index = int(input("Please enter the index of the email to be deleted : "))

            # Call method "delete"
            conteiner_email.delete(sender_address, email_index)

        except ValueError as value_error:
            print(f"\n{red}{bold} Ⓔ {value_error}{endc}\n")

    elif user_choice == "e":
        print("\nGoodbye\n")
        exit()

    else:
        print(f"\n{red}{bold} Ⓔ Oops - incorrect input.{endc}\n")
