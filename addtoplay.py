from tkinter import*
import tkinter.messagebox as msg
import mysql.connector

db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="145632sk",
    database="mldb"
)
def ex():
    def execute_query():
        query = query_entry.get()

        try:
            cursor = db_connection.cursor()
            cursor.execute(query)

            if cursor.with_rows:
                # If the query returns results, fetch and display them
                results = cursor.fetchall()
                display_result(results)
                
            else:
                # For queries like INSERT, UPDATE, DELETE, etc.
                db_connection.commit()
                msg.showinfo("Success", "Query executed successfully.")

            cursor.close()

        except mysql.connector.Error as error:
            msg.showerror("Error", f"Error executing query: {error}")
    
    def display_result(results):
    # Function to display the results of the query in a new window
        result_window = Toplevel()
        result_window.title("Query Result")

        result_listbox = Listbox(result_window, width=100, height=20)
        result_listbox.pack(padx=10, pady=10)

        for row in results:
            result_listbox.insert(END, row)


    root1 = Toplevel()
    root1.title("SQL Query Executor")
    

    # Entry field for the user to input the SQL query
    query_entry = Entry(root1, width=100)
    query_entry.pack(padx=10, pady=5)
    

    # Button to execute the query
    execute_button = Button(root1, text="Execute Query", command=execute_query)
    execute_button.pack(pady=10)
   