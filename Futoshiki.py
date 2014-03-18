'''
Created on Mar 15, 2014

@author: FilipOprisan,IoanaCalinoiu
'''
from PyQt4 import QtGui,QtCore
import sys
import random

class Futoshiki_interface(QtGui.QApplication):
    main_window=""
    game_matrix=""
    game_grid=""
    nrsquares=""
 
    def __init__(self, args):
        
        QtGui.QApplication.__init__(self, args)
        self.initUi()
    
    
    
    
    
    def initUi(self):
        
        
        self.main_window=QtGui.QFrame()
        self.main_window.setLayout(QtGui.QVBoxLayout())
        self.main_window.setFixedSize(600,600)
        self.main_window.setWindowTitle('Futoshiki')
        
        menubar=QtGui.QMenuBar(self.main_window)
        app_menu=QtGui.QMenu('Game',menubar)
        help_menu=QtGui.QMenu('Help',menubar)
    
        menubar.addMenu(app_menu)
        menubar.addMenu(help_menu)
        
        startgame_action = QtGui.QAction( '&Start a new game', self)      
        startgame_action.triggered.connect(self.selectLevel)
        startgame_action.setShortcut('F5')
        app_menu.addAction(startgame_action)
        
        
    #show rules action
        showrules_action=QtGui.QAction('&Rules',self)
        showrules_action.triggered.connect(self.showrules)
        help_menu.addAction(showrules_action)
        
        showtips_action=QtGui.QAction('Tips',self)
        showtips_action.triggered.connect(self.showtips)
        help_menu.addAction(showtips_action)
        
        
        imagelabel=QtGui.QLabel(self.main_window)
        imagelabel.setPixmap(QtGui.QPixmap('fimage.jpg'))
        imagelabel.setScaledContents(True)
        
        self.main_window.layout().addWidget(imagelabel)
        
        
        self.main_window.layout().setMenuBar(menubar)
        self.main_window.show()
    
    def selectLevel(self):
        for i in reversed(range(self.main_window.layout().count())):
            try: 
                self.main_window.layout().itemAt(i).widget().setParent(None)
            except:
                 for j in reversed(range(self.game_grid.count())):
                    self.game_grid.itemAt(j).widget().setParent(None)
        easy_button=QtGui.QPushButton('Easy',self.main_window)
        
        medium_button=QtGui.QPushButton('Medium',self.main_window)
        hard_button=QtGui.QPushButton('Hard',self.main_window)
        
        easy_button.clicked.connect(self.levelclick)
        medium_button.clicked.connect(self.levelclick)
        hard_button.clicked.connect(self.levelclick)
        self.main_window.layout().addWidget(easy_button)
        self.main_window.layout().addWidget(medium_button)
        self.main_window.layout().addWidget(hard_button)
        
        
    def levelclick(self):
        sender=self.sender()
        if(sender.text()=='Easy'):
            self.newgameclick(16)
        elif(sender.text()=='Medium'):
            self.newgameclick(19)
        else:
            self.newgameclick(22)
    def newgameclick(self,level):
        #clear everything already present in the layout
        for i in reversed(range(self.main_window.layout().count())):
            try: 
                self.main_window.layout().itemAt(i).widget().setParent(None)
            except:
                 for j in reversed(range(self.game_grid.count())):
                    self.game_grid.itemAt(j).widget().setParent(None)
               
                
        self.game_matrix=readfile('futoshiki1.txt')         
                
        self.game_grid=generategrid(self.game_matrix,level
                                    ,self.main_window)
        self.main_window.layout().addLayout(self.game_grid)
        verify_button=QtGui.QPushButton('Verify',self.main_window)
        verify_button.clicked.connect(self.verifygrid)
        self.main_window.layout().addWidget(verify_button)
        
      
    def verifygrid(self):
        #verify grid method.
        
        

        numbermat=[[0 for x in range(5)] for y in range(5)]
        aidlist=[0 for z in range(25)]
        
        
        aidlist1=[0 for z in range(25)]
       
        row=0
        column=0
        i=0
        j=0
        k=0
        
        for i in range(9):
            for j in range(9):
                
                try:
                    int(self.game_matrix[i][j])
                    aidlist[k]=self.game_matrix[i][j]
                    k=k+1
                except ValueError:
                    ok=True
                    
        k=0
        for row in range(5):
            for column in range(5):
                numbermat[row][column]=aidlist[k]
                k=k+1
        k=0
        for z in range(0,self.game_grid.count()):
            try:
                int(self.game_grid.itemAt(z).widget().toPlainText())
                aidlist1[k]=self.game_grid.itemAt(z).widget().toPlainText().strip(" ")
                k=k+1
            except:
                ok=True
        
        
        verifymatrix=[[0 for x in range(5)] for y in range(5)]
        k=0
        for i in range(0,5):
            for j in range(0,5):
                verifymatrix[i][j]=aidlist1[k]
                k=k+1
        
        
        result=QtGui.QMessageBox(self.main_window)
        if verifymatrix==numbermat:
            
            
            result.setText('You have completed this puzzle!Great job!')
            
           
        else:
            result.setText('The solution you have found is not correct.Try again!')
            
            
        for i in range(0,9,2):
           for j in range(0,9,2):
               
                self.game_grid.itemAtPosition(i,j).widget().setStyleSheet('color:black')
        for i in range(0,9,2):
           for j in range(0,9,2):
               if self.game_matrix[i][j]!=self.game_grid.itemAtPosition(i,j).widget().toPlainText().strip(' '):
                   x=self.game_grid.itemAtPosition(i, j).widget().toPlainText().strip(' ')
                   
                   
                   self.game_grid.itemAtPosition(i,j).widget().setStyleSheet('color:red')
        
      
        
        
        
        result.setFixedSize(10,10)
        
        
        
        result.setWindowTitle('Result')
        result.show()
             

        
    def showrules(self):
        rulesdialog=QtGui.QDialog(self.main_window)
        rules=QtGui.QTextBrowser(rulesdialog)
        rules.setText("""What are the rules of Futoshiki?

Futoshiki is a fun puzzle game. The rules of futoshiki are as follows:

You start with a grid that is usually 5 x 5 in shape, or 7 x 7 for larger futoshiki puzzles.

There are also greater than and less than signs between certain cells on the grid.

The aim is to fill each row and column with 1 - 5 exactly once (assuming a 5 x 5 grid) - this rule is familiar from sudoku.

However there are no box regions to concern you as in sudoku.

The big difference is the inequality signs, and you must obey these in your answers. For instance if you have that a cell is greater than the one next to it, then you know the left cell cannot be 1 and the right cell cannot be 5.

Use logic alone to deduce where each number goes and solve the puzzle.
""")
        rules.show()
        rules.setFixedSize(500,200)
        rulesdialog.show()
        rulesdialog.setWindowTitle("Futoshiki rules")
        
        
    def showtips(self): 
        tipsdialog=QtGui.QDialog(self.main_window) 
        tips=QtGui.QTextBrowser(tipsdialog)
        tips.setText("""Solving the puzzle requires a combination of logical techniques.[1] Numbers in each row and column restrict the number of possible values for each position, as do the inequalities.
Once the table of possibilities has been determined, a crucial tactic to solve the puzzle involves "AB elimination", in which subsets are identified within a row whose range of values can be determined. For example, if the first two squares within a row must contain 1 or 2, then these numbers can be excluded from the remaining squares. Similarly, if the first three squares must contain 1 or 2; 1 or 3; and 1 or 2 or 3, then those remaining must contain other values (4 and 5 in a 5x5 puzzle).
Another important technique is to work through the range of possibilities in open inequalities. A value on one side of an inequality determines others, which then can be worked through the puzzle until a contradiction is reached and the first value is excluded.
Additionally, many Futoshiki puzzles are promised to possess unique solutions. If this is strictly true, then regions of the form""")
        tips.show()
        tips.setFixedSize(500,200)
        tipsdialog.show()
        tipsdialog.setWindowTitle("Tips & Tricks")
        
  
 
