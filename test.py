#!/usr/bin/env python3

# Testing adding a user
add_user('testuser', 'testpassword')

# Testing authentication
if authenticate('testuser', 'testpassword'):
    print("User authenticated successfully!")
else:
    print("Authentication failed.")


def main():
    # Register a new user
    add_user('new_user', 'secure_password')

    # Attempt to authenticate the user
    if authenticate('new_user', 'secure_password'):
        print("User logged in successfully!")
    else:
        print("Login failed.")

if __name__ == "__main__":
    main()

