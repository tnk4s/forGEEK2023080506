import datetime
import PySimpleGUI as sg

from page import Page

class InputFormPage(Page):
    def __init__(self, page_name, next_pages, main_window_flag):
        super().__init__(page_name, next_pages, main_window_flag)
        years = [str(i) for i in range(2023, 2031)]
        months = [str(i) for i in range(1, 13)]
        days = [str(i) for i in range(1, 32)]
        atimes = [str(i) for i in range(0, 25)]

        self.layout1 = [
            [sg.Text(self.page_name)],
            [sg.Text('下にタスクについて入力してください')],
            [sg.Text('ユーザ名:'), sg.InputText(key='user')],
            [sg.Text('タスク名:'), sg.InputText(key="name")],
            [sg.Text('締切日:'), sg.Combo(years, size=(10, 5), key='year'), sg.Text('年'),
             sg.Combo(months, size=(10, 5), key='month'), sg.Text('月'),
             sg.Combo(days, size=(10, 5), key='day'), sg.Text('日')],
            [sg.Text('タスク詳細:'), sg.Multiline(key="detail", size=(50, 10))],
            [sg.Text('必要時間:'), sg.InputText(size=(5, 1), key="time"), sg.Text('時間')],
            [sg.Button('Task', key = self.form_func)]]

        self.layout2 = [
            [sg.Text('活動時間を入力する日付を選択してください')],
            [sg.Text('日付:'), sg.Combo(years, size=(10, 5), key='year2'), sg.Text('年'),
             sg.Combo(months, size=(10, 5), key='month2'), sg.Text('月'),
             sg.Combo(days, size=(10, 5), key='day2'), sg.Text('日')],
            [sg.Text('下に活動時間入力してください')],
            [sg.Text('Time1:'),
             sg.Combo(atimes, size=(10, 5), key='a1'),
             sg.Text('時'),
             sg.Text('〜'),
             sg.Combo(atimes, size=(10, 5), key='a2'),
             sg.Text('時'),
             sg.Text('Time2:'),
             sg.Combo(atimes, size=(10, 5), key='a3'),
             sg.Text('時'),
             sg.Text('〜'),
             sg.Combo(atimes, size=(10, 5), key='a4'),
             sg.Text('時'),
             sg.Text('Time3:'),
             sg.Combo(atimes, size=(10, 5), key='a5'),
             sg.Text('時'),
             sg.Text('〜'),
             sg.Combo(atimes, size=(10, 5), key='a6'),
             sg.Text('時')],
            [sg.Button('ActiveTime', key = self.form_func2)]]
        
        self.this_layout = [[sg.Frame('タスク入力欄', self.layout1)], [sg.Frame('活動時間入力欄', self.layout2)]]
  
    def form_func(self):
        hizuke = datetime.date(int(self.my_values['year']), int(self.my_values['month']), int(self.my_values['day']))
        nowtime = datetime.datetime.now()

        print(self.my_values['user']+'\n')
        print(self.my_values['name']+'\n')
        print(hizuke.isoformat()+'\n')
        print(self.my_values['detail']+'\n')
        print(self.my_values['time']+'\n')
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

    def form_func2(self):
        
        return self.stable_flag

    
