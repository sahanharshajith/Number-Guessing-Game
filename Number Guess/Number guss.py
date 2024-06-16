import tkinter as tk
import random

window = tk.Tk()

window.state('zoomed')
window.title('Number Guessing Game')
window.iconbitmap(r'E:\Programming\Python\Python GUI\Number Guess\guess_js_logo_icon.ico')
window.configure(bg='#9249FF')

a1, b1 = None, None
x = None

def set_range():
    global a1, b1, x
    a = entry1.get()
    b = entry2.get()
    try:
        a1 = int(a)
        b1 = int(b)
        if a1 >= b1:
            output_label.config(text='The first number should be less than the second number. \nPlease re-enter the numbers.', fg='red')
            return
        x = random.randint(a1, b1)
        output_label.config(text=f'Range set from {a1} to {b1}. Start guessing!', fg='green')
    except ValueError:
        output_label.config(text='Not a valid number, please enter integer numbers.', fg='red')

def guess_number():
    global x
    if a1 is None or b1 is None:
        output_label.config(text='Please set the range first.', fg='red')
        return
    
    n = guess_entry.get()
    try:
        num = int(n)
        if num < a1 or num > b1:
            output_label.config(text='Your guess number is out of range.', fg='red')
            return
        if num == x:
            output_label.config(text=f"Congratulations, YOU WON!!! The number was: {x}", fg='green')
        elif num > x:
            output_label.config(text='Your guess was too high, guess a lower number.', fg='blue')
        else:
            output_label.config(text='Your guess was too low, guess a higher number.', fg='blue')
    except ValueError:
        output_label.config(text='Not a valid number, please re-enter an integer number.', fg='red')

label1 = tk.Label(
    text='Guess My Number',
    font=('Arial', 50, 'bold'),
    bg='#9249FF'
)
label1.pack(pady=15)

label2 = tk.Label(
    text='Guess a random number',
    font=('Arial', 25),
    bg='#9249FF',
    foreground='white'
)
label2.pack(pady=25)

entry1 = tk.Entry(
    bg='#9D5AFF',
    borderwidth=2,
    font=('Arial', 20)
)
entry1.place(x=560, y=225, width=60, height=30)

entry2 = tk.Entry(
    bg='#9D5AFF',
    borderwidth=2,
    font=('Arial', 20)
)
entry2.place(x=640, y=225, width=60, height=30)

set_button = tk.Button(
    text='Set Range',
    bg='#B888FF',
    borderwidth=2,
    relief="solid",
    font=('Arial', 15),
    command=set_range
)
set_button.place(x=720, y=223, height=35)

output_label = tk.Label(
    font=('Arial', 30),
    bg='#9249FF'
)
output_label.place(x=200, y=300)

guess_entry = tk.Entry(
    bg='#9D5AFF',
    borderwidth=2,
    font=('Arial', 20)
)
guess_entry.place(x=610, y=400, width=60, height=30)

guess_button = tk.Button(
    text='Guess',
    bg='#B888FF',
    borderwidth=2,
    relief="solid",
    font=('Arial', 15),
    command=guess_number
)
guess_button.place(x=690, y=400, width=60, height=30)

window.mainloop()
