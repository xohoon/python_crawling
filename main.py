import webcrawling as wc
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import filedialog
window = tk.Tk()
window.title('Search')
window.geometry("220x100+100+100")

select01 = ttk.Combobox(window, width=20, state='readonly')
select01["values"] = ["NAVER", "DAUM"]
input01 = tk.Entry(window, width=20)


def clickEvent():
    window.directory = filedialog.askdirectory()
    win_addaress = window.directory
    keyword = input01.get()
    site_name = select01.get()
    wc.webSearching(keyword, site_name, 2, win_addaress)

submitBtn = tk.Button(window, text='Excel 생성', command=clickEvent)

select01.pack()
input01.pack()
submitBtn.pack()
window.mainloop()
