import sqlite3
import hashlib

# Function to connect to SQLite database
def connect_to_sqlite():
    try:
        connection = sqlite3.connect('trading_system.db')
        print("Connected to SQLite Database")
        return connection
    except sqlite3.Error as error:
        print("Error connecting to SQLite Database:", error)

# Function to create tables
def create_tables(connection):
    try:
        cursor = connection.cursor()
        # Create USER table
        cursor.execute('''CREATE TABLE IF NOT EXISTS "USER" (
                            US_ID INTEGER PRIMARY KEY,
                            PASSWORD TEXT,
                            EMAIL TEXT,
                            "PH NO" TEXT
                        )''')
        # Create STOCK table
        cursor.execute('''CREATE TABLE IF NOT EXISTS STOCK (
                            ST_ID INTEGER PRIMARY KEY,
                            SYMBOL TEXT,
                            COMPANY TEXT
                        )''')
        # Create STOCK_PRICE table
        cursor.execute('''CREATE TABLE IF NOT EXISTS STOCK_PRICE (
                            SP_ID INTEGER PRIMARY KEY,
                            ST_ID INTEGER,
                            HIGH REAL,
                            LOW REAL,
                            OPEN REAL,
                            CLOSE REAL,
                            DATE TEXT,
                            FOREIGN KEY (ST_ID) REFERENCES STOCK(ST_ID)
                        )''')
        # Create ACCOUNT table
        cursor.execute('''CREATE TABLE IF NOT EXISTS ACCOUNT (
                            ACC_ID INTEGER PRIMARY KEY,
                            US_ID INTEGER,
                            BALANCE REAL,
                            FOREIGN KEY (US_ID) REFERENCES "USER"(US_ID)
                        )''')
        # Create DEMAT table
        cursor.execute('''CREATE TABLE IF NOT EXISTS DEMAT (
                            DMT_ID INTEGER PRIMARY KEY,
                            ACC_ID INTEGER,
                            ST_ID INTEGER,
                            QTY_OWNED INTEGER,
                            PNL_STATUS INTEGER,
                            FOREIGN KEY (ACC_ID) REFERENCES ACCOUNT(ACC_ID),
                            FOREIGN KEY (ST_ID) REFERENCES STOCK(ST_ID)
                        )''')
        # Create TRANSACTION table
        cursor.execute('''CREATE TABLE IF NOT EXISTS "TRANSACTION" (
                            TR_ID INTEGER PRIMARY KEY,
                            US_ID INTEGER,
                            ST_ID INTEGER,
                            QTY INTEGER,
                            TOTAL_AMOUNT REAL,
                            BUY INTEGER,
                            SELL INTEGER,
                            DMT_ID INTEGER,
                            SP_ID INTEGER,
                            FOREIGN KEY (US_ID) REFERENCES "USER"(US_ID),
                            FOREIGN KEY (ST_ID) REFERENCES STOCK(ST_ID),
                            FOREIGN KEY (DMT_ID) REFERENCES DEMAT(DMT_ID),
                            FOREIGN KEY (SP_ID) REFERENCES STOCK_PRICE(SP_ID)
                        )''')
        print("Tables created successfully")
    except sqlite3.Error as error:
        print("Error creating tables:", error)

