import PySimpleGUI as sg
from datetime import date
import pandas as pd
import numpy as np
import sqlite3
from my_schedule_2 import MySchedule

from page import Page

class OneDayPlanPage(Page):
    def __init__(self, page_name, next_pages, main_window_flag):
        super().__init__(page_name, next_pages, main_window_flag)
        header = ['masterid', 'タスク名', '期限', 'id', '予定日', '詳細']
        width = [10, 10, 10, 10, 10, 10]
        years = [str(i) for i in range(2022, 2031)]
        months = [str(i) for i in range(1, 13)]
        days = [str(i) for i in range(1, 32)]
        self.schedule = []
        self.graph = sg.Graph((1200, 300), (0, 0), (1440, 1440), background_color="#7f7f7f")
        self.db_system = MySchedule()
        frame1 = sg.Frame('入力フォーム', [[sg.Text(self.page_name)],
             [sg.Text('日付指定'), sg.Combo(years, size=(10, 5), key='-YEAR-'), sg.Text('年'), sg.Combo(months, size=(10, 5), key='-MONTH-'), sg.Text('月'), sg.Combo(days, size=(10, 5), key='-DATE-'), sg.Text('日')],
            [sg.Button('タスク入力', key = self.submit_button_func), sg.Button('終了', key = self.go_back)]],size=(1200, 100))

        frame2 = sg.Frame('計画表', [[sg.Table(self.schedule, headings=header, col_widths=width, key='-TABLE-',  font=('Arial',20), def_col_width=20, auto_size_columns=False, vertical_scroll_only=False)]], size=(1200, 300))
        frame3 = sg.Frame('ガントチャート', [[self.graph]], size=(1200, 300))
        self.this_layout = [
            [frame1],
            [frame2],
            [frame3]
             ]
        
            
    def submit_button_func(self):
        self.graph.Erase()
        do_date = date(int(self.my_values['-YEAR-']), int(self.my_values['-MONTH-']), int(self.my_values['-DATE-']))
        conn = sqlite3.connect(self.db_system.db_name)
        cur = conn.cursor()
        sstr = f"SELECT * FROM {self.db_system.table_name} WHERE exe_date like '{do_date}%'"
        print(sstr)
        df = pd.read_sql(sstr, conn)
        # print(df)
        cur.close()
        conn.close()
        # df = self.db_system.get_shcs('Alice', do_date=f"'{do_date}'")
        schedule = df.values.tolist()
        unique_task = df['title'].unique()
        # それぞれのタスクの時間，数
        task_start_list = []

        start_time = []
        task_count = []



        for task in  unique_task:
            tmp_df = df[df['title'] == task]
            time_str = tmp_df['exe_date'][0].split()[1]
            hours = int(time_str.split(':')[0]) * 60
            minutes = int(time_str.split(':')[1])
            start = hours + minutes
            start_time.append(start) # スタートタイムをとってくる
            task_count.append(len(tmp_df))
            task_start_list.append(tmp_df['exe_date'][0].split()[1])

        print(start_time)
        print(task_count)

        

            


        task_time = np.array(task_count) * 15
        
        # self.graph.draw_rectangle((480, 1140),(540, 1000), fill_color="#505050", line_color="#606060", line_width=1)
        for start, length, task_name, task_start in zip(start_time, task_time, unique_task, task_start_list):

            self.graph.draw_rectangle((start, 1140),(start+length, 950), fill_color="#505050", line_color="#606060", line_width=1)
            self.graph.draw_text(f"{task_name}", (start, 1100), color="#eeeeee", text_location=sg.TEXT_LOCATION_LEFT)
            self.graph.draw_text(f"{task_start}~", (start, 1000), color="#eeeeee", text_location=sg.TEXT_LOCATION_LEFT)
        
        self.window['-TABLE-'].update(values=schedule)

        return self.stable_flag
    
    def recive_inputs():
        pass

    def go_back(self):
        print("終了!")
        super().leave()
        return self.next_page_names[0]