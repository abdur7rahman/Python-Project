import pymysql
import credentials as cr

def get_db_connection():
    return pymysql.connect(host=cr.host, user=cr.user, password=cr.password, database=cr.database)

def login():
    print("\n=== LOGIN ===")
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    if not email or not password:
        print("Error: All fields are required!")
        return

    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Std_Register WHERE email=%s AND password=%s", (email, password))
        user = cursor.fetchone()
        connection.close()

        if user:
            print("Welcome!")
        else:
            print("Error: Invalid email or password.")
    except Exception as e:
        print(f"Error: {str(e)}")

def signup():
    print("\n=== SIGN UP ===")
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    if not all([first_name, last_name, email, password]):
        print("Error: All fields are required!")
        return

    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Std_Register WHERE email=%s", (email,))
        if cursor.fetchone():
            print("Error: Email already exists. Please try a different one.")
        else:
            cursor.execute(
                "INSERT INTO Std_Register (f_name, l_name, email, password) VALUES (%s, %s, %s, %s)",
                (first_name, last_name, email, password)
            )
            connection.commit()
            print("Registration successful!")
        connection.close()
    except Exception as e:
        print(f"Error: {str(e)}")

def main():
    while True:
        print("\n=== MAIN MENU ===")
        print("1. Login")
        print("2. Sign Up")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            login()
        elif choice == '2':
            signup()
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
