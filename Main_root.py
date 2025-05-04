import tkinter as tk
from tkinter import messagebox

#主窗口
root = tk.Tk()
root.title('答题软件')
root.geometry('375x110')


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
    scale = tk.Scale(root1, from_=0, to=100, orient='horizontal')  #水平滑动
    scale.set(0)
    scale.place(x=100, y=30)

    def change():
        value = scale.get()  #获取用户选择的透明度值
        alpha = 1 - value / 100  #透明度的范围，实际上是0-1
        root.attributes('-alpha', alpha)  #-alpha是设置主窗口透明度的属性
        root1.destroy()

    button = tk.Button(root1, text='确认', command=change)
    button.place(x=135, y=85)


def size():
    root2 = tk.Toplevel(root)
    root2.title('设置窗口大小')
    root2.geometry('300x150')

    label1 = tk.Label(root2, text='宽度（200-800）')
    label1.place(x=30, y=20)
    width_text = tk.Entry(root2)
    width_text.insert(0, root.winfo_width())
    width_text.place(x=150, y=20)

    label2 = tk.Label(root2, text='高度（100-400）')
    label2.place(x=30, y=60)
    height_text = tk.Entry(root2)
    height_text.insert(0, root.winfo_height())
    height_text.place(x=150, y=60)

    def cgange_size():
        try:
            new_width = int(width_text.get())  #所选择的宽度
            new_height = int(height_text.get())  #所选择的高度
            if 100 <= new_width <= 800 and 50 <= new_height <= 400:
                root.geometry(f'{new_width}x{new_height}')
                update_buttons(new_width, new_height)  #更新宽度和高度
                root2.destroy()
            else:
                messagebox.showerror('错误', '请输入范围以内的大小')
        except ValueError:
            messagebox.showerror('错误', '请输入数据')

    button = tk.Button(root2, text='确认', command=cgange_size)
    button.place(x=120, y=100)


def update_buttons(new_width, new_height):
    rows = 2  #2行
    cols = 3  #3列
    btn_width = new_width // cols - 20  #按钮的宽度=窗口宽度/列数-20（减去空隙）
    btn_height = new_height // rows - 30  #按钮的高度=窗口高度/行数-30（减去空隙）

    for index, btn in enumerate(root.winfo_children()):  #遍历主窗口root所有子控件
        if isinstance(btn, tk.Button):  #如果控件是一个按钮就继续处理它。
            row = index // cols
            col = index % cols
            btn.place(x=col * (btn_width + 10) + 10,  #每一列按钮右移 (btn_width + 10)，第一个多加 10
                      y=row * (btn_height + 10) + 30,  #每一行按钮下移 (btn_height + 30)，第一个多加 10
                      width=btn_width,
                      height=btn_height)


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
    # 测试 lkt
root.mainloop()