# Function to populate tables with sample data
def populate_tables(connection):
    try:
        cursor = connection.cursor()
        # Populate USER table
        cursor.execute('''DELETE FROM "USER"''')  # Clear existing data
        cursor.execute('''INSERT INTO "USER" (US_ID, PASSWORD, EMAIL, "PH NO")
                          VALUES (1, ?, ?, ?)''', (hashlib.sha256(b'password1').hexdigest(), 'user1@example.com', '1234567890'))
        cursor.execute('''INSERT INTO "USER" (US_ID, PASSWORD, EMAIL, "PH NO")
                          VALUES (2, ?, ?, ?)''', (hashlib.sha256(b'password2').hexdigest(), 'user2@example.com', '2345678901'))
        cursor.execute('''INSERT INTO "USER" (US_ID, PASSWORD, EMAIL, "PH NO")
                          VALUES (3, ?, ?, ?)''', (hashlib.sha256(b'password3').hexdigest(), 'user3@example.com', '3456789012'))
        cursor.execute('''INSERT INTO "USER" (US_ID, PASSWORD, EMAIL, "PH NO")
                          VALUES (4, ?, ?, ?)''', (hashlib.sha256(b'bala123').hexdigest(), 'bala@example.com', '3456789012'))

        # Populate STOCK table
        cursor.execute('''DELETE FROM STOCK''')  # Clear existing data
        cursor.execute('''INSERT INTO STOCK (ST_ID, SYMBOL, COMPANY) 
                          VALUES (1, 'TCS', 'Tata Consultancy Services Limited')''')
        cursor.execute('''INSERT INTO STOCK (ST_ID, SYMBOL, COMPANY) 
                          VALUES (2, 'HDFC', 'Housing Development Finance Corporation Limited')''')
        cursor.execute('''INSERT INTO STOCK (ST_ID, SYMBOL, COMPANY) 
                          VALUES (3, 'INFY', 'Infosys Limited')''')
        cursor.execute('''INSERT INTO STOCK (ST_ID, SYMBOL, COMPANY) 
                          VALUES (4, 'RELIANCE', 'Reliance Industries Limited')''')
        cursor.execute('''INSERT INTO STOCK (ST_ID, SYMBOL, COMPANY) 
                          VALUES (5, 'HCLTECH', 'HCL Technologies Limited')''')
        cursor.execute('''INSERT INTO STOCK (ST_ID, SYMBOL, COMPANY) 
                          VALUES (6, 'WIPRO', 'Wipro Limited')''')
        cursor.execute('''INSERT INTO STOCK (ST_ID, SYMBOL, COMPANY) 
                          VALUES (7, 'TECHM', 'Tech Mahindra Limited')''')
        cursor.execute('''INSERT INTO STOCK (ST_ID, SYMBOL, COMPANY) 
                          VALUES (8, 'INFIBEAM', 'Infibeam Avenues Limited')''')
        cursor.execute('''INSERT INTO STOCK (ST_ID, SYMBOL, COMPANY) 
                          VALUES (9, 'JUSTDIAL', 'Just Dial Limited')''')
        cursor.execute('''INSERT INTO STOCK (ST_ID, SYMBOL, COMPANY) 
                          VALUES (10, 'COFORGE', 'Coforge Limited')''')

        # Populate STOCK_PRICE table
        cursor.execute('''DELETE FROM STOCK_PRICE''')  # Clear existing data
        cursor.execute('''INSERT INTO STOCK_PRICE (ST_ID, HIGH, LOW, OPEN, CLOSE, DATE) 
                          VALUES (1, 3500.00, 3400.00, 3450.00, 3420.00, '2024-04-14')''')
        cursor.execute('''INSERT INTO STOCK_PRICE (ST_ID, HIGH, LOW, OPEN, CLOSE, DATE) 
                          VALUES (2, 2800.00, 2700.00, 2750.00, 2780.00, '2024-04-14')''')
        cursor.execute('''INSERT INTO STOCK_PRICE (ST_ID, HIGH, LOW, OPEN, CLOSE, DATE) 
                          VALUES (3, 1900.00, 1800.00, 1850.00, 1880.00, '2024-04-14')''')
        cursor.execute('''INSERT INTO STOCK_PRICE (ST_ID, HIGH, LOW, OPEN, CLOSE, DATE) 
                          VALUES (4, 3000.00, 2900.00, 2950.00, 2980.00, '2024-04-14')''')
        cursor.execute('''INSERT INTO STOCK_PRICE (ST_ID, HIGH, LOW, OPEN, CLOSE, DATE) 
                          VALUES (5, 1200.00, 1150.00, 1175.00, 1185.00, '2024-04-14')''')
        cursor.execute('''INSERT INTO STOCK_PRICE (ST_ID, HIGH, LOW, OPEN, CLOSE, DATE) 
                          VALUES (6, 750.00, 700.00, 725.00, 730.00, '2024-04-14')''')
        cursor.execute('''INSERT INTO STOCK_PRICE (ST_ID, HIGH, LOW, OPEN, CLOSE, DATE) 
                          VALUES (7, 1300.00, 1250.00, 1275.00, 1285.00, '2024-04-14')''')
        cursor.execute('''INSERT INTO STOCK_PRICE (ST_ID, HIGH, LOW, OPEN, CLOSE, DATE) 
                          VALUES (8, 200.00, 180.00, 190.00, 195.00, '2024-04-14')''')
        cursor.execute('''INSERT INTO STOCK_PRICE (ST_ID, HIGH, LOW, OPEN, CLOSE, DATE) 
                          VALUES (9, 500.00, 480.00, 490.00, 495.00, '2024-04-14')''')
        cursor.execute('''INSERT INTO STOCK_PRICE (ST_ID, HIGH, LOW, OPEN, CLOSE, DATE) 
                          VALUES (10, 3500.00, 3400.00, 3450.00, 3420.00, '2024-04-14')''')

        # Populate ACCOUNT table
        cursor.execute('''DELETE FROM ACCOUNT''')  # Clear existing data
        cursor.execute('''INSERT INTO ACCOUNT (US_ID, BALANCE) 
                          VALUES (1, 10000.00)''')
        cursor.execute('''INSERT INTO ACCOUNT (US_ID, BALANCE) 
                          VALUES (2, 20000.00)''')
        cursor.execute('''INSERT INTO ACCOUNT (US_ID, BALANCE) 
                          VALUES (3, 30000.00)''')
        cursor.execute('''INSERT INTO ACCOUNT (US_ID, BALANCE) 
                          VALUES (4, 40000.00)''')

        connection.commit()
        print("Tables populated successfully")
    except sqlite3.Error as error:
        connection.rollback()
        print("Error populating tables:", error)

