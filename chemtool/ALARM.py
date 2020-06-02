# author: fzb
# time: 2020/3/28
# function: 实现所有的闹钟功能
import datetime
import threading
from win10toast import ToastNotifier


class AlarmClock:
    def __init__(self, Interval1, RemindTime1, SumTime1):
        self.Interval = Interval1
        self.SetTime = datetime.datetime.now()
        self.RemindTime = RemindTime1
        self.DeltaTime = 0
        self.SumTime = SumTime1
        self.SetSumTime = datetime.datetime.now()
        self.DeltaSumTime = 0
        self.on_off = False

    def set_time(self):  # 设定时间
        self.SetTime = datetime.timedelta(minutes=self.Interval) + datetime.datetime.now()
        self.on_off = True

    def set_sum_time(self):
        self.SetSumTime = datetime.timedelta(minutes=self.SumTime) + datetime.datetime.now()

    def remind(self):  # 提醒
        if self.on_off:
            self.DeltaTime = self.SetTime - datetime.datetime.now()
            if self.DeltaTime.seconds == 0:
                print("hello")
                self._ANoteThread()
            if self.DeltaTime.days < 0:
                self.on_off = False

    def Degradation_Time(self):
        if self.on_off:
            self.DeltaSumTime = self.SetSumTime - datetime.datetime.now()
            self.DeltaTime = self.SetTime - datetime.datetime.now()
            if self.DeltaTime.seconds == 0:
                print("hello")
                self._DNoteThread()
            if self.DeltaTime.days < 0:
                self.set_time()
            if self.DeltaSumTime.days < 0:
                self._DNoteThread()
                self.on_off = False

    def _D_note(self):
        toaster = ToastNotifier()
        toaster.show_toast('取样时间到！！！')

    def _A_note(self):
        toaster = ToastNotifier()
        toaster.show_toast('该去分析了！！！')

    def _DNoteThread(self):
        t1 = threading.Thread(target=self._D_note)
        t1.start()
        t1.join()

    def _ANoteThread(self):
        t2 = threading.Thread(target=self._A_note)
        t2.start()
        t2.join()
