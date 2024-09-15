# Importing the 'pymongo' module required for MongoDB interaction
import pymongo


class DatabaseConnection:

    myClient = None     #Initialize to None

    #Constrcutor will get the DB details and associated collection name for further operations.
    def __init__(self):
        #Db connection handler to be used by DB operations
       
        try:
            # Creating a client to local MongoDB server
            myClient = pymongo.MongoClient("mongodb://localhost:27017/")

            # Getting the 'Employees' database from the MongoDB server
            self.db = myClient['Employees']

            #Getting the Developers connection under which all DB operations will be executed
            self.collection = self.db['Developers']
        except Exception as e:
                print(f"Error: {e}")
        finally:
                print("DB fetched is {} and collection name is {}".format(self.db, self.collection))

    def close_connection(self):
        if self.myClient is not None:
            self.myClient.close()
            print("Connection is closed")

    def insert_documents(self):
        try:
            self.collection.insert_many(
                  [
                        {
                            "EmpName": "Employee1",
                            "Project": "Project1",
                            "City": "Bangalore",
                            "Country": "India",
                        },
                        {
                            "EmpName": "Employee2",
                            "Project": "Project1",
                            "City": "Mumbai",
                            "Country": "India",
                        },
                        {
                            "EmpName": "Employee3",
                            "Project": "Project1",
                            "City": "Delhi",
                            "Country": "India",
                        },
                        {
                            "EmpName": "Employee4",
                            "Project": "Project2",
                            "City": "Pune",
                            "Country": "India",
                        },
                        {
                            "EmpName": "Employee5",
                            "Project": "Project2",
                            "City": "Noida",
                            "Country": "India",
                        },
                        {
                            "EmpName": "Employee6",
                            "Project": "Project2",
                            "City": "Hyderabad",
                            "Country": "India",
                        },
                    ]
                )
            print("Data inserted successfully")
        except Exception as e:
                print(f"Error: {e}")

    #Function to fetch all the documents in the collection
    def fetch_documents(self):
        try:
            documents_data = self.collection.find({})
            for document in documents_data:
                print(document)
        except Exception as e:
            print(f"Error: {e}")

    
    #Function to fetch all the documents in the collection based on the project name
    def fetch_documents_condition(self, Project):
        try:
            documents_data = self.collection.find({"Project": Project})
            for document in documents_data:
                print(document)
        except Exception as e:
            print(f"Error: {e}")


    #Function to delete single document based on provided project Name
    def delete_document(self, Project):
        try:
            self.collection.delete_one({'Project':Project})
        except Exception as e:
            print(f"Error: {e}")


    #Function to update the City of single document for given Project
    def update_document(self, Project, City):
        try:
            self.collection.update_one(
                {"Project": Project},
                {"$set" : {"City" : City}}
            )
        except Exception as e:
            print(f"Error: {e}")
