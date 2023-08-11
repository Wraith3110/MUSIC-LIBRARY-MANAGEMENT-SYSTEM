from tkinter import*
import tkinter.messagebox as msg
import mysql.connector

db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="145632sk",
    database="mldb"
)
def dip():
    def display_data():
        table_name = table_name_entry.get()

        try:
            cursor = db_connection.cursor()
            query = f"SELECT * FROM {table_name}"
            cursor.execute(query)
            data = cursor.fetchall()
            cursor.close()

            if not data:
                msg.showwarning("Warning", f"No data found in table '{table_name}'.")
                return

            display_result(data)

        except mysql.connector.Error as error:
            msg.showerror("Error", f"Error fetching data from table '{table_name}': {error}")

    def display_result(results):
        # Function to display the results of the query in a new window
        result_window = Toplevel(root)
        result_window.title("Table Data")

        result_listbox = Listbox(result_window, width=100, height=20)
        result_listbox.pack(padx=10, pady=10)

        for row in results:
            result_listbox.insert(END, row)

    # Create the main application window
    root = Toplevel()
    root.title("Table Data Viewer")

    # Entry field for the user to input the table name
    table_name_entry = Entry(root, width=50)
    table_name_entry.pack(padx=10, pady=5)

    # Button to display the data from the specified table
    display_button = Button(root, text="Display Data", command=display_data)
    display_button.pack(pady=10)

 