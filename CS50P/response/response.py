from validator_collection import validators, errors
def main():
    print(email_input(input("Input: ")),end="")


def email_input(value):
    try:
        validators.email(value, allow_empty = False)
    except errors.InvalidEmailError:
        # handle the error here
         return f"Invalid"
    # except ValueError as error:
    #     # handle other ValueErrors here


    # do something with your new email address value

    return f"Valid"

# email = email_input('email@domain.com')
# # This will return the email address.

# email = email_input('not-a-valid-email')
# # This will raise a ValueError that some_function() will handle.

# email = email_input(None)
# # This will raise a ValueError that some_function() will handle.
if __name__ == "__main__":
    main()
