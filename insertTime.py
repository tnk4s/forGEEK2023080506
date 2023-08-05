import datetime
import pandas as pd
from datetime import date

import my_schedule as ms

class InsertTime:
    def __init__(self, freetime_list: list, daytask_list: list):
        self.freetime_list = freetime_list
        self.daytask_list = daytask_list

