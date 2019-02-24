#Minesweeper.py
import time;
import copy;
import random;
import tkinter;

class Game:
    def __init__(self):
        self.over = False;
        self.win = False;
        self.standard = [];
        self.clickLeftPos = [];
        self.clickRightPos = [];
        self.clickDoublePos = [];
        for i in range(len(grid.field)):
            self.standard.append(str(i+1));
        tk.bind("<Button-1>",self.clickLeft);
        tk.bind("<Button-3>",self.clickRight);
        tk.bind("<Double-Button-1>",self.clickDouble);
        
    def main(self):
        self.T1 = time.time();
        while self.over == False and self.win == False:
            canvas.update();
            if self.clickLeftPos != []:
                self.step();
        if g.over == True:
            canvas.create_text(side/2, side/2, text="Game Over!", font=("Comic Sans MS", 50), fill="red");
            canvas.update();
        elif g.win == True:
            canvas.create_text(side/2, side/2-30, text="You Win!", font=("Comic Sans MS", 50), fill="navy");
            self.T2 = time.time();
            canvas.create_text(side/2, side/2+30, text=("Your Time: %.2f seconds." % (self.T2 - self.T1)), font=("Comic Sans MS", 20), fill="navy");
            canvas.update();

    def step(self):
        self.judgeWin();
        if self.x in self.standard and self.y in self.standard:
            if grid.field[int(self.x)-1][int(self.y)-1] == -1:
                canvas.itemconfig(len(grid.field)*(int(self.x)-1)+int(self.y), fill="black", text="✹", font=("Times", int(grid.L/1.5)));
                self.over = True;
            else:
                try:
                    grid.turned[int(self.x)-1][int(self.y)-1] = 1;
                except:
                    pass;
                finally:
                    grid.extendEmpty();
                    
    def judgeWin(self):
        remain = 0;
        for i in range(0, len(grid.field)):
            for j in range(0, len(grid.field)):
                if grid.turned[i][j] == 0:
                    remain += 1;
        if remain == number:
            self.win = True;
                
    def clickLeft(self, event):
        self.clickLeftPos = [];
        self.clickLeftPos.append(event.x);
        self.clickLeftPos.append(event.y);
        self.x = str(int(self.clickLeftPos[1]/grid.L)+1);
        self.y = str(int(self.clickLeftPos[0]/grid.L)+1);
        
    def clickRight(self, event):
        self.clickRightPos = [];
        self.clickRightPos.append(event.x);
        self.clickRightPos.append(event.y);
        self.x2 = str(int(self.clickRightPos[1]/grid.L)+1);
        self.y2 = str(int(self.clickRightPos[0]/grid.L)+1);
        try:
            grid.marked[int(self.x2)-1][int(self.y2)-1] = not grid.marked[int(self.x2)-1][int(self.y2)-1];
        except:
            pass;
        
    def clickDouble(self, event):
        self.clickDoublePos = [];
        self.clickDoublePos.append(event.x);
        self.clickDoublePos.append(event.y);
        self.x3 = str(int(self.clickDoublePos[1]/grid.L)+1);
        self.y3 = str(int(self.clickDoublePos[0]/grid.L)+1);
        grid.extend();
        
