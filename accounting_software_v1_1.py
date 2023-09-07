import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QInputDialog

class AccountingOptionsWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.additional_buttons_layout = QVBoxLayout()
        self.show_main_options()

    def show_main_options(self):
        # Clear the layout
        for i in reversed(range(self.additional_buttons_layout.count())):
            self.additional_buttons_layout.itemAt(i).widget().setParent(None)

        # Create buttons for main options (Debt and Credit)
        self.debt_btn = QPushButton("Debt", self)
        self.debt_btn.clicked.connect(self.show_debt_options)
        self.additional_buttons_layout.addWidget(self.debt_btn)

        self.credit_btn = QPushButton("Credit", self)
        self.credit_btn.clicked.connect(self.show_credit_options)
        self.additional_buttons_layout.addWidget(self.credit_btn)

        # Create a widget to hold the additional buttons layout
        self.additional_buttons_widget = QWidget()
        self.additional_buttons_widget.setLayout(self.additional_buttons_layout)

        # Set the layout of the main window
        self.setCentralWidget(self.additional_buttons_widget)

    def show_debt_options(self):
        # Clear the layout
        for i in reversed(range(self.additional_buttons_layout.count())):
            self.additional_buttons_layout.itemAt(i).widget().setParent(None)

        # Create buttons for debt options
        self.assets_btn = QPushButton("Assets", self)
        self.assets_btn.clicked.connect(self.get_input_for_assets)
        self.additional_buttons_layout.addWidget(self.assets_btn)

        self.dividends_btn = QPushButton("Dividends", self)
        self.dividends_btn.clicked.connect(self.get_input_for_dividends)
        self.additional_buttons_layout.addWidget(self.dividends_btn)

        self.expenses_btn = QPushButton("Expenses", self)
        self.expenses_btn.clicked.connect(self.get_input_for_expenses)
        self.additional_buttons_layout.addWidget(self.expenses_btn)

        # Add a "Back" button to return to the main menu
        self.back_btn = QPushButton("Back", self)
        self.back_btn.clicked.connect(self.show_main_options)
        self.additional_buttons_layout.addWidget(self.back_btn)

    def show_credit_options(self):
        # Clear the layout
        for i in reversed(range(self.additional_buttons_layout.count())):
            self.additional_buttons_layout.itemAt(i).widget().setParent(None)

        # Create buttons for credit options
        self.liability_btn = QPushButton("Liability", self)
        self.liability_btn.clicked.connect(self.get_input_for_liability)
        self.additional_buttons_layout.addWidget(self.liability_btn)

        self.equity_btn = QPushButton("Equity", self)
        self.equity_btn.clicked.connect(self.get_input_for_equity)
        self.additional_buttons_layout.addWidget(self.equity_btn)

        self.revenue_btn = QPushButton("Revenue", self)
        self.revenue_btn.clicked.connect(self.get_input_for_revenue)
        self.additional_buttons_layout.addWidget(self.revenue_btn)

        # Add a "Back" button to return to the main menu
        self.back_btn = QPushButton("Back", self)
        self.back_btn.clicked.connect(self.show_main_options)
        self.additional_buttons_layout.addWidget(self.back_btn)

    def get_input_for_assets(self):
        # Method to handle the "Assets" button click and get input for the financial amount
        amount, ok = QInputDialog.getDouble(self, "Input", "Enter the financial amount for Assets:")
        if ok:
            print(f"Recorded Assets amount: {amount}")

    def get_input_for_dividends(self):
        # Method to handle the "Dividends" button click and get input for the financial amount
        amount, ok = QInputDialog.getDouble(self, "Input", "Enter the financial amount for Dividends:")
        if ok:
            print(f"Recorded Dividends amount: {amount}")

    def get_input_for_expenses(self):
        # Method to handle the "Expenses" button click and get input for the financial amount
        amount, ok = QInputDialog.getDouble(self, "Input", "Enter the financial amount for Expenses:")
        if ok:
            print(f"Recorded Expenses amount: {amount}")

    def get_input_for_liability(self):
        # Method to handle the "Liability" button click and get input for the financial amount
        amount, ok = QInputDialog.getDouble(self, "Input", "Enter the financial amount for Liability:")
        if ok:
            print(f"Recorded Liability amount: {amount}")

    def get_input_for_equity(self):
        # Method to handle the "Equity" button click and get input for the financial amount
        amount, ok = QInputDialog.getDouble(self, "Input", "Enter the financial amount for Equity:")
        if ok:
            print(f"Recorded Equity amount: {amount}")

    def get_input_for_revenue(self):
        # Method to handle the "Revenue" button click and get input for the financial amount
        amount, ok = QInputDialog.getDouble(self, "Input", "Enter the financial amount for Revenue:")
        if ok:
            print(f"Recorded Revenue amount: {amount}")

# Create an instance of the AccountingOptionsWindow class and run the application
app = QApplication(sys.argv)
window = AccountingOptionsWindow()
window.show()
sys.exit(app.exec_())

#SQLAlchemy integration (untested)
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QInputDialog
from sqlalchemy import create_engine, Column, Integer, Float, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Create a SQLAlchemy database engine and session
engine = create_engine('sqlite:///accounting.db')  # Use SQLite for simplicity
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

# Define a database model for storing financial data
class FinancialTransaction(Base):
    __tablename__ = 'financial_transactions'
    id = Column(Integer, primary_key=True)
    transaction_type = Column(String)
    amount = Column(Float)

# Create the database tables if they don't exist
Base.metadata.create_all(engine)

class AccountingOptionsWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.additional_buttons_layout = QVBoxLayout()
        self.show_main_options()

    # ... rest of the code remains the same ...

    def get_input_for_assets(self):
        # Method to handle the "Assets" button click and get input for the financial amount
        amount, ok = QInputDialog.getDouble(self, "Input", "Enter the financial amount for Assets:")
        if ok:
            print(f"Recorded Assets amount: {amount}")
            self.save_transaction("Assets", amount)

    # ... rest of the get_input_for_XXX methods ...

    def save_transaction(self, transaction_type, amount):
        # Save the transaction to the database
        transaction = FinancialTransaction(transaction_type=transaction_type, amount=amount)
        session.add(transaction)
        session.commit()
        print(f"Saved {transaction_type} amount {amount} to the database")

# Create an instance of the AccountingOptionsWindow class and run the application
app = QApplication(sys.argv)
window = AccountingOptionsWindow()
window.show()
sys.exit(app.exec_())
