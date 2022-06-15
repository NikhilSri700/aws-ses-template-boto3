"""
Main python file for the project.
"""

from utils.email import Email
from utils.template import Template


def template_operations():
    while True:
        print("\nOperations on Templates")
        print("1. Create or Update Templates")
        print("2. Delete a Template")
        print("3. View a Template")
        print("4. List All Templates")
        print("5. Previous Menu")
        print("6. Exit")
        template_choice = int(input("Enter the Choice: "))

        if template_choice == 1:
            Template.create_or_update()
        elif template_choice == 2:
            template_list = Template.list_all()
            delete_choice = int(input("Enter choice for deletion"))

            if 1 <= delete_choice <= len(template_list)+1:
                Template.delete(template_list[delete_choice+1])
            else:
                print("Wrong Choice!")
        elif template_choice == 3:
            template_list = Template.list_all()
            view_choice = int(input("Enter choice for Template Description"))

            if 1 <= view_choice <= len(template_list)+1:
                Template.view(template_list[view_choice+1])
            else:
                print("Wrong Choice!")
        elif template_choice == 4:
            Template.list_all()
        elif template_choice == 5:
            return
        elif template_choice == 6:
            exit()
        else:
            print("Wrong Choice!")


def email_operations():
    while True:
        print("\nOptions for Emails")
        print("1. Verify Email Identity")
        print("2. List all verified identities")
        print("3. Send Templated Email")
        print("4. Send Bulk Templated Emails")
        print("5. Previous Menu")
        print("6. Exit")
        email_choice = int(input("Enter the Choice: "))

        if email_choice == 1:
            email = input("Enter Email Address: ")
            Email.verify_identity(email)
        elif email_choice == 2:
            pass
        elif email_choice == 3:
            pass
        elif email_choice == 4:
            pass
        elif email_choice == 5:
            return
        elif email_choice == 6:
            exit()
        else:
            print("Wrong choice!")


# Program execution will start from here
if __name__ == '__main__':
    while True:
        print("\nPython Client for AWS SES")
        print("1. Template Operations")
        print("2. Email Options")
        print("3. Exit")
        choice = int(input("Enter the Choice: "))

        if choice == 1:
            template_operations()
        elif choice == 2:
            email_operations()
        elif choice == 3:
            print("Thank You, Bye!")
            break
        else:
            print("Wrong Choice!")
