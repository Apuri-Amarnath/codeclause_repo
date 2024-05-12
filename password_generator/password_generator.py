import random
import string
import sys

from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QVBoxLayout, QLabel, QLineEdit, QCheckBox, QPushButton
from PyQt5.QtGui import QIcon

class PasswordGenerator(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "Password Generator by pyqt5"
        self.width = 400
        self.height = 900
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        self.password_label = QLabel("Enter the length of the password :")
        layout.addWidget(self.password_label)

        self.password_length = QLineEdit()
        layout.addWidget(self.password_length)

        self.uppercase_checkbox = QCheckBox("Include uppercase")
        layout.addWidget(self.uppercase_checkbox)

        self.lowercase_checkbox = QCheckBox("Include lowercase")
        layout.addWidget(self.lowercase_checkbox)

        self.digits_checkbox = QCheckBox("Include digits")
        layout.addWidget(self.digits_checkbox)

        self.special_char_checkbox = QCheckBox("Include special characters")
        layout.addWidget(self.special_char_checkbox)

        layout.addStretch()
        generate_button = QPushButton("Generate Password")
        generate_button.clicked.connect(self.generate_pass)
        layout.addWidget(generate_button)

        self.password_line = QLineEdit()
        layout.addWidget(self.password_line)

        self.setLayout(layout)

    def generate_pass(self):
        length_str = self.password_length.text()
        try:
            length = int(length_str)
            if length <= 0:
                raise ValueError("Password length must be greater than zero")
        except ValueError:
            self.password_line.setText("Invalid password length")
            return
        characters = ""
        if self.uppercase_checkbox.isChecked():
            characters += string.ascii_uppercase
        if self.lowercase_checkbox.isChecked():
            characters += string.ascii_lowercase
        if self.digits_checkbox.isChecked():
            characters += string.digits
        if self.special_char_checkbox.isChecked():
            characters += string.punctuation

        if not characters:
            characters = string.ascii_letters + string.digits + string.punctuation
        password = "".join(random.choice(characters) for _ in range(length))
        self.password_line.setText(password)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Password Generator")
        self.central_widget = PasswordGenerator()
        self.setCentralWidget(self.central_widget)
        self.setGeometry(500, 400, 600, 300)
        icon="logo.ico"
        self.setWindowIcon(QIcon(icon))

if __name__ == '__main__':
   app = QApplication(sys.argv)
   window = MainWindow()
   window.show()
   sys.exit(app.exec_())