# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/christianbeiwinkel/Documents/internship/dev/qrouting/qrouting/ui/raw/waypoint_widget.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_WaypointWidget(object):
    def setupUi(self, WaypointWidget):
        WaypointWidget.setObjectName("WaypointWidget")
        WaypointWidget.resize(296, 325)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(WaypointWidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.scrollArea = QtWidgets.QScrollArea(WaypointWidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 270, 299))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.scrollAreaWidgetContents)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.groupBox = QtWidgets.QGroupBox(self.page)
        self.groupBox.setGeometry(QtCore.QRect(0, 10, 241, 261))
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.add_wp = QtWidgets.QToolButton(self.groupBox)
        self.add_wp.setObjectName("add_wp")
        self.horizontalLayout_2.addWidget(self.add_wp)
        self.remove_wp = QtWidgets.QToolButton(self.groupBox)
        self.remove_wp.setObjectName("remove_wp")
        self.horizontalLayout_2.addWidget(self.remove_wp)
        self.add_from_layer = QtWidgets.QToolButton(self.groupBox)
        self.add_from_layer.setObjectName("add_from_layer")
        self.horizontalLayout_2.addWidget(self.add_from_layer)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.move_up = QtWidgets.QToolButton(self.groupBox)
        self.move_up.setObjectName("move_up")
        self.horizontalLayout_2.addWidget(self.move_up)
        self.move_down = QtWidgets.QToolButton(self.groupBox)
        self.move_down.setObjectName("move_down")
        self.horizontalLayout_2.addWidget(self.move_down)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.coord_table = QtWidgets.QTableWidget(self.groupBox)
        self.coord_table.setObjectName("coord_table")
        self.coord_table.setColumnCount(2)
        self.coord_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.coord_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.coord_table.setHorizontalHeaderItem(1, item)
        self.horizontalLayout_4.addWidget(self.coord_table)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.stackedWidget.addWidget(self.page_2)
        self.verticalLayout.addWidget(self.stackedWidget)
        self.verticalLayout_5.addLayout(self.verticalLayout)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout_3.addWidget(self.scrollArea)

        self.retranslateUi(WaypointWidget)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(WaypointWidget)

    def retranslateUi(self, WaypointWidget):
        _translate = QtCore.QCoreApplication.translate
        WaypointWidget.setWindowTitle(_translate("WaypointWidget", "Form"))
        self.groupBox.setTitle(_translate("WaypointWidget", "Waypoints"))
        self.add_wp.setText(_translate("WaypointWidget", "..."))
        self.remove_wp.setText(_translate("WaypointWidget", "..."))
        self.add_from_layer.setText(_translate("WaypointWidget", "..."))
        self.move_up.setText(_translate("WaypointWidget", "..."))
        self.move_down.setText(_translate("WaypointWidget", "..."))
        item = self.coord_table.horizontalHeaderItem(0)
        item.setText(_translate("WaypointWidget", "Lat"))
        item = self.coord_table.horizontalHeaderItem(1)
        item.setText(_translate("WaypointWidget", "Lon"))
