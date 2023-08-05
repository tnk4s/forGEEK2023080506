import datetime
import pandas as pd
from datetime import date

import my_schedule as ms
from raise_Error_list import TimeError


class InsertCalender:
    def __init__(self, task_name: str, difficulty: int, due_date: str, now_time: datetime):
        # インスタンスの作成およびテーブルデータの取得
        self.db_system = ms.MySchedule()
        rs = self.db_system.get_shcs("Alice")
        self.rs = pd.DataFrame(rs).to_numpy()
        due_dateset = pd.DataFrame(rs["due_date"]).to_numpy()
        due_dateset = tuple(map(tuple, due_dateset))
        self.due_dateset = tuple(tuple(dates)[0] for dates in due_dateset)
        #print(self.rs)

        # 変数の定義
        self.task_name = task_name
        self.difficulty = int(difficulty)
        self.due_date = due_date
        self.task_list_ = None
        self.max_diff = 5
        self.exist_diff = None
        self.date_total_diff = {}
        self.now_time = date.fromisoformat(now_time)

        self.task_list = [
            "Alice", self.task_name, date.fromisoformat("2013-01-01"), date.fromisoformat(self.due_date), "detail",
            self.difficulty
        ]


        # 関数呼び出し
        self.cul_diff()
        self.input_table_data()

    # 入力を受付ます(タスク名(str) 難易度(int) 期限(year-month-day))
    def cul_diff(self):
        # 入力の受付
        # task_name, difficulty, self.due_date = input().split()
        # self.difficulty = int(difficulty)

        # 日付ごとの難易度合計を辞書型で作成
        for row in self.rs:
            rs_date = row[3]
            value = row[-1]

            if rs_date in self.date_total_diff:
                self.date_total_diff[rs_date] += value
            else:
                self.date_total_diff[rs_date] = value

    def input_table_data(self):
        flag = True
        prev_1day = datetime.timedelta(days=1)

        if date.fromisoformat(self.due_date) < self.now_time:
            raise TimeError



        # 予定がなかったらそのまま予定代入
        if self.due_date not in self.due_dateset:
            self.db_system.insert_sch([self.task_list])
        else:
            while flag:
                # 日付ごとの難易度を取得
                if self.due_date in self.date_total_diff:
                    diff_cul = self.date_total_diff[self.due_date]
                else:
                    diff_cul = 0

                # 難易度による条件分岐して予定をデータベースに保存
                if self.max_diff - diff_cul > self.difficulty:
                    self.task_list[3] = date.fromisoformat(self.due_date)
                    task_list = [self.task_list]
                    self.db_system.insert_sch(task_list)
                    flag = False

                # 予定に空きがなければ一日前をみる
                else:
                    self.due_date = date.fromisoformat(self.due_date)
                    self.due_date = self.due_date - prev_1day
                    if self.due_date < self.now_time:
                        raise TimeError
                        flag = False

                    self.due_date = str(self.due_date)


if __name__ == "__main__":
    ins = InsertCalender(task_name="task119", difficulty=4, due_date="2001-12-01", now_time="2019-12-30")