# Function to authenticate user
def authenticate_user(connection):
    try:
        cursor = connection.cursor()
        username = input("Enter username: ")
        password = input("Enter password: ")
        cursor.execute('''SELECT US_ID FROM "USER" WHERE US_ID = ? AND PASSWORD = ?''', (username, hashlib.sha256(password.encode()).hexdigest()))
        user = cursor.fetchone()
        if user:
            return user[0]
        else:
            return None
    except sqlite3.Error as error:
        print("Error:", error)

# Function to buy stocks
def buy_stocks(connection, user_id):
    try:
        cursor = connection.cursor()
        cursor.execute('''SELECT BALANCE FROM ACCOUNT WHERE US_ID = ?''', (user_id,))
        account_balance = cursor.fetchone()[0]
        print(f"Your current balance: {account_balance}")
        cursor.execute('''SELECT s.ST_ID, s.SYMBOL, s.COMPANY, sp.OPEN
                          FROM STOCK s
                          JOIN STOCK_PRICE sp ON s.ST_ID = sp.ST_ID''')
        stocks = cursor.fetchall()
        print("Available Stocks:")
        for stock in stocks:
            print(f"ID: {stock[0]}, Symbol: {stock[1]}, Company: {stock[2]}, Open Price: {stock[3]}")
        stock_id = int(input("Enter the stock ID you want to buy: "))
        quantity = int(input("Enter the quantity you want to buy: "))
        
        cursor.execute('''SELECT OPEN FROM STOCK_PRICE WHERE ST_ID = ?''', (stock_id,))
        open_price = cursor.fetchone()[0]
        
        total_amount = quantity * open_price
        print(f"Total amount to be deducted: {total_amount}")
        confirmation = input("Confirm buy (Y/N): ")
        if confirmation.upper() == 'Y':
            if account_balance >= total_amount:
                cursor.execute('''SELECT QTY_OWNED FROM DEMAT WHERE ACC_ID = ? AND ST_ID = ?''', (user_id, stock_id))
                existing_quantity = cursor.fetchone()
                if existing_quantity:
                    updated_quantity = existing_quantity[0] + quantity
                    cursor.execute('''UPDATE DEMAT SET QTY_OWNED = ? WHERE ACC_ID = ? AND ST_ID = ?''', (updated_quantity, user_id, stock_id))
                else:
                    cursor.execute('''INSERT INTO DEMAT (ACC_ID, ST_ID, QTY_OWNED, PNL_STATUS) VALUES (?, ?, ?, ?)''', (user_id, stock_id, quantity, 0))
                
                cursor.execute('''INSERT INTO "TRANSACTION" (US_ID, ST_ID, QTY, TOTAL_AMOUNT, BUY, SELL)
                                  VALUES (?, ?, ?, ?, ?, ?)''', (user_id, stock_id, quantity, total_amount, 1, 0))
                
                cursor.execute('''UPDATE ACCOUNT SET BALANCE = BALANCE - ? WHERE US_ID = ?''', (total_amount, user_id))
                print("Stock bought successfully.")
            else:
                print("Insufficient balance.")
        connection.commit()  # Commit changes to the database
    except sqlite3.Error as error:
        connection.rollback()
        print("Error buying stocks:", error)

