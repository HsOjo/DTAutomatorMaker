# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidgetScene = QtWidgets.QTabWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidgetScene.sizePolicy().hasHeightForWidth())
        self.tabWidgetScene.setSizePolicy(sizePolicy)
        self.tabWidgetScene.setObjectName("tabWidgetScene")
        self.tabFeatures = QtWidgets.QWidget()
        self.tabFeatures.setObjectName("tabFeatures")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tabFeatures)
        self.gridLayout_4.setContentsMargins(8, 8, 8, 8)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.tableWidgetFeatures = QtWidgets.QTableWidget(self.tabFeatures)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidgetFeatures.sizePolicy().hasHeightForWidth())
        self.tableWidgetFeatures.setSizePolicy(sizePolicy)
        self.tableWidgetFeatures.setMinimumSize(QtCore.QSize(0, 0))
        self.tableWidgetFeatures.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidgetFeatures.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidgetFeatures.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidgetFeatures.setObjectName("tableWidgetFeatures")
        self.tableWidgetFeatures.setColumnCount(4)
        self.tableWidgetFeatures.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetFeatures.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetFeatures.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetFeatures.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetFeatures.setHorizontalHeaderItem(3, item)
        self.tableWidgetFeatures.horizontalHeader().setVisible(True)
        self.tableWidgetFeatures.horizontalHeader().setDefaultSectionSize(84)
        self.tableWidgetFeatures.verticalHeader().setVisible(False)
        self.gridLayout_4.addWidget(self.tableWidgetFeatures, 0, 0, 1, 1)
        self.tabWidgetScene.addTab(self.tabFeatures, "")
        self.tabObjects = QtWidgets.QWidget()
        self.tabObjects.setObjectName("tabObjects")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tabObjects)
        self.gridLayout_5.setContentsMargins(8, 8, 8, 8)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.tableWidgetObjects = QtWidgets.QTableWidget(self.tabObjects)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidgetObjects.sizePolicy().hasHeightForWidth())
        self.tableWidgetObjects.setSizePolicy(sizePolicy)
        self.tableWidgetObjects.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidgetObjects.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidgetObjects.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidgetObjects.setObjectName("tableWidgetObjects")
        self.tableWidgetObjects.setColumnCount(5)
        self.tableWidgetObjects.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetObjects.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetObjects.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetObjects.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetObjects.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetObjects.setHorizontalHeaderItem(4, item)
        self.tableWidgetObjects.horizontalHeader().setDefaultSectionSize(84)
        self.tableWidgetObjects.verticalHeader().setVisible(False)
        self.gridLayout_5.addWidget(self.tableWidgetObjects, 0, 0, 1, 1)
        self.tabWidgetScene.addTab(self.tabObjects, "")
        self.tabActions = QtWidgets.QWidget()
        self.tabActions.setObjectName("tabActions")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.tabActions)
        self.gridLayout_6.setContentsMargins(8, 8, 8, 8)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.tableWidgetActions = QtWidgets.QTableWidget(self.tabActions)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidgetActions.sizePolicy().hasHeightForWidth())
        self.tableWidgetActions.setSizePolicy(sizePolicy)
        self.tableWidgetActions.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidgetActions.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidgetActions.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidgetActions.setObjectName("tableWidgetActions")
        self.tableWidgetActions.setColumnCount(5)
        self.tableWidgetActions.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetActions.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetActions.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetActions.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetActions.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetActions.setHorizontalHeaderItem(4, item)
        self.tableWidgetActions.horizontalHeader().setDefaultSectionSize(84)
        self.tableWidgetActions.verticalHeader().setVisible(False)
        self.gridLayout_6.addWidget(self.tableWidgetActions, 0, 0, 1, 1)
        self.tabWidgetScene.addTab(self.tabActions, "")
        self.gridLayout.addWidget(self.tabWidgetScene, 0, 1, 1, 1)
        self.groupBoxPreview = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBoxPreview.sizePolicy().hasHeightForWidth())
        self.groupBoxPreview.setSizePolicy(sizePolicy)
        self.groupBoxPreview.setObjectName("groupBoxPreview")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBoxPreview)
        self.gridLayout_3.setContentsMargins(8, 8, 8, 8)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.scrollArea = QtWidgets.QScrollArea(self.groupBoxPreview)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 431, 254))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_Preview = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_Preview.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_Preview.setObjectName("gridLayout_Preview")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_3.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.horizontalSliderScale = QtWidgets.QSlider(self.groupBoxPreview)
        self.horizontalSliderScale.setMinimum(10)
        self.horizontalSliderScale.setMaximum(100)
        self.horizontalSliderScale.setProperty("value", 100)
        self.horizontalSliderScale.setOrientation(QtCore.Qt.Vertical)
        self.horizontalSliderScale.setObjectName("horizontalSliderScale")
        self.gridLayout_3.addWidget(self.horizontalSliderScale, 0, 1, 1, 1)
        self.gridLayout.addWidget(self.groupBoxPreview, 1, 1, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setContentsMargins(8, 8, 8, 8)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tableWidgetScenes = QtWidgets.QTableWidget(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidgetScenes.sizePolicy().hasHeightForWidth())
        self.tableWidgetScenes.setSizePolicy(sizePolicy)
        self.tableWidgetScenes.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidgetScenes.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidgetScenes.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidgetScenes.setObjectName("tableWidgetScenes")
        self.tableWidgetScenes.setColumnCount(3)
        self.tableWidgetScenes.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetScenes.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetScenes.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetScenes.setHorizontalHeaderItem(2, item)
        self.tableWidgetScenes.horizontalHeader().setDefaultSectionSize(72)
        self.gridLayout_2.addWidget(self.tableWidgetScenes, 0, 1, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 2, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuDevice = QtWidgets.QMenu(self.menubar)
        self.menuDevice.setObjectName("menuDevice")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionCaptureScene = QtWidgets.QAction(MainWindow)
        self.actionCaptureScene.setObjectName("actionCaptureScene")
        self.actionSelectDevice = QtWidgets.QAction(MainWindow)
        self.actionSelectDevice.setObjectName("actionSelectDevice")
        self.actionRenameScene = QtWidgets.QAction(MainWindow)
        self.actionRenameScene.setObjectName("actionRenameScene")
        self.actionDeleteItem = QtWidgets.QAction(MainWindow)
        self.actionDeleteItem.setObjectName("actionDeleteItem")
        self.actionEditItem = QtWidgets.QAction(MainWindow)
        self.actionEditItem.setObjectName("actionEditItem")
        self.actionSetItemParams = QtWidgets.QAction(MainWindow)
        self.actionSetItemParams.setObjectName("actionSetItemParams")
        self.actionRemoveScene = QtWidgets.QAction(MainWindow)
        self.actionRemoveScene.setObjectName("actionRemoveScene")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave)
        self.menuEdit.addAction(self.actionCaptureScene)
        self.menuEdit.addAction(self.actionRenameScene)
        self.menuEdit.addAction(self.actionRemoveScene)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionDeleteItem)
        self.menuEdit.addAction(self.actionEditItem)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionSetItemParams)
        self.menuDevice.addAction(self.actionSelectDevice)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuDevice.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidgetScene.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DTAutomatorMaker"))
        item = self.tableWidgetFeatures.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "index"))
        item = self.tableWidgetFeatures.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "name"))
        item = self.tableWidgetFeatures.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "rect"))
        item = self.tableWidgetFeatures.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "detect_weight"))
        self.tabWidgetScene.setTabText(self.tabWidgetScene.indexOf(self.tabFeatures), _translate("MainWindow", "Features"))
        item = self.tableWidgetObjects.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "index"))
        item = self.tableWidgetObjects.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "name"))
        item = self.tableWidgetObjects.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "rect"))
        item = self.tableWidgetObjects.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "type"))
        item = self.tableWidgetObjects.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "actions"))
        self.tabWidgetScene.setTabText(self.tabWidgetScene.indexOf(self.tabObjects), _translate("MainWindow", "Objects"))
        item = self.tableWidgetActions.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "index"))
        item = self.tableWidgetActions.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "name"))
        item = self.tableWidgetActions.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "type"))
        item = self.tableWidgetActions.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "dest_scene"))
        item = self.tableWidgetActions.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "params"))
        self.tabWidgetScene.setTabText(self.tabWidgetScene.indexOf(self.tabActions), _translate("MainWindow", "Actions"))
        self.groupBoxPreview.setTitle(_translate("MainWindow", "Preview"))
        self.horizontalSliderScale.setToolTip(_translate("MainWindow", "Scale"))
        self.groupBox.setTitle(_translate("MainWindow", "Scenes"))
        item = self.tableWidgetScenes.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "name"))
        item = self.tableWidgetScenes.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "features"))
        item = self.tableWidgetScenes.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "objects"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuDevice.setTitle(_translate("MainWindow", "Device"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionCaptureScene.setText(_translate("MainWindow", "Capture Scene"))
        self.actionCaptureScene.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionSelectDevice.setText(_translate("MainWindow", "Select Device"))
        self.actionSelectDevice.setShortcut(_translate("MainWindow", "Ctrl+D"))
        self.actionRenameScene.setText(_translate("MainWindow", "Rename Scene"))
        self.actionRenameScene.setShortcut(_translate("MainWindow", "F2"))
        self.actionDeleteItem.setText(_translate("MainWindow", "Delete Item"))
        self.actionDeleteItem.setShortcut(_translate("MainWindow", "Del"))
        self.actionEditItem.setText(_translate("MainWindow", "Edit Item"))
        self.actionEditItem.setShortcut(_translate("MainWindow", "Return"))
        self.actionSetItemParams.setText(_translate("MainWindow", "Set Item Parameters"))
        self.actionSetItemParams.setShortcut(_translate("MainWindow", "Ctrl+E"))
        self.actionRemoveScene.setText(_translate("MainWindow", "Remove Scene"))
        self.actionRemoveScene.setShortcut(_translate("MainWindow", "Ctrl+Backspace"))
