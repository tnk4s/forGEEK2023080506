import PySimpleGUI as sg

class Page:
    def __init__(self, page_name, next_page_names, main_window_flag):
        self.page_name = page_name
        self.this_layout = []
        self.window = None
        self.last_x = None
        self.last_y = None

        self.break_flag = "BREAK"
        self.stable_flag = "STABLE"
        self.next_page_names = next_page_names #list

        self.main_window_flag = main_window_flag
        
    def __set_window(self, init_x = None, init_y = None):
        self.window = sg.Window(self.page_name, self.this_layout, finalize=True, size=(1200, 700), location=(init_x, init_y))

    def wake_up_window(self, init_x = None, init_y = None): 
        if self.main_window_flag:
            if self.window == None:
                self.__set_window(init_x, init_y)
            else:
                #self.window.location=(init_x, init_y)
                self.window.UnHide()   
        else:
            self.__set_window(init_x, init_y)


    def loop_funcs(self):
        event, values = self.window.read()
        if event == sg.WIN_CLOSED or event == "Exit" or event is None:#プログラム自体を終了
            return self.break_flag

        elif callable(event):# keyに関数が設定されている場合、設定されている関数をそのまま実行する
            return event()#次の移動先を返す，もしくは"STABLE"か"BREAK"

        else:
            return self.stable_flag #現在のページを維持
    
    def leave(self):
        self.last_x, self.last_y = self.window.current_location()
        if self.main_window_flag:
            self.window.Hide()
        else:
            self.window.close()
        

    def get_last_xy(self):
        return self.last_x, self.last_y
    
    def get_break_flag(self):
        return self.break_flag
    
    def get_stable_flag(self):
        return self.stable_flag