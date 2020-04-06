import tkinter as tk


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # self.hi_there = tk.Button(self)
        # self.hi_there["text"] = "Hello World\n(click me)"
        # self.hi_there["command"] = self.say_hi
        # self.hi_there.pack(side="top")
        #
        # self.quit = tk.Button(self, text="QUIT", fg="red",
        #                       command=self.master.destroy)
        # self.quit.pack(side="bottom")
        self.label_welcome = tk.Label(self, text='Arithmetic Exercise System')
        self.label_welcome.pack(side='top')

    # def say_hi(self):
    #     print("hi there, everyone!")


root = tk.Tk()
root.title('Welcome')

sw = root.winfo_screenwidth()
sh = root.winfo_screenheight()
root.geometry(f"{240}x{120}+{(sw-270)//2}+{(sh-150)//2}")
root.resizable(width=False, height=False)


app = Application(master=root)

app.mainloop()
