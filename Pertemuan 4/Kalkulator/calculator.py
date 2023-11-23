from PyQt5 import QtCore, QtGui, QtWidgets
from interface import Ui_MainWindow
ok=True
#Slots

def affiche1():
    global ok
    if(ok==True):
        ui.lineEdit.setText(ui.lineEdit.text()+"1")
    else:
        ui.lineEdit.setText("1")
        ok=True
def affiche2():
    global ok
    if(ok==True):
        ui.lineEdit.setText(ui.lineEdit.text()+"2")
    else:
        ui.lineEdit.setText("2")
        ok=True
def affiche3():
    global ok
    if(ok==True):
        ui.lineEdit.setText(ui.lineEdit.text()+"3")
    else:
        ui.lineEdit.setText("3")
        ok=True
def affiche4():
    global ok
    if(ok==True):
        ui.lineEdit.setText(ui.lineEdit.text()+"4")
    else:
        ui.lineEdit.setText("4")
        ok=True
def affiche5():
    global ok
    if(ok==True):
        ui.lineEdit.setText(ui.lineEdit.text()+"5")
    else:
        ui.lineEdit.setText("5")
        ok=True
def affiche6():
    global ok
    if(ok==True):
        ui.lineEdit.setText(ui.lineEdit.text()+"6")
    else:
        ui.lineEdit.setText("6")
        ok=True
def affiche7():
    global ok
    if(ok==True):
        ui.lineEdit.setText(ui.lineEdit.text()+"7")
    else:
        ui.lineEdit.setText("7")
        ok=True
def affiche8():
    global ok
    if(ok==True):   
        ui.lineEdit.setText(ui.lineEdit.text()+"8")
    else:
        ui.lineEdit.setText("8")
        ok=True
def affiche9():
    global ok
    if(ok==True):
        ui.lineEdit.setText(ui.lineEdit.text()+"9")
    else:
        ui.lineEdit.setText("9")
        ok=True
def affiche0():
    global ok
    if(ok==True):
        ui.lineEdit.setText(ui.lineEdit.text()+"0")
    else:
        ui.lineEdit.setText("0")
        ok=True
def affichePoint():
    ui.lineEdit.setText(ui.lineEdit.text()+".")
def afficheDivise():
    ui.lineEdit.setText(ui.lineEdit.text()+"/")
def afficheMult():
    ui.lineEdit.setText(ui.lineEdit.text()+"*")
def afficheMoins():
    ui.lineEdit.setText(ui.lineEdit.text()+"-")
def affichePlus():
    ui.lineEdit.setText(ui.lineEdit.text()+"+")
def afficheDiv():
    ui.lineEdit.setText(ui.lineEdit.text()+"//")
def afficheMod():
    ui.lineEdit.setText(ui.lineEdit.text()+"%")
def affichePo():
    ui.lineEdit.setText(ui.lineEdit.text()+"(")
def affichePf():
    ui.lineEdit.setText(ui.lineEdit.text()+")")
def afficheAc():
    ui.lineEdit.setText("")
def afficheDel():
    ui.lineEdit.setText(ui.lineEdit.text()[:-1])
def afficheEgale():
    global ok
    ui.lineEdit.setText(str(eval(ui.lineEdit.text())))
    ok=False
import sys
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()

#Connections
ui.b_del.clicked.connect(afficheDel)
ui.b_ac.clicked.connect(afficheAc)
ui.b_egale.clicked.connect(afficheEgale)
ui.b_1.clicked.connect(affiche1)
ui.b_2.clicked.connect(affiche2)
ui.b_3.clicked.connect(affiche3)
ui.b_4.clicked.connect(affiche4)
ui.b_5.clicked.connect(affiche5)
ui.b_6.clicked.connect(affiche6)
ui.b_7.clicked.connect(affiche7)
ui.b_8.clicked.connect(affiche8)
ui.b_9.clicked.connect(affiche9)
ui.b_0.clicked.connect(affiche0)
ui.b_plus.clicked.connect(affichePlus)
ui.b_moins.clicked.connect(afficheMoins)
ui.b_mult.clicked.connect(afficheMult)
ui.b_divise.clicked.connect(afficheDivise)
ui.b_div.clicked.connect(afficheDiv)
ui.b_mod.clicked.connect(afficheMod)
ui.b_point.clicked.connect(affichePoint)
ui.b_po.clicked.connect(affichePo)
ui.b_pf.clicked.connect(affichePf)


sys.exit(app.exec_())