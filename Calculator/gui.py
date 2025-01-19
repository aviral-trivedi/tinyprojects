import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QPushButton)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
#Global To-Do
#Ask chatGPT whether I use too many "self."
#Reduce Code Length

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.operator = ""
        self.num1 = None
        self.num2 = None
        self.is_result_displayed = None
        self.GUI()

    def number_press(self,number):
        if self.is_result_displayed:
            self.clear_screen()
            self.is_result_displayed = False
        new_text = self.ans_label.text() + number
        self.ans_label.setText(new_text)

    def set_number_and_operator(self,operator):
        self.num1 = self.ans_label.text()
        self.operator = operator
        self.clear_screen()


    def equal(self):
        self.num2 = self.ans_label.text()
        self.clear_screen()
        self.is_result_displayed = True

        if self.operator == "+":
            self.add(self.num1,self.num2)

    def clear_screen(self):
        self.ans_label.setText("")
    
    def clear_info(self):
        self.operator = ""
        self.num1 = None
        self.num2 = None

    def clear_last(self):
        new_text = self.ans_label.text()[0:-1]
        self.ans_label.setText(new_text)

    def my_function(self):
        print("Button clicked!")

    def add(self,num1,num2):
        answer = str(float(num1) + float(num2))
        self.ans_label.setText(answer)
        self.clear_info()

    

    def keyPressEvent(self, event):

        key = event.key()

        if key == Qt.Key_0:
            self.btn_0.click() 
        elif key == Qt.Key_1:
            self.btn_1.click()
        elif key == Qt.Key_2:
            self.btn_2.click()
        elif key == Qt.Key_3:
            self.btn_3.click()
        elif key == Qt.Key_4:
            self.btn_4.click()
        elif key == Qt.Key_5:
            self.btn_5.click()
        elif key == Qt.Key_6:
            self.btn_6.click()
        elif key == Qt.Key_7:
            self.btn_7.click()
        elif key == Qt.Key_8:
            self.btn_8.click()
        elif key == Qt.Key_9:
            self.btn_9.click()
        elif key == Qt.Key_Plus:
            self.btn_add.click()
        elif key == Qt.Key_Minus:
            self.btn_subtract.click()
        elif key == Qt.Key_Asterisk:
            self.btn_multiply.click()
        elif key == Qt.Key_Slash:
            self.btn_divide.click()
        elif key == Qt.Key_Return or key == Qt.Key_Enter:
            self.btn_equal.click()
        elif key == Qt.Key_Period:
            self.btn_point.click()
        elif key == Qt.Key_Backspace:
            self.clear_last()


    def GUI(self):

        self.setWindowTitle("Calculator")
        self.setGeometry(5,5, 400,450)
        self.setWindowIcon(QIcon("Calculator/images/icons/calculator.png"))

        """
        1. For PyQt5 first we need to create a central_widget and make it the central/main widget for the entire program.
        2. Then we need to create a layout seperately
        3. Then we need to add widgets to layout
        4. Then we need to add the layout to the central_widget
        """

        # Main Container
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # Answer Container
        self.ans_widget = QWidget()
        self.ans_layout = QHBoxLayout()

        self.ans_label = QLabel("")
        self.btn_extra = QPushButton("^")
        self.btn_extra.clicked.connect(self.my_function)
        self.btn_extra.setFixedSize(40, 20) 
        self.ans_layout.addWidget(self.btn_extra)
        self.ans_layout.addWidget(self.ans_label)
        self.ans_widget.setLayout(self.ans_layout)  # FIX: Layout set for ans_widget

        # Grid Container
        self.main_widget = QWidget()
        self.main_layout = QGridLayout()

        self.btn_AC = QPushButton("AC")
        self.btn_AC.clicked.connect(self.clear_screen)
        self.btn_x = QPushButton("<")
        self.btn_x.clicked.connect(self.clear_last)
        self.btn_negative = QPushButton("+/-")
        self.btn_negative.clicked.connect(self.my_function)
        self.btn_divide = QPushButton("/")
        self.btn_divide.clicked.connect(self.my_function)
        self.btn_multiply = QPushButton("*")
        self.btn_multiply.clicked.connect(self.my_function)
        self.btn_subtract = QPushButton("-")
        self.btn_subtract.clicked.connect(self.my_function)
        self.btn_add = QPushButton("+")
        self.btn_add.clicked.connect(lambda: self.set_number_and_operator("+"))
        self.btn_equal = QPushButton("=")
        self.btn_equal.clicked.connect(self.equal)
        self.btn_percentage = QPushButton("%")
        self.btn_percentage.clicked.connect(self.my_function)
        self.btn_point = QPushButton(".")
        self.btn_point.clicked.connect(self.my_function)

        self.btn_7 = QPushButton("7")
        self.btn_7.clicked.connect(lambda: self.number_press("7"))
        self.btn_8 = QPushButton("8")
        self.btn_8.clicked.connect(lambda: self.number_press("8"))
        self.btn_9 = QPushButton("9")
        self.btn_9.clicked.connect(lambda: self.number_press("9"))
        self.btn_4 = QPushButton("4")
        self.btn_4.clicked.connect(lambda: self.number_press("4"))
        self.btn_5 = QPushButton("5")
        self.btn_5.clicked.connect(lambda: self.number_press("5"))
        self.btn_6 = QPushButton("6")
        self.btn_6.clicked.connect(lambda: self.number_press("6"))
        self.btn_1 = QPushButton("1")
        self.btn_1.clicked.connect(lambda: self.number_press("1"))
        self.btn_2 = QPushButton("2")
        self.btn_2.clicked.connect(lambda: self.number_press("2"))
        self.btn_3 = QPushButton("3")
        self.btn_3.clicked.connect(lambda: self.number_press("3"))
        self.btn_0 = QPushButton("0")
        self.btn_0.clicked.connect(lambda: self.number_press("0"))


        self.main_layout.addWidget(self.btn_AC, 0, 0)
        self.main_layout.addWidget(self.btn_x, 0, 1)
        self.main_layout.addWidget(self.btn_negative, 0, 2)
        self.main_layout.addWidget(self.btn_divide, 0, 3)
        self.main_layout.addWidget(self.btn_multiply, 1, 3)
        self.main_layout.addWidget(self.btn_subtract, 2, 3)
        self.main_layout.addWidget(self.btn_add, 3, 3)
        self.main_layout.addWidget(self.btn_equal, 4, 3)
        self.main_layout.addWidget(self.btn_percentage, 4, 0)
        self.main_layout.addWidget(self.btn_point, 4, 2)

        self.main_layout.addWidget(self.btn_7, 1, 0)
        self.main_layout.addWidget(self.btn_8, 1, 1)
        self.main_layout.addWidget(self.btn_9, 1, 2)
        self.main_layout.addWidget(self.btn_4, 2, 0)
        self.main_layout.addWidget(self.btn_5, 2, 1)
        self.main_layout.addWidget(self.btn_6, 2, 2)
        self.main_layout.addWidget(self.btn_1, 3, 0)
        self.main_layout.addWidget(self.btn_2, 3, 1)
        self.main_layout.addWidget(self.btn_3, 3, 2)
        self.main_layout.addWidget(self.btn_0, 4, 1)
        
        self.main_widget.setLayout(self.main_layout)  # FIX: Layout set for main_widget

        # Final Widget to combine answer and keys
        self.vertical_widget = QWidget()
        self.horizontal_layout = QVBoxLayout()
        self.horizontal_layout.addWidget(self.ans_widget)
        self.horizontal_layout.addWidget(self.main_widget)
        self.vertical_widget.setLayout(self.horizontal_layout)  # FIX: Layout set for vertical_widget

        # Set Final Layout in Central Widget
        self.final_layout = QVBoxLayout()
        self.final_layout.addWidget(self.vertical_widget)
        self.central_widget.setLayout(self.final_layout)  # FIX: Layout set for central_widget



def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()