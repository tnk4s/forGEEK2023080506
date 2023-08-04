from datetime import date
import PySimpleGUI as sg

import calendar

from page import Page

class DummyPage(Page):
    def __init__(self, page_name, next_page_names, main_window_flag):
        super().__init__(page_name, next_page_names, main_window_flag)
        self.this_layout = [
            [sg.Text(self.page_name)],
            [sg.Button("FUNC", key = self.stabule_func)],
            [sg.Button("Go Next or Back", key = self.go_next_page)],
            [sg.Button("Exit", key = self.quit_all)]
        ]
    
    def stabule_func(self):#ページ（画面）はそのまま，何かしらの処理
        print("func1")
        return self.stable_flag
    
    def go_next_page(self):#次のページ（画面）へ
        print("go_next_page")
        super().leave()
        return self.next_page_names[0]
    
    def quit_all(self):#システムそのものを終了
        print("quit_all on dummy")
        super().leave()
        return self.break_flag