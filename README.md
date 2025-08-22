# Crypto Signals Agent

This agent fetches crypto price data (BTC/USDT, SOL/USDT) and generates simple buy/sell/hold signals daily. 
It sends alerts via Telegram.

## Setup

1. Clone repo or unzip this package
2. Create `.env` from `.env.example` and set your Telegram Bot Token & Chat ID
3. Install docker and build image:
   ```bash
   docker build -t crypto-signals-agent .
   ```
4. Run container:
   ```bash
   docker run -d --name signals --env-file .env crypto-signals-agent
   ```

The container will run daily at 08:00 Africa/Lagos time and send you alerts.

## Files

- `src/agent.py` → fetches prices, generates signals
- `src/alerts.py` → sends alerts to Telegram
- `config.yaml` → config file for coins and thresholds
- `.env` → secrets file
