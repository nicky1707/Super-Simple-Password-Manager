import clipboard
import sqlite3
import os
from pathlib import Path

# Create a new database at appdata if it doesn't exist
path = os.getenv('APPDATA')
try:
    os.mkdir(path + '\\test')
except FileExistsError:
    pass

fle = Path(path + '\\test\\pass.db')
fle.touch(exist_ok=True)

# Class based sqlite3 database for storing passwords 
class Database:
    def __init__(self):
        self.con = sqlite3.Connection(path+'\\test\\pass.db')
        self.cur = self.con.cursor()
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS user_pass
            (name text PRIMARYKEY, pass text,description text)
        """)
        self.con.commit()

    def check(self):
        print('Hello world')

    def get_pass(self, name):
        self.cur.execute("""
            SELECT pass FROM user_pass WHERE name = ?
        """, (name,))
        return self.cur.fetchone()

    def add_pass(self, name, passw, description=""):
        self.cur.execute("""
            INSERT OR IGNORE INTO user_pass values(?,?,?)""", (name, passw, description))
        self.con.commit()

    def delete_pass(self, name):
        self.cur.execute("""
            DELETE FROM user_pass WHERE name = ?
        """, (name,))
        self.con.commit()

    def update_pass(self, name, passw):
        self.cur.execute("""
            UPDATE user_pass SET pass = ? WHERE name = ?
        """, (passw, name))
        self.con.commit()

    def get_all_pass(self):
        self.cur.execute("""
            SELECT * FROM user_pass
        """)
        return self.cur.fetchall()

    def close(self):
        self.con.close()

# Create a new database object
new_databse = Database()

# Main function loop
def main():

    loop = True
    while loop == True:
        print("""
  ________________________
 | 1.Create new password  |
 | 2.Saved passwords      |
 | 3.Delete a password    |
 | 4.Quit                 |
 |________________________|
 
			""")
        choice = input(":: ")

        if choice == "1":
            name = input("Name: ")
            password = input("Password: ")
            description = input("Description: ")
            new_databse.add_pass(name, password, description)
            clipboard.copy(password)
            print("Password copied to clipboard")

        elif choice == "2":
            query = new_databse.get_all_pass()
            print("")

            for i in query:
                print(f" {i[0]} \t  : {i[1]} {i[2]} ")
        elif choice == "3":
            query = new_databse.get_all_pass()
            print('')
            for i in query:
                print(f" {i[0]} \t  : {i[1]} {i[2]} ")
            print('')
            name = input("Delete Name :: ")
            conformation = input(
                "Are you sure you want to delete this password? [ y/n ]: ")

            if conformation == "y":
                new_databse.delete_pass(name)
                print("Password deleted")

            else:
                print("Password not deleted")

        elif choice == "4":
            loop = False
            print("Goodbye !!")

        else:
            print(choice)
            password = new_databse.get_pass(choice)[0]
            print("Password copied to clipboard !")
            clipboard.copy(password)


if __name__ == "__main__":
    main()
