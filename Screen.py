import tkinter as tk
from PIL import ImageGrab
import base64
from io import BytesIO
import ctypes
import Ocr_module

ctypes.windll.shcore.SetProcessDpiAwareness(2)


class SimpleRegionSelector:
    def __init__(self):
        self.root = None
        self.main_root = None
        self.selection = None
        self.base64_str = None
        self.ocr_engine = Ocr_module.OCR()

    def select_region(self,main_root):
        self.main_root=main_root
        main_root.withdraw()
        self.root = tk.Tk()
        self.root.attributes("-fullscreen", True)
        self.root.attributes("-alpha", 0.3)
        self.root.attributes("-topmost", True)
        self.root.bind("<Escape>", lambda e: self._cancel_selection())  # 绑定ESC键
        self.canvas = tk.Canvas(self.root, cursor="cross", bg="gray20")
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.start_x = self.start_y = self.end_x = self.end_y = None
        self.rect = None
        # 绑定鼠标事件
        self.canvas.bind("<ButtonPress-1>", self._on_press)
        self.canvas.bind("<B1-Motion>", self._on_drag)
        self.canvas.bind("<ButtonRelease-1>", self._on_release)
        self.root.mainloop()

    def _cancel_selection(self):
        self.selection = None
        self.base64_str = None
        self.root.destroy()

    def _on_press(self, event):
        self.start_x = self.root.winfo_pointerx()
        self.start_y = self.root.winfo_pointery()
        self.rect = self.canvas.create_rectangle(0, 0, 0, 0, outline="red", width=2)

    def _on_drag(self, event):
        cur_x = self.root.winfo_pointerx()
        cur_y = self.root.winfo_pointery()
        self.canvas.coords(self.rect, self.start_x, self.start_y, cur_x, cur_y)

    def _on_release(self, event):
        self.end_x = self.root.winfo_pointerx()
        self.end_y = self.root.winfo_pointery()
        self.selection = (self.start_x, self.start_y, self.end_x, self.end_y)
        self.root.destroy()
        self.main_root.deiconify()

    def _get_base64(self):
        image = ImageGrab.grab(bbox=self.selection)
        buffered = BytesIO()
        image.save(buffered, format="PNG")
        return base64.b64encode(buffered.getvalue()).decode("utf-8")

    def get_text(self):
        if not self.selection:
            return None
        self.base64_str = self._get_base64()
        return self.ocr_engine.image_to_text(self.base64_str)