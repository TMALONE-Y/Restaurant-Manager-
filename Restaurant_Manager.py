import json
import os



DATA_FILE = "system_data.json"

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"users": {}}

def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def main():
    data = load_data()
    
    print("--- Multi-Owner Restaurant System ---")
    username = input("Enter your username: ")
    
    if username not in data["users"]:
        password = ("Create a new password: ")
        data["users"][username] = {"password": password, "restaurants": {}}
        save_data(data)
        print("Account created successfully!")

    else:
        password = input("Enter your password: ")
        if data["users"][username]["password"] != password:
            print("Incorrect password. Access denied.")
            return

    print(f"\nWelcome back, {username}!")
    user_data = data["users"][username]["restaurants"]
    
    while True:

        print("\n1. Add Restaurant | 2. Search | 3. Delete | 4. Show | 5. Exit | 6.Delete Account ")
        choice = input("Select an option: ")
        
        if choice == "1":
            key = input("Enter unique key: ")
            if key in user_data:
                print("Error: Key already exists.")
            else:
                name = input("Enter restaurant name: ")
                user_data[key] = name
                save_data(data)
                print("Restaurant saved!")
            
        elif choice == "2":
            key = input("Enter key to search: ")
            print(f"Result: {user_data.get(key, 'Key not found.')}")

        elif choice == "3":
            key = input("Enter key to delete: ")
            if key in user_data:
                removed = user_data.pop(key)
                save_data(data)
                print(f"'{removed}' deleted.")

            else:
                print("Key not found.")
                
        elif choice == "4":
           
            if user_data:

                print(f"\n -------- Restaurants owned By {username} -------- \n")

                    
                for Show , Info in user_data.items():
                    print(Show , ":" , Info)
            else:
                print(f"{username} , you have no restaurants registered yet.")
               
        elif choice == "5":
            print("Goodbye!")
            break

        elif choice == "6":

            confirm = input(f"Are you sure you want to delete account '{username}'? (yes/no): ")
            if confirm.lower() == "yes":
               
                del data["users"][username] 
                save_data(data) 

                print(f"Account '{username}' has been deleted successfully.")
                break 

if __name__ == "__main__":
    main()