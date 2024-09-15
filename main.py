from Database_operations import DatabaseConnection

db = DatabaseConnection()


def main():
    #Operation options for end user
    print("Enter 1 to insert the documents in the collection")
    print("Enter 2 to print all the documents in the collection")
    print("Enter 3 to print all the documents in the collection based on the condition")
    print("Enter 4 to update the first document in the collection")
    print("Enter 5 to delete the first document in the collection")

    try:
        choice = int(input("Enter Option: "))

        if choice == 1:
            print("inserting the documents in the collection")
            db.insert_documents()

        if choice == 2:
            print("Display the documents in the collection")
            db.fetch_documents()

        if choice == 3:
            print("Display the documents in the collection based on the Project name")
            db.fetch_documents_condition("Project1")

        if choice == 4:
            print("Update the first document")
            db.update_document("Project1", "Indore")

        if choice == 5:
            print("Delete the first document")
            db.delete_document("Project1")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        db.close_connection()


# Entry point of the program
if __name__ == "__main__":
    main()