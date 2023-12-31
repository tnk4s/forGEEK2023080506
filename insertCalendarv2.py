import calendar
import datetime
from datetime import datetime
import pandas as pd
import numpy as np
import random

import my_schedule_2 as ms
# from raise_Error_list import TimeError


class InsertCalendarv2:
    def __init__(self, res: int):
        self.db_system = ms.MySchedule()
        rs = self.db_system.get_shcs()
        self.rs = pd.DataFrame(rs).to_numpy()
        # print(self.rs)

        # タスクの個数
        self.num_tasks = len(self.rs)

        # タスクの入力日時取得
        nowtimelist = []
        for task in range(self.num_tasks):
            nowtimelist.append(self.rs[task][0])
        earliest = max(nowtimelist)
        earliest = str((earliest // 10) * 10 + 10)
        earliest = datetime.strptime(earliest, "%Y%m%d%H%M")
        last_day = calendar.monthrange(earliest.year, earliest.month)[1]

        # エラー対策
        if earliest.day == last_day and earliest.hour == 23 and earliest.minute == 50:
            # 12月以外
            if earliest.month != 12:
                earliest = earliest.replace(month=earliest.month+1, day=1, hour=0, minute=0)
            else:
                earliest = earliest.replace(year=earliest.year+1, month=1, hour=0, minute=0)

        self.earliest = earliest

        # タスクの締め切り日時取得
        self.duetimelist = []
        self.duetimelist2 = [] #各タスクの締切日str

        for task in range(self.num_tasks):
            duedate = self.rs[task][2]
            duedate = duedate.replace("-", "")
            duedate = duedate.replace(":", "")
            duedate = duedate.replace(" ", "")
            duedate = duedate[:-2]
            duedate2 = duedate[:-2]
            duedate = datetime.strptime(duedate, "%Y%m%d%H%M")

            last_day_due = calendar.monthrange(duedate.year, duedate.month)[1]
            duedate = duedate.replace(minute=(duedate.minute // 10) * 10) #第一の位を0

            # エラー対策
            if duedate.day == last_day_due and duedate.hour == 23 and duedate.minute == 50:
                # 12月以外
                if duedate.month != 12:
                    duedate = duedate.replace(month=duedate.month + 1, day=1, hour=0, minute=0)
                else:
                    duedate = duedate.replace(year=duedate.year + 1, month=1, hour=0, minute=0)

            self.duetimelist.append(duedate)
            self.duetimelist2.append(duedate2)

        finaldeadline = max(self.duetimelist)
        finaldeadline = str(finaldeadline)
        finaldeadline = finaldeadline.replace("-", "")
        finaldeadline = finaldeadline.replace(":", "")
        finaldeadline = finaldeadline.replace(" ", "")
        finaldeadline = finaldeadline[:-2]
        finaldeadline = datetime.strptime(finaldeadline, "%Y%m%d%H%M")

        num_mass = (finaldeadline - earliest).total_seconds() / 60
        num_mass = int(-(-num_mass // res)) #マスの数
        #print(num_mass)
        # すでに予定が入ってるものたち　及び，タスクが何分割されてるか数える
        self.exist_plan_list = []
        self.exist_plan_list2 = []
        self.num_tasks_list = []
        self.due_mass_list = []  # 各タスクの締め切りマス
        num = -1
        for task in range(self.num_tasks):
            hisnum_mass = str(self.rs[task][4])
            if hisnum_mass != "None":
                hisnum_mass = hisnum_mass.replace("-", "")
                hisnum_mass = hisnum_mass.replace(":", "")
                hisnum_mass = hisnum_mass.replace(" ", "")
                hisnum_mass = hisnum_mass[:-2]
                hisnum_mass = datetime.strptime(hisnum_mass, "%Y%m%d%H%M")
                hisnum_mass = (hisnum_mass - earliest).total_seconds() / 60
                hisnum_mass = int(-(-hisnum_mass // res))

                self.exist_plan_list.append(hisnum_mass)

            # タスクの分割数を保存
            if self.rs[task][3] == 0:
                self.num_tasks_list.append(1)
                due_mass = (self.duetimelist[task] - earliest).total_seconds() / 60
                due_mass = int(-(-due_mass // res))  # マスの数
                self.due_mass_list.append(due_mass)
                #print(self.due_mass_list)
                # 新規タスク0，元々あるタスク1
                if self.rs[task][4] is None:
                    self.exist_plan_list2.append(0)
                else:
                    self.exist_plan_list2.append(1)

                num += 1
            else:
                self.num_tasks_list[num] += 1

        #print(f"タスクごとの回数self.num_tasks_list: {self.num_tasks_list}")
        # 入力日から最終締切日までの15分刻み分基礎テーブル作成
        self.kiso_table = np.zeros((len(self.num_tasks_list), num_mass))
        self.kiso_table_exist = self.kiso_table.copy()

        # 元の予定テーブル作成
        num = 0
        for i in self.exist_plan_list2:
            if i == 1:
                for exist_num in self.exist_plan_list:
                    self.kiso_table_exist[num][exist_num] = 1
                num += 1

        print(self.duetimelist2)
        self.base_table = self.kiso_table_exist.copy()

    def generate_plan(self) -> np.ndarray:
        num = 0
        for i in self.exist_plan_list2:
            buf = 0
            if i == 0:
                while buf < self.num_tasks_list[num]:
                    n = np.random.randint(0, self.exist_plan_list[num])
                    if self.base_table[num][n] == 0:
                        self.base_table[num][n] = 1
                        buf += 1
            num += 1
        #kd = self.base_table * self.kiso_table_exist
        #dsa = 0
        #for i in range(2):
        #    for j in range(1020):
        #        if kd[i][j] == 1:
        #            print(i)
        #            dsa += 1
        #print(dsa)
        return self.base_table

    def table_fix(self, base_table: np.ndarray):
        # 締切日をすぎてたら強制的にその分締め切り内に割り振る
        for i in range(len(self.num_tasks_list)):
            for j in range(base_table.shape[1]):
                if base_table[i][j] == 1:
                    if j > int(self.duetimelist2[i]):
                        base_table[i][j] = 0
                        buf = 0
                        while buf < 1:
                            n = np.random.randint(0, self.due_mass_list[i])
                            if base_table[i][n] ==0:
                                base_table[i][n] = 1
                                buf += 1

        # 同じタイミングで二つ以上のタスクが入ってる場合どっちか削除
        #print(base_table.shape)
        for i in range(base_table.shape[1]):
            task_num = 0
            ttt = []
            for j in range(len(self.num_tasks_list)):
                if base_table[j][i] == 1:
                    task_num += 1
                    ttt.append(j)
                if task_num >= 2:
                    hind = task_num -1
                    buf = 0
                    while buf < hind:
                        n = np.random.randint(0, len(ttt))
                        base_table[j][ttt[n]] = 0
                        s = ttt.pop(n)
                        # 削除した分追加
                        buf1 = 0
                        while buf1 < 1:
                            nn = np.random.randint(0, self.due_mass_list[s])
                            if base_table[s][nn] ==0:
                                base_table[s][nn] = 1
                                buf1 += 1
                        buf += 1

        # タスクの数を調整
        s_num = np.sum(base_table, axis=1)
        for i in range(len(self.num_tasks_list)):
            for j in range(base_table.shape[1]):
                if s_num[i] > self.num_tasks_list[i]:
                    lalaland = []
                    for jj in range(base_table.shape[1]):
                        if base_table[i][jj] == 1:
                            lalaland.append(jj)
                    hind = s_num[i] - self.num_tasks_list[i]
                    buf = 0
                    while buf < hind:
                        n = random.choice(lalaland)
                        base_table[i][n] = 0
                        buf += 1

                if s_num[i] < self.num_tasks_list[i]:
                    hind = self.num_tasks_list[i] - s_num[i]
                    buf = 0
                    while buf < hind:
                        n = np.random.randint(0, self.due_mass_list[i])
                        if base_table[i][n] == 0:
                            base_table[i][n] = 1
                            buf += 1

        return base_table

    def kiso_table_2(self):
        return self.kiso_table_exist, self.earliest


if __name__ == "__main__":
    ins = InsertCalendarv2(res=15)
    #x = ins.generate_plan()
    #xx = 0
    #for i in range(2):
    #    for j in range(1020):
    #        if x[i][j] == 1:
    #            xx += 1
    #print(xx)

