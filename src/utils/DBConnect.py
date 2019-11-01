import os, sqlite3

class DBConnect:
    def __init__(self):
        try:
            self.db   = None
            self.conn = None
            print("DBConnect initialized...")
        except Exception as e:
            print("Exception raised:")
            print(e)
            raise

    def createConnection(self):
        self.db   = sqlite3.connect('static/db/database.db')
        self.conn = self.db.cursor()

    def closeConnection(self):
        self.conn.close()


    def createEntry(self, args):
        try:
            # Example Insert
            # sql = "INSERT INTO bills (Title, Amount, MoYr, Duedate, Optional) Values(?,?,?,?,?)";
            # ps  = (TITLE, float(AMOUNT), MOYR, DATE, OPTIONAL, )
            self.conn.execute(sql, ps)
            self.db.commit()
        except Exception as e:
            print("Exception raised:")
            print(e)

    def updateEntry(self, args):
        try:
            # Example Update
            # sql = "UPDATE bills SET Title = ?, Amount = ?, MoYr = ?, Duedate = ?, Optional = ? WHERE id = ?";
            # ps  = (TITLE, float(AMOUNT), MOYR, DATE, OPTIONAL, int(ID), )
            self.conn.execute(sql, ps)
            self.db.commit()
        except Exception as e:
            print("Exception raised:")
            print(e)

    def deleteEntry(self, ID):
        try:
            # Example Delete
            # sql = "DELETE FROM bills WHERE id = ?";
            # ps  = (int(ID), )
            self.conn.execute(sql, ps)
            self.db.commit()
        except Exception as e:
            print("Exception raised:")
            print(e)
