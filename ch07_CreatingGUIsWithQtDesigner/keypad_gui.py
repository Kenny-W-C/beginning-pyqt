"""
Listing 7-1
written by Joshua Willman
Featured in "Beginning Pyqt - A Hands-on Approach to GUI Programming"
"""
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'keypad_.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Keypad(object):
    def setupUi(self, Keypad):
        Keypad.setObjectName("Keypad")
        Keypad.resize(302, 406)
        palette = QtGui.QPalette()

        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)

        brush = QtGui.QBrush(QtGui.QColor(52, 48, 47))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)

        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)

        brush = QtGui.QBrush(QtGui.QColor(52, 48, 47))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)

        brush = QtGui.QBrush(QtGui.QColor(52, 48, 47))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)

        brush = QtGui.QBrush(QtGui.QColor(52, 48, 47))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)

        Keypad.setPalette(palette)
        self.verticalLayout = QtWidgets.QVBoxLayout(Keypad)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Keypad)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText,
                         brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText,
                         brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText,
                         brush)
        self.label.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.frame = QtWidgets.QFrame(Keypad)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(
            self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(0)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.line_edit1 = QtWidgets.QLineEdit(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding,
                                           QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.line_edit1.sizePolicy().hasHeightForWidth())
        self.line_edit1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.line_edit1.setFont(font)
        self.line_edit1.setAlignment(QtCore.Qt.AlignCenter)
        self.line_edit1.setObjectName("line_edit1")
        self.horizontalLayout.addWidget(self.line_edit1)
        self.line_edit2 = QtWidgets.QLineEdit(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding,
                                           QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.line_edit2.sizePolicy().hasHeightForWidth())
        self.line_edit2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.line_edit2.setFont(font)
        self.line_edit2.setAlignment(QtCore.Qt.AlignCenter)
        self.line_edit2.setObjectName("line_edit2")
        self.horizontalLayout.addWidget(self.line_edit2)
        self.line_edit3 = QtWidgets.QLineEdit(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding,
                                           QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.line_edit3.sizePolicy().hasHeightForWidth())
        self.line_edit3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.line_edit3.setFont(font)
        self.line_edit3.setAlignment(QtCore.Qt.AlignCenter)
        self.line_edit3.setObjectName("line_edit3")
        self.horizontalLayout.addWidget(self.line_edit3)
        self.line_edit4 = QtWidgets.QLineEdit(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding,
                                           QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.line_edit4.sizePolicy().hasHeightForWidth())
        self.line_edit4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.line_edit4.setFont(font)
        self.line_edit4.setAlignment(QtCore.Qt.AlignCenter)
        self.line_edit4.setObjectName("line_edit4")
        self.horizontalLayout.addWidget(self.line_edit4)
        self.verticalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(Keypad)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(
            self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_2.setLineWidth(2)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout.setObjectName("gridLayout")
        self.button_7 = QtWidgets.QPushButton(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.button_7.sizePolicy().hasHeightForWidth())
        self.button_7.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(36)
        self.button_7.setFont(font)
        self.button_7.setObjectName("button_7")
        self.gridLayout.addWidget(self.button_7, 0, 0, 1, 1)
        self.button_8 = QtWidgets.QPushButton(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.button_8.sizePolicy().hasHeightForWidth())
        self.button_8.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(36)
        self.button_8.setFont(font)
        self.button_8.setObjectName("button_8")
        self.gridLayout.addWidget(self.button_8, 0, 1, 1, 1)
        self.button_9 = QtWidgets.QPushButton(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.button_9.sizePolicy().hasHeightForWidth())
        self.button_9.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(36)
        self.button_9.setFont(font)
        self.button_9.setObjectName("button_9")
        self.gridLayout.addWidget(self.button_9, 0, 2, 1, 1)
        self.button_4 = QtWidgets.QPushButton(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.button_4.sizePolicy().hasHeightForWidth())
        self.button_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(36)
        self.button_4.setFont(font)
        self.button_4.setObjectName("button_4")
        self.gridLayout.addWidget(self.button_4, 1, 0, 1, 1)
        self.button_5 = QtWidgets.QPushButton(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.button_5.sizePolicy().hasHeightForWidth())
        self.button_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(36)
        self.button_5.setFont(font)
        self.button_5.setObjectName("button_5")
        self.gridLayout.addWidget(self.button_5, 1, 1, 1, 1)
        self.button_6 = QtWidgets.QPushButton(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.button_6.sizePolicy().hasHeightForWidth())
        self.button_6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(36)
        self.button_6.setFont(font)
        self.button_6.setObjectName("button_6")
        self.gridLayout.addWidget(self.button_6, 1, 2, 1, 1)
        self.button_3 = QtWidgets.QPushButton(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.button_3.sizePolicy().hasHeightForWidth())
        self.button_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(36)
        self.button_3.setFont(font)
        self.button_3.setObjectName("button_3")
        self.gridLayout.addWidget(self.button_3, 2, 0, 1, 1)
        self.button_2 = QtWidgets.QPushButton(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.button_2.sizePolicy().hasHeightForWidth())
        self.button_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(36)
        self.button_2.setFont(font)
        self.button_2.setObjectName("button_2")
        self.gridLayout.addWidget(self.button_2, 2, 1, 1, 1)
        self.button_1 = QtWidgets.QPushButton(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.button_1.sizePolicy().hasHeightForWidth())
        self.button_1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(36)
        self.button_1.setFont(font)
        self.button_1.setObjectName("button_1")
        self.gridLayout.addWidget(self.button_1, 2, 2, 1, 1)
        self.button_star = QtWidgets.QPushButton(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.button_star.sizePolicy().hasHeightForWidth())
        self.button_star.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(36)
        self.button_star.setFont(font)
        self.button_star.setObjectName("button_star")
        self.gridLayout.addWidget(self.button_star, 3, 0, 1, 1)
        self.button_0 = QtWidgets.QPushButton(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.button_0.sizePolicy().hasHeightForWidth())
        self.button_0.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(36)
        self.button_0.setFont(font)
        self.button_0.setObjectName("button_0")
        self.gridLayout.addWidget(self.button_0, 3, 1, 1, 1)
        self.button_hash = QtWidgets.QPushButton(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.button_hash.sizePolicy().hasHeightForWidth())
        self.button_hash.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(36)
        self.button_hash.setFont(font)
        self.button_hash.setObjectName("button_hash")
        self.gridLayout.addWidget(self.button_hash, 3, 2, 1, 1)
        self.verticalLayout.addWidget(self.frame_2)

        self.retranslateUi(Keypad)
        self.button_star.clicked.connect(self.line_edit1.clear)
        self.button_star.clicked.connect(self.line_edit2.clear)
        self.button_star.clicked.connect(self.line_edit3.clear)
        self.button_star.clicked.connect(self.line_edit4.clear)
        QtCore.QMetaObject.connectSlotsByName(Keypad)

    def retranslateUi(self, Keypad):
        _translate = QtCore.QCoreApplication.translate
        Keypad.setWindowTitle(_translate("Keypad", "7.1 - Keypad GUI"))
        self.label.setText(_translate("Keypad", "Enter a passcode"))
        self.button_7.setText(_translate("Keypad", "7"))
        self.button_8.setText(_translate("Keypad", "8"))
        self.button_9.setText(_translate("Keypad", "9"))
        self.button_4.setText(_translate("Keypad", "4"))
        self.button_5.setText(_translate("Keypad", "5"))
        self.button_6.setText(_translate("Keypad", "6"))
        self.button_3.setText(_translate("Keypad", "3"))
        self.button_2.setText(_translate("Keypad", "2"))
        self.button_1.setText(_translate("Keypad", "1"))
        self.button_star.setText(_translate("Keypad", "*"))
        self.button_0.setText(_translate("Keypad", "0"))
        self.button_hash.setText(_translate("Keypad", "#"))