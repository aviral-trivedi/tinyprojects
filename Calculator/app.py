import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QPushButton)
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.GUI()

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

        self.ans_label = QLabel("0")
        self.extra_btn = QPushButton("^")
        self.extra_btn.setGeometry(0,0,10,10)

        self.ans_layout.addWidget(self.extra_btn)
        self.ans_layout.addWidget(self.ans_label)
        self.ans_widget.setLayout(self.ans_layout)  # FIX: Layout set for ans_widget

        # Grid Container
        self.main_widget = QWidget()
        self.main_layout = QGridLayout()

        self.btn7 = QPushButton("7")
        self.btn8 = QPushButton("8")
        self.btn9 = QPushButton("9")
        self.btn4 = QPushButton("4")
        self.btn5 = QPushButton("5")
        self.btn6 = QPushButton("6")
        self.btn1 = QPushButton("1")
        self.btn2 = QPushButton("2")
        self.btn3 = QPushButton("3")

        self.main_layout.addWidget(self.btn7, 1, 0)
        self.main_layout.addWidget(self.btn8, 1, 1)
        self.main_layout.addWidget(self.btn9, 1, 2)
        self.main_layout.addWidget(self.btn4, 2, 0)
        self.main_layout.addWidget(self.btn5, 2, 1)
        self.main_layout.addWidget(self.btn6, 2, 2)
        self.main_layout.addWidget(self.btn1, 3, 0)
        self.main_layout.addWidget(self.btn2, 3, 1)
        self.main_layout.addWidget(self.btn3, 3, 2)
        
        self.main_widget.setLayout(self.main_layout)  # FIX: Layout set for main_widget

        # Final Widget to combine answer and keys
        self.vertical = QWidget()
        self.horizontal_layout = QVBoxLayout()
        self.horizontal_layout.addWidget(self.ans_widget)
        self.horizontal_layout.addWidget(self.main_widget)
        self.vertical.setLayout(self.horizontal_layout)  # FIX: Layout set for vertical

        # Set Final Layout in Central Widget
        self.final_layout = QVBoxLayout()
        self.final_layout.addWidget(self.vertical)
        self.central_widget.setLayout(self.final_layout)  # FIX: Layout set for central_widget

    def display(self):
        pass



def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()