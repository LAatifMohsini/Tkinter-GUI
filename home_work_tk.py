import tkinter as tk

# Define the text for each button
button_texts = [
    "there is no home work",
    "there is no home work",
    "thre is no home work"
]

# Define the functions to display the text when each button is clicked
def display_button1_text():
    with open("home_work1.txt", "r") as file:
        context = file.read()
    text_label.config(text=context)
    text_canvas.update_idletasks()  # Update canvas to reflect the text height
    text_canvas.config(scrollregion=text_canvas.bbox("all"))
    text_canvas.yview_moveto(0)
def display_button2_text():
    with open("home_work2.txt", "r") as file:
        context = file.read()
    text_label.config(text=context)
    text_canvas.update_idletasks()  # Update canvas to reflect the text height
    text_canvas.config(scrollregion=text_canvas.bbox("all"))
    text_canvas.yview_moveto(0)

def display_button3_text():
    with open("home_work3.txt","r") as file:
        contex= file.read()
    text_label.config(text=contex)
    text_canvas.update_idletasks()
    text_canvas.config(scrollregion=text_canvas.bbox("all"))
    text_canvas.yview_moveto(0)

def display_button4_text():
    text_label.config(text=button_texts[1])
    text_canvas.update_idletasks()
    text_canvas.config(scrollregion=text_canvas.bbox("all"))
    text_canvas.yview_moveto(0)

def display_button5_text():
    text_label.config(text=button_texts[2])
    text_canvas.update_idletasks()
    text_canvas.config(scrollregion=text_canvas.bbox("all"))
    text_canvas.yview_moveto(0)

# Create the main window
root = tk.Tk()
root.title("home work")

# Create the left panel with buttons
left_panel = tk.Frame(root)
left_panel.pack(side=tk.LEFT, padx=20, pady=20)

# Create the buttons
button1 = tk.Button(left_panel, text="home work1", bg="gray", command=display_button1_text)
button1.pack(side=tk.TOP, pady=10)

button2 = tk.Button(left_panel, text="home work2", bg="white", command=display_button2_text)
button2.pack(side=tk.TOP, pady=10)

button3 = tk.Button(left_panel, text="home work3", bg="gray", command=display_button3_text)
button3.pack(side=tk.TOP, pady=10)

button4 = tk.Button(left_panel, text="home work4", bg="white", command=display_button4_text)
button4.pack(side=tk.TOP, pady=10)

button5 = tk.Button(left_panel, text='home work5', bg="gray", command=display_button5_text)

button5.pack(side=tk.TOP, pady=10)# Create the right panel for displaying the text
right_panel = tk.Frame(root)
right_panel.pack(side=tk.RIGHT, padx=20, pady=20)

# Create the Scrollbar and Canvas
text_canvas = tk.Canvas(right_panel, width=400, height=400)
text_canvas.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

scrollbar = tk.Scrollbar(right_panel, command=text_canvas.yview)
scrollbar.pack(side=tk.LEFT, fill=tk.Y)

text_canvas.config(yscrollcommand=scrollbar.set)

# Create the label to display the text
text_label = tk.Label(text_canvas, text="", font=("Arial", 16), anchor="nw", justify="left", wraplength=380)
text_canvas.create_window((0,0), window=text_label, anchor="nw")

root.mainloop()
import sys
print(sys.path)
