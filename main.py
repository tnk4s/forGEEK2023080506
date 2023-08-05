from calender_page import CalenderPage
from dummy_page import DummyPage

if __name__ == "__main__":
    pages ={
        "INPUT_FORM" : DummyPage("INPUT_FORM", ["CALENDER"], True),
        "CALENDER" : CalenderPage("CALENDER", ["INPUT_FORM", "DAILY_TASKS"], True),#keyとページインスタンスの第一引数は同じものを推奨
        "DAILY_TASKS" : DummyPage("DAILY_TASKS", ["CALENDER"], True)
    } 
        
    base_window = "INPUT_FORM"
    window = pages[base_window]#初期ページを設定
    window.wake_up_window()
    while True:
        next_page= window.loop_funcs()
        if next_page == window.get_break_flag():
            break

        elif not next_page == window.get_stable_flag():
            x, y = window.get_last_xy()
            window = pages[next_page]
            window.wake_up_window(x, y)
        
        elif next_page == window.get_stable_flag():
            continue
        
    #window.close()    
