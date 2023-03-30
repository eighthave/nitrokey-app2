# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'nitrokeyapp/ui/storage.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CreateHiddenVolume(object):
    def setupUi(self, CreateHiddenVolume):
        CreateHiddenVolume.setObjectName("CreateHiddenVolume")
        CreateHiddenVolume.resize(560, 456)
        CreateHiddenVolume.setWizardStyle(QtWidgets.QWizard.ClassicStyle)
        self.wizardPage1 = QtWidgets.QWizardPage()
        self.wizardPage1.setObjectName("wizardPage1")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.wizardPage1)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_14 = QtWidgets.QLabel(self.wizardPage1)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_5.addWidget(self.label_14)
        self.frame = QtWidgets.QFrame(self.wizardPage1)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.l_warning = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.l_warning.sizePolicy().hasHeightForWidth())
        self.l_warning.setSizePolicy(sizePolicy)
        self.l_warning.setMinimumSize(QtCore.QSize(66, 58))
        self.l_warning.setMaximumSize(QtCore.QSize(66, 58))
        self.l_warning.setBaseSize(QtCore.QSize(66, 58))
        self.l_warning.setText("")
        self.l_warning.setPixmap(QtGui.QPixmap("nitrokeyapp/ui/images/new/icon_warning.svg"))
        self.l_warning.setScaledContents(True)
        self.l_warning.setObjectName("l_warning")
        self.horizontalLayout.addWidget(self.l_warning)
        self.l_top_instructions = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.l_top_instructions.sizePolicy().hasHeightForWidth())
        self.l_top_instructions.setSizePolicy(sizePolicy)
        self.l_top_instructions.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.l_top_instructions.setScaledContents(False)
        self.l_top_instructions.setWordWrap(True)
        self.l_top_instructions.setOpenExternalLinks(True)
        self.l_top_instructions.setObjectName("l_top_instructions")
        self.horizontalLayout.addWidget(self.l_top_instructions, 0, QtCore.Qt.AlignVCenter)
        self.verticalLayout_5.addWidget(self.frame)
        self.groupBox_2 = QtWidgets.QGroupBox(self.wizardPage1)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_4.addWidget(self.label_3)
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(500, 50))
        self.label_2.setMaximumSize(QtCore.QSize(100, 150))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("nitrokeyapp/ui/images/HiddenVolumes_0.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_4.addWidget(self.label_2)
        self.verticalLayout_5.addWidget(self.groupBox_2)
        CreateHiddenVolume.addPage(self.wizardPage1)
        self.wizardPage = QtWidgets.QWizardPage()
        self.wizardPage.setObjectName("wizardPage")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.wizardPage)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_12 = QtWidgets.QLabel(self.wizardPage)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_2.addWidget(self.label_12)
        self.label_13 = QtWidgets.QLabel(self.wizardPage)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_2.addWidget(self.label_13)
        self.line_2 = QtWidgets.QFrame(self.wizardPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_2.sizePolicy().hasHeightForWidth())
        self.line_2.setSizePolicy(sizePolicy)
        self.line_2.setMinimumSize(QtCore.QSize(100, 0))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_2.addWidget(self.line_2)
        self.password_group = QtWidgets.QGroupBox(self.wizardPage)
        self.password_group.setObjectName("password_group")
        self.passwordObjects = QtWidgets.QFormLayout(self.password_group)
        self.passwordObjects.setObjectName("passwordObjects")
        self.label = QtWidgets.QLabel(self.password_group)
        self.label.setObjectName("label")
        self.passwordObjects.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.HVPasswordEdit = QtWidgets.QLineEdit(self.password_group)
        self.HVPasswordEdit.setText("")
        self.HVPasswordEdit.setMaxLength(20)
        self.HVPasswordEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.HVPasswordEdit.setObjectName("HVPasswordEdit")
        self.passwordObjects.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.HVPasswordEdit)
        self.label_4 = QtWidgets.QLabel(self.password_group)
        self.label_4.setObjectName("label_4")
        self.passwordObjects.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.HVPasswordEdit_2 = QtWidgets.QLineEdit(self.password_group)
        self.HVPasswordEdit_2.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.HVPasswordEdit_2.setText("")
        self.HVPasswordEdit_2.setMaxLength(20)
        self.HVPasswordEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.HVPasswordEdit_2.setObjectName("HVPasswordEdit_2")
        self.passwordObjects.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.HVPasswordEdit_2)
        self.ShowPasswordCheckBox = QtWidgets.QCheckBox(self.password_group)
        self.ShowPasswordCheckBox.setObjectName("ShowPasswordCheckBox")
        self.passwordObjects.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.ShowPasswordCheckBox)
        self.entropy_verticalLayout = QtWidgets.QVBoxLayout()
        self.entropy_verticalLayout.setObjectName("entropy_verticalLayout")
        self.label_10 = QtWidgets.QLabel(self.password_group)
        self.label_10.setObjectName("label_10")
        self.entropy_verticalLayout.addWidget(self.label_10)
        self.password_strength_progressBar = QtWidgets.QProgressBar(self.password_group)
        self.password_strength_progressBar.setProperty("value", 42)
        self.password_strength_progressBar.setObjectName("password_strength_progressBar")
        self.entropy_verticalLayout.addWidget(self.password_strength_progressBar)
        self.chars_kind_layout = QtWidgets.QHBoxLayout()
        self.chars_kind_layout.setObjectName("chars_kind_layout")
        self.cb_length = QtWidgets.QCheckBox(self.password_group)
        self.cb_length.setEnabled(False)
        self.cb_length.setFocusPolicy(QtCore.Qt.NoFocus)
        self.cb_length.setObjectName("cb_length")
        self.chars_kind_layout.addWidget(self.cb_length)
        self.cb_lower_case = QtWidgets.QCheckBox(self.password_group)
        self.cb_lower_case.setEnabled(False)
        self.cb_lower_case.setFocusPolicy(QtCore.Qt.NoFocus)
        self.cb_lower_case.setObjectName("cb_lower_case")
        self.chars_kind_layout.addWidget(self.cb_lower_case)
        self.cb_upper_case = QtWidgets.QCheckBox(self.password_group)
        self.cb_upper_case.setEnabled(False)
        self.cb_upper_case.setFocusPolicy(QtCore.Qt.NoFocus)
        self.cb_upper_case.setCheckable(True)
        self.cb_upper_case.setObjectName("cb_upper_case")
        self.chars_kind_layout.addWidget(self.cb_upper_case)
        self.cb_numbers = QtWidgets.QCheckBox(self.password_group)
        self.cb_numbers.setEnabled(False)
        self.cb_numbers.setFocusPolicy(QtCore.Qt.NoFocus)
        self.cb_numbers.setObjectName("cb_numbers")
        self.chars_kind_layout.addWidget(self.cb_numbers)
        self.cb_symbols = QtWidgets.QCheckBox(self.password_group)
        self.cb_symbols.setEnabled(False)
        self.cb_symbols.setFocusPolicy(QtCore.Qt.NoFocus)
        self.cb_symbols.setObjectName("cb_symbols")
        self.chars_kind_layout.addWidget(self.cb_symbols)
        self.entropy_verticalLayout.addLayout(self.chars_kind_layout)
        self.passwordObjects.setLayout(3, QtWidgets.QFormLayout.SpanningRole, self.entropy_verticalLayout)
        self.verticalLayout_2.addWidget(self.password_group)
        CreateHiddenVolume.addPage(self.wizardPage)
        self.wizardPage_2 = QtWidgets.QWizardPage()
        self.wizardPage_2.setObjectName("wizardPage_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.wizardPage_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_11 = QtWidgets.QLabel(self.wizardPage_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_3.addWidget(self.label_11)
        self.label_9 = QtWidgets.QLabel(self.wizardPage_2)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_3.addWidget(self.label_9)
        self.line = QtWidgets.QFrame(self.wizardPage_2)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_3.addWidget(self.line)
        self.HV_settings_groupBox = QtWidgets.QGroupBox(self.wizardPage_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.HV_settings_groupBox.sizePolicy().hasHeightForWidth())
        self.HV_settings_groupBox.setSizePolicy(sizePolicy)
        self.HV_settings_groupBox.setMinimumSize(QtCore.QSize(100, 101))
        self.HV_settings_groupBox.setCheckable(False)
        self.HV_settings_groupBox.setObjectName("HV_settings_groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.HV_settings_groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.label_5 = QtWidgets.QLabel(self.HV_settings_groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1, QtCore.Qt.AlignTop)
        self.horizontalSlider_storage = QtWidgets.QSlider(self.HV_settings_groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalSlider_storage.sizePolicy().hasHeightForWidth())
        self.horizontalSlider_storage.setSizePolicy(sizePolicy)
        self.horizontalSlider_storage.setInputMethodHints(QtCore.Qt.ImhNone)
        self.horizontalSlider_storage.setMaximum(30)
        self.horizontalSlider_storage.setPageStep(1)
        self.horizontalSlider_storage.setProperty("value", 15)
        self.horizontalSlider_storage.setSliderPosition(15)
        self.horizontalSlider_storage.setTracking(False)
        self.horizontalSlider_storage.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_storage.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.horizontalSlider_storage.setTickInterval(1)
        self.horizontalSlider_storage.setObjectName("horizontalSlider_storage")
        self.gridLayout.addWidget(self.horizontalSlider_storage, 1, 0, 1, 2)
        self.StartControls_3 = QtWidgets.QHBoxLayout()
        self.StartControls_3.setObjectName("StartControls_3")
        self.l_sd_start_3 = QtWidgets.QLabel(self.HV_settings_groupBox)
        self.l_sd_start_3.setText("Hidden Volume Size:")
        self.l_sd_start_3.setObjectName("l_sd_start_3")
        self.StartControls_3.addWidget(self.l_sd_start_3)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.StartControls_3.addItem(spacerItem)
        self.StartBlockSpin_3 = QtWidgets.QDoubleSpinBox(self.HV_settings_groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.StartBlockSpin_3.sizePolicy().hasHeightForWidth())
        self.StartBlockSpin_3.setSizePolicy(sizePolicy)
        self.StartBlockSpin_3.setAccessibleName("")
        self.StartBlockSpin_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.StartBlockSpin_3.setDecimals(0)
        self.StartBlockSpin_3.setMaximum(30.0)
        self.StartBlockSpin_3.setProperty("value", 15.0)
        self.StartBlockSpin_3.setObjectName("StartBlockSpin_3")
        self.StartControls_3.addWidget(self.StartBlockSpin_3)
        self.label_7 = QtWidgets.QLabel(self.HV_settings_groupBox)
        self.label_7.setObjectName("label_7")
        self.StartControls_3.addWidget(self.label_7)
        self.rd_MB_3 = QtWidgets.QRadioButton(self.HV_settings_groupBox)
        self.rd_MB_3.setObjectName("rd_MB_3")
        self.StartControls_3.addWidget(self.rd_MB_3)
        self.rd_GB_3 = QtWidgets.QRadioButton(self.HV_settings_groupBox)
        self.rd_GB_3.setChecked(True)
        self.rd_GB_3.setObjectName("rd_GB_3")
        self.StartControls_3.addWidget(self.rd_GB_3)
        self.gridLayout.addLayout(self.StartControls_3, 0, 0, 1, 2)
        self.label_6 = QtWidgets.QLabel(self.HV_settings_groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 2, 1, 1, 1, QtCore.Qt.AlignRight|QtCore.Qt.AlignTop)
        self.verticalLayout_3.addWidget(self.HV_settings_groupBox)
        CreateHiddenVolume.addPage(self.wizardPage_2)
        self.wizardPage_3 = QtWidgets.QWizardPage()
        self.wizardPage_3.setObjectName("wizardPage_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.wizardPage_3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_16 = QtWidgets.QLabel(self.wizardPage_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.verticalLayout.addWidget(self.label_16)
        self.label_8 = QtWidgets.QLabel(self.wizardPage_3)
        self.label_8.setObjectName("label_8")
        self.verticalLayout.addWidget(self.label_8)
        self.line_3 = QtWidgets.QFrame(self.wizardPage_3)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout.addWidget(self.line_3)
        self.frame_2 = QtWidgets.QFrame(self.wizardPage_3)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.l_warning_2 = QtWidgets.QLabel(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.l_warning_2.sizePolicy().hasHeightForWidth())
        self.l_warning_2.setSizePolicy(sizePolicy)
        self.l_warning_2.setMinimumSize(QtCore.QSize(66, 58))
        self.l_warning_2.setMaximumSize(QtCore.QSize(66, 58))
        self.l_warning_2.setBaseSize(QtCore.QSize(66, 58))
        self.l_warning_2.setText("")
        self.l_warning_2.setPixmap(QtGui.QPixmap("nitrokeyapp/ui/images/new/icon_warning.svg"))
        self.l_warning_2.setScaledContents(True)
        self.l_warning_2.setObjectName("l_warning_2")
        self.horizontalLayout_2.addWidget(self.l_warning_2)
        self.label_17 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("")
        self.label_17.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_2.addWidget(self.label_17)
        self.verticalLayout.addWidget(self.frame_2)
        self.label_15 = QtWidgets.QLabel(self.wizardPage_3)
        self.label_15.setObjectName("label_15")
        self.verticalLayout.addWidget(self.label_15)
        self.checkBox_confirm = QtWidgets.QCheckBox(self.wizardPage_3)
        self.checkBox_confirm.setObjectName("checkBox_confirm")
        self.verticalLayout.addWidget(self.checkBox_confirm)
        CreateHiddenVolume.addPage(self.wizardPage_3)

        self.retranslateUi(CreateHiddenVolume)
        QtCore.QMetaObject.connectSlotsByName(CreateHiddenVolume)

    def retranslateUi(self, CreateHiddenVolume):
        _translate = QtCore.QCoreApplication.translate
        CreateHiddenVolume.setWindowTitle(_translate("CreateHiddenVolume", "Wizard"))
        self.label_14.setText(_translate("CreateHiddenVolume", "Information"))
        self.l_top_instructions.setText(_translate("CreateHiddenVolume", "<html><head/><body><p><span style=\" font-weight:600;\">You should understand the properties of hidden volume before proceeding. It can destroy your encrypted data! </span></p></body></html>"))
        self.groupBox_2.setTitle(_translate("CreateHiddenVolume", "Hidden Volume Conditions"))
        self.label_3.setText(_translate("CreateHiddenVolume", "1. If you decide to configure hidden volume, you can not use the\n"
" encrypted storage anymore. \n"
"2. This process may damage your existing encrypted volume data."))
        self.label_12.setText(_translate("CreateHiddenVolume", "Password"))
        self.label_13.setText(_translate("CreateHiddenVolume", "You must set a password to open the hidden volume in the future."))
        self.password_group.setTitle(_translate("CreateHiddenVolume", "Password settings"))
        self.label.setText(_translate("CreateHiddenVolume", "Password:"))
        self.HVPasswordEdit.setAccessibleName(_translate("CreateHiddenVolume", "Hidden volume password"))
        self.HVPasswordEdit.setAccessibleDescription(_translate("CreateHiddenVolume", "Please use shift+tab key shortcut for instructions"))
        self.label_4.setText(_translate("CreateHiddenVolume", "confirm Password:"))
        self.HVPasswordEdit_2.setAccessibleName(_translate("CreateHiddenVolume", "Hidden volume password (repeated)"))
        self.ShowPasswordCheckBox.setText(_translate("CreateHiddenVolume", "Show password"))
        self.label_10.setText(_translate("CreateHiddenVolume", "Password strength:"))
        self.password_strength_progressBar.setAccessibleName(_translate("CreateHiddenVolume", "Password strength:"))
        self.cb_length.setText(_translate("CreateHiddenVolume", "length"))
        self.cb_lower_case.setText(_translate("CreateHiddenVolume", "lower case"))
        self.cb_upper_case.setText(_translate("CreateHiddenVolume", "upper case"))
        self.cb_numbers.setText(_translate("CreateHiddenVolume", "numbers"))
        self.cb_symbols.setText(_translate("CreateHiddenVolume", "symbols"))
        self.label_11.setText(_translate("CreateHiddenVolume", "Hidden Volume Settings"))
        self.label_9.setText(_translate("CreateHiddenVolume", "Here you can define the size of the hidden volume."))
        self.HV_settings_groupBox.setTitle(_translate("CreateHiddenVolume", "Hidden Volume Size"))
        self.label_5.setText(_translate("CreateHiddenVolume", "Min"))
        self.label_7.setText(_translate("CreateHiddenVolume", "Unit:"))
        self.rd_MB_3.setAccessibleDescription(_translate("CreateHiddenVolume", "Use this as hidden volume size unit"))
        self.rd_MB_3.setText(_translate("CreateHiddenVolume", "MB"))
        self.rd_GB_3.setAccessibleDescription(_translate("CreateHiddenVolume", "Use this as hidden volume size unit"))
        self.rd_GB_3.setText(_translate("CreateHiddenVolume", "GB"))
        self.label_6.setText(_translate("CreateHiddenVolume", "Max"))
        self.label_16.setText(_translate("CreateHiddenVolume", "Confirmation"))
        self.label_8.setText(_translate("CreateHiddenVolume", "Are you sure to create hidden volume on your Nitrokey Storage?"))
        self.label_17.setText(_translate("CreateHiddenVolume", "Note: once you have created the hidden volume,\n"
"\n"
"you should not use the encrypted volume again, \n"
"\n"
"as you may damage data in the process!"))
        self.label_15.setText(_translate("CreateHiddenVolume", "Are you sure you want to set up the hidden volume?"))
        self.checkBox_confirm.setText(_translate("CreateHiddenVolume", "Create Hidden Volume"))
