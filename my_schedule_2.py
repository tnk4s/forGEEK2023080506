import sqlite3
import pandas as pd
from datetime import date
import datetime


class MySchedule:
    def __init__(self):
        self.db_name = "shedule.db"
        self.table_name = "taskCalender"

    def create_table(self):
        conn = sqlite3.connect(self.db_name)
        cur = conn.cursor()

        sstr = "CREATE TABLE IF NOT EXISTS " + self.table_name + "(master_id  int, title varchar(50), due_date datetime, id int, exe_date datetime,  detail varchar(500), PRIMARY KEY(master_id, id))"

        cur.execute(sstr)
        conn.commit()

        cur.close()
        conn.close()

    def insert_sch(self, task_list):
        # "task_list = [(master_id, title, due_date, id, exe_date, detail)]"
        conn = sqlite3.connect(self.db_name)
        cur = conn.cursor()

        sstr = "INSERT INTO " + self.table_name + " VALUES(?, ?, ?, ?, ?, ?)"
        cur.executemany(sstr, task_list)
        conn.commit()

        cur.close()
        conn.close()

    def insert_dummy(self):  # for debag
        '''
        task_list = [#(master_id, title, due_date, id, exe_date, detail)
            (202308051821, "task00", datetime.datetime.fromisoformat('2023-12-05T23:59:59'), 0, datetime.datetime.fromisoformat('2023-12-04T20:15:00'), "Hello World"),
            (202308051821, "task00", datetime.datetime.fromisoformat('2023-12-05T23:59:59'), 1, datetime.datetime.fromisoformat('2023-12-04T20:30:00'), "Hello World"),
            (202308051821, "task00", datetime.datetime.fromisoformat('2023-12-05T23:59:59'), 2, datetime.datetime.fromisoformat('2023-12-05T08:00:00'), "Hello World"),
            (202308051821, "task00", datetime.datetime.fromisoformat('2023-12-05T23:59:59'), 3, datetime.datetime.fromisoformat('2023-12-05T08:15:00'), "Hello World"),
            (202308060909, "task01", datetime.datetime.fromisoformat('2023-12-04T23:59:59'), 0, None , "test detail str"),
            (202308060909, "task01", datetime.datetime.fromisoformat('2023-12-04T23:59:59'), 1, None, "test detail str")
        ]'''
        task_list = [  # (master_id, title, due_date, id, exe_date, detail)
            (202308061821, "cal_test0", datetime.datetime.fromisoformat('2023-12-05T23:59:59'), 0,
             datetime.datetime.fromisoformat('2023-08-04T20:15:00'), "Hello World"),
            (202308061821, "cal_test0", datetime.datetime.fromisoformat('2023-12-05T23:59:59'), 1,
             datetime.datetime.fromisoformat('2023-08-04T20:30:00'), "Hello World"),
            (202308061821, "cal_test0", datetime.datetime.fromisoformat('2023-12-05T23:59:59'), 2,
             datetime.datetime.fromisoformat('2023-08-05T08:00:00'), "Hello World"),
            (202308061821, "cal_test0", datetime.datetime.fromisoformat('2023-12-05T23:59:59'), 3,
             datetime.datetime.fromisoformat('2023-08-05T08:15:00'), "Hello World"),
            (202308090909, "task03", datetime.datetime.fromisoformat('2023-12-04T23:59:59'), 0,
             datetime.datetime.fromisoformat('2023-08-05T08:15:00'), "test detail str"),
            (202308090909, "task03", datetime.datetime.fromisoformat('2023-12-04T23:59:59'), 1,
             datetime.datetime.fromisoformat('2023-08-05T08:15:00'), "test detail str")
        ]
        self.insert_sch(task_list)

    def update_shcs(self, master_id, iid, new_exe_date):
        conn = sqlite3.connect(self.db_name)
        cur = conn.cursor()

        sstr = "UPDATE " + self.table_name + " SET exe_date='" + new_exe_date + "' WHERE master_id=" + str(
            master_id) + " AND id=" + str(iid)

        try:
            cur.execute(sstr)

        except sqlite3.Error as e:
            print("error", e.args[0])
        conn.commit()

        cur.close()
        conn.close()

    def get_shcs(self, exe_date=None):
        conn = sqlite3.connect(self.db_name)
        cur = conn.cursor()

        sstr = "SELECT * FROM " + self.table_name
        if not exe_date == None:
            sstr += (" WHERE exe_date LIKE '" + exe_date + "'")  # For example, exe_date = '2022-11-24'

        df = pd.read_sql(sstr, conn)

        cur.close()
        conn.close()

        return df
    
    def get_shcs_after(self, start_datetime):
        conn = sqlite3.connect(self.db_name)
        cur = conn.cursor()

        sstr = "SELECT * FROM " + self.table_name + " WHERE due_date > '" + start_datetime + "'"
        
        df = pd.read_sql(sstr, conn)

        cur.close()
        conn.close()

        return df

    def delete_shcs(self, mid, task_name):
        conn = sqlite3.connect(self.db_name)
        cur = conn.cursor()

        sstr = "DELETE FROM " + self.table_name + " WHERE master_id='" + mid + "' AND title='" + task_name + "'"
        print(sstr)
        try:
            cur.execute(sstr)
            print("do")

        except sqlite3.Error as e:
            print("error",e.args[0])
        conn.commit()

        cur.close()
        conn.close()

if __name__ == "__main__":
    db_system = MySchedule()
    db_system.create_table()
    db_system.insert_dummy()
    #db_system.update_shcs(202308051821, 3 ,'2023-12-05 09:30:00')
    #rs = db_system.get_shcs('2023-12-05%')
    #db_system.delete_shcs("202308051821", "task00")
    rs = db_system.get_shcs()
    print(rs)