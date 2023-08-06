class TimeError(Exception):
    def __init__(self):
        pass

    def errTime(self):
        print("エラー：締切日が現在より前，もしくは予定がいっぱいです")
        exit
