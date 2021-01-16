from tkinter import *
VALUE = 1.60934

def calculate():
    get_value = int(input_element.get())
    calculation = round(get_value * VALUE)
    calculation_string = str(calculation)
    result_label.config(text=calculation_string)

window = Tk()
# Title
window.title("Mile to Km converter")
# Window size
window.minsize(width=500, height=300)
# Padding
window.config(padx=30, pady=30)

# # Blank label
# blank = Label()
# blank.grid(column=0, row=0)

# Entry
input_element = Entry()
# Focus
input_element.focus()
# print(input.get())
input_element.grid(column=1, row=0)

# Label
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

# equal label
is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

# result_label
result_label = Label(text="0")
result_label.grid(column=1, row=1)

# Label
km_label = Label(text="Km")
km_label.grid(column=2, row=1)

# Button
calculate_button = Button(text="Calculate", command=calculate)
calculate_button.grid(column=1, row=2)






window.mainloop()