import tkinter
from tkinter import BOTH

#define window
root = tkinter.Tk()
root.title("Label Basics")
#root.iconbitmap("thinking.ico")
root.geometry("1080x1920")
root.resizable(0,0)
root.config(bg="blue")


#create widgets
name_label_1 = tkinter.Label(root, text="Hello, this is Joe")
name_label_1.pack()

name_label_2 = tkinter.Label(root, text="Hello, this is Mr. Buro", font=("Arial", 18, 'bold'))
name_label_2.pack()

name_label_3 = tkinter.Label(root, text="Hello, this is Mr. Henriques", font=("Cambria", 10), bg="#ff0000")
name_label_3.pack(padx=50, pady=10)

name_label_4 = tkinter.Label(root, text="Hello, this is Daniel!!!", font=("Times New Roman", 75, 'bold'), bg="#53131E")
name_label_4.pack()


root.mainloop()