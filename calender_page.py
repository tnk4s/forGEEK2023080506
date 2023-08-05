from datetime import date
import PySimpleGUI as sg

import calendar

from page import Page

class CalenderPage(Page):
    def __init__(self, page_name, next_pages, main_window_flag):
        super().__init__(page_name, next_pages, main_window_flag)
        self.my_today = date.today()
        self.this_layout = [
            [sg.Text(self.page_name)],
            self.__create_calender_layout(self.my_today),
            [sg.Button("Func", key = self.func1)],
            [sg.Button("Next", key = self.go_next_page)],
            [sg.Button("Back", key = self.go_back)]
            
        ]

    def __create_calender_layout(self, cal_date):
        weekday = ['SUN','MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']  
        cal = calendar.Calendar(firstweekday=6)
        days = cal.monthdatescalendar(cal_date.year, cal_date.month)
        layout = [[sg.Text(cal_date.year, font=(None, 13, 'bold'))],
                [sg.Push(), sg.Button('<<'), sg.Button('<'), sg.Text(cal_date.month, font=(None, 30)), sg.Button('>'), sg.Button('>>'), sg.Push()]]
        inner = []
        
        for week in weekday:
            inner.append(sg.Text(week, size=(4,1), text_color='white', background_color='green', justification='center'))
        layout.append(inner.copy())

        def date_judgement(i, day):
            if day == self.my_today:
                return sg.Text(day.day, size=(4,1), justification='right', text_color='white', background_color='gray')
            elif i == 0 and day.month == cal_date.month:
                return sg.Text(day.day, size=(4,1), justification='right', text_color='red')
            elif i == 6 and day.month == cal_date.month:
                return sg.Text(day.day, size=(4,1), justification='right', text_color='blue')
            elif day.month == cal_date.month:
                return sg.Text(day.day, size=(4,1), justification='right')
            elif i == 0:
                return sg.Text(day.day, size=(4,1), justification='right', text_color='#ff9999')
            elif i == 6:
                return sg.Text(day.day, size=(4,1), justification='right', text_color='#9999ff')
            else:
                return sg.Text(day.day, size=(4,1), justification='right', text_color='#cccccc')

        for row in days:
            inner = []
            for i, day in enumerate(row):
                sg_text = date_judgement(i, day)
                inner.append(sg_text)
            layout.append(inner.copy())
        return layout
    
    def func1(self):
        print("func1")
        return self.stable_flag
    
    def go_next_page(self):
        print("func2")
        super().leave()
        return self.next_page_names[1]
    
    def go_back(self):
        print("func2")
        super().leave()
        return self.next_page_names[0]

    