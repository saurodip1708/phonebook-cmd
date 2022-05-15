import sys
from ascii import logo, manual
from utility import take_multiple_inputs, validate

print(logo)
print(manual)


def main():
    command = input("> ")

    # exit program
    if command == "exit":
        print("")
        sys.exit(0)

    # list all contacts
    elif command == "lc":
        print("all contacts")

    # create a contact
    elif command == "create":
        inputs = take_multiple_inputs(["Name", "Phone Number", "Email"])
        if validate(inputs[0]) and validate(inputs[1]):
            # run your code
            print("Code goes here")
        else:
            print("> Enter a valid name or phone number")

    # delete a contact
    elif command == "delete":
        del_element = take_multiple_inputs(["Name or Phone No or Email"])[0]
        if validate(del_element):
            print("Code goes here")
        else:
            print("> Enter a valid name or phone number or email")

    # update a contact
    elif command == "update":
        up_elem = take_multiple_inputs(["Name or Phone No or Email to update"])[0]
        if validate(up_elem):
            print("Code goes here")
        else:
            print("> Enter a valid name or phone number or email")

    main()


main()
