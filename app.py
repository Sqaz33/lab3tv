from task_enum import TaskEnum
from bernuli_oper_enum import BernuliOperEnum
from formulas import BernuliCalcul, IntegralLaplace
import form

import sys
from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap


class App:
    def __init__(self):
        self.bernuli = BernuliCalcul()
        self.laplace = IntegralLaplace()

        self.app = QtWidgets.QApplication(sys.argv)
        self.Widget = QtWidgets.QWidget()
        self.ui = form.Ui_Widget()
        self.ui.setupUi(self.Widget)

        self.ber_f = {
            BernuliOperEnum.equal: QPixmap(),
            BernuliOperEnum.less: QPixmap(),
            BernuliOperEnum.more_or_equal: QPixmap(),
            BernuliOperEnum.between: QPixmap()
        }

        # -----------загрузка картинок------
        self.ber_f[BernuliOperEnum.equal].load("image/equal.png")
        self.ber_f[BernuliOperEnum.less].load("image/less.png")
        self.ber_f[BernuliOperEnum.more_or_equal].load("image/more_or_equal.png")
        self.ber_f[BernuliOperEnum.between].load("image/between.png")

        pol = QPixmap()
        pol.load("image/pol.png")
        self.ui.pol_formulas_LB.setPixmap(pol)

        lap = QPixmap()
        x1 = QPixmap()
        x2 = QPixmap()
        lap.load("image/laplace.png")
        x1.load("image/x1")
        x2.load("image/x2")
        self.ui.lap_formulas_LB.setPixmap(lap)
        self.ui.lap_x1_formulas_LB.setPixmap(x1)
        self.ui.lap_x2_formulas_LB.setPixmap(x2)
        # ----------------------------------

        # ----------коннекты-----------
        # коннекты для смены страницы
        self.ui.task_selection.currentIndexChanged.connect(self.set_task)
        self.ui.ber_formulas_CB_1.currentIndexChanged.connect(self.set_ber)
        self.ui.ber_formulas_CB_2.currentIndexChanged.connect(self.set_pol)

        # коннект для смены формулы бернули
        self.ui.bernuli_oper_CB.currentIndexChanged.connect(self.change_bernuli_oper)

        # коннекты кнопок
        self.ui.compute_bernuli_BT.clicked.connect(self.calculate)
        self.ui.pol_copmute_BT.clicked.connect(self.calculate)
        self.ui.lap_compudte_BT.clicked.connect(self.calculate)
        # ----------------------------

        self.change_bernuli_oper()

    def calculate(self):
        match TaskEnum(self.ui.stackedWidget.currentIndex()):
            case TaskEnum.bernuli:
                oper = BernuliOperEnum(
                    self.ui.bernuli_oper_CB.currentIndex()
                )
                i = [
                    self.ui.n_ber.text(),
                    self.ui.m_ber.text(),
                    self.ui.m1_ber.text(),
                    self.ui.m2_ber.text()
                ]

                i = map(lambda j: 0 if not len(j) else int(j), i)
                n, m, m1, m2 = i
                p = self.ui.p_ber.text()
                p = 0 if not len(p) else float(p)

                if m1 > n or m2 > n or p > 1 or p < 0:
                    answer = "Неверный входные данные"
                else:
                    answer = f'Ответ: {str(self.bernuli.bernuli_calcul(n, m, m1, m2, p, oper))}'
                self.ui.answer_bernuli.setText(answer)
            case TaskEnum.polynomial:
                n = int(self.ui.n_pol.text())
                k = int(self.ui.k_pol.text())
                m = [int(i) for i in self.ui.m_pol.text().replace(' ', '').split(';')]
                p = [float(i) for i in self.ui.p_pol.text().replace(' ', '').split(';')]
                if len(m) != k or len(p) != k:
                    answer = "Неверный входные данные"
                else:
                    answer = f'Ответ: {self.bernuli.bernuli_polynomial(m, p)}'
                self.ui.pol_answer_LB.setText(answer)
            case TaskEnum.laplace:
                n = int(self.ui.n_lap.text())
                p = float(self.ui.p_lap.text())
                m1 = int(self.ui.m1_lap.text())
                m2 = int(self.ui.m2_lap.text())
                if m1 > n or m2 > n or p > 1:
                    answer = "Неверный входные данные"
                    answerx1 = "Неверный входные данные"
                    answerx2 = "Неверный входные данные"
                else:
                    answer = f'Ответ: {self.laplace.laplace_integer(n, m1, m2, p)}'
                    answerx1 = f'x1 = {self.laplace.x1(n, p, m1)}'
                    answerx2 = f'x2 = {self.laplace.x2(n, p, m2)}'
                self.ui.lap_answer_LB.setText(answer)
                self.ui.lap_x1_answer_LB.setText(answerx1)
                self.ui.lap_x2_answer_LB.setText(answerx2)

    def set_task(self):
        i = self.ui.task_selection.currentIndex()
        self.ui.stackedWidget.setCurrentIndex(2 if i == 1 else i)

    def set_ber(self):
        self.ui.stackedWidget.setCurrentIndex(self.ui.ber_formulas_CB_1.currentIndex())
        self.ui.ber_formulas_CB_2.setCurrentIndex(
            self.ui.ber_formulas_CB_1.currentIndex()
        )

    def set_pol(self):
        self.ui.stackedWidget.setCurrentIndex(self.ui.ber_formulas_CB_2.currentIndex())
        self.ui.ber_formulas_CB_1.setCurrentIndex(
            self.ui.ber_formulas_CB_2.currentIndex()
        )

    def change_bernuli_oper(self):
        self.ui.bernuli_formulas_LB.setPixmap(
            self.ber_f[
                BernuliOperEnum(self.ui.bernuli_oper_CB.currentIndex())
            ]
        )

    def run(self):
        self.Widget.show()
        sys.exit(self.app.exec_())
