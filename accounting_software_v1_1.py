import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Accounting Software")
        self.setGeometry(100, 100, 400, 300)

        # Create buttons for different transaction types
        self.invoice_btn = QPushButton("Record Invoice", self)
        self.invoice_btn.setGeometry(100, 50, 200, 50)
        self.invoice_btn.clicked.connect(self.record_invoice)

        self.expense_btn = QPushButton("Record Expense", self)
        self.expense_btn.setGeometry(100, 150, 200, 50)
        self.expense_btn.clicked.connect(self.record_expense)

    def record_invoice(self):
        # Code to handle recording an invoice
        print("Recording an invoice...")

    def record_expense(self):
        # Code to handle recording an expense
        print("Recording an expense...")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())