# Function to sell stocks
def sell_stocks(connection, user_id):
    try:
        cursor = connection.cursor()
        cursor.execute('''SELECT d.ST_ID, s.SYMBOL, s.COMPANY, d.QTY_OWNED, sp.CLOSE
                          FROM DEMAT d
                          JOIN STOCK s ON d.ST_ID = s.ST_ID
                          JOIN STOCK_PRICE sp ON d.ST_ID = sp.ST_ID
                          WHERE d.ACC_ID = ?''', (user_id,))
        stocks_owned = cursor.fetchall()
        
        if not stocks_owned:
            print("NO STOCKS CURRENTLY IN YOUR PORTFOLIO")
            return
        
        print("Stocks owned:")
        for stock in stocks_owned:
            print(f"ID: {stock[0]}, Symbol: {stock[1]}, Company: {stock[2]}, Quantity: {stock[3]}, Close Price: {stock[4]}")
        stock_id = int(input("Enter the stock ID you want to sell: "))
        quantity = int(input("Enter the quantity you want to sell: "))
        available_quantity = [s[3] for s in stocks_owned if s[0] == stock_id][0]
        if available_quantity >= quantity:
            cursor.execute('''SELECT CLOSE FROM STOCK_PRICE WHERE ST_ID = ?''', (stock_id,))
            close_price = cursor.fetchone()[0]
            total_amount = quantity * close_price
            print(f"Total amount to be added: {total_amount}")
            confirmation = input("Confirm sell (Y/N): ")
            if confirmation.upper() == 'Y':
                cursor.execute('''UPDATE ACCOUNT SET BALANCE = BALANCE + ? WHERE US_ID = ?''', (total_amount, user_id))
                updated_quantity = available_quantity - quantity
                cursor.execute('''UPDATE DEMAT SET QTY_OWNED = ? WHERE ACC_ID = ? AND ST_ID = ?''', (updated_quantity, user_id, stock_id))
                cursor.execute('''INSERT INTO "TRANSACTION" (US_ID, ST_ID, QTY, TOTAL_AMOUNT, BUY, SELL)
                                  VALUES (?, ?, ?, ?, ?, ?)''', (user_id, stock_id, quantity, total_amount, 0, 1))
                print("Stock sold successfully.")
                
                # Check if quantity becomes zero and delete the entry from DEMAT
                if updated_quantity == 0:
                    cursor.execute('''DELETE FROM DEMAT WHERE ACC_ID = ? AND ST_ID = ?''', (user_id, stock_id))
                    print("Stock removed from portfolio.")
                connection.commit()  # Commit changes to the database
        else:
            print("Insufficient quantity.")
    except sqlite3.Error as error:
        connection.rollback()
        print("Error selling stocks:", error)

