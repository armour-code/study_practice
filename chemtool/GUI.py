# author: fzb
# time: 2020/3/27
# function: 实现交互式界面的设计

import tkinter
import ALARM

# 界面初始化设计
MainForm = tkinter.Tk()
MainForm.geometry("250x250")
MainForm.title("降解实验辅助工具")
MainForm['background'] = 'Azure'  # 蔚蓝色背景
try:
    MainForm.iconbitmap('C:\\Users\\94331\\Desktop\\主要任务\\pyex\\favicon.ico')
except:
    print("检查图标文件储存位置")
# 闹钟界面
AlarmBtn = tkinter.LabelFrame(MainForm, text="", padx=5, pady=5)
AlarmBtn.pack(side="bottom", fill="x")
AlarmBtn1 = tkinter.Button(AlarmBtn, text="降解", fg="Blue", padx=15, pady=10)
AlarmBtn1.pack(side="left", anchor="nw", padx="2m")
AlarmBtn2 = tkinter.Button(AlarmBtn, text="分析", fg="Blue", padx=15, pady=10)
AlarmBtn2.pack(side="left", anchor="n", padx="2m")
AlarmBtn3 = tkinter.Button(AlarmBtn, text="重置", fg="gray", padx=15, pady=10)
AlarmBtn3.pack(side="left", anchor="ne", padx="2m")


AlarmShow1 = tkinter.LabelFrame(MainForm, text="降解")
AlarmShow1.pack(side="top", fill="x")
AlarmShow11 = tkinter.LabelFrame(MainForm, text="")
AlarmShow11.pack(side="top", fill="x")
tkinter.Label(AlarmShow1, text="剩余时间：").pack(side="left", anchor="w")

AlarmShow2 = tkinter.LabelFrame(MainForm, text="分析")
AlarmShow2.pack(side="top", fill="x")
AlarmShow22 = tkinter.LabelFrame(MainForm, text="")
AlarmShow22.pack(side="top", fill="x")
tkinter.Label(AlarmShow2, text="剩余时间：").pack(side="left", anchor="w")

AlarmShow3 = tkinter.LabelFrame(MainForm, text="", padx=5, pady=5)
AlarmShow3.pack(side="top", fill="x")

# 人机交互部分编写
# 设定时间部分

setOn1 = tkinter.IntVar()
setOn2 = tkinter.IntVar()
setOn3 = tkinter.IntVar()
setOn4 = tkinter.IntVar()
SetTime1 = tkinter.IntVar()
SetTime2 = tkinter.IntVar()
WarnTime = tkinter.IntVar()
SumTime = tkinter.IntVar()
SetTimeBox1 = tkinter.Spinbox(AlarmShow11, from_=0, to=500, increment=20, textvariable=SetTime1)
SetTimeBox4 = tkinter.Spinbox(AlarmShow11, from_=0, to=500, increment=20, textvariable=SumTime)
SetTimeBox2 = tkinter.Spinbox(AlarmShow22, from_=0, to=500, increment=20, textvariable=SetTime2)
SetTimeBox3 = tkinter.Spinbox(AlarmShow3, from_=0, to=500, increment=20, textvariable=WarnTime)


def set_time():
    if setOn1.get() == 1:  # 摁键降解
        SetTimeBox1.pack(side="left", anchor="w")
    if setOn1.get() == 0:
        SetTimeBox1.pack_forget()
    if setOn4.get() == 1:  # 总时长设置
        SetTimeBox4.pack(side="left", anchor="w")
    if setOn4.get() == 0:
        SetTimeBox4.pack_forget()

    if setOn2.get() == 1:  # 摁键分析
        SetTimeBox2.pack(side="left", anchor="w")
    if setOn2.get() == 0:
        SetTimeBox2.pack_forget()
    if setOn3.get() == 1:  # 设定提醒时间
        SetTimeBox3.pack(side="left", anchor="w")
    if setOn3.get() == 0:
        SetTimeBox3.pack_forget()


tkinter.Checkbutton(AlarmShow11, text="间隔时间", variable=setOn1, fg="gray", command=set_time) \
    .pack(side="left", anchor="w")
tkinter.Checkbutton(AlarmShow11, text="总时长", variable=setOn4, fg="gray", command=set_time) \
    .pack(side="left", anchor="w")
tkinter.Checkbutton(AlarmShow22, text="间隔时间", variable=setOn2, fg="gray", command=set_time) \
    .pack(side="left", anchor="w")
tkinter.Checkbutton(AlarmShow3, text="提醒时间", variable=setOn3, fg="gray", command=set_time) \
    .pack(side="left", anchor="w")

