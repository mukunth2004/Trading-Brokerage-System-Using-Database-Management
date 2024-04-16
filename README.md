# Trading-Brokerage-System-Using-Database-Management
1. Database Connection:
- The code uses SQLite, a lightweight database engine, to manage the trading system's data.
- A connection to the SQLite database named 'trading_system.db' is established using the `sqlite3` library in Python.
2. Table Creation:
- The code defines and creates several tables in the database to organize different types of data.
  - USER Table: Stores user information such as user ID, password, email, and phone number.
  - STOCK Table: Contains details about different stocks, including their ID, symbol, and company name.
  - STOCK_PRICE Table: Stores daily stock price information, including high, low, open, close prices, and the date.
  - ACCOUNT Table: Manages user accounts, including the user ID and account balance.
  - DEMAT Table: Tracks the ownership of stocks in dematerialized (DEMAT) form, including account ID, stock ID, quantity owned, and profit/loss status.
  - TRANSACTION Table: Records buy and sell transactions, including user ID, stock ID, quantity, total amount, buy/sell flags, and references to the demat and stock price tables.
3. Data Population:
- Sample data is inserted into each table to provide initial information for testing and demonstration purposes.
  - User accounts are created with hashed passwords, emails, and phone numbers.
  - Stock information such as symbols, company names, and stock IDs are populated.
  - Daily stock prices (high, low, open, close) for various stocks are added.
  - Account balances for users are initialized.
  - Initial ownership of stocks in demat accounts and transaction history are set up.
4. User Authentication:
- The system prompts users to enter their username and password for authentication.
- The entered credentials are checked against the database's user table to validate the user's identity.
- If authentication is successful, the system allows the user to proceed with trading operations.
5. Buying Stocks:
- Users can buy stocks by selecting the desired stock ID and specifying the quantity they want to purchase.
- The system checks the user's account balance to ensure they have sufficient funds.
- It calculates the total amount based on the stock's open price and updates the demat account, transaction history, and account balance accordingly.
6. Selling Stocks:
- Users can sell stocks they own by providing the stock ID and quantity they wish to sell.
- The system verifies the availability of the specified quantity in the demat account.
- It calculates the total amount based on the stock's close price and updates the demat account, transaction history, and account balance accordingly.
7. Viewing Portfolio:
- The system allows users to view their portfolio, which includes stocks they own and their transaction history.
- It retrieves relevant data from the demat account and transaction tables to display the user's holdings, stock details, buy/sell transactions, and profit/loss information.
8. Main Functionality:
- The `main()` function acts as the program's entry point and orchestrates the entire trading process.
- It handles user interaction by presenting a menu with options to buy stocks, sell stocks, view the portfolio, or exit the program.
- Based on the user's input, it calls the appropriate functions to perform the requested actions and interacts with the database to update and retrieve data.
- The code includes error handling mechanisms using try-except blocks to catch and handle exceptions that may occur during database operations.
- Errors such as connection failures, table creation issues, data population errors, authentication failures, and transactional errors are handled gracefully, ensuring the program's stability and reliability.
