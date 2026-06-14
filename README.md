# Binance Futures Testnet Trading Bot

## Overview

This project is a Python-based trading bot built for the Binance Futures Testnet. It allows users to execute simulated market and limit orders through the Binance API using a command-line interface.

The bot focuses on modular design, input validation, logging, and reliable order execution.

---

## Features

- Market BUY and SELL orders  
- Limit BUY and SELL orders  
- Command Line Interface (CLI) support  
- Input validation for all trading parameters  
- Error handling for API and runtime issues  
- Logging of all trading activity  
- Binance Futures Testnet integration  


## Configuration

Create a `.env` file in the root directory:

API_KEY=your_binance_api_key  
API_SECRET=your_binance_api_secret  

---

## Installation

Clone the repository:

git clone https://github.com/your-username/primetrade-ai.git  
cd primetrade-ai  

Install dependencies:

pip install -r requirements.txt  

---

## Usage

### Market Orders

Buy Market:

py main.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001  

Sell Market:

py main.py --symbol BTCUSDT --side SELL --type MARKET --quantity 0.001  

---

### Limit Orders

Buy Limit:

py main.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.001 --price 50000  

Sell Limit:

py main.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 70000  

---

## Logging

All trading activity is stored in:

logs/trading.log  

It records:
- Order requests  
- API responses  
- Errors and exceptions  

---

## Validation Rules

- Order side: BUY / SELL  
- Order type: MARKET / LIMIT  
- Quantity must be > 0  
- Price must be > 0 for LIMIT orders  

---

## Technologies Used

- Python  
- Binance Futures Testnet API  
- python-binance  
- python-dotenv  
- argparse  
- logging  

---

## Sample Output

========== ORDER SUMMARY ==========  
Symbol: BTCUSDT  
Side: BUY  
Type: MARKET  
Quantity: 0.001  

========== RESPONSE ==========  
Order ID: 15141888736  
Status: NEW  
Executed Qty: 0.0000  

SUCCESS  

---

## Screenshots

Screenshots of successful order execution are available in the screenshots/ folder.

---

## Disclaimer

This bot runs only on Binance Futures Testnet and is intended for educational and testing purposes. It does not execute real trades unless explicitly configured for live trading.

---

## Author

Atharv Singh