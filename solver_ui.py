from tkinter import *
import example_puzzles
import solver

root = Tk()
root.title('Sudoku Solver')
#root.geometry('400x500')

mylabel = Label(root, text='Fill in the numbers and click solve').grid(row=0, column=0,columnspan=10)

def callback(P):
    if (str.isdigit(P) and int(P) in range(1,10)) or P == "":
        #if str.isdigit(P) and int(P) in range(1,10):
            #entry.focus_set()
        return True
    else:
        return False

# Create the grid
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
grids = beg()

def clear():
    for i in range(9):
        for j in range(9):
            grids[i][j].delete(0, 'end')

def solvebutt():
    gridtsolve = []
    for i in range(9):
        gridtsolve_r = []
        for j in range(9):
            if grids[i][j].get() == '':
                gridtsolve_r.append(0)
            else:
                gridtsolve_r.append(int(grids[i][j].get()))
        gridtsolve.append(gridtsolve_r)
    answer = solve.solve(gridtsolve)
    for i in range(9):
        for j in range(9):
            if grids[i][j].get() == '':
                grids[i][j].insert(0, answer[i][j])

clearer = Button(root, text='Clear', command=clear)
solver = Button(root, text='Solve', command=solvebutt)

clearer.grid(row=11, column=3, pady=30)
solver.grid(row=11, column=7, pady=30)

root.mainloop()

#print(solve.solve((example_puzzles.easy)))