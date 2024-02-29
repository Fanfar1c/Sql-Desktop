from PyQt5 import QtCore, QtGui, QtWidgets
from database_utils import DatabaseManager

database_name = "tutorial.db"


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(809, 602)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 811, 561))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.listWidget_2 = QtWidgets.QListWidget(self.horizontalLayoutWidget)
        self.listWidget_2.setObjectName("listWidget_2")
        self.horizontalLayout.addWidget(self.listWidget_2)
        self.listWidget_3 = QtWidgets.QListWidget(self.horizontalLayoutWidget)
        self.listWidget_3.setObjectName("listWidget_3")
        self.horizontalLayout.addWidget(self.listWidget_3)
        self.listWidget = QtWidgets.QListWidget(self.horizontalLayoutWidget)
        self.listWidget.setObjectName("listWidget")
        self.horizontalLayout.addWidget(self.listWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 809, 21))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menu.addSeparator()
        self.menubar.addAction(self.menu.menuAction())
        self.retranslateUi(MainWindow)
        self.setup_list_widget()
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.createdatebase()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menu.setTitle(_translate("MainWindow", "Меню"))
        
    def setup_list_widget(self):

        self.listWidget_2.clicked.connect(lambda: self.item_double_clicked(self.listWidget_2))

    def item_double_clicked(self, list_widget):

        selected_item = list_widget.currentItem()
        if selected_item:
            item_text = selected_item.text()
            
            with DatabaseManager(database_name) as db_manager:
                tables = db_manager.select_slot_two(item_text)
                
                item = QtWidgets.QListWidgetItem(item_text)
                for table in tables:
                    item.addChild(table[1])
                    #self.listWidget_2.addItem(item)
                    self.listWidget_3.addTopLevelItem(item)
                    #table_item.addChild(id_item)
                    

    def createdatebase(self):
        with DatabaseManager(database_name) as db_manager:
            tables = db_manager.fetch_tables()
            for table in tables:
                item = QtWidgets.QListWidgetItem(table[0])
                self.listWidget_2.addItem(item)
        
        