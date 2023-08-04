import sqlite3
import pandas as pd

class MySchedule:
    def __init__(self):
        self db_name = "hoge.db"
        self table_name = "taskCalender"

    def create_table(self):
        conn = sqlite3.connect(self.db_name)
        cur = conn.cursor()

        sstr = "CREATE TABLE IF NOT EXISTS " + self.table_name + "(user_name  varchar(50), title varchar(50), do_date smalldatetime, due_date smalldatetime, detail varchar(500), diffculty int,"\
            + " PRIMARY KEY(user_name, title, do_date))DEFAULT CHARSET=utf8;"

        cur.execute(sstr)
        conn.commit()

        cur.close()
        conn.close()
        

    def insert_sch(self, task_list)
        "task_list = [(user_name, title, do_date, due_date, detail, diffculty)]
        conn = sqlite3.connect(self.db_name)
        cur = conn.cursor()

        sstr = "INSERT INTO " + self.table_name + " VALUES(?, ?, ?, ?, ?, ?)"
        cur.executemany(sstr, task_list)
        conn.commit()

        cur.close()
        conn.close()

    def insert_dummy(self):#fro debag
        task_list = [#(user_name, title, do_date, due_date, detail, diffculty)
            ("Alice", "task00", date.fromisoformat('2022-12-03'), date.fromisoformat('2023-12-04'), "Hello World", 3),
            ("Alice", "task01", date.fromisoformat('2022-12-04'), date.fromisoformat('2024-01-01'), "test detail str", 5)
            ("Bob", "ほげ", date.fromisoformat('2022-11-24'), date.fromisoformat('2022-11-29'), "あああああ！", 1)
        ]
        self.insert_sch(task_list)

    def get_shcs(self, user_name, do_date=None, due_date=None):
        conn = sqlite3.connect(self.db_name)
        cur = conn.cursor()

        sstr = "SELECT FROM " + self.table_name + " WHERE user_name = " + user_name
        if not do_date == None:
            sstr += (" AND do_date = " + do_date)
        if not due_date == None:
            sstr += (" AND due_date = " + due_date)
        
        df = pd.read_sql(sstr, conn)

        cur.close()
        conn.close()

        return df



if __name__ == "__main__":
    db_system = MySchedule()
    db_system.create_table()
    db_system.insert_dummy()
    rs = db_system.get_shcs("Alice")
    print(rs)