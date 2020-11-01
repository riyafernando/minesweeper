from tkinter import *
from tkinter import filedialog

root = Tk()
root.title('Shadow')

class MineCell(Label):
    '''represents a MineSweeper cell'''

    def __init__(self,master, number,coord1, coord2):
        '''SudokuCell(master,coord) -> SudokuCell
        creates a new blank SudokuCell with (row,column) coord'''

        Label.__init__(self, master, width=2, height=1, text ='', bg='white', font=('Arial', 24), fg='dim grey', bd=5,\
                       relief=GROOVE)
        self.highlighted = False  # starts unhighlighted
        # set up listeners
        self.bind('<1>', self.check_pressed)
        self.exposed = False
        self.coord1 = coord1
        self.coord2 = coord2
        self.grid(row=self.coord1, column=self.coord2)
        self.num = number
        self.coords = [self.coord1, self.coord2]

    def check_exposed(self):
        return self.exposed

    def check_pressed(self, other):
        self['relief'] = SUNKEN
        self['bg'] = 'grey'
        self.display(self.num)

    def num(self):
        return self.num

    def display(self, other):
        self['text'] = str(self.num)
        if self.num == 0:
            self['text'] = ''
            self.exposed = True
        self.color()

    def coords(self):
        return self.coords


    def color(self):
        colormap = ['', 'blue', 'darkgreen', 'red', 'purple', 'maroon', 'cyan', 'black', 'dim gray']

        if self['text'] == '1':
            self['fg'] = colormap[1]

        if self['text'] == '2':
            self['fg'] = colormap[2]

        if self['text'] == '3':
            self['fg'] = colormap[3]

        if self['text'] == '4':
            self['fg'] = colormap[4]

        if self['text'] == '5':
            self['fg'] = colormap[5]

        if self['text'] == '6':
            self['fg'] = colormap[6]

        if self['text'] == '7':
            self['fg'] = colormap[7]

        if self['text'] == '8':
            self['fg'] = colormap[8]



class MineGrid:
    '''represents a MineSweeper Grid'''

    def __init__(self, num1, num2):
        #rows,cols
        self.cells = []
        self.coords = {}
        for i in range(0, num1):
            for y in range(0, num2):
                d = MineCell(root, i+y, int(i), int(y))
                self.cells += [d]
                self.coords[i, y] = d

        self.exposed_cells = []
        self.passButton = Button(text='Mark',command=self.mark_button)
        self.passButton.grid(row= 18, column= 17)




    def number(self):
        pass

    def isclicked(self):
            for i in self.cells:
                if i.check_exposed():
                    self.exposed_cells += i.coords


    def get_cells(self):
        print(self.cells)

    def bomb(self):
        pass

    def auto_expose(self):
        for i in self.exposed_cells:
            print('sdfdsdfs')

    def mark_button(self):
        print("sigh")








r = MineGrid(10, 15)
root.mainloop()
