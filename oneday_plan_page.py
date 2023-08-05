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
        width = [10, 10, 10, 10, 10, 10]
        years = [str(i) for i in range(2022, 2031)]
        months = [str(i) for i in range(1, 13)]
        days = [str(i) for i in range(1, 32)]
        self.schedule = []
        self.db_system = MySchedule()
        frame1 = sg.Frame('入力フォーム', [[sg.Text(self.page_name)],
             [sg.Text('日付指定'), sg.Combo(years, size=(10, 5), key='-YEAR-'), sg.Text('年'), sg.Combo(months, size=(10, 5), key='-MONTH-'), sg.Text('月'), sg.Combo(days, size=(10, 5), key='-DATE-'), sg.Text('日')],
            [sg.Button('送信', key = self.submit_button_func), sg.Button('終了', key = self.go_back)]],size=(500, 700))

        frame2 = sg.Frame('計画表', [[sg.Table(self.schedule, headings=header, col_widths=width, key='-TABLE-', size=(400, 500))]], size=(400, 700))
        self.this_layout = [
            [frame1,
             frame2]
             ]
        # self.this_layout = [
        #     [sg.Text(self.page_name)],
        #      [sg.Text('日付指定'), sg.Combo(years, size=(10, 5), key='-YEAR-'), sg.Text('年'), sg.Combo(months, size=(10, 5), key='-MONTH-'), sg.Text('月'), sg.Combo(days, size=(10, 5), key='-DATE-'), sg.Text('日')],
        #     [sg.Button('送信', key = self.submit_button_func), sg.Button('終了', key = self.go_back)], 
        #     [sg.Table(self.schedule, headings=header, key='-TABLE-', size=(160, 80))]
        # ]
    
    def submit_button_func(self):
        
        do_date = date(int(self.my_values['-YEAR-']), int(self.my_values['-MONTH-']), int(self.my_values['-DATE-']))
        print(do_date)
        df = self.db_system.get_shcs('Alice', do_date=f"'{do_date}'")
        schedule = df.values.tolist()
        self.window['-TABLE-'].update(values=schedule)

        return self.stable_flag
    
    def go_back(self):
        print("終了!")
        super().leave()
        return self.next_page_names[0]