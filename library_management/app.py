import database
import models
from utils import print_data

# Create tables (database setup)
database.create_tables()

# ---------------- MAIN MENU ----------------

while True:
    print("\n--- Library Management System ---")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Delete Book")
    print("5. Add Member")
    print("6. View Members")
    print("7. Issue Book")
    print("8. Return Book")
    print("9. View Transactions")
    print("10. Exit")

    choice = input("Enter your choice: ")

    # -------- BOOK --------
    if choice == "1":
        title = input("Enter Title: ")
        author = input("Enter Author: ")
        quantity = int(input("Enter Quantity: "))
        models.add_book(title, author, quantity)
        print("Book Added Successfully!")

    elif choice == "2":
        print("\n--- Book List ---")
        print_data(models.view_books())

    elif choice == "3":
        keyword = input("Enter title to search: ")
        print("\n--- Search Results ---")
        print_data(models.search_book(keyword))

    elif choice == "4":
        book_id = input("Enter Book ID to delete: ")
        models.delete_book(book_id)
        print("Book Deleted Successfully!")

    # -------- MEMBER --------
    elif choice == "5":
        name = input("Enter Member Name: ")
        contact = input("Enter Contact: ")
        models.add_member(name, contact)
        print("Member Added Successfully!")

    elif choice == "6":
        print("\n--- Member List ---")
        print_data(models.view_members())

    # -------- TRANSACTION --------
    elif choice == "7":
        book_id = input("Enter Book ID: ")
        member_id = input("Enter Member ID: ")

        if models.issue_book(book_id, member_id):
            print("Book Issued Successfully!")
        else:
            print("Book Not Available!")

    elif choice == "8":
        transaction_id = input("Enter Transaction ID: ")
        models.return_book(transaction_id)
        print("Book Returned Successfully!")

    elif choice == "9":
        print("\n--- Transactions ---")
        print_data(models.view_transactions())

    # -------- EXIT --------
    elif choice == "10":
        print("Exiting... Thank you!")
        break

    else:
        print("Invalid choice! Please try again.")