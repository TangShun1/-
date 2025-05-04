import tkinter as tk
from tkinter import messagebox

#主窗口
root = tk.Tk()
root.title('答题软件')
root.geometry('380x120')


# 定义每个按钮的功能
def select_area():
    messagebox.showinfo("提示", "请选择区域")


def ai_answer():
    messagebox.showinfo("提示", "AI作答")


def ai_chat():
    messagebox.showinfo("提示", "AI对话")


def copy_text():
    messagebox.showinfo("提示", "复制文字")


def transparency():
    root1 = tk.Toplevel(root)
    root1.title('设置窗口透明度')
    root1.geometry('300x120')

    label = tk.Label(root1, text='请选择窗口透明度（0-100）')
    label.place(x=80, y=10)

    #透明度进度条范围
    scale = tk.Scale(root1, from_=0, to=100, orient='horizontal')#水平滑动
    scale.set(0)
    scale.place(x=100, y=30)

    def change():
        value = scale.get()#获取用户选择的透明度值
        alpha = 1 - value / 100#透明度的范围，实际上是0-1
        root.attributes('-alpha', alpha)#-alpha是设置主窗口透明度的属性
        root1.destroy()

    button = tk.Button(root1, text='确认', command=change)
    button.place(x=135, y=85)


def size():
    messagebox.showinfo("提示", "窗口大小")


#按钮布置
buttons = [
    ("选题区域", select_area),
    ("AI作答", ai_answer),
    ("AI对话", ai_chat),
    ("复制文字", copy_text),
    ("透明度", transparency),
    ("窗口大小", size)
]
for index, (text, command) in enumerate(buttons):
    row = index // 3
    col = index % 3
    btn = tk.Button(root, text=text, width=15, height=2, command=command)
    btn.grid(row=row, column=col, padx=5, pady=5)
root.mainloop()