# 显示剩余时间
# 摁键功能
if WarnTime.get() == 0:
    WarnTime.set(10)
ShowTime1 = ALARM.AlarmClock(SetTime1.get(), WarnTime.get(), SumTime.get())
ShowTime = []
ShowTimeNum = -1      # 动态增加闹钟

# 子菜单显示


def Confirm_Show1(m):
    def star_time1(m):
        ShowTime1.Interval = SetTime1.get()
        ShowTime1.RemindTime = WarnTime.get()
        ShowTime1.SumTime = SumTime.get()
        ShowTime1.set_time()
        ShowTime1.set_sum_time()
        TLShow.destroy()
    TLShow = tkinter.Toplevel(MainForm)
    TLShow.wm_attributes("-topmost", 1)
    TLShow.title("提示！！！")
    TLShow.geometry("100x100")
    tkinter.Label(TLShow, text="确定这么做？").pack()
    ConfirmBtn = tkinter.Button(TLShow, text="确定", fg="red", padx=15, pady=10)
    ConfirmBtn.pack()
    ConfirmBtn.bind("<Button-1>", star_time1)


def Confirm_Show2(m):
    def star_time2(m):
        global ShowTimeNum
        ShowTimeNum = ShowTimeNum + 1          # 后面可以直接用，为对应
        ShowTime.append(ALARM.AlarmClock(SetTime2.get(), WarnTime.get(), SumTime.get()))
        ShowTime[ShowTimeNum].set_time()
        TLShow.destroy()
    TLShow = tkinter.Toplevel(MainForm)
    TLShow.wm_attributes("-topmost", 1)
    TLShow.title("提示！！！")
    TLShow.geometry("100x100")
    tkinter.Label(TLShow, text="确定这么做？").pack()
    ConfirmBtn = tkinter.Button(TLShow, text="确定", fg="red", padx=15, pady=10)
    ConfirmBtn.pack()
    ConfirmBtn.bind("<Button-1>", star_time2)


def Setting_Show(even):
    def setting1(m):
        ShowTime1.on_off = False
        TLShow.destroy()

    def setting2(m):
        ShowTime[ShowTimeNum].on_off = False
        TLShow.destroy()

    def setting3(m):
        global ShowTimeNum
        del(ShowTime[ShowTimeNum])
        ShowTimeNum = ShowTimeNum-1
        TLShow.destroy()
    TLShow = tkinter.Toplevel(MainForm)
    TLShow.wm_attributes("-topmost", 1)
    TLShow.title("提示！！！")
    TLShow.geometry("100x200")
    tkinter.Label(TLShow, text="确定这么做？").pack()
    SettingBtn1 = tkinter.Button(TLShow, text="暂停降解", fg="red", padx=15, pady=10)
    SettingBtn1.pack()
    SettingBtn1.bind("<Button-1>", setting1)

    SettingBtn2 = tkinter.Button(TLShow, text="暂停分析", fg="red", padx=15, pady=10)
    SettingBtn2.pack()
    SettingBtn2.bind("<Button-1>", setting2)

    SettingBtn3 = tkinter.Button(TLShow, text="删除分析", fg="red", padx=15, pady=10)
    SettingBtn3.pack()
    SettingBtn3.bind("<Button-1>", setting3)


AlarmBtn1.bind("<Button-1>", Confirm_Show1)
AlarmBtn2.bind("<Button-1>", Confirm_Show2)
AlarmBtn3.bind("<Button-1>", Setting_Show)

# 显示功能
ShowVar1 = tkinter.StringVar()
ShowVar = []
for i in range(10):
    ShowVar.append(tkinter.StringVar())


def TimeShow1():
        ShowTime1.Degradation_Time()
        ShowVar1.set(str(ShowTime1.DeltaSumTime))
        clock1.after(500, TimeShow1)


def TimeShow2():
    for i in range(ShowTimeNum+1):
        ShowTime[i].remind()
        ShowVar[i].set(str(ShowTime[i].DeltaTime))
    for i in range(ShowTimeNum+1, 10):
        ShowVar[i].set('***')
    clock1.after(500, TimeShow2)


clock1 = tkinter.Label(AlarmShow1, textvariable=ShowVar1)
clock1.pack(side="left", anchor="w")
TimeShow1()
for i in range(10):
    clock2 = tkinter.Label(AlarmShow2, textvariable=ShowVar[i])
    clock2.pack(side="left", anchor="w")
TimeShow2()

MainForm.mainloop()
