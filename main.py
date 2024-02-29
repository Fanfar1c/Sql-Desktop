from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidgetItem
import sys
from PyQt5 import QtCore, QtGui
from designer_main import Ui_MainWindow


# def zop_database(ui):
#     con = connect_database("tutorial.db")
#     cursor = con.cursor()

#     tables = fetch_tables(cursor)

#     for table in tables:
#         item = QListWidgetItem(table[0])
#         ui.listWidget_2.addItem(item)

#     close_database(con)
    

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    # zop_database(ui)

    MainWindow.show()
    sys.exit(app.exec_())
