
#Эминидис Маркос 11-312 


import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
import requests
from io import BytesIO


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("изменить фон")
        self.setGeometry(100, 100, 300, 150)

        self.url_input = QLineEdit(self)
        self.url_input.setPlaceholderText("код цвета или ссылочка")
        self.url_input.move(10, 10)
        self.url_input.resize(280, 30)

        self.change_button = QPushButton("изменить фон", self)
        self.change_button.move(10, 50)
        self.change_button.clicked.connect(self.change_background)

        self.label = QLabel(self)  
        self.label.move(10, 80)
        self.label.resize(280, 50)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter) 
        self.label.setStyleSheet("color: red;")  

    def change_background(self):
        input_text = self.url_input.text()
        self.label.setText("") 

        try:
            if input_text.startswith("http"):  
                response = requests.get(input_text, stream=True)
                response.raise_for_status() 
                image = QPixmap()
                image.loadFromData(response.content)
                self.setStyleSheet(f"background-image: url(:image);") 
                self.label.setText("Background changed successfully!")

            else: 
                self.setStyleSheet(f"background-color: {input_text};")
                self.label.setText("ура цвет поменялся йоу")

        except requests.exceptions.RequestException as e:
            self.label.setText(f"Error: {e}") 
        except Exception as e:
            self.label.setText(f"Error: Invalid input. Please provide a valid URL or color. {e}")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
