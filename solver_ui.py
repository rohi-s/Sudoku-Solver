from tkinter import *
import puzzles
import solve

root = Tk()
root.title('Sudoku Solver')

mylabel = Label(root, text='Fill in the numbers and click solve').grid(row=0, column=0,columnspan=10)

def callback(P):
    if (str.isdigit(P) and int(P) in range(1,10)) or P == "":
        return True
    else:
        return False

def beg():
    cells = {}
    grid = []
    for row in range(1, 10):
        rgrid = []
        for column in range(1, 10):
            if ((row in (1,2,3,7,8,9) and column in (4,5,6)) or (row in (4,5,6) and column in (1,2,3,7,8,9))):
                kleur='green'
            else:
                kleur='orange'
            cell = Frame(root, bg='white', highlightbackground=kleur,
                         highlightcolor=kleur, highlightthickness=2,
                         width=50, height=50,  padx=3,  pady=3)
            cell.grid(row=row, column=column)
            cells[(row, column)] = cell
            
            vcmd = (cells[row, column].register(callback))
            
            e = Entry(cells[row, column], width=3, justify='center', validate='all', validatecommand=(vcmd, '%P'))
            e.pack()
            rgrid.append(e)
        grid.append(rgrid)
    return grid

def clear():
    for i in range(9):
        for j in range(9):
            grids[i][j].delete(0, 'end')
            grids[i][j].config(bg='white')

def solvebutt():
    timeLabel.config(text=f'Time Taken : Computing...')
    root.update() 
    
    gridtsolve = []
    for i in range(9):
        gridtsolve_r = []
        for j in range(9):
            if grids[i][j].get() == '':
                gridtsolve_r.append(0)
            else:
                gridtsolve_r.append(int(grids[i][j].get()))
                grids[i][j].config(bg='lightgray')
        gridtsolve.append(gridtsolve_r)
    answer, tme = solve.solve(gridtsolve)
    try:
        answer, tme = solve.solve(gridtsolve)
        if answer is None:
            timeLabel.config(text='Cannot Solve.')
        else:
            for i in range(9):
                for j in range(9):
                    if grids[i][j].get() == '':
                        grids[i][j].insert(0, answer[i][j])
                        grids[i][j].config(bg='white')
            timeLabel.config(text=f'Time Taken : {tme:.6f} s')
    except Exception as e:
        timeLabel.config(text='Error in solving.')
        print(f"An error occurred: {e}")
    
        

def fillRand():
    sudoku = puzzles.any()
    clear()
    for i in range(9):
        for j in range(9):
            if sudoku[i][j]==0:
                grids[i][j].insert(0, "")
                grids[i][j].config(bg='white')
            else:
                grids[i][j].insert(0, sudoku[i][j])
                grids[i][j].config(bg='lightgray')

grids = beg()  # Your existing function to create the Sudoku grid

# Create a separate frame for buttons
button_frame = Frame(root)
button_frame.grid(row=11, column=0, columnspan=10, pady=20)  # Place button frame below the Sudoku grid
            

clearer = Button(button_frame, text='Clear', command=clear)
solver = Button(button_frame, text='Solve', command=solvebutt)
getRand = Button(button_frame, text='Get Random', command=fillRand)
timeLabel = Label(button_frame, text='Time Taken : 0.000000 s')

# Arrange buttons inside the button frame
clearer.grid(row=0, column=0, padx=10)
solver.grid(row=0, column=1, padx=10)
getRand.grid(row=0, column=2, padx=10)
timeLabel.grid(row=1, column=0,columnspan=10)



root.mainloop()
