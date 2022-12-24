import tkinter
from tkinter import ttk, END
import requests

#GET CURRENT DATA
# Where USD is the base currency you want to use
url = 'https://v6.exchangerate-api.com/v6/edd8cd8ad765c428fc7cb3ba/latest/USD'

# Making our request
response = requests.get(url)
global data
data = response.json()


#Define window
root = tkinter.Tk()
root.title('Metric Helper')
root.iconbitmap('ruler.ico')
root.resizable(0,0)

#Define fonts and colors
field_font = ('Cambria', 10)
bg_color = "gray"
button_color = "#f5cf87"
root.config(bg=bg_color)

#Define functions
def convert():
    #Clear the output field
    output_field.delete(0, END)

    #Get all user information
    start_value = float(input_field.get())
    start_prefix = input_combobox.get()
    end_prefix = output_combobox.get()

    #Covert to the base unit first
    base_value = start_value*data['conversion_rates'][start_prefix]
    #Covert to new metric value
    end_value = base_value*data['conversion_rates'][end_prefix]

    #Update output field with answer
    output_field.insert(0, str(end_value))
    

#Define layout
#Create the input and output entry fields
input_field = tkinter.Entry(root, width=20, font=field_font, borderwidth=3)
output_field = tkinter.Entry(root, width=20, font=field_font, borderwidth=3)
equal_label = tkinter.Label(root, text="=", font=field_font, bg=bg_color)

input_field.grid(row=0, column=0, padx=10, pady=10)
equal_label.grid(row=0, column=1, padx=10, pady=10)
output_field.grid(row=0, column=2, padx=10, pady=10)

input_field.insert(0, 'Enter your quantity')

#Create combobox for metric values
metric_list = []
for key in data['conversion_rates'].keys():
    metric_list.append(key)
input_combobox = ttk.Combobox(root, value=metric_list, font=field_font, justify='center')
output_combobox = ttk.Combobox(root, value=metric_list, font=field_font, justify='center')
to_label = tkinter.Label(root, text="to", font=field_font, bg=bg_color)

input_combobox.grid(row=1, column=0, padx=10, pady=10)
to_label.grid(row=1, column=1, padx=10, pady=10)
output_combobox.grid(row=1, column=2, padx=10, pady=10)

input_combobox.set('base value')
output_combobox.set('base value')

#Create a conversion button
convert_button = tkinter.Button(root, text='Convert', font=field_font, bg=button_color, command=convert)
convert_button.grid(row=2, column=0, columnspan=3, padx=10, pady=10, ipadx=50)

#Run the root window's main loop
root.mainloop()