# Only actually do something if this script is run standalone, so we can test our 
# application, but we're also able to import this program without actually running
# any code.
def readfile(filename):       
        matric=[[0 for j in range(9)] for i in range(9)]
        with open(filename, mode="r",encoding="utf-8") as my_file:
            animals = my_file.read().strip('\n').split(" ")
            
        k=0  
        for i in range(0,9):
            for j in range(0,9):
                matric[i][j]=animals[k].rstrip('\n')
                k=k+1
        return matric
def generategrid(matrice,nrsquares,parent):
    
    
    
    matrice=readfile("futoshiki1.txt")
    xi=0
    
    while(xi<nrsquares):
        
        x=random.randrange(0,10,2)
        y=random.randrange(0,10,2)
        if matrice[x][y]!="0":
                matrice[x][y]="0"
                xi=xi+1
                      
    grid=QtGui.QGridLayout()
        
    for i in range (0,9):
        for j in range (0,9):
            try:
                 
                int(matrice[i][j])
                    
                box=QtGui.QTextEdit(matrice[i][j])
                box.setAlignment(QtCore.Qt.AlignCenter)
                if int(matrice[i][j])==0:
                    box.setText("")
                    
                    box.setFixedSize(40,40)
   
                else:
                    box.setReadOnly(True)
                    
                        
                    box.setFixedSize(40,40)
                box.setFont(QtGui.QFont("Courier",16))    
                grid.addWidget(box,i,j)
                    
            except ValueError:
                if matrice[i][j]=='|' or matrice [i][j]=='-':
                    label=QtGui.QTextEdit(parent)
                   
                    label.setReadOnly(True)
                    label.setFixedSize(40,40)
                    label.setStyleSheet('background-color:rgba(139,0,0,0);border:0px')
                        
                else:
                        
                    label=QtGui.QTextEdit(parent)
                    label.setText(matrice[i][j])
                   
                    label.setAlignment(QtCore.Qt.AlignCenter)
                    label.setReadOnly(True)
                    label.setFixedSize(40,40)
                    label.setStyleSheet('background-color:rgba(139,0,0,0);border:0px;font-size:20px')
                
                
                grid.addWidget(label,i,j)
                
    return grid

def printGrid(grid):
    for i in range(0,5):
        for j in range(0,5):
            if i==5:
                print(grid[i][j])
            else:
                print(grid[i][j],end="")
if __name__ == "__main__":
    Game = Futoshiki_interface(sys.argv)
    sys.exit(Game.exec_())
        
    
        
