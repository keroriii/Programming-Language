def user_information():
    print("\n=== User Information Collection ===")
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    birth_year = input("Enter your birth year: ")
    
    print("\n--- Collected Information ---")
    print(f"Hello {name}! You are {age} years old and were born in {birth_year}.")

def password_check():
    print("\n=== Password Validation ===")
    correct_password = "default123"
    
    while True:
        password = input("Enter the password: ")
        if password == correct_password:
            print("Access granted!")
            break
        else:
            print("Incorrect password. Try again.")

def main():
    print("===== Laboratory Exercise - Control Structures =====")
    user_information()  # Task A
    password_check()    # Task C

if __name__ == "__main__":
    main()