class Grid:
    def __init__(self, length, number):
        self.length = length;
        self.number = number;
        self.field = self.field();
        self.turned = self.turned();
        self.marked = self.marked();
        self.setMine();
        self.genNumber();
        self.drawGrid();

    def drawGrid(self):
        self.L = side / self.length;
        for i in range(0, len(self.field)):
            for j in range(0, len(self.field)):
                canvas.create_text(self.L/2+self.L*j, self.L/2+self.L*i, text="?", font=("Comic Sans MS", int(self.L/2.5)));
        for i in range(0, len(self.field)-1):
            canvas.create_line(0, self.L*(i+1), side, self.L*(i+1));
            canvas.create_line(self.L*(i+1), 0, self.L*(i+1), side);
        
    def field(self):
        self.field = [[0 for i in range(self.length)] for i in range(self.length)];
        return self.field;

    def turned(self):
        self.turned = [[0 for i in range(len(self.field))] for i in range(len(self.field))];
        return self.turned;

    def marked(self):
        self.marked = [[False for i in range(len(self.field))] for i in range(len(self.field))];
        return self.marked;

    def setMine(self):
        for i in range(self.number):
            x = random.randint(0, len(self.field)-1);
            y = random.randint(0, len(self.field)-1);
            while self.field[x][y] == -1:
                x = random.randint(0, len(self.field)-1);
                y = random.randint(0, len(self.field)-1);
            self.field[x][y] = -1;

    def extendEmpty(self):
        copied = [];
        while copied != self.turned:
            copied = copy.deepcopy(self.turned);
            for i in range(0, len(self.field)):
                for j in range(0, len(self.field)):
                    if self.field[i][j] == 0 and self.turned[i][j] == 1:
                        if i>=1 and j>=1:
                            self.turned[i-1][j-1] = 1;
                        if i>=1 and j>=0:
                            self.turned[i-1][j] = 1;
                        if i>=1 and j<=len(self.field)-2:
                            self.turned[i-1][j+1] = 1;
                        if i>=0 and j>=1:
                            self.turned[i][j-1] = 1;
                        if i>=0 and j<=len(self.field)-2:
                            self.turned[i][j+1] = 1;
                        if i<=len(self.field)-2 and j>=1:
                            self.turned[i+1][j-1] = 1;
                        if i<=len(self.field)-2 and j>=0:
                            self.turned[i+1][j] = 1;
                        if i<=len(self.field)-2 and j<=len(self.field)-2:
                            self.turned[i+1][j+1] = 1;
            self.writeNumber();
        
    def writeNumber(self):
        for i in range(0, len(self.field)):
            for j in range(0, len(self.field)):
                if self.turned[i][j] == 1:
                    if self.field[i][j] == 0:
                        canvas.itemconfig(len(self.field)*i+j+1, text=" ", font=("Times", int(self.L/1.75)));
                    if self.field[i][j] == 1:
                        canvas.itemconfig(len(self.field)*i+j+1, fill="blue", text="1", font=("Comic Sans MS", int(self.L/1.75)));
                    if self.field[i][j] == 2:
                        canvas.itemconfig(len(self.field)*i+j+1, fill="green", text="2", font=("Comic Sans MS", int(self.L/1.75)));
                    if self.field[i][j] == 3:
                        canvas.itemconfig(len(self.field)*i+j+1, fill="red", text="3", font=("Comic Sans MS", int(self.L/1.75)));
                    if self.field[i][j] == 4:
                        canvas.itemconfig(len(self.field)*i+j+1, fill="orange", text="4", font=("Comic Sans MS", int(self.L/1.75)));
                    if self.field[i][j] == 5:
                        canvas.itemconfig(len(self.field)*i+j+1, fill="magenta", text="5", font=("Comic Sans MS", int(self.L/1.75)));
                    if self.field[i][j] == 6:
                        canvas.itemconfig(len(self.field)*i+j+1, fill="cyan", text="6", font=("Comic Sans MS", int(self.L/1.75)));
                    if self.field[i][j] == 7:
                        canvas.itemconfig(len(self.field)*i+j+1, fill="teal", text="7", font=("Comic Sans MS", int(self.L/1.75)));
                    if self.field[i][j] == 8:
                        canvas.itemconfig(len(self.field)*i+j+1, fill="navy", text="8", font=("Comic Sans MS", int(self.L/1.75)));
                elif self.turned[i][j] == 0:
                    if self.marked[i][j] == False:
                        canvas.itemconfig(len(self.field)*i+j+1, fill="black", text="?", font=("Comic Sans MS", int(self.L/2.5)));
                    if self.marked[i][j] == True:
                        canvas.itemconfig(len(self.field)*i+j+1, fill="black", text="♖", font=("Comic Sans MS", int(self.L/2.5)));
                                
    def extend(self):
        try:
            self.x3 = int(g.x3)-1;
            self.y3 = int(g.y3)-1;
            self.mineAround = 0;
            self.markedAround = 0;
            if 0 < self.field[self.x3][self.y3] < 9:
                if self.x3>=1 and self.y3>=1:
                    if self.field[self.x3-1][self.y3-1] == -1:
                        self.mineAround += 1;
                    if self.marked[self.x3-1][self.y3-1] == True:
                        self.markedAround += 1;
                if self.x3>=1 and self.y3>=0:
                    if self.field[self.x3-1][self.y3] == -1:
                        self.mineAround += 1;
                    if self.marked[self.x3-1][self.y3] == True:
                        self.markedAround += 1;
                if self.x3>=1 and self.y3<=len(self.field)-2:
                    if self.field[self.x3-1][self.y3+1] == -1:
                        self.mineAround += 1;
                    if self.marked[self.x3-1][self.y3+1] == True:
                        self.markedAround += 1;
                if self.x3>=0 and self.y3>=1:
                    if self.field[self.x3][self.y3-1] == -1:
                        self.mineAround += 1;
                    if self.marked[self.x3][self.y3-1] == True:
                        self.markedAround += 1;
                if self.x3>=0 and self.y3<=len(self.field)-2:
                    if self.field[self.x3][self.y3+1] == -1:
                        self.mineAround += 1;
                    if self.marked[self.x3][self.y3+1] == True:
                        self.markedAround += 1;
                if self.x3<=len(self.field)-2 and self.y3>=1:
                    if self.field[self.x3+1][self.y3-1] == -1:
                        self.mineAround += 1;
                    if self.marked[self.x3+1][self.y3-1] == True:
                        self.markedAround += 1;
                if self.x3<=len(self.field)-2 and self.y3>=0:
                    if self.field[self.x3+1][self.y3] == -1:
                        self.mineAround += 1;
                    if self.marked[self.x3+1][self.y3] == True:
                        self.markedAround += 1;
                if self.x3<=len(self.field)-2 and self.y3<=len(self.field)-2:
                    if self.field[self.x3+1][self.y3+1] == -1:
                        self.mineAround += 1;
                    if self.marked[self.x3+1][self.y3+1] == True:
                        self.markedAround += 1;
                                
            if self.mineAround == self.markedAround:
                if self.x3>=1 and self.y3>=1 and self.field[self.x3-1][self.y3-1] != -1:
                    self.turned[self.x3-1][self.y3-1] = 1;
                    if self.marked[self.x3-1][self.y3-1] == True:
                        canvas.itemconfig(len(self.field)*(self.x3-1)+self.y3, fill="red", text="×", font=("Times", int(self.L)));
                        g.over = True;
                if self.x3>=1 and self.y3>=0 and self.field[self.x3-1][self.y3] != -1:
                    self.turned[self.x3-1][self.y3] = 1;
                    if self.marked[self.x3-1][self.y3] == True:
                        canvas.itemconfig(len(self.field)*(self.x3-1)+self.y3+1, fill="red", text="×", font=("Times", int(self.L)));
                        g.over = True;
                if self.x3>=1 and self.y3<=len(self.field)-2 and self.field[self.x3-1][self.y3+1] != -1:
                    self.turned[self.x3-1][self.y3+1] = 1;
                    if self.marked[self.x3-1][self.y3+1] == True:
                        canvas.itemconfig(len(self.field)*(self.x3-1)+self.y3+2, fill="red", text="×", font=("Times", int(self.L)));
                        g.over = True;
                if self.x3>=0 and self.y3>=1 and self.field[self.x3][self.y3-1] != -1:
                    self.turned[self.x3][self.y3-1] = 1;
                    if self.marked[self.x3][self.y3-1] == True:
                        canvas.itemconfig(len(self.field)*self.x3+self.y3, fill="red", text="×", font=("Times", int(self.L)));
                        g.over = True;
                if self.x3>=0 and self.y3<=len(self.field)-2 and self.field[self.x3][self.y3+1] != -1:
                    self.turned[self.x3][self.y3+1] = 1;
                    if self.marked[self.x3][self.y3+1] == True:
                        canvas.itemconfig(len(self.field)*self.x3+self.y3+2, fill="red", text="×", font=("Times", int(self.L)));
                        g.over = True;
                if self.x3<=len(self.field)-2 and self.y3>=1 and self.field[self.x3+1][self.y3-1] != -1:
                    self.turned[self.x3+1][self.y3-1] = 1;
                    if self.marked[self.x3+1][self.y3-1] == True:
                        canvas.itemconfig(len(self.field)*(self.x3+1)+self.y3, fill="red", text="×", font=("Times", int(self.L)));
                        g.over = True;
                if self.x3<=len(self.field)-2 and self.y3>=0 and self.field[self.x3+1][self.y3] != -1:
                    self.turned[self.x3+1][self.y3] = 1;
                    if self.marked[self.x3+1][self.y3] == True:
                        canvas.itemconfig(len(self.field)*(self.x3+1)+self.y3+1, fill="red", text="×", font=("Times", int(self.L)));
                        g.over = True;
                if self.x3<=len(self.field)-2 and self.y3<=len(self.field)-2 and self.field[self.x3+1][self.y3+1] != -1:
                    self.turned[self.x3+1][self.y3+1] = 1;
                    if self.marked[self.x3+1][self.y3+1] == True:
                        canvas.itemconfig(len(self.field)*(self.x3+1)+self.y3+2, fill="red", text="×", font=("Times", int(self.L)));
                        g.over = True;
        except:
            pass;
                    
    def genNumber(self):
        for i in range(0, len(self.field)):
            for j in range(0, len(self.field)):
                if self.field[i][j] == -1:
                    if i>=1 and j>=1 and self.field[i-1][j-1] != -1:
                        self.field[i-1][j-1] += 1;
                    if i>=1 and j>=0 and self.field[i-1][j] != -1:
                        self.field[i-1][j] += 1;
                    if i>=1 and j<=len(self.field)-2 and self.field[i-1][j+1] != -1:
                        self.field[i-1][j+1] += 1;
                    if i>=0 and j>=1 and self.field[i][j-1] != -1:
                        self.field[i][j-1] += 1;
                    if i>=0 and j<=len(self.field)-2 and self.field[i][j+1] != -1:
                        self.field[i][j+1] += 1;
                    if i<=len(self.field)-2 and j>=1 and self.field[i+1][j-1] != -1:
                        self.field[i+1][j-1] += 1;
                    if i<=len(self.field)-2 and j>=0 and self.field[i+1][j] != -1:
                        self.field[i+1][j] += 1;
                    if i<=len(self.field)-2 and j<=len(self.field)-2 and self.field[i+1][j+1] != -1:
                        self.field[i+1][j+1] += 1;

side = 800;
tk = tkinter.Tk();
tk.title("Minesweeper");
tk.resizable(0,0);
tk.wm_attributes("-topmost", 1);
canvas = tkinter.Canvas(tk, width=side, height=side);
        
length = 16;
number = 35;
grid = Grid(length=length, number=number);
canvas.pack();

g = Game();

g.main();











