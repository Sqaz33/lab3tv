# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form2.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Widget(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(1332, 683)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(Widget)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.task_selection = QtWidgets.QComboBox(Widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.task_selection.setFont(font)
        self.task_selection.setObjectName("task_selection")
        self.task_selection.addItem("")
        self.task_selection.addItem("")
        self.verticalLayout_6.addWidget(self.task_selection)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(Widget)
        self.stackedWidget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_1 = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.page_1.sizePolicy().hasHeightForWidth())
        self.page_1.setSizePolicy(sizePolicy)
        self.page_1.setObjectName("page_1")
        self.gridLayout = QtWidgets.QGridLayout(self.page_1)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.ber_formulas_CB_1 = QtWidgets.QComboBox(self.page_1)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ber_formulas_CB_1.setFont(font)
        self.ber_formulas_CB_1.setObjectName("ber_formulas_CB_1")
        self.ber_formulas_CB_1.addItem("")
        self.ber_formulas_CB_1.addItem("")
        self.verticalLayout_5.addWidget(self.ber_formulas_CB_1)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_11 = QtWidgets.QLabel(self.page_1)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_9.addWidget(self.label_11)
        self.label_12 = QtWidgets.QLabel(self.page_1)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_9.addWidget(self.label_12)
        self.label_10 = QtWidgets.QLabel(self.page_1)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_9.addWidget(self.label_10)
        self.label_9 = QtWidgets.QLabel(self.page_1)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_9.addWidget(self.label_9)
        self.label_2 = QtWidgets.QLabel(self.page_1)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_9.addWidget(self.label_2)
        self.verticalLayout_8.addLayout(self.horizontalLayout_9)
        self.verticalLayout_5.addLayout(self.verticalLayout_8)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_5.addLayout(self.horizontalLayout_5)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.p_ber = QtWidgets.QLineEdit(self.page_1)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.p_ber.setFont(font)
        self.p_ber.setObjectName("p_ber")
        self.horizontalLayout_8.addWidget(self.p_ber)
        self.n_ber = QtWidgets.QLineEdit(self.page_1)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.n_ber.setFont(font)
        self.n_ber.setObjectName("n_ber")
        self.horizontalLayout_8.addWidget(self.n_ber)
        self.m_ber = QtWidgets.QLineEdit(self.page_1)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.m_ber.setFont(font)
        self.m_ber.setObjectName("m_ber")
        self.horizontalLayout_8.addWidget(self.m_ber)
        self.m1_ber = QtWidgets.QLineEdit(self.page_1)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.m1_ber.setFont(font)
        self.m1_ber.setObjectName("m1_ber")
        self.horizontalLayout_8.addWidget(self.m1_ber)
        self.m2_ber = QtWidgets.QLineEdit(self.page_1)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.m2_ber.setFont(font)
        self.m2_ber.setObjectName("m2_ber")
        self.horizontalLayout_8.addWidget(self.m2_ber)
        self.verticalLayout_7.addLayout(self.horizontalLayout_8)
        self.verticalLayout_5.addLayout(self.verticalLayout_7)
        self.label_13 = QtWidgets.QLabel(self.page_1)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_5.addWidget(self.label_13)
        self.bernuli_oper_CB = QtWidgets.QComboBox(self.page_1)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.bernuli_oper_CB.setFont(font)
        self.bernuli_oper_CB.setObjectName("bernuli_oper_CB")
        self.bernuli_oper_CB.addItem("")
        self.bernuli_oper_CB.addItem("")
        self.bernuli_oper_CB.addItem("")
        self.bernuli_oper_CB.addItem("")
        self.verticalLayout_5.addWidget(self.bernuli_oper_CB)
        self.bernuli_formulas_LB = QtWidgets.QLabel(self.page_1)
        self.bernuli_formulas_LB.setObjectName("bernuli_formulas_LB")
        self.verticalLayout_5.addWidget(self.bernuli_formulas_LB)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.answer_bernuli = QtWidgets.QLabel(self.page_1)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.answer_bernuli.setFont(font)
        self.answer_bernuli.setObjectName("answer_bernuli")
        self.horizontalLayout_3.addWidget(self.answer_bernuli)
        self.compute_bernuli_BT = QtWidgets.QPushButton(self.page_1)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.compute_bernuli_BT.setFont(font)
        self.compute_bernuli_BT.setObjectName("compute_bernuli_BT")
        self.horizontalLayout_3.addWidget(self.compute_bernuli_BT)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.gridLayout.addLayout(self.verticalLayout_5, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_1)
        self.page_2 = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.page_2.sizePolicy().hasHeightForWidth())
        self.page_2.setSizePolicy(sizePolicy)
        self.page_2.setObjectName("page_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.page_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.ber_formulas_CB_2 = QtWidgets.QComboBox(self.page_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ber_formulas_CB_2.setFont(font)
        self.ber_formulas_CB_2.setObjectName("ber_formulas_CB_2")
        self.ber_formulas_CB_2.addItem("")
        self.ber_formulas_CB_2.addItem("")
        self.verticalLayout_3.addWidget(self.ber_formulas_CB_2)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_6 = QtWidgets.QLabel(self.page_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_11.addWidget(self.label_6)
        self.label_7 = QtWidgets.QLabel(self.page_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_11.addWidget(self.label_7)
        self.label_4 = QtWidgets.QLabel(self.page_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_11.addWidget(self.label_4)
        self.label_3 = QtWidgets.QLabel(self.page_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_11.addWidget(self.label_3)
        self.verticalLayout_3.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.n_pol = QtWidgets.QLineEdit(self.page_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.n_pol.setFont(font)
        self.n_pol.setObjectName("n_pol")
        self.horizontalLayout_4.addWidget(self.n_pol)
        self.k_pol = QtWidgets.QLineEdit(self.page_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.k_pol.setFont(font)
        self.k_pol.setObjectName("k_pol")
        self.horizontalLayout_4.addWidget(self.k_pol)
        self.p_pol = QtWidgets.QLineEdit(self.page_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.p_pol.setFont(font)
        self.p_pol.setObjectName("p_pol")
        self.horizontalLayout_4.addWidget(self.p_pol)
        self.m_pol = QtWidgets.QLineEdit(self.page_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.m_pol.setFont(font)
        self.m_pol.setObjectName("m_pol")
        self.horizontalLayout_4.addWidget(self.m_pol)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.gridLayout_3.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.pol_formulas_LB = QtWidgets.QLabel(self.page_2)
        self.pol_formulas_LB.setObjectName("pol_formulas_LB")
        self.horizontalLayout_12.addWidget(self.pol_formulas_LB)
        self.gridLayout_3.addLayout(self.horizontalLayout_12, 1, 0, 1, 1)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.pol_answer_LB = QtWidgets.QLabel(self.page_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pol_answer_LB.setFont(font)
        self.pol_answer_LB.setObjectName("pol_answer_LB")
        self.horizontalLayout_13.addWidget(self.pol_answer_LB)
        self.pol_copmute_BT = QtWidgets.QPushButton(self.page_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pol_copmute_BT.setFont(font)
        self.pol_copmute_BT.setObjectName("pol_copmute_BT")
        self.horizontalLayout_13.addWidget(self.pol_copmute_BT)
        self.gridLayout_3.addLayout(self.horizontalLayout_13, 2, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.page_3.sizePolicy().hasHeightForWidth())
        self.page_3.setSizePolicy(sizePolicy)
        self.page_3.setObjectName("page_3")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.page_3)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.label_16 = QtWidgets.QLabel(self.page_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_16.addWidget(self.label_16)
        self.label_15 = QtWidgets.QLabel(self.page_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_16.addWidget(self.label_15)
        self.label_5 = QtWidgets.QLabel(self.page_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_16.addWidget(self.label_5)
        self.label = QtWidgets.QLabel(self.page_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_16.addWidget(self.label)
        self.gridLayout_2.addLayout(self.horizontalLayout_16, 0, 0, 1, 1)
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.lap_x1_formulas_LB = QtWidgets.QLabel(self.page_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lap_x1_formulas_LB.setFont(font)
        self.lap_x1_formulas_LB.setObjectName("lap_x1_formulas_LB")
        self.horizontalLayout_22.addWidget(self.lap_x1_formulas_LB)
        self.lap_x1_answer_LB = QtWidgets.QLabel(self.page_3)
        self.lap_x1_answer_LB.setText("")
        self.lap_x1_answer_LB.setObjectName("lap_x1_answer_LB")
        self.horizontalLayout_22.addWidget(self.lap_x1_answer_LB)
        self.verticalLayout_13.addLayout(self.horizontalLayout_22)
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.lap_x2_formulas_LB = QtWidgets.QLabel(self.page_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lap_x2_formulas_LB.setFont(font)
        self.lap_x2_formulas_LB.setObjectName("lap_x2_formulas_LB")
        self.horizontalLayout_20.addWidget(self.lap_x2_formulas_LB)
        self.lap_x2_answer_LB = QtWidgets.QLabel(self.page_3)
        self.lap_x2_answer_LB.setObjectName("lap_x2_answer_LB")
        self.horizontalLayout_20.addWidget(self.lap_x2_answer_LB)
        self.verticalLayout_13.addLayout(self.horizontalLayout_20)
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.lap_formulas_LB = QtWidgets.QLabel(self.page_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lap_formulas_LB.setFont(font)
        self.lap_formulas_LB.setObjectName("lap_formulas_LB")
        self.horizontalLayout_21.addWidget(self.lap_formulas_LB)
        self.verticalLayout_13.addLayout(self.horizontalLayout_21)
        self.gridLayout_2.addLayout(self.verticalLayout_13, 2, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.p_lap = QtWidgets.QLineEdit(self.page_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.p_lap.setFont(font)
        self.p_lap.setObjectName("m1_lapa")
        self.horizontalLayout.addWidget(self.p_lap)
        self.n_lap = QtWidgets.QLineEdit(self.page_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.n_lap.setFont(font)
        self.n_lap.setObjectName("p_lap")
        self.horizontalLayout.addWidget(self.n_lap)
        self.m1_lap = QtWidgets.QLineEdit(self.page_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.m1_lap.setFont(font)
        self.m1_lap.setObjectName("n_lap")
        self.horizontalLayout.addWidget(self.m1_lap)
        self.m2_lap = QtWidgets.QLineEdit(self.page_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.m2_lap.setFont(font)
        self.m2_lap.setObjectName("m2_lap")
        self.horizontalLayout.addWidget(self.m2_lap)
        self.gridLayout_2.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lap_answer_LB = QtWidgets.QLabel(self.page_3)
        self.lap_answer_LB.setObjectName("lap_answer_LB")
        self.horizontalLayout_2.addWidget(self.lap_answer_LB)
        self.lap_compudte_BT = QtWidgets.QPushButton(self.page_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lap_compudte_BT.setFont(font)
        self.lap_compudte_BT.setObjectName("lap_compudte_BT")
        self.horizontalLayout_2.addWidget(self.lap_compudte_BT)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 3, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_3)
        self.verticalLayout.addWidget(self.stackedWidget)
        self.verticalLayout_6.addLayout(self.verticalLayout)

        self.retranslateUi(Widget)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "Widget"))
        self.task_selection.setItemText(0, _translate("Widget", "Задача №1"))
        self.task_selection.setItemText(1, _translate("Widget", "Задача №2"))
        self.ber_formulas_CB_1.setItemText(0, _translate("Widget", "Формула Бернулли"))
        self.ber_formulas_CB_1.setItemText(1, _translate("Widget", "Полиномиальная формула"))
        self.label_11.setText(_translate("Widget", "Введите число p,  где 0 <= p <= 1"))
        self.label_12.setText(_translate("Widget", "Введите натуральное число n"))
        self.label_10.setText(_translate("Widget", "Введите натуральное число m (m <= n)"))
        self.label_9.setText(_translate("Widget", "Введите натуральное число m1 (0 <= m1 <= n)"))
        self.label_2.setText(_translate("Widget", "Введите натуральное число m2 (0 <= m2 <= n)"))
        self.label_13.setText(_translate("Widget", "Выберите из перечня одно событие, вероятность которого хотите посчитать"))
        self.bernuli_oper_CB.setItemText(0, _translate("Widget", "Pn(k = m)"))
        self.bernuli_oper_CB.setItemText(1, _translate("Widget", "Pn(k < m)"))
        self.bernuli_oper_CB.setItemText(2, _translate("Widget", "Pn(k >= m)"))
        self.bernuli_oper_CB.setItemText(3, _translate("Widget", "Pn(m1 < = k <= m2)"))
        self.bernuli_formulas_LB.setText(_translate("Widget", "TextLabel"))
        self.answer_bernuli.setText(_translate("Widget", "TextLabel"))
        self.compute_bernuli_BT.setText(_translate("Widget", "Вычислить"))
        self.ber_formulas_CB_2.setItemText(0, _translate("Widget", "Формула Бернулли"))
        self.ber_formulas_CB_2.setItemText(1, _translate("Widget", "Полиномиальная формула"))
        self.label_6.setText(_translate("Widget", "Введите натуральное число n"))
        self.label_7.setText(_translate("Widget", "Введите натуральное число k, 0 <= k <= n"))
        self.label_4.setText(_translate("Widget", "Введите k натуральных чисел через точку с запятой"))
        self.label_3.setText(_translate("Widget", "Введите k десятичных чисел через точку с запятой"))
        self.pol_formulas_LB.setText(_translate("Widget", "TextLabel"))
        self.pol_answer_LB.setText(_translate("Widget", "TextLabel"))
        self.pol_copmute_BT.setText(_translate("Widget", "Вычислить"))
        self.label_16.setText(_translate("Widget", "Введите число p, где  0,1 <= p <= 0,9"))
        self.label_15.setText(_translate("Widget", "Введите натуральное число n, где n >= 100"))
        self.label_5.setText(_translate("Widget", "Введите натуральное число m1, где  0 <= m1 < n"))
        self.label.setText(_translate("Widget", "Введите натуральное число m2, где  0 <= m2 < n"))
        self.lap_x1_formulas_LB.setText(_translate("Widget", "TextLabel"))
        self.lap_x2_formulas_LB.setText(_translate("Widget", "TextLabel"))
        self.lap_x2_answer_LB.setText(_translate("Widget", "TextLabel"))
        self.lap_formulas_LB.setText(_translate("Widget", "TextLabel"))
        self.lap_answer_LB.setText(_translate("Widget", "TextLabel"))
        self.lap_compudte_BT.setText(_translate("Widget", "Вычислить"))
        self.answer_bernuli.setText("Ответ")
        self.pol_answer_LB.setText("Ответ")
        self.lap_x1_answer_LB.font()
        self.lap_x1_answer_LB.setText("x1 = ...")
        self.lap_x2_answer_LB.setText("x2 = ...")
        self.lap_answer_LB.setText("Ответ")
