import tkinter as tk
import tkinter.filedialog
import tkinter.messagebox
from utils.Generator import *
import os
import threading


class InitWindows(object):

    def __init__(self):
        self.btn_width = 16

        self.expression_range = ''
        self.expression_number = ''

        self.expression_file_name = ''
        self.answer_file_name = ''

        self.root = tk.Tk()
        self.root.iconbitmap("./views/favicon.ico")
        self.root.geometry(f"220x360+{int(self.root.winfo_screenwidth()/2) - 110}+{int(self.root.winfo_screenheight()/2) - 180}")
        self.root.title("Exercise")
        self.init_widgets()
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.order = 0

        self.root.mainloop()

    def on_closing(self):
        if tk.messagebox.askokcancel("退出", "确认退出？"):
            # 退出 gui 直接结束进程, 防止程序继续执行消耗资源
            os.system('taskkill /f /im %s' % 'python.exe')
            self.root.destroy()

    def get_(self):
        self.order += 1
        # 判断是否已经存在相关文件
        if os.path.exists('./docs/Exercises.txt'):
            os.remove('./docs/Exercises.txt')
        if os.path.exists('./docs/Answer.txt'):
            os.remove('./docs/Answer.txt')

        n = int(self.entry_input_num.get())
        r = int(self.entry_input_range.get())
        if n and r:
            if n > 30000 or r < 50:
                tk.messagebox.showinfo("Info", "生成时间将较长,请耐心等待")
            Generator(n, r, self.order).multi_processor()
            tk.messagebox.showinfo("Info", "Success")
            self.open_explorer()

    def init_widgets(self):

        # All label
        lb_info_generate = tk.Label(self.root, text="生成四则运算表达式", anchor="center", width=self.btn_width, fg="red")
        lb_info_select = tk.Label(self.root, text="检查答案", anchor="center", width=self.btn_width, fg="red")

        lb_input_num = tk.Label(self.root, text="请输入生成表达式数量", anchor="center", width=self.btn_width)
        lb_input_range = tk.Label(self.root, text="请输入生成表达式范围", anchor="center", width=self.btn_width)

        # All Entry box
        self.entry_input_num = tk.Entry(self.root, width=self.btn_width + 1)
        self.entry_input_range = tk.Entry(self.root, width=self.btn_width + 1)

        # All buttons
        btn_commit_generate = tk.Button(self.root, text="生成", command=lambda: self.thread_event(self.get_), anchor="center", width=self.btn_width)
        btn_commit_inspect = tk.Button(self.root, text="检查", command=lambda: self.thread_event(self.inspect_dual_file), anchor="center", width=self.btn_width)
        btn_open_exploer = tk.Button(self.root, text="打开文件夹", command=lambda: self.thread_event(self.open_explorer), anchor="center", width=self.btn_width)

        # All file select buttons
        self.btn_select_expressions = tk.Button(self.root, text="选择题目文件", command=lambda: self.thread_event(self.select_expression_file), anchor="center", width=self.btn_width)
        self.btn_select_answers = tk.Button(self.root, text="选择答案文件", command=lambda: self.thread_event(self.select_answer_file), anchor="center", width=self.btn_width)

        # Create placement

        x_init, y_init, y_step = 90, 10, 30

        lb_info_generate.place(x=50, y=y_init + 5, )
        lb_input_num.place(x=50, y=y_init + y_step, )
        self.entry_input_num.place(x=50, y=y_init + y_step * 2)
        lb_input_range.place(x=50, y=y_init + y_step * 3)
        self.entry_input_range.place(x=50, y=y_init + y_step * 4)
        btn_commit_generate.place(x=50, y=y_init + y_step * 5)

        lb_info_select.place(x=50, y=y_init + y_step * 6)
        self.btn_select_expressions.place(x=50, y=y_init + y_step * 7)
        self.btn_select_answers.place(x=50, y=y_init + y_step * 8)
        btn_commit_inspect.place(x=50, y=y_init + y_step * 9)
        btn_open_exploer.place(x=50, y=y_init + y_step * 10)

    def select_expression_file(self):
        self.expression_file_name = tkinter.filedialog.askopenfilename()
        self.btn_select_expressions.config(text="题目: {}".format(self.expression_file_name.split("/")[-1]))

    def select_answer_file(self):
        self.answer_file_name = tkinter.filedialog.askopenfilename()
        self.btn_select_answers.config(text="答案: {}".format(self.answer_file_name.split("/")[-1]))

    def inspect_dual_file(self):
        if self.expression_file_name != '' and self.answer_file_name != '':
            inspect(self.answer_file_name, self.expression_file_name)
            tk.messagebox.showinfo("Info", "Success")
        else:
            tk.messagebox.showinfo("Info", "Failed")
            return False

    @staticmethod
    def open_explorer():
        os.system("explorer.exe .\\docs")

    @staticmethod
    def thread_event(func):
        # 创建
        t = threading.Thread(target=func)
        # 守护 !!!
        t.setDaemon(True)
        # 启动
        t.start()
        # 阻塞--卡死界面！
        # t.join()


if __name__ == '__main__':
    InitWindows()
