import requests

BASE_URL = "http://127.0.0.1:5133"

def print_menu():
    print("\n" + "=" * 31)
    print("   LIBNIRYAN LIBRARY SYSTEM   ")
    print("=" * 31)
    print("[1] View All Books")
    print("[2] View Book by ID")
    print("[3] Add a New Book")
    print("[4] Borrow a Book")
    print("[5] Return a Book")
    print("[6] Exit")
    print("-" * 31)

def main():
    while True:
        print_menu()
        choice = input("Enter your choice (1-6): ").strip()
        
        if choice == '1':
            print("\n--- FETCHING ALL BOOKS ---")
            try:
                response = requests.get(f"{BASE_URL}/api/books")
                print(f"Status Code: {response.status_code}")
                
                if response.status_code == 200:
                    result = response.json()
                    books = result.get("data", [])
                    
                    print("\nLIBRARY CATALOG:")
                    print("-" * 65)
                    print(f"{'ID':<5} | {'Title':<30} | {'Author':<20} | {'Available'}")
                    print("-" * 65)
                    
                    for book in books:
                        print(f"{book['book_id']:<5} | {book['title']:<30} | {book['author']:<20} | {book['available']}/{book['copies']}")
                    print("-" * 65)
                else:
                    print("Response:", response.json())
            except Exception as e:
                print(f"Error connecting to server: {e}")

        elif choice == '2':
            print("\n--- VIEW BOOK BY ID ---")
            book_id = input("Enter Book ID: ").strip()
            try:
                response = requests.get(f"{BASE_URL}/api/books/{book_id}")
                print(f"Status Code: {response.status_code}")
                print("Response:", response.json())
            except Exception as e:
                print(f"Error connecting to server: {e}")

        elif choice == '3':
            print("\n--- ADD A NEW BOOK ---")
            title = input("Enter Book Title: ").strip()
            author = input("Enter Author: ").strip()
            copies = input("Enter Number of Copies: ").strip()
            
            payload = {
                "title": title,
                "author": author,
                "copies": int(copies) if copies.isdigit() else 1
            }
            try:
                response = requests.post(f"{BASE_URL}/api/books", json=payload)
                print(f"Status Code: {response.status_code}")
                print("Response:", response.json())
            except Exception as e:
                print(f"Error connecting to server: {e}")

        elif choice == '4':
            print("\n--- BORROW A BOOK ---")
            student_id = input("Enter your Student ID: ").strip()
            book_id = input("Enter Book ID to borrow: ").strip()
            
            payload = {
                "student_id": student_id,
                "book_id": int(book_id) if book_id.isdigit() else book_id
            }
            try:
                response = requests.post(f"{BASE_URL}/api/borrow", json=payload)
                print(f"Status Code: {response.status_code}")
                print("Response:", response.json())
            except Exception as e:
                print(f"Error connecting to server: {e}")

        elif choice == '5':
            print("\n--- RETURN A BOOK ---")
            transaction_id = input("Enter Transaction ID: ").strip()
            try:
                response = requests.put(f"{BASE_URL}/api/return/{transaction_id}")
                print(f"Status Code: {response.status_code}")
                print("Response:", response.json())
            except Exception as e:
                print(f"Error connecting to server: {e}")

        elif choice == '6':
            print("\nThank you for stopping by and checking out your books today! I hope your new reads take you on a wonderful adventure. Have a wonderful rest of your day, and happy reading!")
            print("Exiting LibniRyan System. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()