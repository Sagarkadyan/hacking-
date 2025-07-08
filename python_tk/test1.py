import tkinter as tk
from tkinter import ttk

import time

def start_progress():
    progress.start()
    for i in range(101):
        time.sleep(0.05)
        progress['value'] = i
        root.update_idletasks()
    progress.stop()

root = tk.Tk()
root.title("Tkinter Widgets Example")

# Progressbar Frame
progress_frame = tk.Frame(root)
progress_frame.pack(pady=10)
progress = ttk.Progressbar(progress_frame, orient="horizontal", length=300, mode="determinate")
progress.pack()
start_button = tk.Button(progress_frame, text="Start Progress", command=start_progress)
start_button.pack(pady=5)

# Label Example
label = tk.Label(root, text='GeeksForGeeks.org!')
label.pack(pady=10)

# Entry Form Frame
form_frame = tk.Frame(root)
form_frame.pack(pady=10)
tk.Label(form_frame, text='First Name').grid(row=0, column=0)
tk.Label(form_frame, text='Last Name').grid(row=1, column=0)
e1 = tk.Entry(form_frame)
e2 = tk.Entry(form_frame)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

# Listbox in a Toplevel window
def open_listbox():
    top = tk.Toplevel(root)
    top.title('Programming Languages')
    lb = tk.Listbox(top)
    lb.insert(1, 'Python')
    lb.insert(2, 'Java')
    lb.insert(3, 'C++')
    lb.insert(4, 'Any other')
    lb.pack(padx=10, pady=10)

listbox_btn = tk.Button(root, text='Show Listbox', command=open_listbox)
listbox_btn.pack(pady=10)



root.mainloop()

pri