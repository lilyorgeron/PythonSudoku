from tkinter import *
from functools import partial
from PIL import ImageTk,Image
import numpy as np

import SudSolveAdapt 



def instructions(menu):
    interface = Toplevel(menu)
    interface.title("Sudoku Instructions")
    interface.iconbitmap("./favicon.ico")
    interface.geometry("1000x145")
    
    # rules
    rules1 = "SUDOKU RULES\n-> Fill the board such that each row, column, and 3x3 grid features each number 1-9 only once.\n"
    rules2 = "-> Click any blank square to fill it in with a number 1-9.\n-> When you have filled the board, click 'DONE' to check your answer.\n"
    rules3 = "-> If you get stuck and would like to see the solution, click 'SOLVE' to see an automatic solution.\n"

    # putting rules in a block of text
    words = Text(interface, height=12,width=100)
    words.grid(row=0, column=0, rowspan=3)
    words.insert(END, rules1+rules2+rules3)
    words.configure(font=("Courier", 12, "italic"))

    # button to exit
    button_exit_instructions = Button(interface, text="GOT IT!", padx=70, bg='#c7c8c8', command=interface.quit)
    button_exit_instructions.grid(row=1,column=0)

    interface.mainloop()
    return


def game(board, setup):
    # gameboard base
    board.destroy()
    board = Tk()
    board.title('Sudoku Game')
    board.iconbitmap("./favicon.ico")
    board.geometry("750x600")
    board.configure(background="#eeffeb")

    overall_dim = 522
    # using canvas method to create board
    base = Canvas(board, height=overall_dim, width=overall_dim, bg="#f8ffeb")
    base.pack()

    one_third = overall_dim // 3
    two_thirds = one_third * 2
    # creating grids and outline (board is 522x522; divided sections into threes)
    base.create_rectangle(2,2,overall_dim,overall_dim,outline="black")
    base.create_rectangle(2,2,one_third,one_third,fill="#fff",outline="black")
    base.create_rectangle(two_thirds,2,overall_dim,one_third,fill="#fff",outline="black")
    base.create_rectangle(one_third,one_third,two_thirds,two_thirds,fill="#fff",outline="black")
    base.create_rectangle(2,two_thirds,one_third,overall_dim,fill="#fff",outline="black")
    base.create_rectangle(two_thirds,two_thirds,overall_dim,overall_dim,fill="#fff",outline="black")

    one_ninth = overall_dim // 9
    one_18 = one_ninth // 2
    
    
    # saving function to validate numbers entered in boxes
    vcmd = (base.register(validate), '%S', '%i')

    color = "#f8ffeb"
    # creating individual squares
    for i in range(0, overall_dim, one_ninth):
        for j in range(0, overall_dim, one_ninth):
            # creating individual squares
            base.create_rectangle(j,i,j+one_ninth,i+one_ninth)

            # setting the right color for the grids
            if (j % 3 == 0 and j != 0) or (i % 3 == 0 and j == 0):
                color = switch(color)



            # adding entry box to empty squares
            if setup[i//one_ninth][j//one_ninth] == 0:
                answer = Entry(base, font=("Purisa",14,'bold'), justify="center", validate='key', validatecommand=vcmd)
                base.create_window(j+one_18,i+one_18,window=answer,height=one_ninth-5,width=one_ninth-5)
                
                # set background color of entry box
                answer.config({"background":color})

                answer.delete(0, END)
        
            # adding the default numbers into boxes
            else:
                base.create_text(j+one_18, i+one_18, text=str(setup[i//one_ninth][j//one_ninth]), font=("Purisa",14,'bold'))

    # creating buttons
    # button_solve = Button(menu, text="SOLVE", padx=80, bg='#c7c8c8', font='sans 14 bold', command=solve)
    # button_check = Button(menu, text="CHECK", padx=40, bg='#c7c8c8', command=check)
    button_exit = Button(board, text="EXIT", padx=70, bg='#c7c8c8', command=board.quit)
    button_exit.pack()

    board.mainloop()

    return

def start(setup):
    # building the menu
    menu = Tk()
    menu.title('Sudoku')
    menu.iconbitmap("./favicon.ico")

    # will call the function to play random board
    play = partial(game, menu, setup)
    # will open instructions page
    instruct = partial(instructions, menu)

    # creating buttons
    button_play = Button(menu, text="PLAY", padx=80, bg='#c7c8c8', font='sans 14 bold', command=play)
    button_instruct = Button(menu, text="HOW TO PLAY", padx=40, bg='#c7c8c8', command=instruct)
    button_exit = Button(menu, text="EXIT", padx=70, bg='#c7c8c8', command=menu.quit)

    # setting up display image
    my_img = ImageTk.PhotoImage(Image.open("sudokutitle.jpg"))
    img_label = Label(image=my_img)

    # setting up grid for title screen
    img_label.grid(row=0,column=0,columnspan=3)
    button_instruct.grid(row=1,column=0)
    button_play.grid(row=1,column=1)
    button_exit.grid(row=1,column=2)



    menu.mainloop()
    return

def validate(input, index):
    # function to ensure user input is within 1-9 and only one number is entered
    if input in ['1','2','3','4','5','6','7','8','9']:
        if index == '0':
            return True
    return False

def switch(color):
    # function to switch color of entry box
    if color == "#f8ffeb":
        color ="#fff"
    else:
        color = "#f8ffeb"
    return color

def auto_solve(board):
    # solving board w/ sudoku solver
    global solve_pressed
    solve_pressed = True
    SudSolveAdapt.full_solver(board)
    return

def check_answer():
    # TO DO
    return


def main():

    setup = np.array([[0, 0, 6, 0, 5, 4, 9, 0, 0],
                      [1, 0, 0, 0, 6, 0, 0, 4, 2],
                      [7, 0, 0, 0, 8, 9, 0, 0, 0],
                      [0, 7, 0, 0, 0, 5, 0, 8, 1],
                      [0, 5, 0, 3, 4, 0, 6, 0, 0],
                      [4, 0, 2, 0, 0, 0, 0, 0, 0],
                      [0, 3, 4, 0, 0, 0, 1, 0, 0],
                      [9, 0, 0, 8, 0, 0, 0, 5, 0],
                      [0, 0, 0, 4, 0, 0, 3, 0, 7]])

    start(setup)
    return







# Call main function
if __name__ == '__main__':
    main()