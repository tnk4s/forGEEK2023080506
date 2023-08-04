import PySimpleGUI as sg
import datetime

class InputForm:
    def __init__(self):
        sg.theme('LightBlue')
        
        years = [str(i) for i in range(2023, 2031)]
        months = [str(i) for i in range(1, 13)]
        days = [str(i) for i in range(1, 32)]
        levels = [i for i in range(1, 6)]

        self.layout = [[sg.Text('下にタスクについて入力してください')],
                    [sg.Text('ユーザ名'), sg.InputText(key='user')],
                    [sg.Text('タスク名'), sg.InputText(key="name")],
                    [sg.Text('締切日'), sg.Combo(years, size=(10, 5), key='year'), sg.Text('年'), sg.Combo(months, size=(10, 5), key='month'), sg.Text('月'), sg.Combo(days, size=(10, 5), key='day'), sg.Text('日')],
                    [sg.Text('タスク詳細'), sg.Multiline(key="detail", size=(50, 10))],
                    [sg.Text('難易度'), sg.Combo(levels, size=(5, 1), key="level")],
                    [sg.Button('Enter')]]

        self.window = sg.Window('  タスク入力フォーム  ', self.layout)

    def function(self):
        while True:
            event,values=self.window.read()
            if event==sg.WIN_CLOSED:
                break
            if event=='Enter':
                hizuke = datetime.date(int(values['year']), int(values['month']), int(values['day']))

                print(values['user']+'\n')
                print(values['name']+'\n')
                print(hizuke.isoformat()+'\n')
                print(values['detail']+'\n')
                print(str(values['level'])+'\n')
               
                self.window['user'].update('')
                self.window['name'].update('')
                self.window['year'].update('')
                self.window['month'].update('')
                self.window['day'].update('')
                self.window['detail'].update('')
                self.window['level'].update('')
                

        self.window.close()

if __name__ == "__main__":
    IF = InputForm()
    IF.function()