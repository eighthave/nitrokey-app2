# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'nitrokeyapp/ui/stick20responsedialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Stick20ResponseDialog(object):
    def setupUi(self, Stick20ResponseDialog):
        Stick20ResponseDialog.setObjectName("Stick20ResponseDialog")
        Stick20ResponseDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        Stick20ResponseDialog.resize(342, 123)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Stick20ResponseDialog.sizePolicy().hasHeightForWidth())
        Stick20ResponseDialog.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/new/icon_NK.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap(":/images/new/icon_NK.svg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        Stick20ResponseDialog.setWindowIcon(icon)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Stick20ResponseDialog)
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.HeaderText = QtWidgets.QLabel(Stick20ResponseDialog)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.HeaderText.setFont(font)
        self.HeaderText.setText("HeaderLabel")
        self.HeaderText.setTextFormat(QtCore.Qt.PlainText)
        self.HeaderText.setAlignment(QtCore.Qt.AlignCenter)
        self.HeaderText.setObjectName("HeaderText")
        self.verticalLayout.addWidget(self.HeaderText)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.LabelProgressWheel = QtWidgets.QLabel(Stick20ResponseDialog)
        self.LabelProgressWheel.setText("LabelProgressWheel")
        self.LabelProgressWheel.setAlignment(QtCore.Qt.AlignCenter)
        self.LabelProgressWheel.setObjectName("LabelProgressWheel")
        self.horizontalLayout_2.addWidget(self.LabelProgressWheel)
        self.label = QtWidgets.QLabel(Stick20ResponseDialog)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setText("")
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.progressBar = QtWidgets.QProgressBar(Stick20ResponseDialog)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.OutputText = QtWidgets.QLabel(Stick20ResponseDialog)
        font = QtGui.QFont()
        font.setFamily("Courier 10 Pitch")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.OutputText.setFont(font)
        self.OutputText.setText("TextLabel")
        self.OutputText.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.OutputText.setWordWrap(True)
        self.OutputText.setObjectName("OutputText")
        self.verticalLayout_2.addWidget(self.OutputText)
        spacerItem1 = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)

        self.retranslateUi(Stick20ResponseDialog)
        self.HeaderText.customContextMenuRequested['QPoint'].connect(Stick20ResponseDialog.open) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Stick20ResponseDialog)

    def retranslateUi(self, Stick20ResponseDialog):
        _translate = QtCore.QCoreApplication.translate
        Stick20ResponseDialog.setWindowTitle(_translate("Stick20ResponseDialog", "Progress"))
import resources_rc
