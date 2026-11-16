# Student Info Formatter - Version 2.0 (Added string formatting)
def main():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    section = input("Enter your section: ")
    favorite_subject = input("Enter your favorite subject: ")

    full_name_proper = f"{first_name.capitalize()} {last_name.capitalize()}"
    full_name_upper = f"{first_name.upper()} {last_name.upper()}"
    section_upper = section.upper()
    favorite_subject_proper = favorite_subject.capitalize()

    print("\nStudent Information:")
    print(f"Name (Proper Case): {full_name_proper}")
    print(f"Name (Upper Case): {full_name_upper}")
    print(f"Section (Upper Case): {section_upper}")
    print(f"Favorite Subject (Proper Case): {favorite_subject_proper}")

if __name__ == "__main__":
    main()