from tkinter import *
import random



root = Tk()
root.title("GET CLOSEST")
root.geometry("400x400")


def home():                                         # for home screen
    global available_numbers, counter, cal
    available_numbers = [0] * 5
    counter = 0
    cal = ""
    for i in root.winfo_children():
        i.destroy()
    welcome = Label(root, text="WELCOME TO GET CLOSEST", font=("Arial", 18))
    welcome.grid(row=0, column=1, padx=(25, 10), pady=30)
    start = Button(root, text="START", command=start_game, width=20)
    start.grid(row=1, column=1)


def game():                   # for calculation screen
    global goal, calculation, goal_label
    for i in root.winfo_children():
        i.destroy()
    goal = random.randint(100, 999)
    goal_label = Label(root, text=f"GOAL : {goal}", font=("Arial", 20))
    goal_label.grid(row=0, columnspan=5, padx=10, pady=10)
    calculation = Text(root, height=2, width=29, font=("Arial", 18))
    calculation.grid(row=1, columnspan=5, padx=10, pady=10)
    game_buttons()


def start_game():
    global available_numbers, counter, available_numbers_label,  widgets_start, goal
    for i in root.winfo_children():
        i.destroy()

    choose_label = Label(root, text="CHOOSE YOUR NUMBERS",  font=("Arial", 18))
    choose_label.grid(row=0, column=0, columnspan=2, padx=(40, 30), pady=30)
    available_numbers_label = Label(root, text=available_numbers, font=("Arial", 18))
    available_numbers_label.grid(row=1, column=0, columnspan=2, padx=(40, 30), pady=30)
    big_button = Button(root, text="BIG", command=big_number, width=10)
    big_button.grid(row=2, column=1)
    small_button = Button(root, text="SMALL", command=small_number, width=10)
    small_button.grid(row=2, column=0)
    clear_button = Button(root, text="CLEAR", command=clear, width=10)
    clear_button.grid(row=3, column=0, pady=20)
    game_button = Button(root, text="NEXT", command=game, width=10)
    game_button.grid(row=3, column=1, pady=20)
    widgets_start = [choose_label, big_button, small_button, clear_button, game_button]


def again():                        # bring back to choosing screen
    global available_numbers, counter, cal, result
    available_numbers = [0] * 5
    counter = 0
    cal = ""
    result = ""
    for i in root.winfo_children():
        i.destroy()
    start_game()


# Choosing numbers
def big_number():
    global counter, available_numbers, available_numbers_label
    if counter < len(available_numbers):
        available_numbers[counter] = random.randint(10,99)
        counter +=1
        available_numbers_label.destroy()
        available_numbers_label = Label(root, text=available_numbers, font=("Arial", 18))
        available_numbers_label.grid(row=1, column=0, columnspan=2, padx=(40, 30), pady=30)


def small_number():
    global counter, available_numbers, available_numbers_label
    if counter < len(available_numbers):
        available_numbers[counter] = random.randint(1,9)
        counter += 1
        available_numbers_label.destroy()
        available_numbers_label = Label(root, text=available_numbers, font=("Arial", 18))
        available_numbers_label.grid(row=1, column=0, columnspan=2, padx=(40, 30), pady=30)


def add_to_calculation(symbol):
    global cal, result
    cal += str(symbol)
    calculation.delete(1.0, "end")
    calculation.insert(1.0, cal)


def clear():                                                      # clears choosing numbers screen
    global available_numbers, counter, available_numbers_label
    available_numbers = [0]*5
    counter = 0
    available_numbers_label.destroy()
    available_numbers_label = Label(root, text=available_numbers, font=("Arial", 18))
    available_numbers_label.grid(row=1, column=0, columnspan=2, padx=(40, 30), pady=30)


def clear2():                                                        # clears calculation screen
    global goal, calculation, goal_label, cal
    for i in root.winfo_children():
        i.destroy()
    goal_label = Label(root, text=f"GOAL : {goal}", font=("Arial", 20))
    goal_label.grid(row=0, columnspan=5, padx=10, pady=10)
    cal = ""
    calculation = Text(root, height=2, width=29, font=("Arial", 18))
    calculation.grid(row=1, columnspan=5, padx=10, pady=10)
    game_buttons()


