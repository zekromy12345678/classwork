import tkinter
from tkinter import BOTH, StringVar, END


# Define window
root = tkinter.Tk()
root.title("Hello World GUI")
root.geometry('400x400')
root.resizable(400, 400)

# Define fonts and colors
root_color = "#224870"
input_color = "#2a4494"
output_color = "#4ea5d9"
root.config(bg=root_color)


# Define functions
def submit_name():
    """Say Hello to the Users"""
    if case_style.get() == 'normal':
        name_label.config(text="Hello " + name.get() + "! Dr. Frusci loves you.")
    elif case_style.get() == 'upper':
        name_label.config(text=("Hello " + name.get() + "! Dr. Frusci loves you").upper())

    name_label.pack()
    name.delete(0, END)

# GUI Layout
# Define frames
input_frame = tkinter.LabelFrame(root, bg=input_color)
output_frame = tkinter.LabelFrame(root, bg=output_color)
input_frame.pack(pady=10)
output_frame.pack(padx=10, pady=(0, 10), fill=BOTH, expand=True)

# Create widgets
name = tkinter.Entry(input_frame, text='Enter your name', width=20)
submit_button = tkinter.Button(input_frame, text="Submit", command=submit_name)
name.grid(row=0, column=0, padx=10, pady=10)
submit_button.grid(row=0, column=1, padx=10, pady=10, ipadx=20)

# Create radio buttons for text display
case_style = StringVar()
case_style.set('normal')
normal_button = tkinter.Radiobutton(input_frame, text="Normal Case", variable=case_style, value='normal', bg=input_color)
upper_button = tkinter.Radiobutton(input_frame, text="Upper Case", variable=case_style, value='upper', bg=input_color)
normal_button.grid(row=1, column=0, padx=2, pady=2)
upper_button.grid(row=1, column=1, padx=2, pady=2)

# Create a blank label for the output
name_label = tkinter.Label(output_frame, bg=output_color)
name_label.pack()

# Run root window's main loop
root.mainloop()