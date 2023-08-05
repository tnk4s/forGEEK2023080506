import PySimpleGUI as sg
from datetime import date
import pandas as pd
import sqlite3
from my_schedule import MySchedule

from page import Page

class OneDayPlanPage(Page):
    def __init__(self, page_name, next_pages, main_window_flag):
        super().__init__(page_name, next_pages, main_window_flag)
        header = ['ユーザー名', 'タスク', '予定日', '期限', '詳細', '難易度']
        self.schedule = []
        self.db_system = MySchedule()
        self.this_layout = [
            [sg.Text(self.page_name)],
            [sg.Text('日付入力'), sg.Input(key='-DATE-'), sg.Button('送信', key = self.submit_button_func), sg.Button('終了', key = self.go_back)], 
            [sg.Table(self.schedule, headings=header, key='table')]
        ]
    
    def submit_button_func(self):
        do_date = self.my_values['-DATE-']
        df = self.db_system.get_shcs('Alice', do_date=f"'{do_date}'")
        schedule = df.values.tolist()
        self.window['table'].update(values=schedule)

        return self.stable_flag
    
    def go_back(self):
        print("終了!")
        super().leave()
        return self.next_page_names[0]