# Function to view portfolio
def view_portfolio(connection, user_id):
    try:
        cursor = connection.cursor()
        # Fetch stocks from DEMAT table
        cursor.execute('''SELECT s.ST_ID, s.SYMBOL, s.COMPANY, d.QTY_OWNED, sp.OPEN, sp.CLOSE
                          FROM DEMAT d
                          JOIN STOCK s ON d.ST_ID = s.ST_ID
                          JOIN STOCK_PRICE sp ON d.ST_ID = sp.ST_ID
                          WHERE d.ACC_ID = ?''', (user_id,))
        stocks_owned = cursor.fetchall()

        # Fetch bought and sold transactions from TRANSACTION table
        cursor.execute('''SELECT t.ST_ID, s.SYMBOL, s.COMPANY, t.QTY, sp.OPEN, sp.CLOSE, t.BUY, t.SELL
                          FROM "TRANSACTION" t
                          JOIN STOCK s ON t.ST_ID = s.ST_ID
                          JOIN STOCK_PRICE sp ON t.ST_ID = sp.ST_ID
                          WHERE t.US_ID = ?''', (user_id,))
        transactions = cursor.fetchall()

        if stocks_owned or transactions:
            print("Portfolio:")
            print("{:<5} {:<10} {:<20} {:<10} {:<10} {:<10} {:<10} {:<10}".format("ID", "Symbol", "Company", "Quantity", "Open", "Close", "Type", "Profit/Loss"))
            
            # Display stocks owned from DEMAT table
            for stock in stocks_owned:
                stock_id, symbol, company, quantity, open_price, close_price = stock[:6]
                profit_loss = (close_price - open_price) * quantity
                print("{:<5} {:<10} {:<20} {:<10} {:<10} {:<10} {:<10} {:<10}".format(stock_id, symbol, company, quantity, open_price, close_price, "Owned", profit_loss))
            
            # Display bought and sold transactions from TRANSACTION table
            for transaction in transactions:
                stock_id, symbol, company, quantity, open_price, close_price, buy_flag, sell_flag = transaction[:8]
                profit_loss = (close_price - open_price) * quantity
                if buy_flag:
                    transaction_type = "Bought"
                elif sell_flag:
                    transaction_type = "Sold"
                else:
                    transaction_type = "N/A"
                print("{:<5} {:<10} {:<20} {:<10} {:<10} {:<10} {:<10} {:<10}".format(stock_id, symbol, company, quantity, open_price, close_price, transaction_type, profit_loss))
        else:
            print("No stocks owned.")
    except sqlite3.Error as error:
        print("Error viewing portfolio:", error)

# Main function
def main():
    connection = connect_to_sqlite()
    if connection:
        create_tables(connection)
        populate_tables(connection)
        user_id = authenticate_user(connection)
        if user_id:
            while True:
                print("\nMenu:")
                print("1. Buy Stocks")
                print("2. Sell Stocks")
                print("3. View Portfolio")
                print("4. Exit")
                choice = input("Enter your choice: ")
                if choice == '1':
                    buy_stocks(connection, user_id)
                elif choice == '2':
                    sell_stocks(connection, user_id)
                elif choice == '3':
                    view_portfolio(connection, user_id)
                elif choice == '4':
                    print("Exiting...")
                    break
                else:
                    print("Invalid choice. Please try again.")
        else:
            print("Authentication failed.")
        connection.close()
        print("Connection to SQLite Database closed")

if __name__ == "__main__":
    main()
