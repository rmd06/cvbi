import Tkinter as tk
import tkFileDialog

def create_window_from_list(object_list):

    window = tk.Tk()

    def close_window():
        window.destroy()

    object_select = tk.StringVar()
    object_select.set(object_list[0])

    tk.Label(window, textvariable=object_select).pack()

    for item in object_list:
        selection_button = tk.Radiobutton(window, text=item, variable=object_select, value=item)
        selection_button.pack()

    closing_button = tk.Button(master=window, text='Selection Complete', command=close_window)
    closing_button.pack()

    window.mainloop()

    object_string = object_select.get()

    return(object_string)


def get_output_dir():

    def close_window():

        window.destroy()

    window = tk.Tk()
    window.dirpath = tkFileDialog.askdirectory(initialdir = "~", title = "Select Folder")
    output_dir = window.dirpath

    closing_button = tk.Button(master=window, text='Selection Complete', command=close_window)
    closing_button.pack()
    window.mainloop()

    #output_dir = output_dir.replace(':','-')

    return output_dir
