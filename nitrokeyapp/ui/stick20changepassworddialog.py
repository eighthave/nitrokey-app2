# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'nitrokeyapp/ui/stick20changepassworddialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DialogChangePassword(object):
    def setupUi(self, DialogChangePassword):
        DialogChangePassword.setObjectName("DialogChangePassword")
        DialogChangePassword.resize(420, 369)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DialogChangePassword.sizePolicy().hasHeightForWidth())
        DialogChangePassword.setSizePolicy(sizePolicy)
        DialogChangePassword.setMinimumSize(QtCore.QSize(420, 300))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/new/icon_NK.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DialogChangePassword.setWindowIcon(icon)
        self.verticalLayout = QtWidgets.QVBoxLayout(DialogChangePassword)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(DialogChangePassword)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setAutoFillBackground(False)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setObjectName("frame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setText("Old PIN")
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEdit_OldPW = QtWidgets.QLineEdit(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_OldPW.sizePolicy().hasHeightForWidth())
        self.lineEdit_OldPW.setSizePolicy(sizePolicy)
        self.lineEdit_OldPW.setObjectName("lineEdit_OldPW")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_OldPW)
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setText("New PIN")
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.lineEdit_NewPW_1 = QtWidgets.QLineEdit(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_NewPW_1.sizePolicy().hasHeightForWidth())
        self.lineEdit_NewPW_1.setSizePolicy(sizePolicy)
        self.lineEdit_NewPW_1.setObjectName("lineEdit_NewPW_1")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_NewPW_1)
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setText("New PIN")
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.lineEdit_NewPW_2 = QtWidgets.QLineEdit(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_NewPW_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_NewPW_2.setSizePolicy(sizePolicy)
        self.lineEdit_NewPW_2.setObjectName("lineEdit_NewPW_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_NewPW_2)
        self.checkBox = QtWidgets.QCheckBox(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox.sizePolicy().hasHeightForWidth())
        self.checkBox.setSizePolicy(sizePolicy)
        self.checkBox.setObjectName("checkBox")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.checkBox)
        self.verticalLayout_4.addLayout(self.formLayout)
        self.label_additional_information = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_additional_information.sizePolicy().hasHeightForWidth())
        self.label_additional_information.setSizePolicy(sizePolicy)
        self.label_additional_information.setMouseTracking(True)
        self.label_additional_information.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.label_additional_information.setScaledContents(False)
        self.label_additional_information.setWordWrap(True)
        self.label_additional_information.setObjectName("label_additional_information")
        self.verticalLayout_4.addWidget(self.label_additional_information)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.retryCountLabel = QtWidgets.QLabel(self.frame)
        self.retryCountLabel.setObjectName("retryCountLabel")
        self.horizontalLayout.addWidget(self.retryCountLabel)
        self.retryCount = QtWidgets.QLabel(self.frame)
        self.retryCount.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.retryCount.setAccessibleName("")
        self.retryCount.setText("3")
        self.retryCount.setObjectName("retryCount")
        self.horizontalLayout.addWidget(self.retryCount)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.verticalLayout.addWidget(self.frame)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.line = QtWidgets.QFrame(DialogChangePassword)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.buttonBox = QtWidgets.QDialogButtonBox(DialogChangePassword)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout_2.addWidget(self.buttonBox)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(DialogChangePassword)
        self.buttonBox.accepted.connect(DialogChangePassword.accept) # type: ignore
        self.buttonBox.rejected.connect(DialogChangePassword.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(DialogChangePassword)
        DialogChangePassword.setTabOrder(self.lineEdit_OldPW, self.lineEdit_NewPW_1)
        DialogChangePassword.setTabOrder(self.lineEdit_NewPW_1, self.lineEdit_NewPW_2)
        DialogChangePassword.setTabOrder(self.lineEdit_NewPW_2, self.checkBox)
        DialogChangePassword.setTabOrder(self.checkBox, self.label_additional_information)
        DialogChangePassword.setTabOrder(self.label_additional_information, self.retryCount)

    def retranslateUi(self, DialogChangePassword):
        _translate = QtCore.QCoreApplication.translate
        DialogChangePassword.setWindowTitle(_translate("DialogChangePassword", "Change user PIN"))
        self.lineEdit_OldPW.setAccessibleName(_translate("DialogChangePassword", "Current PIN or password"))
        self.lineEdit_NewPW_1.setAccessibleName(_translate("DialogChangePassword", "New PIN or password"))
        self.lineEdit_NewPW_2.setAccessibleName(_translate("DialogChangePassword", "New PIN or password"))
        self.checkBox.setText(_translate("DialogChangePassword", "Show PIN"))
        self.label_additional_information.setText(_translate("DialogChangePassword", "<html><head/><body><p><span style=\" font-style:italic;\">Nitrokey prevents against brute force password guessing attacks by allowing a maximum of 3 incorrect PIN attempts. Therefore a PIN of %1 digits is sufficient. The PIN must be between %1 and %2 characters.</span></p></body></html>"))
        self.retryCountLabel.setText(_translate("DialogChangePassword", "Retry count left:"))
        self.retryCount.setAccessibleDescription(_translate("DialogChangePassword", "Retry count left:"))
import resources_rc
