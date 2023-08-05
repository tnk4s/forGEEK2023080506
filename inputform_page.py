import datetime
import PySimpleGUI as sg

from page import Page

class InputFormPage(Page):
    def __init__(self, page_name, next_pages, main_window_flag):
        super().__init__(page_name, next_pages, main_window_flag)
        years = [str(i) for i in range(2023, 2031)]
        months = [str(i) for i in range(1, 13)]
        days = [str(i) for i in range(1, 32)]

        self.this_layout = [
            [sg.Text(self.page_name)],
            [sg.Text('下にタスクについて入力してください')],
            [sg.Text('ユーザ名:'), sg.InputText(key='user')],
            [sg.Text('タスク名:'), sg.InputText(key="name")],
            [sg.Text('締切日:'), sg.Combo(years, size=(10, 5), key='year'), sg.Text('年'), sg.Combo(months, size=(10, 5), key='month'), sg.Text('月'), sg.Combo(days, size=(10, 5), key='day'), sg.Text('日')],
            [sg.Text('タスク詳細:'), sg.Multiline(key="detail", size=(50, 10))],
            [sg.Text('必要時間:'), sg.InputText(size=(5, 1), key="time"), sg.Text('時間')],
            [sg.Button('Enter', key = self.form_func)]]
  
    def form_func(self):
        hizuke = datetime.date(int(self.my_values['year']), int(self.my_values['month']), int(self.my_values['day']))
        nowtime = datetime.datetime.now()

        print(self.my_values['user']+'\n')
        print(self.my_values['name']+'\n')
        print(hizuke.isoformat()+'\n')
        print(self.my_values['detail']+'\n')
        print(str(self.my_values['time'])+'\n')
        print(nowtime.isoformat())
        
        self.window['user'].update('')
        self.window['name'].update('')
        self.window['year'].update('')
        self.window['month'].update('')
        self.window['day'].update('')
        self.window['detail'].update('')
        self.window['time'].update('')

        super().leave()
        return self.next_page_names[0]
    
