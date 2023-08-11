from tkinter import*
import tkinter.messagebox as msg
import mysql.connector

db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="145632sk",
    database="mldb"
)
def table():
    def show_tables():
        try:
            cursor = db_connection.cursor()
            cursor.execute("SHOW TABLES")
            tables = cursor.fetchall()
            cursor.close()

            if not tables:
                msg.showwarning("Warning", "No tables found in the database.")
                return

            display_tables(tables)

        except mysql.connector.Error as error:
            msg.showerror("Error", f"Error fetching table names: {error}")

    def display_tables(tables):
        # Function to display the list of tables in a new window
        table_window = Toplevel()
        table_window.title("Tables in Database")

        table_listbox = Listbox(table_window, width=50, height=20)
        table_listbox.pack(padx=10, pady=10)

        for table in tables:
            table_listbox.insert(END, table[0])

    
    show_tables()






