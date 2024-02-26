from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidgetItem
import sys
from PyQt5 import QtCore, QtGui
from ss import Ui_MainWindow  
from database_utils import connect_database, fetch_tables, close_database

def zop_database():
    con = connect_database("tutorial.db")
    cursor = con.cursor()

    tables = fetch_tables(cursor)

    for table in tables:
        item = QListWidgetItem(table[0])
        ui.listWidget_2.addItem(item)

    close_database(con)
    

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    zop_database()

    MainWindow.show()
    sys.exit(app.exec_())
