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


def guide():
    messagebox.showinfo("提示", "使用指南")


def more():
    messagebox.showinfo("提示", "更多功能")


#按钮布置
buttons = [
    ("选题区域", select_area),
    ("AI作答", ai_answer),
    ("AI对话", ai_chat),
    ("复制文字", copy_text),
    ("使用指南", guide),
    ("更多功能", more)
]
for index, (text, command) in enumerate(buttons):
    row = index // 3
    col = index % 3
    btn = tk.Button(root, text=text, width=15, height=2, command=command)
    btn.grid(row=row, column=col, padx=5, pady=5)
root.mainloop()