def calculate():                    # for = button
    global cal, result
    result = eval(cal)
    cal = str(result)
    calculation.delete(1.0, "end")
    calculation.insert(1.0, cal)


def submit():                  # for submit button / submits the answer
    result = eval(cal)
    for i in root.winfo_children():
        i.destroy()
    result2 = goal - result
    result_label = Label(root, text="YOU WERE "+str(result2)+" OFF!!", font=("Arial", 20))
    result_label.grid(row=0, columnspan=2, padx=40, pady=10)
    home_button = Button(root, text="HOME", command=home, width=10)
    home_button.grid(row=1, column=0, padx=10, pady=10)
    again_button = Button(root, text="AGAIN", command=again, width=10)
    again_button.grid(row=1, column=1, padx=10, pady=10)


def game_buttons():             # for buttons used in calculation screen
    o1_btn = Button(root, text=available_numbers[0], command= lambda: [add_to_calculation(available_numbers[0]), disable1(o1_btn)], width=4, font=('Arial', 18))
    o1_btn.grid(row=3, column=0)
    o2_btn = Button(root, text=available_numbers[1], command= lambda: [add_to_calculation(available_numbers[1]), disable2(o2_btn)], width=4, font=('Arial', 18))
    o2_btn.grid(row=3, column=1)
    o3_btn = Button(root, text=available_numbers[2], command=lambda: [add_to_calculation(available_numbers[2]), disable3(o3_btn)], width=4, font=('Arial', 18))
    o3_btn.grid(row=3, column=2)
    o4_btn = Button(root, text=available_numbers[3], command=lambda: [add_to_calculation(available_numbers[3]), disable4(o4_btn)], width=4, font=('Arial', 18))
    o4_btn.grid(row=3, column=3)
    o5_btn = Button(root, text=available_numbers[4], command=lambda: [add_to_calculation(available_numbers[4]), disable5(o5_btn)], width=4, font=('Arial', 18))
    o5_btn.grid(row=3, column=4)

    add_btn = Button(root, text="+", command=lambda: add_to_calculation("+"), width=5, font=('Arial', 18))
    add_btn.grid(row=4, column=0)
    minus_btn = Button(root, text="-", command=lambda: add_to_calculation("-"), width=5, font=('Arial', 18))
    minus_btn.grid(row=4, column=1)
    multiply_btn = Button(root, text="*", command=lambda: add_to_calculation("*"), width=5, font=('Arial', 18))
    multiply_btn.grid(row=4, column=2)
    divide_btn = Button(root, text="/", command=lambda: add_to_calculation("/"), width=5, font=('Arial', 18))
    divide_btn.grid(row=5, column=0)
    open_btn = Button(root, text="(", command=lambda: add_to_calculation("("), width=5, font=('Arial', 18))
    open_btn.grid(row=5, column=1)
    close_btn = Button(root, text=")", command=lambda: add_to_calculation(")"), width=5, font=('Arial', 18))
    close_btn.grid(row=5, column=2)
    clear2_btn = Button(root, text="CLEAR", command=clear2, width = 9, font=('Arial', 18))
    clear2_btn.grid(row=4, column=3, columnspan=2)
    call_btn = Button(root, text=" = ", command=calculate, width=9, font=('Arial', 18))
    call_btn.grid(row=5, column=3, columnspan=2)

    submit_btn = Button(root, text="Submit", command=submit, width=9, font=('Arial', 18))
    submit_btn.grid(row=6, column=1, columnspan=3, pady=10)



# disable numebrs


def disable1(btn):
    btn = Button(root, text=available_numbers[0], state=DISABLED, width=4, font=('Arial', 18))
    btn.grid(row=3, column=0)


def disable2(btn):
    btn = Button(root, text=available_numbers[1], state=DISABLED, width=4, font=('Arial', 18))
    btn.grid(row=3, column=1)


def disable3(btn):
    btn = Button(root, text=available_numbers[2], state=DISABLED, width=4, font=('Arial', 18))
    btn.grid(row=3, column=2)


def disable4(btn):
    btn = Button(root, text=available_numbers[3], state=DISABLED, width=4, font=('Arial', 18))
    btn.grid(row=3, column=3)


def disable5(btn):
    btn = Button(root, text=available_numbers[4], state=DISABLED, width=4, font=('Arial', 18))
    btn.grid(row=3, column=4)


home()
root.mainloop()