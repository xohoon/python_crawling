import webcrawling as wc
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

window = tk.Tk()
window.title('Search')
window.geometry("250x170+100+100")

select01 = ttk.Combobox(window, width=20, state='readonly')
select01["values"] = ["NAVER", "DAUM"]
input01 = tk.Entry(window, width=20)
label01 = Label(window, text="WEB")
label02 = Label(window, text="KeyWord")

def clickEvent():
    keyword = input01.get()
    site_name = select01.get()
    if  len(keyword) < 1 or len(site_name) < 1:
        messagebox.showinfo("알림", "검색어를 입력해주세요.")
        return
    else:
        window.directory = filedialog.askdirectory()
        win_addaress = window.directory
        wc.webSearching(keyword, site_name, 2, win_addaress)

submitBtn = tk.Button(window, text='Excel 생성', command=clickEvent)

label01.pack()
select01.pack()
label02.pack()
input01.pack()
submitBtn.pack()
window.mainloop()
