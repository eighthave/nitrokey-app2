# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'nitrokeyapp/ui/settings.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(916, 605)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.btn_writeSettings = QtWidgets.QDialogButtonBox(Dialog)
        self.btn_writeSettings.setOrientation(QtCore.Qt.Horizontal)
        self.btn_writeSettings.setStandardButtons(QtWidgets.QDialogButtonBox.Close|QtWidgets.QDialogButtonBox.Save)
        self.btn_writeSettings.setObjectName("btn_writeSettings")
        self.gridLayout.addWidget(self.btn_writeSettings, 1, 0, 1, 1)
        self.tabWidget_2 = QtWidgets.QTabWidget(Dialog)
        self.tabWidget_2.setEnabled(True)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_8 = QtWidgets.QWidget()
        self.tab_8.setObjectName("tab_8")
        self.formLayout = QtWidgets.QFormLayout(self.tab_8)
        self.formLayout.setObjectName("formLayout")
        self.frame_9 = QtWidgets.QFrame(self.tab_8)
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.frame_9)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.gr_general = QtWidgets.QGroupBox(self.frame_9)
        self.gr_general.setObjectName("gr_general")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.gr_general)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.cb_first_run_message_2 = QtWidgets.QCheckBox(self.gr_general)
        self.cb_first_run_message_2.setObjectName("cb_first_run_message_2")
        self.horizontalLayout_20.addWidget(self.cb_first_run_message_2)
        self.cb_show_window_on_start_2 = QtWidgets.QCheckBox(self.gr_general)
        self.cb_show_window_on_start_2.setObjectName("cb_show_window_on_start_2")
        self.horizontalLayout_20.addWidget(self.cb_show_window_on_start_2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_20)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.cb_hide_main_window_on_close_2 = QtWidgets.QCheckBox(self.gr_general)
        self.cb_hide_main_window_on_close_2.setChecked(True)
        self.cb_hide_main_window_on_close_2.setObjectName("cb_hide_main_window_on_close_2")
        self.horizontalLayout_18.addWidget(self.cb_hide_main_window_on_close_2)
        self.cb_hide_main_window_on_connection_2 = QtWidgets.QCheckBox(self.gr_general)
        self.cb_hide_main_window_on_connection_2.setChecked(True)
        self.cb_hide_main_window_on_connection_2.setObjectName("cb_hide_main_window_on_connection_2")
        self.horizontalLayout_18.addWidget(self.cb_hide_main_window_on_connection_2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_18)
        self.cb_show_main_window_on_connection_2 = QtWidgets.QCheckBox(self.gr_general)
        self.cb_show_main_window_on_connection_2.setChecked(True)
        self.cb_show_main_window_on_connection_2.setObjectName("cb_show_main_window_on_connection_2")
        self.verticalLayout_4.addWidget(self.cb_show_main_window_on_connection_2)
        self.cb_check_symlink_2 = QtWidgets.QCheckBox(self.gr_general)
        self.cb_check_symlink_2.setChecked(True)
        self.cb_check_symlink_2.setObjectName("cb_check_symlink_2")
        self.verticalLayout_4.addWidget(self.cb_check_symlink_2)
        self.cb_device_connection_message_2 = QtWidgets.QCheckBox(self.gr_general)
        self.cb_device_connection_message_2.setChecked(True)
        self.cb_device_connection_message_2.setObjectName("cb_device_connection_message_2")
        self.verticalLayout_4.addWidget(self.cb_device_connection_message_2)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_29 = QtWidgets.QLabel(self.gr_general)
        self.label_29.setObjectName("label_29")
        self.horizontalLayout_13.addWidget(self.label_29)
        self.combo_languages_2 = QtWidgets.QComboBox(self.gr_general)
        self.combo_languages_2.setObjectName("combo_languages_2")
        self.horizontalLayout_13.addWidget(self.combo_languages_2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_13)
        self.verticalLayout_15.addWidget(self.gr_general)
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.frame_9)
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_8)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.spin_PWS_time = QtWidgets.QSpinBox(self.groupBox_2)
        self.spin_PWS_time.setMinimum(10)
        self.spin_PWS_time.setMaximum(600)
        self.spin_PWS_time.setProperty("value", 60)
        self.spin_PWS_time.setObjectName("spin_PWS_time")
        self.gridLayout_4.addWidget(self.spin_PWS_time, 1, 1, 1, 1)
        self.spin_OTP_time = QtWidgets.QSpinBox(self.groupBox_2)
        self.spin_OTP_time.setMinimum(10)
        self.spin_OTP_time.setMaximum(600)
        self.spin_OTP_time.setProperty("value", 120)
        self.spin_OTP_time.setObjectName("spin_OTP_time")
        self.gridLayout_4.addWidget(self.spin_OTP_time, 3, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem, 1, 2, 1, 1)
        self.label_31 = QtWidgets.QLabel(self.groupBox_2)
        self.label_31.setObjectName("label_31")
        self.gridLayout_4.addWidget(self.label_31, 3, 0, 1, 1)
        self.label_30 = QtWidgets.QLabel(self.groupBox_2)
        self.label_30.setObjectName("label_30")
        self.gridLayout_4.addWidget(self.label_30, 1, 0, 1, 1)
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.groupBox_2)
        self.frame_4 = QtWidgets.QFrame(self.tab_8)
        self.frame_4.setAutoFillBackground(False)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_11 = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_12.addWidget(self.label_11)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.enableUserPasswordCheckBox = QtWidgets.QCheckBox(self.frame_4)
        self.enableUserPasswordCheckBox.setObjectName("enableUserPasswordCheckBox")
        self.verticalLayout_2.addWidget(self.enableUserPasswordCheckBox)
        self.deleteUserPasswordCheckBox = QtWidgets.QCheckBox(self.frame_4)
        self.deleteUserPasswordCheckBox.setObjectName("deleteUserPasswordCheckBox")
        self.verticalLayout_2.addWidget(self.deleteUserPasswordCheckBox)
        self.verticalLayout_12.addLayout(self.verticalLayout_2)
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.frame_4)
        self.line_4 = QtWidgets.QFrame(self.tab_8)
        self.line_4.setMinimumSize(QtCore.QSize(870, 0))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.line_4)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.formLayout.setLayout(4, QtWidgets.QFormLayout.LabelRole, self.horizontalLayout_11)
        self.tabWidget_2.addTab(self.tab_8, "")
        self.tab_12 = QtWidgets.QWidget()
        self.tab_12.setObjectName("tab_12")
        self.formLayout_2 = QtWidgets.QFormLayout(self.tab_12)
        self.formLayout_2.setObjectName("formLayout_2")
        self.groupBox = QtWidgets.QGroupBox(self.tab_12)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.edit_debug_file_path = QtWidgets.QLineEdit(self.groupBox)
        self.edit_debug_file_path.setObjectName("edit_debug_file_path")
        self.gridLayout_3.addWidget(self.edit_debug_file_path, 1, 1, 1, 1)
        self.spin_debug_verbosity = QtWidgets.QSpinBox(self.groupBox)
        self.spin_debug_verbosity.setMaximum(6)
        self.spin_debug_verbosity.setProperty("value", 2)
        self.spin_debug_verbosity.setObjectName("spin_debug_verbosity")
        self.gridLayout_3.addWidget(self.spin_debug_verbosity, 3, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.groupBox)
        self.label_10.setObjectName("label_10")
        self.gridLayout_3.addWidget(self.label_10, 1, 0, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.groupBox)
        self.label_20.setObjectName("label_20")
        self.gridLayout_3.addWidget(self.label_20, 3, 0, 1, 1)
        self.cb_debug_enabled = QtWidgets.QCheckBox(self.groupBox)
        self.cb_debug_enabled.setAccessibleName("")
        self.cb_debug_enabled.setObjectName("cb_debug_enabled")
        self.gridLayout_3.addWidget(self.cb_debug_enabled, 0, 0, 1, 1)
        self.btn_select_debug_console = QtWidgets.QPushButton(self.groupBox)
        self.btn_select_debug_console.setObjectName("btn_select_debug_console")
        self.gridLayout_3.addWidget(self.btn_select_debug_console, 1, 2, 1, 1)
        self.btn_select_debug_file_path = QtWidgets.QPushButton(self.groupBox)
        self.btn_select_debug_file_path.setObjectName("btn_select_debug_file_path")
        self.gridLayout_3.addWidget(self.btn_select_debug_file_path, 1, 3, 1, 1)
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.groupBox)
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_12)
        self.pushButton_2.setObjectName("pushButton_2")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.pushButton_2)
        self.tabWidget_2.addTab(self.tab_12, "")
        self.tab_13 = QtWidgets.QWidget()
        self.tab_13.setObjectName("tab_13")
        self.tabWidget_2.addTab(self.tab_13, "")
        self.gridLayout.addWidget(self.tabWidget_2, 0, 0, 1, 1)
        self.label_10.setBuddy(self.edit_debug_file_path)
        self.label_20.setBuddy(self.spin_debug_verbosity)

        self.retranslateUi(Dialog)
        self.tabWidget_2.setCurrentIndex(0)
        self.btn_writeSettings.accepted.connect(Dialog.accept) # type: ignore
        self.btn_writeSettings.rejected.connect(Dialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.gr_general.setTitle(_translate("Dialog", "General"))
        self.cb_first_run_message_2.setText(_translate("Dialog", "Show first-run message"))
        self.cb_show_window_on_start_2.setText(_translate("Dialog", "Show main window on start"))
        self.cb_hide_main_window_on_close_2.setText(_translate("Dialog", "Do not quit when the main window is closed"))
        self.cb_hide_main_window_on_connection_2.setText(_translate("Dialog", "Hide main window when device disconnects"))
        self.cb_show_main_window_on_connection_2.setText(_translate("Dialog", "Show main window when device connects"))
        self.cb_check_symlink_2.setText(_translate("Dialog", "Show warning when no partitions could be detected on Encrypted Volume (Linux only)"))
        self.cb_device_connection_message_2.setText(_translate("Dialog", "Show message about device\'s connection / disconnection"))
        self.label_29.setText(_translate("Dialog", "<html><head/><body><p>Translation file (needs restart)</p></body></html>"))
        self.combo_languages_2.setAccessibleName(_translate("Dialog", "Translation file (needs restart)"))
        self.groupBox_2.setTitle(_translate("Dialog", "Clipboard settings"))
        self.spin_PWS_time.setAccessibleName(_translate("Dialog", "TIme to store Password Safe secrets in clipboard (in seconds):"))
        self.spin_OTP_time.setAccessibleName(_translate("Dialog", "Time to store OTP secrets in clipboard (in seconds):"))
        self.label_31.setText(_translate("Dialog", "Time to store OTP secrets in clipboard (in seconds):"))
        self.label_30.setText(_translate("Dialog", "Time to store Password Safe secrets in clipboard (in seconds):"))
        self.label_11.setText(_translate("Dialog", "OTP Password settings"))
        self.enableUserPasswordCheckBox.setText(_translate("Dialog", "Protect OTP by user PIN (will be requested on first use each session)"))
        self.deleteUserPasswordCheckBox.setText(_translate("Dialog", "Forget user PIN after 10 minutes (if unchecked user PIN will remain in memory until application exits)"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_8), _translate("Dialog", "General"))
        self.groupBox.setTitle(_translate("Dialog", "Debug log settings"))
        self.edit_debug_file_path.setAccessibleName(_translate("Dialog", "Path for debug log file:"))
        self.spin_debug_verbosity.setAccessibleName(_translate("Dialog", "Verbosity level:"))
        self.label_10.setText(_translate("Dialog", "Path for debug log file:"))
        self.label_20.setText(_translate("Dialog", "Verbosity level:"))
        self.cb_debug_enabled.setText(_translate("Dialog", "Logging enabled"))
        self.btn_select_debug_console.setText(_translate("Dialog", "Log to console"))
        self.btn_select_debug_file_path.setText(_translate("Dialog", "Select path"))
        self.pushButton_2.setText(_translate("Dialog", "Send Problem"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_12), _translate("Dialog", "Debug"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_13), _translate("Dialog", "Firmware"))
