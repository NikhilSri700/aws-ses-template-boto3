"""
Main python file for the project.
"""

from utils.email import Email
from utils.template import Template


def template_delete():
    template_list = Template.list_all()
    delete_choice = int(input("Enter choice for deletion"))

    if 1 <= delete_choice <= len(template_list)+1:
        return Template.delete(template_list[delete_choice+1])
    else:
        print("Wrong Choice!")


def view_template():
    template_list = Template.list_all()
    view_choice = int(input("Enter choice for Template Description"))

    if 1 <= view_choice <= len(template_list)+1:
        Template.view(template_list[view_choice+1])
    else:
        print("Wrong Choice!")


def verify_email():
    email = input("Enter Email Address: ")
    return Email.verify_identity(email)


def send_mail():
    email = input("Enter source email Address: ")
    return Email.send_using_template(email)


def send_mail_bulk():
    email = input("Enter source email Address: ")
    return Email.send_using_template(email, bulk=True)


template_options = {
    1: Template.create_or_update,
    2: template_delete,
    3: view_template,
    4: Template.list_all,
}

email_dict = {
    1: verify_email,
    2: send_mail,
    3: send_mail_bulk,
}


def template_operations():
    """
    Function for menu on template operations.
    :return: None
    """
    while True:
        print("\nOperations on Templates")
        print("1. Create or Update Templates")
        print("2. Delete a Template")
        print("3. View a Template")
        print("4. List All Templates")
        print("5. Previous Menu")
        print("6. Exit")
        template_choice = int(input("Enter the Choice: "))

        if 1 <= template_choice <= 4:
            print(template_options[template_choice]())
        elif template_choice == 5:
            return
        elif template_choice == 6:
            exit()
        else:
            print("Wrong Choice!")


def email_operations():
    """
    Function for menu options for email.
    :return: None
    """
    while True:
        print("\nOptions for Emails")
        print("1. Verify Email Identity")
        print("2. Send Templated Email")
        print("3. Send Bulk Templated Emails")
        print("4. Previous Menu")
        print("5. Exit")
        email_choice = int(input("Enter the Choice: "))

        if 1 <= email_choice <= 3:
            print(email_dict[email_choice]())
        elif email_choice == 4:
            return
        elif email_choice == 5:
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
