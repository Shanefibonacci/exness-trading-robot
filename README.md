# Exness Trading Robot

An automated trading robot for the Exness platform using Moving Average and Oscillator strategies with live trading capabilities.

## Features

- **Technical Indicators**: Moving Average and Oscillators (RSI, MACD, Stochastic)
- **Live Trading**: Direct integration with Exness API
- **Risk Management**: Stop loss, take profit, and position sizing
- **Backtesting**: Historical data analysis and strategy testing
- **Price Data Fetching**: Real-time market data
- **Logging & Monitoring**: Comprehensive logging and trade tracking

## Prerequisites

- Python 3.8+
- Exness API credentials
- TA-Lib library

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Shanefibonacci/exness-trading-robot.git
cd exness-trading-robot
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file with your Exness credentials:
```
EXNESS_API_KEY=your_api_key_here
EXNESS_API_SECRET=your_api_secret_here
EXNESS_ACCOUNT_ID=your_account_id_here
EXNESS_ENV=live  # or demo for testing
```

## Configuration

Edit `config.yaml` to customize:
- Trading symbols and timeframes
- Moving Average periods
- Oscillator parameters
- Risk management settings (stop loss %, take profit %, position size)

## Usage

```bash
# Run live trading
python main.py

# Run backtesting
python backtest.py
```

## Project Structure

```
├── main.py                 # Main trading bot entry point
├── backtest.py             # Backtesting script
├── requirements.txt        # Python dependencies
├── config.yaml             # Configuration file
├── .env                    # Environment variables (create this)
├── .gitignore
└── src/
    ├── __init__.py
    ├── api/
    │   ├── __init__.py
    │   └── exness_client.py      # Exness API wrapper
    ├── indicators/
    │   ├── __init__.py
    │   ├── moving_average.py      # Moving Average calculations
    │   └── oscillators.py         # RSI, MACD, Stochastic
    ├── strategy/
    │   ├── __init__.py
    │   └── trading_strategy.py    # Main trading logic
    ├── risk_management/
    │   ├── __init__.py
    │   └── position_manager.py    # Risk management logic
    ├── backtester/
    │   ├── __init__.py
    │   └── backtester.py          # Backtesting engine
    └── utils/
        ├── __init__.py
        ├── logger.py              # Logging configuration
        └── data_handler.py        # Data processing
```

## License

MIT License