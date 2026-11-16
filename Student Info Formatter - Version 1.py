# Student Info Formatter - Version 1.0 (Initial version - basic input and output)
def main():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    section = input("Enter your section: ")
    favorite_subject = input("Enter your favorite subject: ")

    print("\nStudent Information:")
    print(f"Name: {first_name} {last_name}")
    print(f"Section: {section}")
    print(f"Favorite Subject: {favorite_subject}")

if __name__ == "__main__":
    main()


