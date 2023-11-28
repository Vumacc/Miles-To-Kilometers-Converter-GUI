import tkinter as tk
import ttkbootstrap as ttk

def convert():
    print(entry_int.get())
    mile_input = entry_int.get()
    km_output = mile_input * 1.61
    output_string.set(km_output)

# Window
window = tk.Tk()
window.geometry('300x150')
window.title('Miles to Kilometers Converter')

# Title
title_label = ttk.Label(master=window, text='Miles To Kilometers', font='Calibri 24 bold')
title_label.pack()

# Input Field
input_frame = ttk.Frame(master=window)

entry_int = ttk.IntVar()
entry = ttk.Entry(master=input_frame, textvariable=entry_int)
button = ttk.Button(master = input_frame, text = 'Convert', command = convert)

entry.pack(side = 'left', padx = 10)
button.pack(side = 'left')
input_frame.pack(pady = 10)

# Output
output_string = ttk.StringVar()
output_label = ttk.Label(master=window, text='output', font='Calibri 12 bold', textvariable=output_string)

output_label.pack()

window.mainloop()